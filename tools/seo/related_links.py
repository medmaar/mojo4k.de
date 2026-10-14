#!/usr/bin/env python3
"""Topic-cluster internal linking (SEO audit 2026-10-13).

Every indexable topic page gets a "Verwandte Themen" block: its cluster hub plus a rotating
window of siblings, so every page in a cluster receives links from several siblings.
Every hub gets a complete "Alle Seiten" index of its cluster. State pages get a complete
list of their towns, and /iptv-deutschland/ lists every Bundesland.
Idempotent: re-running replaces the blocks it wrote before.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402
import places  # noqa: E402

PUB = audit.PUB

CLUSTERS = {
    'sport': ('iptv-sport', 'Sport', """
        iptv-bundesliga iptv-2-bundesliga iptv-champions-league iptv-europa-league iptv-conference-league
        iptv-premier-league iptv-la-liga iptv-serie-a iptv-ligue-1 iptv-frauen-bundesliga iptv-wm-2026 iptv-dazn
        iptv-dazn-alternative iptv-sky-sport iptv-sport-live iptv-sport1 iptv-sport1-plus iptv-eurosport
        iptv-bein-sports iptv-f1 iptv-formel-e iptv-dtm iptv-moto-gp iptv-tennis iptv-2-bundesliga-tennis
        iptv-handball iptv-handball-bundesliga iptv-basketball iptv-nba iptv-nfl iptv-eishockey iptv-volleyball
        iptv-beachvolleyball iptv-darts iptv-snooker iptv-golf iptv-radsport iptv-tour-de-france iptv-triathlon
        iptv-schwimmen iptv-leichtathletik iptv-ski-alpin iptv-wintersport iptv-olympia iptv-boxen iptv-ufc
        iptv-wrestling iptv-kampfsport iptv-ringen iptv-gewichtheben iptv-cricket iptv-rugby iptv-esports
        blog/iptv-bundesliga-2026"""),
    'sender': ('iptv-alle-sender', 'Sender & Streaming', """
        iptv-ard-zdf iptv-zdf-info iptv-zdf-neo iptv-3sat iptv-arte iptv-br iptv-hr iptv-mdr iptv-ndr iptv-swr
        iptv-wdr iptv-rtl iptv-rtl-plus iptv-sat1 iptv-sat1-gold iptv-prosieben iptv-prosieben-maxx iptv-vox
        iptv-kabel-1 iptv-sixx iptv-ntv iptv-nachrichten iptv-comedy-central iptv-mtv-hits iptv-vh1 iptv-musik
        iptv-disney iptv-kindersender iptv-kinder-familien iptv-dokumentation iptv-anime iptv-hbo iptv-fox
        iptv-sky iptv-sky-alternative iptv-sky-atlantic iptv-sky-cinema iptv-sky-documentaries iptv-sky-go
        sky-q-iptv-box iptv-amazon-prime iptv-disney-plus iptv-netflix-alternative iptv-zattoo iptv-magenta-tv
        iptv-telekom iptv-vodafone-internet iptv-senioren"""),
    'international': ('iptv-alle-sender', 'Internationale Sender', """
        iptv-europe iptv-england iptv-oesterreich iptv-oesterreich-sender iptv-schweiz iptv-schweiz-sender
        iptv-suedtirol iptv-alpen iptv-albanisch iptv-ex-yu iptv-franzoesisch iptv-georgisch iptv-griechisch
        iptv-italienisch iptv-kurdisch iptv-niederlaendisch iptv-persisch iptv-polnisch iptv-polnische-sender
        iptv-portugiesisch iptv-rumaenisch iptv-russisch iptv-russische-sender iptv-schwedisch iptv-spanisch
        iptv-tuerkisch iptv-tuerkische-sender iptv-ukrainisch"""),
    'geraete': ('iptv-geraete', 'Geräte', """
        iptv-firestick fire-tv-stick-iptv iptv-fire-stick-deutschland iptv-fire-cube iptv-stick iptv-box
        beste-iptv-box iptv-set-top-box iptv-android-box iptv-android-box-deutschland iptv-android iptv-android-tv
        iptv-smart-tv iptv-samsung-tv-deutschland iptv-samsung-qled iptv-samsung-frame iptv-lg-tv-deutschland
        iptv-lg-oled iptv-sony-tv iptv-philips-tv iptv-philips-ambilight iptv-hisense-tv iptv-tcl-tv
        iptv-panasonic-tv iptv-toshiba-tv iptv-4k-tv iptv-apple-tv iptv-apple-tv-4k iptv-iphone iptv-ipad
        iptv-macbook iptv-pc iptv-windows-10 iptv-windows-11 iptv-linux iptv-chromecast iptv-chromecast-google-tv
        iptv-roku iptv-xbox iptv-playstation iptv-nvidia-shield iptv-xiaomi iptv-ugoos iptv-homatics
        iptv-formuler formuler-tv-box iptv-box-formuler-mag iptv-mag-box mag-box-modelle tvip-s-box
        iptv-receiver-deutschland iptv-enigma2 iptv-raspberry-pi iptv-ohne-receiver
        blog/bester-iptv-stick-test-2026 blog/iptv-stick-test-deutschland"""),
    'apps': ('iptv-apps', 'Apps & Player', """
        iptv-smarters-pro iptv-smarters iptv-smarters-pro-deutschland iptv-smarters-pro-fire-tv-stick
        iptv-smarters-pro-samsung-tv iptv-smarters-pro-lg-tv iptv-smarters-pro-android iptv-smarters-pro-windows
        iptv-smarters-pro-apple-tv iptv-smarters-lite iptv-smarters-pro-premium tivimate iptv-tivimate
        iptv-tivimate-deutschland tivimate-premium tivimate-fire-tv-stick tivimate-samsung-tv tivimate-apple-tv
        smart-iptv-deutschland smart-iptv-download smart-iptv-playlist-hochladen smart-iptv-samsung siptv ssiptv
        set-iptv smartone-iptv flix-iptv hot-iptv duplecast-iptv gse-iptv ibo-player implayer ott-navigator
        xciptv stb-emu iptv-extreme iptv-streamplayer iptvpro iptvx cloud-stream iptv-app beste-iptv-app bester-iptv-player
        iptv-player-android iptv-vlc iptv-kodi iptv-kodi-deutschland iptv-plex iptv-jellyfin iptv-web-player
        iptv-downloader blog/iptv-smarters-pro-anleitung blog/tivimate-einrichten-anleitung"""),
    'hilfe': ('iptv-einrichten', 'Einrichtung & Hilfe', """
        iptv-einrichten-anleitung iptv-setup iptv-ruckelt iptv-ruckelt-buffering iptv-buffer iptv-wlan-probleme
        iptv-epg iptv-epg-probleme iptv-catchup iptv-aufnehmen iptv-router iptv-fritzbox iptv-vpn
        iptv-mobile-daten iptv-m3u iptv-m3u8 iptv-m3u-playlist-deutschland iptv-playlist iptv-playlist-deutsch
        iptv-liste xtream-iptv iptv-line iptv-server iptv-kundenservice iptv-4k iptv-8k"""),
    'kaufen': ('iptv-kaufen', 'Pakete & Preise', """
        iptv-abo iptv-abonnement iptv-subscription iptv-kosten iptv-guenstig iptv-gutschein iptv-per-paypal
        iptv-1-monat iptv-3-monate iptv-6-monate iptv-12-monate iptv-jahresabo iptv-2-geraete iptv-3-geraete
        iptv-4-geraete iptv-5-geraete iptv-6-geraete iptv-7-geraete iptv-8-geraete iptv-9-geraete iptv-10-geraete
        iptv-premium iptv-premium-4k iptv-sofort iptv-ohne-vertrag iptv-lifetime iptv-reseller
        iptv-reseller-deutschland"""),
    'testen': ('iptv-gratis-testen', 'Kostenlos testen', """
        iptv-free-trial iptv-gratis iptv-kostenlos iptv-probe iptv-test iptv-test-2026 iptv-testline iptv-tester"""),
    'vergleich': ('iptv-anbieter-vergleich', 'Anbieter-Vergleich', """
        bester-iptv-anbieter best-iptv-provider iptv-anbieter iptv-vergleich iptv-testsieger iptv-testbericht
        iptv-legal iptv-legal-deutschland iptv-legal-sicher iptv-forum iptv-aliexpress iptv-anbieter-alternativen
        iptv-streaming-vergleich"""),
    'alternativen': ('iptv-anbieter-alternativen', 'Anbieter-Alternativen', """
        b1g-iptv crystal-iptv eagle-iptv extreme-iptv fast-iptv forevertv golden-iptv hakuna-iptv
        helix-iptv lion-iptv mango-iptv mega-iptv norago-iptv nord-iptv nova-iptv ottiptv pandar-tv perfect-iptv
        ragnar-iptv room-iptv sebastian-iptv sero-iptv strong-iptv trex-iptv upiptv world-iptv xtreme-hd-iptv
        iptvportal"""),
    'grundlagen': ('was-ist-iptv', 'IPTV verstehen', """
        ip-television blog/was-ist-iptv-erklaert iptv-deutschland iptv-germany german-iptv tv-und-internet
        iptv-vs-kabel iptv-vs-satellit iptv-glasfaser sat-ip"""),
}

START, END = '<!-- seo-related -->', '<!-- /seo-related -->'
HSTART, HEND = '<!-- seo-hub-index -->', '<!-- /seo-hub-index -->'


def members(key):
    return CLUSTERS[key][2].split()


def page_path(slug):
    return os.path.join(PUB, slug, 'index.html')


def label(slug, cache={}):
    if slug in cache:
        return cache[slug]
    s = open(page_path(slug), encoding='utf-8').read()
    m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    t = re.sub(r'<[^>]+>', '', m.group(1)) if m else slug
    t = re.sub(r'\s+', ' ', t.replace('&amp;', '&')).strip()
    t = re.split(r' [–|:-] | \(', t)[0]
    t = re.sub(r'\s*\b20\d\d\b\s*', ' ', t).strip(' –-:?') or slug
    if len(t) > 48:
        t = t[:46].rsplit(' ', 1)[0] + '…'
    cache[slug] = t
    return t


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;')


def card(slug, text):
    return (f'<a href="/{slug}/" style="background:#0d0d0d;border:1px solid #1e1e1e;border-radius:8px;padding:12px 16px;'
            f'color:#aaa;font-size:0.88rem;display:block">→ {esc(text)}</a>')


def box(title, inner, start, end):
    return (f'{start}<div style="max-width:900px;margin:32px auto;padding:28px;background:#111;border:1px solid #1e1e1e;'
            f'border-radius:12px"><h2 style="font-size:1.1rem;font-weight:700;margin-bottom:16px;color:#fff">{esc(title)}</h2>'
            f'{inner}</div>{end}')


def unique_cards(slugs):
    """Cards for a full index; pages sharing a short label get their URL slug added so readers can tell them apart."""
    from collections import Counter
    c = Counter(label(m) for m in slugs)
    return (card(m, label(m) if c[label(m)] == 1 else f'{label(m)} ({m.replace("-", " ")})') for m in slugs)


def grid(cards):
    return f'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px">{"".join(cards)}</div>'


def insert(s, block, start, end):
    s = re.sub(re.escape(start) + '.*?' + re.escape(end) + r'\n?', '', s, flags=re.S)
    if '<!-- seo-cluster-links -->' in s:  # keep next to the older "Mehr zum Thema" block
        return s.replace('<!-- /seo-cluster-links -->', '<!-- /seo-cluster-links -->\n' + block, 1)
    if '<div class="cta-block">' in s:
        return s.replace('<div class="cta-block">', block + '\n<div class="cta-block">', 1)
    m = re.search(r'<footer\b', s)
    if not m:
        return None
    return s[:m.start()] + block + '\n' + s[m.start():]


def existing_links(s):
    return set(re.findall(r'href="/([^"#?]+?)/?"', s))


def related_for(slug, key, s, n=8):
    hub = CLUSTERS[key][0]
    mem = [m for m in members(key) if os.path.exists(page_path(m))]
    pool = [m for m in mem if m != slug]
    have = existing_links(re.sub(re.escape(START) + '.*?' + re.escape(END), '', s, flags=re.S))
    picks = []
    if slug != hub:
        picks.append(hub)
    if slug in mem:
        i = mem.index(slug)
        ring = mem[i + 1:] + mem[:i]
    else:
        ring = pool
    for m in ring:
        if len(picks) >= n:
            break
        if m not in picks and m not in have and label(m) not in {label(x) for x in picks} | {label(slug)}:
            picks.append(m)
    for m in ring:  # top up with already-linked siblings if the cluster is small
        if len(picks) >= n:
            break
        if m not in picks and label(m) not in {label(x) for x in picks} | {label(slug)}:
            picks.append(m)
    return picks


def main():
    stats = {'related': 0, 'hub': 0, 'state': 0}
    where = {}
    for key, (hub, _, _) in CLUSTERS.items():
        for m in members(key):
            where.setdefault(m, key)
        where.setdefault(hub, key)
    # sibling blocks
    for slug, key in where.items():
        p = page_path(slug)
        if not os.path.exists(p):
            print('missing page', slug)
            continue
        s = open(p, encoding='utf-8').read()
        picks = related_for(slug, key, s)
        block = box('Verwandte Themen', grid(card(m, label(m)) for m in picks), START, END)
        new = insert(s, block, START, END)
        if new and new != s:
            open(p, 'w', encoding='utf-8').write(new)
            stats['related'] += 1
    # hub indexes
    hubs = {}
    for key, (hub, title, _) in CLUSTERS.items():
        hubs.setdefault(hub, []).append(key)
    for hub, keys in hubs.items():
        p = page_path(hub)
        s = open(p, encoding='utf-8').read()
        inner = ''
        for key in keys:
            mem = [m for m in members(key) if os.path.exists(page_path(m)) and m != hub]
            if len(keys) > 1:
                inner += f'<h3 style="font-size:0.95rem;color:#fff;margin:16px 0 10px">{esc(CLUSTERS[key][1])}</h3>'
            inner += grid(unique_cards(mem))
        block = box(f'Alle Seiten: {CLUSTERS[keys[0]][1]}' if len(keys) == 1 else 'Alle Sender-Seiten', inner, HSTART, HEND)
        new = insert(s, block, HSTART, HEND)
        if new and new != s:
            open(p, 'w', encoding='utf-8').write(new)
            stats['hub'] += 1
    # Bundesland pages list all their towns; /iptv-deutschland/ lists the Bundesländer
    for code, hub in places.STATE_HUB.items():
        towns = sorted((k for k, (nm, c) in places.PLACES.items() if c == code and k != hub
                        and os.path.exists(page_path(k))), key=lambda k: places.PLACES[k][0])
        if not towns or not os.path.exists(page_path(hub)):
            continue
        s = open(page_path(hub), encoding='utf-8').read()
        block = box(f'IPTV in {places.STATES[code]}: alle Orte', grid(card(k, f'IPTV {places.PLACES[k][0]}') for k in towns), HSTART, HEND)
        new = insert(s, block, HSTART, HEND)
        if new and new != s:
            open(page_path(hub), 'w', encoding='utf-8').write(new)
            stats['state'] += 1
    states = [(hub, places.STATES[c]) for c, hub in places.STATE_HUB.items() if c not in ('CH', 'AT')]
    extra = [('iptv-ruhrgebiet', 'Ruhrgebiet'), ('iptv-rhein-main', 'Rhein-Main-Gebiet'),
             ('iptv-oesterreich', 'Österreich'), ('iptv-schweiz', 'Schweiz')]
    p = page_path('iptv-deutschland')
    s = open(p, encoding='utf-8').read()
    block = box('IPTV nach Bundesland & Region',
                grid(card(h, f'IPTV {n}') for h, n in sorted(states, key=lambda x: x[1]) + extra), HSTART, HEND)
    new = insert(s, block, HSTART, HEND)
    if new and new != s:
        open(p, 'w', encoding='utf-8').write(new)
        stats['state'] += 1
    print(stats)


if __name__ == '__main__':
    main()
