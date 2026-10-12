#!/usr/bin/env python3
"""Deepen existing pages with keyword sections, extra FAQs and schema.

Content lives in enrich_*.py (one dict ENRICH per file):
    'path/index.html': {
        'sections': [(h2, [blocks…])],      # same block format as build.py
        'faq': [(question, answer)],        # shown on the page AND merged into FAQPage JSON-LD
        'app': {...},                       # optional SoftwareApplication JSON-LD
    }

The block is inserted before the "Mehr zum Thema" links (or the CTA, or the footer)
between <!-- seo-enrich --> markers. Re-running replaces the block and never
duplicates FAQ entries, so the script is idempotent.

Run order: build.py → fix_faq_json.py → enrich.py (build.py rewrites the generated pages,
and FAQs can only be merged into JSON-LD that parses).
Usage:  python3 tools/seo/enrich.py
"""
import html
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.abspath(os.path.join(HERE, '..', '..', 'public'))
UPDATED_ISO = '2026-10-11'
FILES = ['enrich_apps', 'enrich_devices', 'enrich_topics']

STYLE = ('<style>.seo-enrich{max-width:900px;margin:0 auto 56px}'
         '.seo-enrich h2{font-size:1.5rem;font-weight:900;margin-bottom:20px;color:#fff}'
         '.seo-enrich p{color:#aaa;font-size:0.95rem;line-height:1.8;margin-bottom:14px}'
         '.seo-enrich ul,.seo-enrich ol{color:#aaa;font-size:0.95rem;line-height:1.8;margin:0 0 16px 22px}'
         '.seo-enrich li{margin-bottom:6px}.seo-enrich strong{color:#fff}.seo-enrich a{color:#e53935}'
         '.seo-enrich .se-info{background:#111;border-left:4px solid #e53935;border-radius:0 10px 10px 0;padding:16px 20px;margin-bottom:20px}'
         '.seo-enrich .se-info p{margin:0}'
         '.seo-enrich .se-table{overflow-x:auto;margin-bottom:20px}'
         '.seo-enrich table{width:100%;min-width:520px;border-collapse:collapse;font-size:0.86rem;background:#111;border:1px solid #1e1e1e;border-radius:10px}'
         '.seo-enrich th,.seo-enrich td{padding:12px 16px;border-bottom:1px solid #1a1a1a;text-align:left;color:#aaa;vertical-align:top}'
         '.seo-enrich th{color:#fff;font-weight:700}'
         '.seo-enrich .se-faq{display:grid;gap:12px}'
         '.seo-enrich .se-faq div{background:#111;border:1px solid #1e1e1e;border-radius:10px;padding:20px}'
         '.seo-enrich .se-faq h3{color:#fff;font-weight:700;font-size:0.95rem;margin-bottom:8px}'
         '.seo-enrich .se-faq p{color:#8c8c8c;font-size:0.88rem;line-height:1.7;margin:0}</style>')

START, END = '<!-- seo-enrich -->', '<!-- /seo-enrich -->'


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def anchor(title):
    s = strip_tags(title).lower()
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        s = s.replace(a, b)
    return 'mehr-' + re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:50]


def render_block(b):
    kind = b[0]
    if kind == 'p':
        return f'<p>{b[1]}</p>'
    if kind in ('ul', 'ol'):
        return f'<{kind}>' + ''.join(f'<li>{x}</li>' for x in b[1]) + f'</{kind}>'
    if kind == 'info':
        return f'<div class="se-info"><p>{b[1]}</p></div>'
    if kind == 'table':
        head, rows = b[1], b[2]
        out = '<div class="se-table"><table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>'
        out += ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
        return out + '</tbody></table></div>'
    raise ValueError(kind)


def render(spec):
    out = [START, STYLE]
    for h, blocks in spec.get('sections', []):
        out.append(f'<section class="seo-enrich" id="{anchor(h)}"><h2>{h}</h2>')
        out.extend(render_block(b) for b in blocks)
        out.append('</section>')
    if spec.get('faq'):
        out.append(f'<section class="seo-enrich" id="mehr-fragen"><h2>{spec.get("faq_title", "Weitere Fragen")}</h2><div class="se-faq">')
        out.extend(f'<div><h3>{q}</h3><p>{a}</p></div>' for q, a in spec['faq'])
        out.append('</div></section>')
    out.append(END)
    return '\n'.join(out) + '\n'


LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)


def find_faq(obj):
    if isinstance(obj, dict):
        if obj.get('@type') == 'FAQPage':
            return obj
        for v in obj.values():
            r = find_faq(v)
            if r:
                return r
    if isinstance(obj, list):
        for v in obj:
            r = find_faq(v)
            if r:
                return r
    return None


def bump_modified(obj):
    if isinstance(obj, dict):
        if 'dateModified' in obj:
            obj['dateModified'] = UPDATED_ISO
        for v in obj.values():
            bump_modified(v)
    elif isinstance(obj, list):
        for v in obj:
            bump_modified(v)


def update_schema(page, spec, canon):
    faq_done = False
    new_q = [{'@type': 'Question', 'name': strip_tags(q),
              'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in spec.get('faq', [])]

    def repl(m):
        nonlocal faq_done
        raw = m.group(2)
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            return m.group(0)
        if isinstance(obj, dict) and obj.get('@id', '').endswith(('#seo-enrich-app', '#seo-enrich-faq')):
            return ''  # rebuilt below
        changed = False
        faq = find_faq(obj)
        if faq is not None and not faq_done and new_q:
            have = {q.get('name') for q in faq.get('mainEntity', [])}
            add = [q for q in new_q if q['name'] not in have]
            if add:
                faq.setdefault('mainEntity', []).extend(add)
                changed = True
            faq_done = True
        before = json.dumps(obj, ensure_ascii=False, sort_keys=True)
        bump_modified(obj)
        if json.dumps(obj, ensure_ascii=False, sort_keys=True) != before:
            changed = True
        if not changed:
            return m.group(0)
        return m.group(1) + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + m.group(3)

    page = LD_RE.sub(repl, page)
    extra = []
    if new_q and not faq_done:
        extra.append({'@context': 'https://schema.org', '@type': 'FAQPage', '@id': canon + '#seo-enrich-faq', 'mainEntity': new_q})
    if spec.get('app'):
        a = spec['app']
        app = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', '@id': canon + '#seo-enrich-app',
               'name': a['name'], 'applicationCategory': a.get('category', 'MultimediaApplication'),
               'operatingSystem': a['os'], 'inLanguage': 'de-DE', 'url': canon}
        if a.get('free'):
            app['offers'] = {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}
        if a.get('publisher'):
            app['publisher'] = {'@type': 'Organization', 'name': a['publisher']}
        extra.append(app)
    if extra:
        tags = ''.join('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
                       for o in extra)
        page = page.replace('</head>', tags + '</head>', 1)
    return page


def canonical(page, rel):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', page)
    return m.group(1) if m else 'https://mojo4k.de/' + rel.replace('index.html', '')


def load():
    sys.path.insert(0, HERE)
    specs = {}
    for f in FILES:
        mod = importlib.import_module(f)
        for k, v in mod.ENRICH.items():
            if k in specs:
                raise SystemExit(f'{k} enriched twice ({f})')
            specs[k] = v
    return specs


def apply(rel, spec):
    path = os.path.join(PUBLIC, rel)
    page = open(path, encoding='utf-8').read()
    page = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', page, flags=re.S)
    page = re.sub(r'<script type="application/ld\+json">[^<]*#seo-enrich-(?:app|faq)"[^<]*</script>\n?', '', page)
    block = render(spec)
    for marker in ('<!-- seo-cluster-links -->', '<div class="cta-block">', '<footer'):
        i = page.find(marker)
        if i != -1:
            page = page[:i] + block + page[i:]
            break
    else:
        raise SystemExit(f'{rel}: no insertion point')
    page = update_schema(page, spec, canonical(page, rel))
    open(path, 'w', encoding='utf-8').write(page)


def main():
    specs = load()
    for rel, spec in specs.items():
        if not os.path.isfile(os.path.join(PUBLIC, rel)):
            raise SystemExit(f'missing page {rel}')
        apply(rel, spec)
    print(f'enriched {len(specs)} pages')


if __name__ == '__main__':
    main()
