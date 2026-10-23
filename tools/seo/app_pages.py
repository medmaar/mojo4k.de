#!/usr/bin/env python3
"""Rebuild player-app pages that the old template treated as competing IPTV providers (SEO audit 2026-10-13).

Searchers for "flix iptv", "set iptv", "siptv" & co. look for the player app: what it is, which devices
it runs on and how to load a playlist. The old pages compared these apps on "uptime" and "channel count",
which a player app does not have. This script replaces everything from <main> up to the first SEO link
block (or the footer) with an app guide built from the specs in app_specs.py, and updates title,
description, OG/Twitter copies and the WebPage/BreadcrumbList names to match.

The head, nav, footer and the later <!-- seo-* --> blocks stay as they are. Idempotent.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
from deepen import set_head  # noqa: E402
from faqlib import LD_RE, dump  # noqa: E402

STYLE = ('<style>.app-guide p,.app-guide li{color:rgba(255,255,255,.8);font-size:15px;line-height:1.75}'
         '.app-guide p{margin-bottom:16px}.app-guide ol,.app-guide ul{padding-left:22px;margin:0 0 20px}'
         '.app-guide li{margin-bottom:8px}.app-guide a{color:#FFD700}.app-guide h3{font-size:1.1rem;margin:22px 0 10px}'
         '.app-guide .note{background:rgba(255,206,0,.06);border-left:3px solid #FFD700;padding:14px 18px;border-radius:8px}'
         '</style>')
MARKERS = ('<!-- seo-enrich -->', '<!-- seo-cluster-links -->', '<!-- seo-sources -->', '<!-- seo-related -->', '<footer')


def block(b):
    kind = b[0]
    if kind == 'p':
        return f'<p>{b[1]}</p>'
    if kind == 'note':
        return f'<p class="note">{b[1]}</p>'
    if kind in ('ol', 'ul'):
        return f'<{kind}>' + ''.join(f'<li>{i}</li>' for i in b[1]) + f'</{kind}>'
    if kind == 'h3':
        return f'<h3>{b[1]}</h3>'
    if kind == 'cards':
        return '<div class="cards">' + ''.join(f'<div class="card"><strong>{t}</strong><p>{d}</p></div>' for t, d in b[1]) + '</div>'
    if kind == 'table':
        head = ''.join(f'<th>{h}</th>' for h in b[1])
        rows = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in b[2])
        return f'<div class="compare-section" style="margin-bottom:24px"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    raise ValueError(kind)


def render_main(spec):
    out = ['<main>', STYLE, '  <section class="hero">', '    <div class="hero-inner">',
           f'      <div class="badge">{spec["badge"]}</div>', f'      <h1>{spec["h1"]}</h1>', f'      <p>{spec["intro"]}</p>',
           '      <div class="hero-btns">',
           '        <a href="/kostenlos-testen-de" class="btn-p">24h kostenlos testen</a>',
           '        <a href="/preise-de" class="btn-s">Preise ansehen</a>',
           '      </div>', '    </div>', '  </section>']
    for i, (h2, blocks) in enumerate(spec['sections']):
        bg = ' style="background:rgba(255,255,255,.015)"' if i % 2 else ''
        out.append(f'  <section class="app-guide"{bg}><div class="container"><h2>{h2}</h2>')
        out.extend('    ' + block(b) for b in blocks)
        out.append('  </div></section>')
    out.append(f'  <section><div class="container"><h2>Häufige Fragen zu {spec["name"]}</h2>')
    for q, a in spec['faq']:
        out.append(f'    <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>')
    out.append('  </div></section>')
    out += ['  <section><div class="container"><div class="cta-section">',
            f'    <h2>{spec.get("cta_h2", "IPTV-Zugang für " + spec["name"] + " testen")}</h2>',
            f'    <p style="opacity:.85;margin-bottom:24px">{spec.get("cta_p", CTA_P)}</p>',
            '    <div class="hero-btns"><a href="/kostenlos-testen-de" class="btn-p">Kostenlosen Test anfordern</a>'
            '<a href="/preise-de" class="btn-s">Pakete ab 9 € ansehen</a></div>',
            '  </div></div></section>', '</main>', '']
    return '\n'.join(out)


CTA_P = ('MOJO4K.DE liefert die Zugangsdaten als Xtream-Codes-Login und als M3U-Link. Testen Sie 24 Stunden kostenlos, '
         'danach ab 9 € im Monat, 29 € für 3 Monate, 39 € für 6 Monate oder 49 € für 12 Monate. Support per WhatsApp '
         'und an info@mojo4k.de.')


def fix_ld(page, url, title, desc, crumb):
    def repl(m):
        try:
            data = json.loads(m.group(2))
        except Exception:
            return m.group(0)
        nodes = data.get('@graph', [data]) if isinstance(data, dict) else []
        hit = False
        for n in nodes:
            if not isinstance(n, dict):
                continue
            if n.get('@type') == 'WebPage':
                n['name'], n['description'], n['dateModified'] = title, desc, '2026-10-13'
                hit = True
            if n.get('@type') == 'BreadcrumbList' and n.get('itemListElement'):
                n['itemListElement'][-1]['name'] = crumb
                n['itemListElement'][-1]['item'] = url
                hit = True
        return m.group(1) + dump(data) + m.group(3) if hit else m.group(0)
    return LD_RE.sub(repl, page)


def apply(slug, spec):
    path = os.path.join(audit.PUB, slug, 'index.html')
    page = open(path, encoding='utf-8').read()
    a = page.index('<main>')
    b = page.index('</main>')
    ends = [page.find(mk, b) for mk in MARKERS]
    e = min(x for x in ends if x != -1)
    page = page[:a] + render_main(spec) + page[e:]
    page = set_head(page, spec['title'], spec['desc'])
    page = fix_ld(page, f'{audit.DOMAIN}/{slug}/', spec['title'], spec['desc'], spec['name'])
    open(path, 'w', encoding='utf-8').write(page)


def main():
    from app_specs import APPS
    only = set(sys.argv[1:])
    n = 0
    for slug, spec in APPS.items():
        if only and slug not in only:
            continue
        apply(slug, spec)
        n += 1
    print('rebuilt', n, 'app pages')


if __name__ == '__main__':
    main()
