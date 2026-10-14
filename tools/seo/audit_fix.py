#!/usr/bin/env python3
"""Mechanical fixes from the full-site SEO audit (2026-10-13).

Run once from the repo root:  python3 tools/seo/audit_fix.py
Steps: consolidate/rename duplicate pages (301), retire meta-refresh plan stubs (301),
point internal links at final URLs, normalise <head> tags, rebuild FAQPage JSON-LD
from the FAQ visitors see, repair the templated "Was Sie wissen sollten" block, fix
place schema, regenerate sitemap.xml.
"""
import json
import os
import re
import shutil
import sys
from urllib.parse import quote, unquote, urlparse

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
import faqlib  # noqa: E402
import places  # noqa: E402

PUB = audit.PUB
DOMAIN = audit.DOMAIN
TODAY = '2026-10-13'

# ── 1. duplicate pages ───────────────────────────────────────────────────────
# Same place or same intent as another page: 301 to the page that stays.
CONSOLIDATE = {
    'iptv-hamm-2': 'iptv-hamm', 'iptv-moers-2': 'iptv-moers', 'iptv-tübingen-2': 'iptv-tuebingen',
    'iptv-görlitz-sa': 'iptv-goerlitz', 'iptv-hildesheim-ns': 'iptv-hildesheim', 'iptv-jena-th': 'iptv-jena',
    'iptv-salzgitter-ns': 'iptv-salzgitter', 'iptv-wolfsburg-ns': 'iptv-wolfsburg', 'iptv-flensburg-sh': 'iptv-flensburg',
    'iptv-muelheim-ruhr': 'iptv-muelheim', 'iptv-chemnitz-2': 'iptv-plauen', 'iptv-offenbach-2': 'iptv-hanau',
    'iptv-hamburg-region': 'iptv-hamburg', 'iptv-bremen-region': 'iptv-bremen', 'iptv-hessen-land': 'iptv-hessen',
    'iptv-niedersachsen-land': 'iptv-niedersachsen', 'iptv-brandenburg-land': 'iptv-brandenburg',
    'iptv-sachsen-land': 'iptv-sachsen', 'iptv-bw': 'iptv-badenwuerttemberg', 'iptv-sofort-aktiv': 'iptv-sofort',
    'iptv-saarland-region': 'iptv-saarland',
}
# Page content is fine but the slug is wrong (non-ASCII, or names a different town).
RENAME = {
    'iptv-böblingen': 'iptv-boeblingen', 'iptv-fürstenfeldbruck': 'iptv-fuerstenfeldbruck',
    'iptv-göppingen': 'iptv-goeppingen', 'iptv-gütersloh': 'iptv-guetersloh', 'iptv-ibbenbüren': 'iptv-ibbenbueren',
    'iptv-lüneburg': 'iptv-lueneburg', 'iptv-mühlhausen': 'iptv-muehlhausen', 'iptv-neumünster': 'iptv-neumuenster',
    'iptv-nürtingen': 'iptv-nuertingen', 'iptv-rüsselsheim': 'iptv-ruesselsheim',
    'iptv-schwäbisch-gmünd': 'iptv-schwaebisch-gmuend', 'iptv-schwäbisch-hall': 'iptv-schwaebisch-hall',
    'iptv-sprockhövel': 'iptv-sprockhoevel', 'iptv-tübingen': 'iptv-tuebingen', 'iptv-völklingen': 'iptv-voelklingen',
    'iptv-überlingen': 'iptv-ueberlingen', 'iptv-lüdenscheid-2': 'iptv-altena', 'iptv-koblenz-2': 'iptv-bad-kreuznach',
    'iptv-dresden-ost': 'iptv-pirna', 'iptv-bedburg': 'iptv-bergheim',
}
# /iptv-saarland/ showed Saarbrücken (which has its own page); the Bundesland page takes its URL.
REPLACE_CONTENT = {'iptv-saarland': 'iptv-saarland-region'}

