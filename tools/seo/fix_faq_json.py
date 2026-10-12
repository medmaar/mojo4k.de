#!/usr/bin/env python3
"""Repair FAQPage JSON-LD blocks where a Question was spliced into the previous answer's text.

Broken:  ...answer text.,{"@type":"Question",...}}"}}]
Fixed:   ...answer text."}},{"@type":"Question",...}}]
Only touches blocks that fail to parse, and only writes them back if the repair parses.
"""
import json
import os
import re

PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'public')
LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
SPLICE = re.compile(r'([^"]),(\{"@type":"Question".*?\}\})"\}\}\]', re.S)

def escape_inner_quotes(raw):
    """Escape quotes that end a string too early, e.g. "text":"Suche "Smart IPTV" eingeben"."""
    raw = re.sub(r'<span class="hl">(.*?)</spa(?:n>)?', r'\1', raw)  # HTML leaked into a breadcrumb name
    for _ in range(100):
        try:
            json.loads(raw)
            return raw
        except json.JSONDecodeError as e:
            if not e.msg.startswith("Expecting ',' delimiter") and not e.msg.startswith("Expecting ':' delimiter"):
                return raw
            q = raw.rfind('"', 0, e.pos)
            if q <= 0 or raw[q - 1] == '\\':
                return raw
            raw = raw[:q] + '\\"' + raw[q + 1:]
    return raw


fixed = failed = 0
for root, _, files in os.walk(PUBLIC):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        page = open(path, encoding='utf-8').read()
        state = {'changed': False}

        def repl(m):
            global fixed, failed
            raw = m.group(2)
            try:
                json.loads(raw)
                return m.group(0)
            except json.JSONDecodeError:
                pass
            new = SPLICE.sub(lambda s: s.group(1) + '"}},' + s.group(2) + ']', raw)
            new = escape_inner_quotes(new)
            try:
                json.loads(new)
            except json.JSONDecodeError:
                failed += 1
                print('could not repair', path)
                return m.group(0)
            fixed += 1
            state['changed'] = True
            return m.group(1) + new + m.group(3)

        page = LD_RE.sub(repl, page)
        if state['changed']:
            open(path, 'w', encoding='utf-8').write(page)
print(f'repaired {fixed} JSON-LD blocks, {failed} left')


# Merge duplicate top-level FAQPage blocks into the first one (Search Console flags duplicates).
merged = 0
for root, _, files in os.walk(PUBLIC):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        page = open(path, encoding='utf-8').read()
        blocks = [(m, json.loads(m.group(2))) for m in LD_RE.finditer(page)]
        faqs = [(m, o) for m, o in blocks if isinstance(o, dict) and o.get('@type') == 'FAQPage']
        if len(faqs) < 2:
            continue
        first_m, first = faqs[0]
        names = {q.get('name') for q in first.get('mainEntity', [])}
        for _, o in faqs[1:]:
            for q in o.get('mainEntity', []):
                if q.get('name') not in names:
                    first['mainEntity'].append(q)
                    names.add(q.get('name'))
            if '@id' in o and '@id' not in first:
                first['@id'] = o['@id']
        out, pos = [], 0
        for m, _ in faqs:
            out.append(page[pos:m.start()])
            if m is first_m:
                out.append(m.group(1) + json.dumps(first, ensure_ascii=False, separators=(',', ':')) + m.group(3))
            pos = m.end()
        out.append(page[pos:])
        page = ''.join(out)
        page = re.sub(r'\n[ \t]*\n(?=<script type="application/ld\+json">)', '\n', page)
        open(path, 'w', encoding='utf-8').write(page)
        merged += 1
print(f'merged duplicate FAQPage blocks on {merged} pages')
