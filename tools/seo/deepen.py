#!/usr/bin/env python3
"""Deepen thin keyword pages with hand-written sections (SEO audit 2026-10-13).

Content lives in deepen_*.py (dict DEEPEN):
    'slug': {
        'head': {'title': ..., 'desc': ...},        # optional new <title>/description (+ OG/Twitter copies)
        'h1': '...',                                 # optional new H1 text
        'intro': '...',                              # optional: replaces the paragraph right after the H1
        'drop': [regex, ...],                        # optional: template sections to remove (whole match)
        'sections': [(h2, [blocks])],                # blocks as in enrich.py: ('p', html) ('ul', [..]) ('ol', [..]) ('info', html) ('table', head, rows)
        'faq_title': '...', 'faq': [(q, a)],
    }
Inserted between <!-- seo-deepen --> markers before the link blocks / CTA. Idempotent.
FAQ schema is rebuilt afterwards by sync_faq.py from what is visible.
"""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
from enrich import STYLE, anchor, render_block  # noqa: E402

START, END = '<!-- seo-deepen -->', '<!-- /seo-deepen -->'
FILES = ['deepen_apps', 'deepen_topics']


def esc_attr(v):
    return v.replace('&', '&amp;').replace('"', '&quot;')


def render(spec, page):
    out = [START]
    if '.seo-enrich{' not in page:
        out.append(STYLE)
    for h, blocks in spec.get('sections', []):
        out.append(f'<section class="seo-enrich" id="{anchor(h)}"><h2>{h}</h2>')
        out.extend(render_block(b) for b in blocks)
        out.append('</section>')
    if spec.get('faq'):
        out.append(f'<section class="seo-enrich" id="mehr-fragen-{anchor(spec.get("faq_title", "x"))[5:]}">'
                   f'<h2>{spec.get("faq_title", "Weitere Fragen")}</h2><div class="se-faq">')
        out.extend(f'<div><h3>{q}</h3><p>{a}</p></div>' for q, a in spec['faq'])
        out.append('</div></section>')
    out.append(END)
    return '\n'.join(out) + '\n'


def set_head(page, title=None, desc=None):
    if title:
        page = re.sub(r'<title>.*?</title>', lambda m: f'<title>{title.replace("&", "&amp;")}</title>', page, count=1, flags=re.S)
        for attr, key in (('property', 'og:title'), ('name', 'twitter:title'), ('property', 'og:image:alt')):
            page = re.sub(r'(<meta ' + attr + '="' + key + r'" content=")[^"]*(")', lambda m: m.group(1) + esc_attr(title) + m.group(2), page, count=1)
    if desc:
        for attr, key in (('name', 'description'), ('property', 'og:description'), ('name', 'twitter:description')):
            page = re.sub(r'(<meta ' + attr + '="' + key + r'" content=")[^"]*(")', lambda m: m.group(1) + esc_attr(desc) + m.group(2), page, count=1)
    return page


def apply(slug, spec):
    path = os.path.join(audit.PUB, slug, 'index.html')
    page = open(path, encoding='utf-8').read()
    page = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', page, flags=re.S)
    head = spec.get('head', {})
    page = set_head(page, head.get('title'), head.get('desc'))
    if spec.get('h1'):
        page, n = re.subn(r'(<h1[^>]*>).*?(</h1>)', lambda m: m.group(1) + spec['h1'] + m.group(2), page, count=1, flags=re.S)
        assert n, slug
    if spec.get('intro'):
        page, n = re.subn(r'(</h1>\s*<p[^>]*>).*?(</p>)', lambda m: m.group(1) + spec['intro'] + m.group(2), page, count=1, flags=re.S)
        assert n, slug + ' intro'
    for rx in spec.get('drop', []):
        page, n = re.subn(rx, '', page, count=1, flags=re.S)
        if not n:
            print(f'{slug}: drop pattern not found (already removed?): {rx[:50]}')
    block = render(spec, page)
    for marker in ('<!-- seo-cluster-links -->', '<!-- seo-sources -->', '<!-- seo-related -->', '<div class="cta-block">', '<footer'):
        i = page.find(marker)
        if i != -1:
            page = page[:i] + block + page[i:]
            break
    else:
        raise SystemExit(f'{slug}: no insertion point')
    open(path, 'w', encoding='utf-8').write(page)


def main():
    only = set(sys.argv[1:])
    n = 0
    for f in FILES:
        try:
            mod = importlib.import_module(f)
        except ModuleNotFoundError:
            continue
        for slug, spec in mod.DEEPEN.items():
            if only and slug not in only:
                continue
            apply(slug, spec)
            n += 1
    print('deepened', n, 'pages')


if __name__ == '__main__':
    main()
