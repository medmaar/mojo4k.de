#!/usr/bin/env python3
"""Add new pages to sitemap.xml and bump <lastmod> for pages changed in the working tree.

Usage:  python3 tools/seo/sitemap_update.py slug [slug …]
Pages listed on the command line are added if missing; every page with uncommitted
changes (git diff) gets today's date as lastmod.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SITEMAP = os.path.join(ROOT, 'public', 'sitemap.xml')
TODAY = '2026-10-11'
DOMAIN = 'https://mojo4k.de'


def changed_urls():
    out = subprocess.run(['git', '-c', 'core.quotepath=off', 'diff', '--name-only', '--', 'public'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    urls = set()
    for path in out.split('\n'):
        if not path.endswith('.html'):
            continue
        rel = path[len('public/'):]
        if rel == 'index.html':
            urls.add(DOMAIN + '/')
        elif rel.endswith('/index.html'):
            urls.add(f'{DOMAIN}/{rel[:-len("index.html")]}')
        else:
            urls.add(f'{DOMAIN}/{rel}')
    return urls


def main():
    xml = open(SITEMAP, encoding='utf-8').read()
    added = 0
    for slug in sys.argv[1:]:
        loc = f'{DOMAIN}/{slug}/'
        if f'<loc>{loc}</loc>' in xml:
            continue
        line = (f'  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>'
                f'<changefreq>monthly</changefreq><priority>0.75</priority></url>\n')
        xml = xml.replace('</urlset>', line + '</urlset>')
        added += 1
    bumped = 0
    for loc in changed_urls():
        new, n = re.subn(r'(<loc>' + re.escape(loc) + r'</loc><lastmod>)[^<]*(</lastmod>)', r'\g<1>' + TODAY + r'\g<2>', xml)
        if n and new != xml:
            bumped += 1
        xml = new
    open(SITEMAP, 'w', encoding='utf-8').write(xml)
    print(f'sitemap: {added} added, {bumped} lastmod updated')


if __name__ == '__main__':
    main()
