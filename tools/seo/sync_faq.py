#!/usr/bin/env python3
"""Rebuild every indexable page's FAQPage JSON-LD from the FAQ visitors can see. Idempotent."""
import os
import re
import sys

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
import faqlib  # noqa: E402


def main():
    n = 0
    for rel in audit.html_files():
        p = os.path.join(audit.PUB, rel)
        s0 = s = open(p, encoding='utf-8').read()
        if re.search(r'<meta name="robots" content="[^"]*noindex', s):
            continue
        pairs = faqlib.visible_faq(BeautifulSoup(s, 'lxml'))
        pairs = [(re.sub(r'\s*[+−–▾▼›]\s*$', '', q), a) for q, a in pairs]
        s, _ = faqlib.rewrite_faq_schema(s, pairs if len(pairs) >= 2 else [])
        if s != s0:
            open(p, 'w', encoding='utf-8').write(s)
            n += 1
    print('faq schema updated on', n, 'pages')


if __name__ == '__main__':
    main()
