"""Read the FAQ a visitor actually sees on a page, and rewrite a page's FAQPage JSON-LD to match it."""
import json
import re

from bs4 import NavigableString, Tag

FAQ_H2 = re.compile(r'fragen|faq|questions', re.I)
Q_TAGS = ('summary', 'h3', 'h4', 'dt')


def _clean(s):
    return re.sub(r'\s+', ' ', s).strip()


def _is_question(el):
    if not isinstance(el, Tag):
        return False
    cls = ' '.join(el.get('class', []))
    txt = _clean(el.get_text(' '))
    if not txt or len(txt) > 250:
        return False
    if el.name == 'summary' or 'faq-q' in cls.split():
        return True
    return el.name in Q_TAGS and '?' in txt


def _contains_question(el):
    if _is_question(el):
        return True
    return isinstance(el, Tag) and any(_is_question(x) for x in el.find_all(list(Q_TAGS) + ['div']))


def _answer(q):
    parts = []
    node = q
    for _ in range(2):  # look at siblings, then at the wrapper's siblings
        for sib in node.next_siblings:
            if isinstance(sib, NavigableString):
                if sib.strip():
                    parts.append(str(sib))
                continue
            if sib.name in ('h2',) or _contains_question(sib):
                break
            if sib.name in ('script', 'style'):
                continue
            parts.append(sib.get_text(' '))
        if _clean(' '.join(parts)):
            break
        node = node.parent
        if node is None or node.name in ('section', 'main', 'body'):
            break
    return _clean(' '.join(parts))


def visible_faq(soup):
    """List of (question, answer) pairs shown in the page's FAQ sections."""
    out, seen = [], set()
    for h2 in soup.find_all('h2'):
        if not FAQ_H2.search(h2.get_text(' ')):
            continue
        for el in h2.find_all_next():
            if el.name == 'h2':
                break
            if el.name in ('footer', 'nav'):
                break
            if not _is_question(el):
                continue
            # a summary inside details, or an h3 inside .faq-q: take the outermost question element
            if el.parent is not None and _is_question(el.parent):
                continue
            q = _clean(el.get_text(' '))
            a = _answer(el)
            key = q.lower()
            if a and len(a) >= 20 and key not in seen:
                seen.add(key)
                out.append((q, a))
    if len(out) < 2:
        # no FAQ section: question headings in the main content are the visible Q&A
        out, seen = [], set()
        for el in soup.find_all(['h3', 'h4']):
            if el.find_parent(['footer', 'nav', 'header']) or not _is_question(el):
                continue
            q, a = _clean(el.get_text(' ')), _answer(el)
            if a and len(a) >= 20 and q.lower() not in seen:
                seen.add(q.lower())
                out.append((q, a))
    return out


def faq_node(pairs, at_id=None):
    node = {'@context': 'https://schema.org', '@type': 'FAQPage'}
    if at_id:
        node['@id'] = at_id
    node['mainEntity'] = [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pairs
    ]
    return node


LD_RE = re.compile(r'(<script type="application/ld\+json"[^>]*>)(.*?)(</script>)', re.S)


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


def rewrite_faq_schema(html, pairs):
    """Replace every FAQPage node with one built from `pairs` (drop it when pairs is empty).

    Returns (new_html, changed)."""
    done = [False]
    changed = [False]

    def repl(m):
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except Exception:
            return m.group(0)
        def is_faq(n):
            t = n.get('@type') if isinstance(n, dict) else None
            return t == 'FAQPage' or (isinstance(t, list) and 'FAQPage' in t)
        if isinstance(data, dict) and is_faq(data):
            changed[0] = True
            if done[0] or not pairs:
                return ''
            done[0] = True
            return m.group(1) + dump(faq_node(pairs, data.get('@id'))) + m.group(3)
        if isinstance(data, dict) and isinstance(data.get('@graph'), list) and any(is_faq(n) for n in data['@graph']):
            changed[0] = True
            g = []
            for n in data['@graph']:
                if is_faq(n):
                    if done[0] or not pairs:
                        continue
                    done[0] = True
                    fn = faq_node(pairs, n.get('@id'))
                    fn.pop('@context')
                    g.append(fn)
                else:
                    g.append(n)
            data['@graph'] = g
            return m.group(1) + dump(data) + m.group(3)
        return m.group(0)

    new = LD_RE.sub(repl, html)
    if pairs and not done[0]:
        tag = '<script type="application/ld+json">' + dump(faq_node(pairs)) + '</script>\n'
        new = new.replace('</head>', tag + '</head>', 1)
        changed[0] = True
    return new, changed[0]
