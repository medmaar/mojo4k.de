#!/usr/bin/env python3
"""Count internal inbound links per indexable page (from other pages' HTML, nav/footer included)."""
import os, re, sys
from collections import Counter
from urllib.parse import urlparse, unquote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit

def inbound():
    files = list(audit.html_files())
    idx = audit.build_path_index(files)
    red = audit.load_redirects()
    cnt = Counter()
    for rel in files:
        s = open(os.path.join(audit.PUB, rel), encoding='utf-8').read()
        seen = set()
        for h in re.findall(r'href="([^"#?]*)', s):
            pu = urlparse(h)
            if pu.netloc and pu.netloc not in ('mojo4k.de',):
                continue
            if not pu.path.startswith('/'):
                continue
            st, fin = audit.resolve(pu.path, idx, red)
            if st != 'dead' and fin in idx.values() and fin != rel:
                seen.add(fin)
        for f in seen:
            cnt[f] += 1
    return files, cnt

if __name__ == '__main__':
    files, cnt = inbound()
    idx = [r for r in files if 'noindex' not in open(os.path.join(audit.PUB, r)).read()[:3000]]
    low = sorted((cnt[r], r) for r in idx)
    for n, r in low[:int(sys.argv[1]) if len(sys.argv) > 1 else 60]:
        print(n, r)
