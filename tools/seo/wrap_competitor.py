#!/usr/bin/env python3
"""Constrain the full-width <!-- competitor-unique --> boxes (placed after </main>) to the 900px content column.

Layout only: the text inside is left as it is. Idempotent (SEO audit 2026-10-13)."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402

OPEN = '<div class="cu-wrap" style="max-width:900px;margin:0 auto;padding:0 20px">'
STOP = re.compile(r'<!-- seo-|<footer')


def main():
    n = 0
    for rel in audit.html_files():
        p = os.path.join(audit.PUB, rel)
        s = open(p, encoding='utf-8').read()
        i = s.find('<!-- competitor-unique -->')
        if i == -1 or 'class="cu-wrap"' in s or i < s.find('</main>'):
            continue
        m = STOP.search(s, i)
        if not m:
            continue
        s = s[:i] + OPEN + s[i:m.start()].rstrip() + '\n</div>\n' + s[m.start():]
        open(p, 'w', encoding='utf-8').write(s)
        n += 1
    print('wrapped', n)


if __name__ == '__main__':
    main()