STATIC_LINKS = {
    '/index.html': '/', '/preise.html': '/preise/', '/faqs.html': '/faqs/', '/kontakt.html': '/kontakt/',
    '/impressum.html': '/impressum', '/datenschutz.html': '/datenschutz', '/kostenlos-testen.html': '/kostenlos-testen',
    '/whatsapp-kontakt.html': '/support/nachricht', '/whatsapp-kontakt': '/support/nachricht',
}


def read(rel):
    return open(os.path.join(PUB, rel), encoding='utf-8').read()


def write(rel, s):
    open(os.path.join(PUB, rel), 'w', encoding='utf-8').write(s)


def url_variants(slug):
    enc = quote(slug)
    out = {f'{DOMAIN}/{slug}/', f'{DOMAIN}/{slug}'}
    if enc != slug:
        out |= {f'{DOMAIN}/{enc}/', f'{DOMAIN}/{enc}'}
    return out


def move_pages(log):
    for dst, src in REPLACE_CONTENT.items():
        s = read(f'{src}/index.html')
        for v in sorted(url_variants(src), key=len, reverse=True):
            s = s.replace(v, f'{DOMAIN}/{dst}' + ('/' if v.endswith('/') else ''))
        write(f'{dst}/index.html', s)
        log.append(f'content of /{src}/ now served at /{dst}/')
    for old, new in RENAME.items():
        src = os.path.join(PUB, old)
        if not os.path.isdir(src):
            continue
        s = read(f'{old}/index.html')
        for v in sorted(url_variants(old), key=len, reverse=True):
            s = s.replace(v, f'{DOMAIN}/{new}' + ('/' if v.endswith('/') else ''))
        os.makedirs(os.path.join(PUB, new), exist_ok=True)
        write(f'{new}/index.html', s)
        shutil.rmtree(src)
        log.append(f'renamed /{old}/ -> /{new}/')
    for old in CONSOLIDATE:
        src = os.path.join(PUB, old)
        if os.path.isdir(src):
            shutil.rmtree(src)
            log.append(f'consolidated /{old}/ -> /{CONSOLIDATE[old]}/')
    # meta-refresh stubs for checkout pages
    for f in sorted(os.listdir(PUB)):
        if re.match(r'^\d+-(monat|monate|jahr)-\d+-gerate?-iptv\.html$', f):
            os.remove(os.path.join(PUB, f))
            log.append(f'retired stub /{f}')


def redirect_rules():
    rules = []
    def add(src, dst):
        rules.append((src, dst))
        enc = quote(src)
        if enc != src:
            rules.append((enc, dst))
    for old, new in list(CONSOLIDATE.items()) + list(RENAME.items()):
        add(f'/{old}/', f'/{new}/')
        add(f'/{old}', f'/{new}/')
    for m in ['1-monat', '3-monate', '6-monate', '1-jahr']:
        for n in range(1, 11):
            base = f'/{m}-{n}-gerat' if n == 1 else f'/{m}-{n}-gerate'
            add(f'{base}-iptv', base)
            add(f'{base}-iptv.html', base)
    add('/impressum.html', '/impressum')
    add('/datenschutz.html', '/datenschutz')
    return rules


def update_redirects(log):
    path = os.path.join(PUB, '_redirects')
    txt = open(path, encoding='utf-8').read()
    moved = {f'/{o}/': f'/{n}/' for o, n in list(CONSOLIDATE.items()) + list(RENAME.items())}
    moved.update({f'/{o}': f'/{n}/' for o, n in list(CONSOLIDATE.items()) + list(RENAME.items())})
    lines, fixed = [], 0
    existing = set()
    for line in txt.split('\n'):
        parts = line.split()
        if len(parts) >= 3 and not line.lstrip().startswith('#'):
            tgt = parts[1]
            if tgt in moved:
                line = line.replace(tgt, moved[tgt], 1)
                fixed += 1
            existing.add(parts[0])
        lines.append(line)
    new = [f'{s}  {d}  301' for s, d in redirect_rules() if s not in existing]
    out = '\n'.join(lines).rstrip('\n') + '\n\n# ── SEO audit 2026-10-13: duplicate pages, renamed slugs, retired plan stubs ──\n' + '\n'.join(new) + '\n'
    open(path, 'w', encoding='utf-8').write(out)
    log.append(f'_redirects: {len(new)} rules added, {fixed} targets repointed')


