#!/usr/bin/env python3
"""Generate the SEO cluster pages in public/<slug>/index.html.

Page content lives in pages_*.py (one list PAGES per batch). The nav, shared
CSS and footer are copied from public/iptv-smarters-pro/index.html so every
generated page matches the existing design exactly.

Usage:  python3 tools/seo/build.py            # build all pages
        python3 tools/seo/build.py --check    # build + validate only
"""
import html
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PUBLIC = os.path.join(ROOT, 'public')
DOMAIN = 'https://mojo4k.de'
UPDATED_ISO = '2026-10-11'
UPDATED_DE = '11.10.2026'

sys.path.insert(0, HERE)
BATCHES = ['pages_batch1', 'pages_batch2', 'pages_batch3']


def load_pages():
    pages = []
    for b in BATCHES:
        try:
            mod = importlib.import_module(b)
        except ModuleNotFoundError:
            continue
        pages.extend(mod.PAGES)
    return pages


# ── design parts copied from the reference page ──────────────────────────────
REF = open(os.path.join(PUBLIC, 'iptv-smarters-pro', 'index.html'), encoding='utf-8').read()
HEAD_CSS = REF[REF.index('<style id="shared-nav-css">'):REF.index('</head>')]
NAV = REF[REF.index('<body>') + len('<body>'):REF.index('<div class="page-content">')]
FOOTER = REF[REF.index('<footer>'):REF.index('</body>')]

EXTRA_CSS = """<style>
.prose{margin-bottom:56px}
.prose p{color:#aaa;font-size:0.95rem;line-height:1.8;margin-bottom:14px}
.prose ul,.prose ol{color:#aaa;font-size:0.95rem;line-height:1.8;margin:0 0 16px 22px}
.prose li{margin-bottom:6px}
.prose strong{color:#fff}
.prose a,.faq-item a,.step-item a,.card a,.info-box a,.page-intro a{color:#e53935}
.updated{color:#666;font-size:0.8rem;margin:-28px 0 32px}
.toc{background:#111;border:1px solid #1e1e1e;border-radius:12px;padding:20px 24px;margin-bottom:48px}
.toc h2{font-size:0.8rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#888;margin-bottom:10px}
.toc ol{margin-left:20px;color:#aaa;font-size:0.9rem;line-height:1.9}
.toc a{color:#ccc}
.hub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin-bottom:56px}
.hub-card{background:#111;border:1px solid #1e1e1e;border-radius:10px;padding:18px;display:block;transition:border-color .2s}
.hub-card:hover{border-color:rgba(229,57,53,0.5)}
.hub-card strong{display:block;color:#fff;font-size:0.95rem;margin-bottom:6px}
.hub-card span{color:#8c8c8c;font-size:0.82rem;line-height:1.6}
.table-wrap{overflow-x:auto;margin-bottom:56px}
.table-wrap .compare-table{min-width:560px;margin-bottom:0}
</style>"""


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def url(slug):
    return f'{DOMAIN}/{slug}/'


# ── blocks ───────────────────────────────────────────────────────────────────
def render_block(b):
    kind = b[0]
    if kind == 'p':
        return f'<p>{b[1]}</p>'
    if kind == 'ul':
        return '<ul>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ul>'
    if kind == 'ol':
        return '<ol>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ol>'
    if kind == 'info':
        return f'<div class="info-box"><p>{b[1]}</p></div>'
    if kind == 'steps':
        out = ['<div class="step-list">']
        for i, (t, d) in enumerate(b[1], 1):
            out.append(f'<div class="step-item"><div class="step-num">{i:02d}</div><div><h3>{t}</h3><p>{d}</p></div></div>')
        out.append('</div>')
        return '\n'.join(out)
    if kind == 'cards':
        out = ['<div class="grid-cards">']
        for t, d in b[1]:
            out.append(f'<div class="card"><div class="card-head"><h3>{t}</h3></div><p>{d}</p></div>')
        out.append('</div>')
        return '\n'.join(out)
    if kind == 'table':
        head, rows = b[1], b[2]
        cols = f'grid-template-columns:repeat({len(head)},1fr)'
        out = ['<div class="table-wrap"><div class="compare-table">']
        out.append(f'<div class="compare-row" style="{cols}">' + ''.join(
            f'<span class="compare-head {"col-label" if i == 0 else "col-a"}">{h}</span>' for i, h in enumerate(head)) + '</div>')
        for r in rows:
            out.append(f'<div class="compare-row" style="{cols}">' + ''.join(
                f'<span class="{"col-label" if i == 0 else "col-a"}">{c}</span>' for i, c in enumerate(r)) + '</div>')
        out.append('</div></div>')
        return '\n'.join(out)
    if kind == 'hub':
        out = ['<div class="hub-grid">']
        for slug, name, d in b[1]:
            out.append(f'<a class="hub-card" href="/{slug}/"><strong>{name}</strong><span>{d}</span></a>')
        out.append('</div>')
        return '\n'.join(out)
    raise ValueError(kind)


