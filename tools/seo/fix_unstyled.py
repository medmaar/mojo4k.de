#!/usr/bin/env python3
"""Give the 6 pages that shipped without any CSS the site's dark template styles and the mobile menu (SEO audit 2026-10-13)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402

PAGES = ['cloud-stream', 'flix-iptv', 'forevertv', 'hot-iptv', 'set-iptv', 'iptv-line']
MENU = '''<div class="mobile-menu" id="mMe">
  <a href="/">Startseite</a>
  <a href="/preise-de">Preise</a>
  <a href="/bester-iptv-anbieter-de">Bester IPTV Anbieter</a>
  <a href="/iptv-test/">IPTV Test</a>
  <a href="/kostenlos-testen-de">Gratis Testen</a>
  <a href="/faqs-de">FAQs</a>
</div>
'''


def main():
    tpl = open(os.path.join(audit.PUB, 'b1g-iptv', 'index.html'), encoding='utf-8').read()
    style = tpl[tpl.index('  <style>'):tpl.index('</style>') + len('</style>')]
    style = style.replace('</style>', '  .logo-icon{width:34px;height:34px}.logo-main{color:#fff}[style*="background:#fff;"],[style*="background:#f9fafb"]{color:#1f2937}[style*="background:#fff;"] td,[style*="background:#f9fafb"] td{color:#374151}\n  </style>')
    for slug in PAGES:
        p = os.path.join(audit.PUB, slug, 'index.html')
        s = open(p, encoding='utf-8').read()
        if '<style' not in s.split('</head>')[0]:
            s = s.replace('</head>', style + '\n</head>', 1)
        if 'class="mobile-menu"' not in s:
            s = s.replace('</nav>\n', '</nav>\n' + MENU, 1)
        open(p, 'w', encoding='utf-8').write(s)
        print('styled', slug)


if __name__ == '__main__':
    main()