# ── 2. internal links ────────────────────────────────────────────────────────
def build_resolver():
    files = list(audit.html_files())
    idx = audit.build_path_index(files)
    red = audit.load_redirects()
    fset = set(files)

    def final(path):
        p = unquote(path)
        if p in STATIC_LINKS:
            return STATIC_LINKS[p]
        if re.match(r'^/\d+-(monat|monate|jahr)-\d+-gerate?\.html$', p):
            return p[:-5]
        st, fin = audit.resolve(p, idx, red)
        if st != 'dead' and isinstance(fin, str) and fin in fset:
            tgt = urlparse(audit.url_for(fin)).path
            return tgt if tgt != p else None
        return None
    return final


HREF_RE = re.compile(r'href="([^"]*)"')


def fix_links(s, rel, final):
    n = [0]

    def repl(m):
        h = m.group(1)
        if h.startswith(('mailto:', 'tel:', 'javascript:', '#', 'whatsapp:')):
            return m.group(0)
        pu = urlparse(h)
        if pu.netloc and pu.netloc not in ('mojo4k.de', 'www.mojo4k.de'):
            return m.group(0)
        path = pu.path
        if not path:
            return m.group(0)
        if not path.startswith('/'):
            path = os.path.normpath(os.path.join('/' + os.path.dirname(rel), path)) + ('/' if path.endswith('/') else '')
        tgt = final(path)
        if not tgt:
            return m.group(0)
        new = tgt + (('?' + pu.query) if pu.query else '') + (('#' + pu.fragment) if pu.fragment else '')
        if pu.netloc:
            new = DOMAIN + new
        if new == h:
            return m.group(0)
        n[0] += 1
        return f'href="{new}"'
    return HREF_RE.sub(repl, s), n[0]


# ── 3. <head> ────────────────────────────────────────────────────────────────
def esc(v):
    return v.replace('&', '&amp;').replace('"', '&quot;').replace('&amp;amp;', '&amp;')


def unesc(v):
    return v.replace('&amp;', '&').replace('&quot;', '"')


def meta_re(attr, key):
    return re.compile(r'<meta\s+' + attr + r'="' + re.escape(key) + r'"\s+content="([^"]*)"\s*/?>')


def get_meta(s, attr, key):
    m = meta_re(attr, key).search(s)
    return unesc(m.group(1)) if m else None


def set_meta(s, attr, key, value, anchor):
    tag = f'<meta {attr}="{key}" content="{esc(value)}"/>'
    rx = meta_re(attr, key)
    if rx.search(s):
        return rx.sub(lambda m: tag, s, count=1)
    return s.replace(anchor, anchor + '\n' + tag, 1)


