#!/usr/bin/env python3
"""Page-by-page SEO audit over every HTML file in public/.

Usage:  python3 tools/seo/audit.py [--json out.json]
Prints a summary of issue counts; --json writes the per-page findings.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PUB = os.path.join(ROOT, 'public')
DOMAIN = 'https://mojo4k.de'


def html_files():
    for dp, dn, fn in os.walk(PUB):
        for f in fn:
            if f.endswith('.html'):
                yield os.path.relpath(os.path.join(dp, f), PUB)


def url_for(rel):
    """Public URL Cloudflare Pages serves a file at (pretty URLs)."""
    if rel == 'index.html':
        return DOMAIN + '/'
    if rel.endswith('/index.html'):
        return f'{DOMAIN}/{rel[:-len("index.html")]}'
    return f'{DOMAIN}/{rel[:-len(".html")]}'


def load_redirects():
    rules = {}
    for line in open(os.path.join(PUB, '_redirects'), encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 2:
            rules.setdefault(parts[0], parts[1])
    return rules


def sitemap_locs():
    xml = open(os.path.join(PUB, 'sitemap.xml'), encoding='utf-8').read()
    return re.findall(r'<loc>([^<]+)</loc>', xml)


def build_path_index(files):
    """Map every path that resolves to a 200 page to its file."""
    idx = {}
    for rel in files:
        u = urlparse(url_for(rel)).path
        idx[u] = rel
        if rel.endswith('/index.html'):
            idx[u.rstrip('/')] = rel          # /x -> /x/ (CF adds slash)
            idx[u + 'index.html'] = rel
        elif rel != 'index.html':
            idx[u + '.html'] = rel            # /x.html -> /x
        else:
            idx['/index.html'] = rel
    return idx


def resolve(path, idx, redirects, depth=0):
    """Return ('ok'|'redirect'|'dead', final) for an internal path."""
    p = unquote(path.split('#')[0].split('?')[0]) or '/'
    if p in redirects and depth < 5:
        tgt = redirects[p]
        if tgt.startswith('http') and not tgt.startswith(DOMAIN):
            return 'redirect', tgt
        st, fin = resolve(urlparse(tgt).path, idx, redirects, depth + 1)
        return ('redirect' if st != 'dead' else 'dead'), fin
    if p in idx:
        return 'ok', idx[p]
    if os.path.isfile(os.path.join(PUB, p.lstrip('/'))):
        return 'ok', p
    if p.startswith('/support/') or p.startswith('/api/'):
        return 'ok', p  # Pages Functions
    return 'dead', p


def visible_text(soup):
    s = BeautifulSoup(str(soup), 'lxml')
    for t in s(['script', 'style', 'noscript', 'nav', 'footer', 'header', 'svg', 'template']):
        t.decompose()
    body = s.body or s
    return re.sub(r'\s+', ' ', body.get_text(' ')).strip()


def audit():
    files = sorted(html_files())
    redirects = load_redirects()
    idx = build_path_index(files)
    locs = set(unquote(l) for l in sitemap_locs())
    pages = {}
    titles = defaultdict(list)
    descs = defaultdict(list)
    for rel in files:
        raw = open(os.path.join(PUB, rel), encoding='utf-8').read()
        soup = BeautifulSoup(raw, 'lxml')
        url = url_for(rel)
        issues = []
        info = {'url': url}
        head = soup.head or soup
        robots = head.find('meta', attrs={'name': 'robots'})
        noindex = bool(robots and 'noindex' in robots.get('content', ''))
        info['noindex'] = noindex
        t = soup.title.get_text(strip=True) if soup.title else ''
        info['title'] = t
        if not t:
            issues.append('title_missing')
        elif len(t) < 30:
            issues.append('title_short')
        elif len(t) > 65:
            issues.append('title_long')
        if len(soup.find_all('title')) > 1:
            issues.append('title_multiple')
        md = head.find_all('meta', attrs={'name': 'description'})
        d = md[0].get('content', '').strip() if md else ''
        info['desc'] = d
        if not d:
            issues.append('desc_missing')
        elif len(d) < 110:
            issues.append('desc_short')
        elif len(d) > 160:
            issues.append('desc_long')
        if len(md) > 1:
            issues.append('desc_multiple')
        if not noindex:
            titles[t].append(rel)
            descs[d].append(rel)
        cans = head.find_all('link', rel='canonical')
        can = cans[0].get('href', '') if cans else ''
        info['canonical'] = can
        if not can:
            issues.append('canonical_missing')
        elif len(cans) > 1:
            issues.append('canonical_multiple')
        elif can != url and not noindex:
            issues.append('canonical_mismatch')
        hl = head.find_all('link', rel='alternate', hreflang=True)
        info['hreflang'] = [(h.get('hreflang'), h.get('href')) for h in hl]
        if not hl:
            issues.append('hreflang_missing')
        else:
            codes = [h.get('hreflang') for h in hl]
            if 'x-default' not in codes:
                issues.append('hreflang_no_xdefault')
            if not any(h.get('href') == url for h in hl):
                issues.append('hreflang_no_self')
        def meta(prop=None, name=None):
            m = head.find('meta', attrs={'property': prop} if prop else {'name': name})
            return m.get('content', '') if m else ''
        for p in ['og:title', 'og:description', 'og:url', 'og:image', 'og:type', 'og:locale', 'og:site_name']:
            v = meta(prop=p)
            if not v:
                issues.append(f'{p}_missing')
            elif p == 'og:url' and v != url and not noindex:
                issues.append('og:url_mismatch')
        for n in ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
            if not meta(name=n):
                issues.append(f'{n}_missing')
        if url not in locs and not noindex:
            issues.append('not_in_sitemap')
        if noindex and url in locs:
            issues.append('noindex_in_sitemap')
        # render-blocking
        for s in head.find_all('script', src=True):
            if not (s.has_attr('defer') or s.has_attr('async') or s.get('type') == 'module'):
                issues.append('render_blocking_script')
        for l in head.find_all('link', rel='stylesheet'):
            if 'fonts.googleapis' in l.get('href', '') or l.get('href', '').startswith('http'):
                issues.append('external_css')
        imgs = soup.find_all('img')
        if any(not i.get('alt') for i in imgs):
            issues.append('img_alt_missing')
        if any(not (i.get('width') and i.get('height')) for i in imgs):
            info['img_nodims'] = True
        # headings
        h1s = soup.find_all('h1')
        info['h1'] = [h.get_text(' ', strip=True) for h in h1s]
        if not h1s:
            issues.append('h1_missing')
        elif len(h1s) > 1:
            issues.append('h1_multiple')
        levels = [int(h.name[1]) for h in soup.find_all(re.compile(r'^h[1-6]$'))]
        prev = 0
        for lv in levels:
            if prev and lv > prev + 1:
                issues.append('heading_skip')
                break
            prev = lv
        if levels and levels[0] != 1:
            issues.append('heading_before_h1')
        text = visible_text(soup)
        wc = len(text.split())
        info['words'] = wc
        if wc < 600 and not noindex:
            issues.append('thin_lt600')
        # links
        dead, redir, internal, outbound = [], [], 0, []
        for a in soup.find_all('a', href=True):
            h = a['href'].strip()
            if h.startswith(('mailto:', 'tel:', 'javascript:', '#', 'whatsapp:')):
                continue
            pu = urlparse(h)
            if pu.netloc and pu.netloc not in ('mojo4k.de', 'www.mojo4k.de'):
                outbound.append(h)
                continue
            path = pu.path if pu.netloc else (h if h.startswith('/') else
                    os.path.normpath(os.path.join('/' + os.path.dirname(rel), pu.path)) + ('/' if pu.path.endswith('/') else ''))
            if not path:
                continue
            internal += 1
            st, fin = resolve(path, idx, redirects)
            if st == 'dead':
                dead.append(h)
            elif st == 'redirect':
                redir.append(h)
        info['internal_links'] = internal
        info['outbound'] = outbound
        info['dead_links'] = sorted(set(dead))
        info['redirect_links'] = sorted(set(redir))
        if dead:
            issues.append('dead_internal_links')
        if redir:
            issues.append('links_via_redirect')
        if internal < 8 and not noindex:
            issues.append('few_internal_links')
        auth = [o for o in outbound if not re.search(r'wa\.me|whatsapp|t\.me|instagram|facebook|tiktok|youtube\.com/@', o)]
        info['authority_out'] = auth
        # schema
        types = []
        faq_q = []
        for s in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(s.string or '')
            except Exception:
                issues.append('jsonld_invalid')
                continue
            items = data if isinstance(data, list) else data.get('@graph', [data]) if isinstance(data, dict) else []
            for it in items:
                if not isinstance(it, dict):
                    continue
                ty = it.get('@type')
                tys = ty if isinstance(ty, list) else [ty]
                types += tys
                if 'FAQPage' in tys:
                    for q in it.get('mainEntity', []) or []:
                        faq_q.append((q.get('name', ''), (q.get('acceptedAnswer') or {}).get('text', '')))
                if 'aggregateRating' in it or 'AggregateRating' in tys:
                    info['has_rating'] = True
                if 'Product' in tys and 'offers' not in it and 'aggregateRating' not in it and 'review' not in it:
                    issues.append('product_no_offer')
                if 'BreadcrumbList' in tys:
                    for el in it.get('itemListElement', []):
                        if not el.get('item') and el != it.get('itemListElement')[-1]:
                            issues.append('breadcrumb_item_missing')
                            break
        info['schema'] = types
        tc = Counter(types)
        if tc['FAQPage'] > 1:
            issues.append('faq_duplicate')
        if not tc['FAQPage'] and not noindex:
            issues.append('faq_missing')
        if not tc['BreadcrumbList'] and rel != 'index.html' and not noindex:
            issues.append('breadcrumb_missing')
        if not (tc['WebPage'] or tc['Article'] or tc['BlogPosting'] or tc['CollectionPage']
                or tc['AboutPage'] or tc['ContactPage'] or tc['FAQPage'] or tc['WebSite']):
            issues.append('webpage_schema_missing')
        if faq_q:
            low = text.lower()
            missing = [q for q, a in faq_q if q and q.lower()[:40] not in low]
            if missing:
                issues.append('faq_schema_not_visible')
                info['faq_missing_visible'] = missing[:5]
        # CTA / trust
        hrefs = ' '.join(a['href'] for a in soup.find_all('a', href=True))
        if not re.search(r'kostenlos-testen|/preise|wa\.me|/support/|#pricing|#trial|bestellen|checkout', hrefs):
            issues.append('cta_missing')
        info['issues'] = issues
        info['text_head'] = text[:400]
        pages[rel] = info
    for k, v in titles.items():
        if len(v) > 1:
            for r in v:
                pages[r]['issues'].append('title_duplicate')
    for k, v in descs.items():
        if k and len(v) > 1:
            for r in v:
                pages[r]['issues'].append('desc_duplicate')
    files_urls = {url_for(r) for r in files}
    orphans_sitemap = sorted(l for l in locs if l not in files_urls)
    return pages, orphans_sitemap


def main():
    pages, orphan_locs = audit()
    c = Counter(i for p in pages.values() for i in set(p['issues']))
    print(f'{len(pages)} pages audited')
    for k, v in c.most_common():
        print(f'  {k:28} {v}')
    print(f'sitemap URLs with no page: {len(orphan_locs)}')
    for l in orphan_locs[:20]:
        print('   ', l)
    if '--json' in sys.argv:
        out = sys.argv[sys.argv.index('--json') + 1]
        json.dump({'pages': pages, 'orphan_locs': orphan_locs}, open(out, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
