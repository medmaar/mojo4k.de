#!/usr/bin/env python3
"""Second pass of the 2026-10-13 audit: tidy the place block layout and repair LocalBusiness
name/locality on place pages (many said "IPTV" instead of the town)."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
import faqlib  # noqa: E402
import places  # noqa: E402
from audit_fix import city_block  # noqa: E402

PUB = audit.PUB
NEW_BLOCK_RE = re.compile(r'<div id="city-local-block".*?</div>\n</div>\n(?:<p [^\n]*\n<div>[^\n]*</div>\n)?(?:<p [^\n]*\n)?</div>\n', re.S)
CODES = {'NW': 'NW', 'BW': 'BW', 'BY': 'BY', 'HE': 'HE', 'NI': 'NI', 'SN': 'SN', 'TH': 'TH', 'RP': 'RP', 'SH': 'SH',
         'MV': 'MV', 'BB': 'BB', 'ST': 'ST', 'SL': 'SL', 'HB': 'HB', 'BE': 'BE', 'HH': 'HH'}


def fix_lb(s, slug):
    pl = places.PLACES.get(slug) or places.REGIONS.get(slug)
    if not pl:
        return s
    name, code = pl

    def repl(m):
        try:
            d = json.loads(m.group(2))
        except Exception:
            return m.group(0)
        if not isinstance(d, dict) or d.get('@type') != 'LocalBusiness':
            return m.group(0)
        d['name'] = f'MOJO4K.DE IPTV – {name}'
        if isinstance(d.get('description'), str):
            d['description'] = re.sub(r'\bin (IPTV( auf( dem)?| als| mit)?|[^–]*?) –', f'in {name} –', d['description'], count=1)
        addr = d.setdefault('address', {'@type': 'PostalAddress'})
        addr['addressLocality'] = name
        if code in ('CH', 'AT'):
            addr['addressCountry'] = 'CH' if code == 'CH' else 'AT'
            addr.pop('addressRegion', None)
        else:
            addr['addressRegion'] = places.STATES[code]
            addr['addressCountry'] = 'DE'
        d['areaServed'] = {'@type': 'City' if slug in places.PLACES else 'State', 'name': name}
        return m.group(1) + faqlib.dump(d) + m.group(3)
    return faqlib.LD_RE.sub(repl, s)


def main():
    n_block = n_lb = 0
    for rel in audit.html_files():
        slug = rel.split('/')[0] if '/' in rel else ''
        p = os.path.join(PUB, rel)
        s0 = s = open(p, encoding='utf-8').read()
        pl = places.PLACES.get(slug) or places.REGIONS.get(slug)
        if pl and NEW_BLOCK_RE.search(s):
            s = NEW_BLOCK_RE.sub(lambda m: city_block(slug, pl[0], pl[1]), s, count=1)
            n_block += s != s0
        s1 = fix_lb(s, slug)
        n_lb += s1 != s
        s = s1
        if s != s0:
            open(p, 'w', encoding='utf-8').write(s)
    print('blocks', n_block, 'localbusiness', n_lb)


if __name__ == '__main__':
    main()