def fix_head(s, url, lang):
    head_end = s.find('</head>')
    head, rest = s[:head_end], s[head_end:]
    title_m = re.search(r'<title>(.*?)</title>', head, re.S)
    title = unesc(title_m.group(1).strip()) if title_m else ''
    desc = get_meta(head, 'name', 'description') or ''
    # canonical
    if re.search(r'<link rel="canonical"[^>]*>', head):
        head = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{url}"/>', head, count=1)
    else:
        head = head.replace(title_m.group(0), title_m.group(0) + f'\n<link rel="canonical" href="{url}"/>', 1)
    # hreflang: one language per page, self-referencing, plus x-default
    head = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>', '', head)
    canon_tag = f'<link rel="canonical" href="{url}"/>'
    hl = 'en' if lang == 'en' else 'de'
    head = head.replace(canon_tag, canon_tag + f'\n<link rel="alternate" hreflang="{hl}" href="{url}"/>'
                        f'\n<link rel="alternate" hreflang="x-default" href="{url}"/>', 1)
    anchor = f'<link rel="alternate" hreflang="x-default" href="{url}"/>'
    og_title = get_meta(head, 'property', 'og:title') or title
    og_desc = get_meta(head, 'property', 'og:description') or desc
    og_img = get_meta(head, 'property', 'og:image') or ''
    if not og_img or 'og-iptv-stick-test' in og_img or 'og-bundesliga' in og_img:
        og_img = f'{DOMAIN}/iptv-kaufen.jpg'
    vals = [
        ('property', 'og:type', get_meta(head, 'property', 'og:type') or 'website'),
        ('property', 'og:site_name', 'MOJO4K.DE'),
        ('property', 'og:locale', 'en_GB' if lang == 'en' else 'de_DE'),
        ('property', 'og:url', url),
        ('property', 'og:title', og_title),
        ('property', 'og:description', og_desc),
        ('property', 'og:image', og_img),
    ]
    if og_img.endswith('/iptv-kaufen.jpg'):
        vals += [('property', 'og:image:width', '1200'), ('property', 'og:image:height', '630')]
    vals += [('property', 'og:image:alt', get_meta(head, 'property', 'og:image:alt') or og_title),
             ('name', 'twitter:card', 'summary_large_image'),
             ('name', 'twitter:title', get_meta(head, 'name', 'twitter:title') or og_title),
             ('name', 'twitter:description', get_meta(head, 'name', 'twitter:description') or og_desc),
             ('name', 'twitter:image', og_img)]
    for attr, key, v in vals:
        if v:
            head = set_meta(head, attr, key, v, anchor)
    return head + rest


# ── 4. city block, place schema ──────────────────────────────────────────────
CITY_BLOCK_RE = re.compile(r'<div id="city-local-block".*?</div>\s*</div>\s*</div>\n?', re.S)


def nearby(slug, code, n=6):
    same = sorted(k for k, (nm, c) in places.PLACES.items() if c == code and k != slug
                  and os.path.isdir(os.path.join(PUB, k)) and k not in places.CITY_STATES)
    if not same:
        return []
    i = sum(ord(ch) for ch in slug) % len(same)  # stable, different window per page
    return [(k, places.PLACES[k][0]) for k in (same[i:] + same[:i])[:n]]


def city_block(slug, name, code):
    state = places.STATES[code]
    hub = places.STATE_HUB.get(code)
    abroad = code in ('CH', 'AT')
    if abroad:
        net = (f'In {name} laufen die Streams über jeden Breitband-, Kabel- oder Glasfaseranschluss. '
               f'Für HD reichen stabile 16 Mbit/s, für 4K planen Sie besser 50 Mbit/s ein.')
        tv = (f'Deutsche Sender wie ARD, ZDF, RTL und ProSieben sind auch in {name} im Paket – '
              f'dazu Sport, Filme und Serien. Die Bedienung bleibt auf Deutsch, der Support antwortet per WhatsApp.')
    else:
        net = (f'In {name} funktioniert IPTV über DSL, Kabel und Glasfaser – egal ob Telekom, Vodafone, O2, 1&1 '
               f'oder ein regionaler Glasfaser-Anbieter. Für HD reichen stabile 16 Mbit/s, für 4K etwa 50 Mbit/s.')
        tv = (f'Alle regionalen Programme aus {state} und die großen deutschen Sender laufen live, mit '
              f'Programmführer (EPG) und Catch-Up – auf Fire TV Stick, Smart TV, Handy oder PC.')
    links = nearby(slug, code)
    li = ''.join(f'<a href="/{k}/" style="display:inline-block;margin:0 8px 8px 0;padding:6px 12px;background:#0d0d0d;border:1px solid #222;border-radius:20px;color:#ddd;font-size:0.8rem">IPTV {nm}</a>' for k, nm in links)
    hub_link = ''
    if hub and hub != slug:
        label = f'IPTV {state}'
        hub_link = f' Alle Orte in {state} im Überblick: <a href="/{hub}/" style="color:#e53935">{label}</a>.'
    card = ('<div style="background:#0d0d0d;border-radius:8px;padding:14px">'
            '<h3 style="color:#fff;font-size:0.85rem;font-weight:700;margin-bottom:5px">{}</h3>'
            '<p style="color:#8c8c8c;font-size:0.8rem;line-height:1.55">{}</p></div>')
    html = (
        '<div id="city-local-block" style="margin-bottom:32px;padding:22px;background:#111;border:1px solid #1e1e1e;border-radius:12px">\n'
        f'<h2 style="font-size:1.2rem;font-weight:900;margin-bottom:14px">📡 IPTV in {name} – Was Sie wissen sollten</h2>\n'
        '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px">\n'
        + card.format(f'🌐 Internet in {name}', net) + '\n'
        + card.format('📺 Sender &amp; Geräte', tv) + '\n'
        + card.format('⚡ Aktivierung', 'Paket wählen oder 24h gratis testen, Zugangsdaten per WhatsApp erhalten, '
                      'in der App eintragen – fertig. Fragen beantwortet der deutschsprachige Support.') + '\n'
        '</div>\n'
    )
    if links:
        html += (f'<p style="color:#8c8c8c;font-size:0.85rem;margin:18px 0 10px">IPTV in der Nähe von {name}:</p>\n'
                 f'<div>{li}</div>\n')
    if hub_link:
        html += f'<p style="color:#8c8c8c;font-size:0.85rem;margin:8px 0 0">{hub_link.strip()}</p>\n'
    html += '</div>\n'
    return html