def anchor_id(title):
    s = strip_tags(title).lower()
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60]


def render_page(p, names):
    slug = p['slug']
    canon = url(slug)
    crumbs = [('Startseite', DOMAIN + '/')]
    if p.get('parent'):
        crumbs.append((names[p['parent']], url(p['parent'])))
    crumbs.append((p['crumb'], canon))

    faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', '@id': canon + '#faq',
              'mainEntity': [{'@type': 'Question', 'name': strip_tags(q),
                              'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in p['faq']]}
    bc_ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', '@id': canon + '#breadcrumb',
             'itemListElement': [{'@type': 'ListItem', 'position': i, 'name': n, 'item': u}
                                 for i, (n, u) in enumerate(crumbs, 1)]}
    page_ld = {'@context': 'https://schema.org', '@type': p.get('ld_type', 'WebPage'), '@id': canon + '#webpage',
               'url': canon, 'name': strip_tags(p['title']), 'headline': strip_tags(p['h1']),
               'description': p['desc'], 'inLanguage': 'de-DE', 'dateModified': UPDATED_ISO,
               'datePublished': p.get('published', UPDATED_ISO),
               'isPartOf': {'@type': 'WebSite', 'name': 'MOJO4K.DE', 'url': DOMAIN + '/'},
               'publisher': {'@type': 'Organization', 'name': 'MOJO4K.DE', 'url': DOMAIN + '/',
                             'logo': {'@type': 'ImageObject', 'url': DOMAIN + '/apple-touch-icon.png'}},
               'breadcrumb': {'@id': canon + '#breadcrumb'}}
    if p.get('ld_type') == 'CollectionPage':
        page_ld.pop('headline')

    def ld(o):
        return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '</script>'

    title = p['title']
    og_desc = p.get('og_desc', p['desc'])
    head = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{esc(p['desc'])}"/>
<meta name="keywords" content="{esc(', '.join(p['keywords']))}"/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1"/>
<link rel="alternate" hreflang="de" href="{canon}"/>
<link rel="alternate" hreflang="x-default" href="{canon}"/>
<link rel="canonical" href="{canon}"/>
<meta property="og:title" content="{esc(title)}"/>
<meta property="og:description" content="{esc(og_desc)}"/>
<meta property="og:url" content="{canon}"/>
<meta property="og:type" content="{'website' if p.get('ld_type') == 'CollectionPage' else 'article'}"/>
<meta property="og:site_name" content="MOJO4K.DE"/>
<meta property="og:locale" content="de_DE"/>
<meta property="og:image" content="{DOMAIN}/iptv-kaufen.jpg"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="MOJO4K.DE – {esc(p['crumb'])}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{esc(title)}"/>
<meta name="twitter:description" content="{esc(og_desc)}"/>
<meta name="twitter:image" content="{DOMAIN}/iptv-kaufen.jpg"/>
<meta name="twitter:image:alt" content="MOJO4K.DE – {esc(p['crumb'])}"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
<meta name="theme-color" content="#140438"/>
{ld(faq_ld)}
{ld(bc_ld)}
{ld(page_ld)}
{HEAD_CSS}{EXTRA_CSS}
</head>
<body>'''

    bc_html = ''.join(
        (f'<li><a href="{u.replace(DOMAIN, "")}">{n}</a></li><li>›</li>' if i < len(crumbs) - 1 else f'<li class="current">{n}</li>')
        for i, (n, u) in enumerate(crumbs))
    body = [NAV, '<div class="page-content">',
            f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{bc_html}</ol></nav>',
            f'<div class="badge"><span>{p["badge"]}</span></div>',
            f'<h1 class="page-h1">{p["h1"]}</h1>',
            f'<p class="page-intro">{p["intro"]}</p>',
            f'<p class="updated">Zuletzt aktualisiert: {UPDATED_DE} · Redaktion MOJO4K.DE</p>']
    if p.get('info'):
        body.append(f'<div class="info-box"><p>{p["info"]}</p></div>')

    sections = p['sections']
    if len(sections) >= 4:
        body.append('<nav class="toc" aria-label="Inhalt"><h2>Inhalt</h2><ol>' + ''.join(
            f'<li><a href="#{anchor_id(h)}">{strip_tags(h)}</a></li>' for h, _ in sections) +
            f'<li><a href="#faq">Häufige Fragen</a></li></ol></nav>')
    for h, blocks in sections:
        body.append(f'<section class="prose" id="{anchor_id(h)}">\n<h2 class="sec-title">{h}</h2>')
        body.extend(render_block(b) for b in blocks)
        body.append('</section>')

    body.append(f'<section style="margin-bottom:56px" id="faq">\n<h2 class="sec-title">{p.get("faq_title", "Häufige Fragen zu " + p["crumb"])}</h2>\n<div class="faq-list">')
    for q, a in p['faq']:
        body.append(f'  <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>')
    body.append('</div>\n</section>')

    cta = p.get('cta', ('MOJO4K.DE – IPTV Deutschland', '50.000+ Kanäle ab €9/Monat',
                        'Kein Vertrag, monatlich kündbar. Zugangsdaten in Minuten – jetzt 24 Stunden gratis testen.'))
    body.append(f'''<div class="cta-block">
  <p class="cta-label">{cta[0]}</p>
  <h2>{cta[1]}</h2>
  <p>{cta[2]}</p>
  <div class="cta-btns">
    <a href="/kostenlos-testen-de" class="btn-primary">24h kostenlos testen</a>
    <a href="/preise-de" class="btn-outline">Preise ansehen</a>
  </div>
</div>''')

    rel = [r for r in p['related'] if r != slug]
    body.append('''
<div style="margin-top:48px;padding:32px;background:#111;border:1px solid #1e1e1e;border-radius:12px">
  <h2 style="font-size:1.1rem;font-weight:700;margin-bottom:16px;color:#fff">Verwandte Seiten</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px">''')
    for r in rel:
        body.append(f'    <a href="/{r}/" style="background:#0d0d0d;border:1px solid #1e1e1e;border-radius:8px;padding:12px 16px;color:#aaa;font-size:0.88rem;display:block">→ {names[r]}</a>')
    body.append('  </div>\n</div>\n</div>\n')
    body.append(FOOTER + '</body>\n</html>\n')
    return head + '\n'.join(body)


# ── names of existing pages we link to (anchor text) ─────────────────────────
EXISTING_NAMES = {
    'preise': 'IPTV Preise', 'iptv-kaufen': 'IPTV kaufen', 'bester-iptv-anbieter': 'Bester IPTV Anbieter',
    'iptv-anbieter-vergleich': 'IPTV Anbieter Vergleich', 'iptv-gratis-testen': 'IPTV gratis testen',
    'iptv-smarters-pro': 'IPTV Smarters Pro', 'iptv-smarters': 'IPTV Smarters', 'iptv-smarters-pro-deutschland': 'Smarters Pro Anleitung',
    'tivimate': 'TiviMate', 'tivimate-premium': 'TiviMate Premium', 'iptv-tivimate-deutschland': 'TiviMate Anleitung',
    'smart-iptv-deutschland': 'Smart IPTV', 'siptv': 'SIPTV', 'ssiptv': 'SS IPTV', 'set-iptv': 'SET IPTV',
    'smartone-iptv': 'SmartOne IPTV', 'xciptv': 'XCIPTV', 'ott-navigator': 'OTT Navigator', 'gse-iptv': 'GSE Smart IPTV',
    'implayer': 'iMPlayer', 'stb-emu': 'STB Emu', 'iptv-kodi': 'IPTV Kodi', 'iptv-plex': 'IPTV Plex',
    'beste-iptv-app': 'Beste IPTV App', 'iptv-app': 'IPTV App', 'iptv-player-android': 'IPTV Player Android',
    'iptv-fire-stick-deutschland': 'IPTV Fire TV Stick', 'fire-tv-stick-iptv': 'Fire TV Stick IPTV', 'iptv-firestick': 'IPTV Firestick',
    'iptv-samsung-tv-deutschland': 'IPTV Samsung TV', 'iptv-lg-tv-deutschland': 'IPTV LG TV', 'iptv-android-box-deutschland': 'IPTV Android Box',
    'iptv-android-tv': 'IPTV Android TV', 'iptv-apple-tv': 'IPTV Apple TV', 'iptv-iphone': 'IPTV iPhone', 'iptv-ipad': 'IPTV iPad',
    'iptv-pc': 'IPTV am PC', 'iptv-windows-11': 'IPTV Windows 11', 'iptv-macbook': 'IPTV MacBook', 'iptv-chromecast-google-tv': 'IPTV Chromecast / Google TV',
    'iptv-nvidia-shield': 'IPTV Nvidia Shield', 'iptv-formuler': 'IPTV Formuler', 'iptv-mag-box': 'IPTV MAG Box',
    'iptv-receiver-deutschland': 'IPTV Receiver', 'iptv-box': 'IPTV Box', 'iptv-stick': 'IPTV Stick', 'iptv-smart-tv': 'IPTV Smart TV',
    'iptv-hisense-tv': 'IPTV Hisense TV', 'iptv-sony-tv': 'IPTV Sony TV', 'iptv-philips-tv': 'IPTV Philips TV', 'iptv-xiaomi': 'IPTV Xiaomi',
    'iptv-m3u': 'IPTV M3U', 'iptv-m3u-playlist-deutschland': 'M3U Playlist', 'iptv-playlist': 'IPTV Playlist', 'iptv-epg': 'IPTV EPG',
    'iptv-sky': 'IPTV Sky', 'iptv-sky-sport': 'Sky Sport IPTV', 'iptv-sky-alternative': 'Sky Alternative', 'iptv-ruckelt-buffering': 'IPTV ruckelt',
    'iptv-einrichten': 'IPTV einrichten', 'iptv-legal': 'Ist IPTV legal?', 'iptv-vpn': 'IPTV VPN', 'was-ist-iptv': 'Was ist IPTV?',
    'iptv-alle-sender': 'IPTV alle Sender', 'iptv-albanisch': 'IPTV Albanisch', 'iptv-russisch': 'IPTV Russisch', 'iptv-polnisch': 'IPTV Polnisch',
    'iptv-griechisch': 'IPTV Griechisch', 'iptv-tuerkisch': 'IPTV Türkisch', 'iptv-italienisch': 'IPTV Italienisch',
    'iptv-telekom': 'IPTV Telekom', 'iptv-magenta-tv': 'MagentaTV vs. IPTV', 'iptv-vodafone-internet': 'IPTV Vodafone',
    'iptv-glasfaser': 'IPTV Glasfaser', 'iptv-router': 'IPTV Router', 'iptv-fritzbox': 'IPTV FritzBox', 'iptv-catchup': 'IPTV Catch-Up',
    'iptv-4k': 'IPTV 4K', 'iptv-premium-4k': 'IPTV Premium 4K', 'iptv-test': 'IPTV Test', 'iptv-abo': 'IPTV Abo',
    'iptv-12-monate': 'IPTV 12 Monate', 'iptv-free-trial': 'IPTV Free Trial', 'iptv-reseller': 'IPTV Reseller',
    'iptv-vergleich': 'IPTV Vergleich', 'iptv-line': 'IPTV Line', 'iptv-bundesliga': 'IPTV Bundesliga',
    'iptv-anbieter': 'IPTV Anbieter', 'german-iptv': 'German IPTV', 'iptv-deutschland': 'IPTV Deutschland',
    'iptv-ugoos': 'IPTV Ugoos', 'iptv-homatics': 'IPTV Homatics', 'iptv-fire-cube': 'IPTV Fire TV Cube',
    'iptv-apple-tv-4k': 'IPTV Apple TV 4K', 'iptv-raspberry-pi': 'IPTV Raspberry Pi', 'iptv-linux': 'IPTV Linux',
    'iptv-box-formuler-mag': 'Formuler & MAG Boxen', 'iptv-android-box': 'IPTV Android Box (Kauf)',
    'iptv-xbox': 'IPTV Xbox', 'iptv-playstation': 'IPTV PlayStation', 'iptv-tcl-tv': 'IPTV TCL TV',
    'iptv-streamplayer': 'IPTV Streamplayer', 'iptvapp': 'IPTVApp', 'iptvx': 'IPTVX', 'iptvpro': 'IPTVPro',
    'xtream-iptv': 'Xtream IPTV', 'upiptv': 'UPIPTV', 'iptv-epg-probleme': 'IPTV EPG Probleme', 'iptv-wlan-probleme': 'IPTV WLAN Probleme',
    'iptv-ohne-receiver': 'IPTV ohne Receiver', 'iptv-vs-kabel': 'IPTV vs. Kabel', 'iptv-vs-satellit': 'IPTV vs. Satellit',
    'iptv-dazn': 'IPTV DAZN', 'iptv-champions-league': 'IPTV Champions League', 'iptv-sport': 'IPTV Sport',
    'iptv-hbo': 'IPTV HBO', 'iptv-netflix-alternative': 'Netflix Alternative', 'iptv-disney-plus': 'IPTV Disney+',
    'iptv-oesterreich': 'IPTV Österreich', 'iptv-schweiz': 'IPTV Schweiz', 'iptv-europe': 'IPTV Europe',
    'iptv-premium': 'IPTV Premium', 'iptv-premier-league': 'IPTV Premier League', 'iptv-playlist-deutsch': 'IPTV Playlist Deutsch', 'iptv-dazn-alternative': 'DAZN Alternative', 'kontakt': 'Kontakt', 'iptv-sofort': 'IPTV sofort aktiv', 'iptv-legal-deutschland': 'IPTV legal in Deutschland',
}


def all_names(pages):
    names = dict(EXISTING_NAMES)
    for p in pages:
        names[p['slug']] = p['crumb']
    return names


def validate(pages, names):
    errors = []
    seen = set()
    for p in pages:
        s = p['slug']
        if s in seen:
            errors.append(f'duplicate slug {s}')
        seen.add(s)
        if not re.fullmatch(r'[a-z0-9-]+', s):
            errors.append(f'{s}: slug not ascii')
        if not (30 <= len(p['title']) <= 65):
            errors.append(f'{s}: title length {len(p["title"])}')
        if not (110 <= len(p['desc']) <= 160):
            errors.append(f'{s}: desc length {len(p["desc"])}')
        if len(p['faq']) < 4:
            errors.append(f'{s}: only {len(p["faq"])} FAQs')
        for r in p['related'] + ([p['parent']] if p.get('parent') else []):
            if r not in names:
                errors.append(f'{s}: unknown link target {r}')
            elif r not in {q['slug'] for q in pages} and not os.path.isdir(os.path.join(PUBLIC, r)):
                errors.append(f'{s}: link target dir missing {r}')
        text = json.dumps(p['sections'], ensure_ascii=False) + p['intro']
        for href in re.findall(r'href="/([^"#]*)"', text):
            path = href.rstrip('/')
            if path and not (os.path.isdir(os.path.join(PUBLIC, path)) or os.path.isfile(os.path.join(PUBLIC, path))
                             or path in {q['slug'] for q in pages}):
                errors.append(f'{s}: inline link /{href} missing')
        for _, blocks in p['sections']:
            for b in blocks:
                if b[0] == 'hub':
                    for hs, _, _ in b[1]:
                        if hs not in {q['slug'] for q in pages} and not os.path.isdir(os.path.join(PUBLIC, hs)):
                            errors.append(f'{s}: hub target missing {hs}')
        words = len(strip_tags(text + json.dumps(p['faq'], ensure_ascii=False)).split())
        if words < 330 and p.get('ld_type') != 'CollectionPage':
            errors.append(f'{s}: thin ({words} words)')
    redirect_sources = {l.split()[0].rstrip('/') for l in open(os.path.join(PUBLIC, '_redirects'), encoding='utf-8')
                        if l.strip() and not l.startswith('#')}
    for p in pages:
        if '/' + p['slug'] in redirect_sources:
            errors.append(f'{p["slug"]}: shadowed by a rule in _redirects')
    titles = {}
    for p in pages:
        titles.setdefault(p['title'], []).append(p['slug'])
    for t, ss in titles.items():
        if len(ss) > 1:
            errors.append(f'duplicate title {ss}')
    return errors


def main():
    pages = load_pages()
    names = all_names(pages)
    errs = validate(pages, names)
    if errs:
        print('\n'.join(errs))
        sys.exit(1)
    for p in pages:
        d = os.path.join(PUBLIC, p['slug'])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(render_page(p, names))
    print(f'built {len(pages)} pages')


if __name__ == '__main__':
    main()
