#!/usr/bin/env python3
"""Rebuild sitemap.xml from the indexable pages on disk; pages changed since HEAD get today's lastmod."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
from audit_fix import regen_sitemap  # noqa: E402


def main():
    out = subprocess.run(['git', '-c', 'core.quotepath=off', 'status', '--porcelain', '-uall', '--', 'public'],
                         cwd=audit.ROOT, capture_output=True, text=True, check=True).stdout
    changed = set()
    for line in out.splitlines():
        path = line[3:].split(' -> ')[-1].strip('"')
        if path.endswith('.html'):
            changed.add(audit.url_for(path[len('public/'):]))
    log = []
    regen_sitemap(changed, log)
    print('\n'.join(log))


if __name__ == '__main__':
    main()