def place_of(slug):
    if slug in places.PLACES:
        return places.PLACES[slug]
    if slug in places.REGIONS:
        return places.REGIONS[slug]
    return None


def fix_place_schema(s, slug):
    """Service.areaServed must name a real place; fake LocalBusiness phone/postcode are dropped."""
    pl = place_of(slug)

    def repl(m):
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except Exception:
            return m.group(0)
        changed = False
        nodes = data.get('@graph', [data]) if isinstance(data, dict) else []
        for n in nodes:
            if not isinstance(n, dict):
                continue
            t = n.get('@type')
            if t == 'Service' and isinstance(n.get('areaServed'), dict) and n['areaServed'].get('@type') == 'City':
                if pl and slug in places.PLACES and pl[1] not in ('CH', 'AT'):
                    want = {'@type': 'City', 'name': pl[0],
                            'containedInPlace': {'@type': 'State', 'name': places.STATES[pl[1]]}}
                elif pl and pl[1] in ('CH', 'AT'):
                    want = {'@type': 'City', 'name': pl[0], 'containedInPlace': {'@type': 'Country', 'name': places.STATES[pl[1]]}}
                elif pl:
                    want = {'@type': 'State', 'name': pl[0]} if slug != 'iptv-ruhrgebiet' and slug != 'iptv-rhein-main' else {'@type': 'Place', 'name': pl[0]}
                else:
                    want = {'@type': 'Country', 'name': 'Deutschland'}
                if n['areaServed'] != want:
                    n['areaServed'] = want
                    changed = True
            if t == 'LocalBusiness':
                if n.pop('telephone', None) is not None:
                    changed = True
                addr = n.get('address')
                if isinstance(addr, dict) and addr.pop('postalCode', None) is not None:
                    changed = True
        if not changed:
            return m.group(0)
        return m.group(1) + faqlib.dump(data) + m.group(3)
    return faqlib.LD_RE.sub(repl, s)


# ── 5. sitemap ───────────────────────────────────────────────────────────────
def regen_sitemap(changed_urls, log):
    path = os.path.join(PUB, 'sitemap.xml')
    old = open(path, encoding='utf-8').read()
    prev = {}
    for m in re.finditer(r'<url>\s*<loc>([^<]+)</loc>(.*?)</url>', old, re.S):
        loc = unquote(m.group(1))
        lm = re.search(r'<lastmod>([^<]+)</lastmod>', m.group(2))
        cf = re.search(r'<changefreq>([^<]+)</changefreq>', m.group(2))
        pr = re.search(r'<priority>([^<]+)</priority>', m.group(2))
        prev[loc] = (lm.group(1) if lm else TODAY, cf.group(1) if cf else 'monthly', pr.group(1) if pr else '0.70')
    rows = []
    for rel in sorted(audit.html_files()):
        s = read(rel)
        if re.search(r'<meta name="robots" content="[^"]*noindex', s):
            continue
        url = audit.url_for(rel)
        lm, cf, pr = prev.get(url, (TODAY, 'monthly', '0.70'))
        if url in changed_urls:
            lm = TODAY
        rows.append((url, lm, cf, pr))
    order = {u: i for i, u in enumerate(prev)}
    rows.sort(key=lambda r: (order.get(r[0], 10 ** 6), r[0]))
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lm, cf, pr in rows:
        loc = quote(url, safe=':/')
        out.append(f'  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>')
    out.append('</urlset>')
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    log.append(f'sitemap: {len(rows)} URLs (was {len(prev)})')


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    log = []
    move_pages(log)
    update_redirects(log)
    final = build_resolver()
    stats = {'links': 0, 'faq': 0, 'faq_dropped': 0, 'head': 0, 'city_fixed': 0, 'city_removed': 0, 'schema': 0}
    changed_urls = set()
    for rel in sorted(audit.html_files()):
        s0 = s = read(rel)
        s, n = fix_links(s, rel, final)
        stats['links'] += n
        noindex = bool(re.search(r'<meta name="robots" content="[^"]*noindex', s))
        if not noindex:
            url = audit.url_for(rel)
            lang_m = re.search(r'<html[^>]*lang="([a-z]+)"', s)
            lang = lang_m.group(1) if lang_m else 'de'
            h = fix_head(s, url, lang)
            if h != s:
                stats['head'] += 1
            s = h
            slug = rel.split('/')[0] if '/' in rel else ''
            # templated "Was Sie wissen sollten" block
            if CITY_BLOCK_RE.search(s):
                pl = places.PLACES.get(slug)
                if pl:
                    s = CITY_BLOCK_RE.sub(lambda m: city_block(slug, pl[0], pl[1]), s, count=1)
                    stats['city_fixed'] += 1
                elif slug in places.REGIONS:
                    nm, code = places.REGIONS[slug]
                    s = CITY_BLOCK_RE.sub(lambda m: city_block(slug, nm, code), s, count=1)
                    stats['city_fixed'] += 1
                else:
                    s = CITY_BLOCK_RE.sub('', s, count=1)
                    stats['city_removed'] += 1
            s2 = fix_place_schema(s, slug)
            if s2 != s:
                stats['schema'] += 1
            s = s2
            # FAQ schema mirrors the visible FAQ
            pairs = faqlib.visible_faq(BeautifulSoup(s, 'lxml'))
            pairs = [(re.sub(r'\s*[+−–▾▼›]\s*$', '', q), a) for q, a in pairs]
            if len(pairs) >= 2:
                s, ch = faqlib.rewrite_faq_schema(s, pairs)
                stats['faq'] += ch
            elif '"FAQPage"' in s:
                s, ch = faqlib.rewrite_faq_schema(s, [])
                stats['faq_dropped'] += ch
                log.append(f'FAQ schema removed (no visible FAQ): {rel}')
            if s != s0:
                changed_urls.add(url)
        if s != s0:
            write(rel, s)
    # nav.js
    nav = os.path.join(PUB, 'nav.js')
    js = open(nav, encoding='utf-8').read()
    js2, n = fix_links(js, 'nav.js', final)
    if js2 != js:
        open(nav, 'w', encoding='utf-8').write(js2)
        stats['links'] += n
    regen_sitemap(changed_urls, log)
    print('\n'.join(log))
    print(stats)


if __name__ == '__main__':
    main()
