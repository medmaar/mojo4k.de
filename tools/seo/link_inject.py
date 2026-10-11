#!/usr/bin/env python3
"""Inject internal links from existing pages to the SEO cluster pages.

1. Footer: adds the three hub pages to the footer "Navigation" column of every page.
2. Cluster blocks: adds a "Mehr zum Thema" link block to existing pillar pages.
Idempotent: re-running replaces earlier injected blocks instead of duplicating them.
"""
import glob
import os
import re

PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'public')

HUB_LINKS = ('<a href="/iptv-apps/">IPTV Apps</a><a href="/iptv-geraete/">IPTV Geräte</a>'
             '<a href="/iptv-anbieter-alternativen/">Anbieter-Alternativen</a>')

CLUSTERS = {
    'smarters': [('iptv-smarters-pro-fire-tv-stick', 'Smarters Pro auf dem Fire TV Stick'),
                 ('iptv-smarters-pro-samsung-tv', 'Smarters Pro auf Samsung TV'),
                 ('iptv-smarters-pro-android', 'Smarters Pro für Android'),
                 ('iptv-smarters-pro-windows', 'Smarters Pro Windows Download'),
                 ('iptv-smarters-pro-apple-tv', 'Smarters auf iPhone & Apple TV'),
                 ('iptv-smarters-lite', 'IPTV Smarters Lite'),
                 ('iptv-smarters-pro-premium', 'Smarters Pro Premium erklärt'),
                 ('bester-iptv-player', 'Bester IPTV Player 2026')],
    'tivimate': [('tivimate-fire-tv-stick', 'TiviMate auf dem Fire TV Stick'),
                 ('tivimate-samsung-tv', 'TiviMate auf Samsung TV'),
                 ('tivimate-apple-tv', 'TiviMate für Apple TV & iPhone'),
                 ('iptv-aufnehmen', 'IPTV aufnehmen'),
                 ('bester-iptv-player', 'Bester IPTV Player 2026'),
                 ('iptv-apps', 'Alle IPTV Apps')],
    'smartiptv': [('smart-iptv-playlist-hochladen', 'Smart IPTV Playlist hochladen'),
                  ('smart-iptv-samsung', 'Smart IPTV auf Samsung'),
                  ('smart-iptv-download', 'Smart IPTV herunterladen'),
                  ('ibo-player', 'IBO Player einrichten'),
                  ('iptv-apps', 'Alle IPTV Apps')],
    'apps': [('iptv-apps', 'Alle IPTV Apps im Überblick'), ('bester-iptv-player', 'Bester IPTV Player 2026'),
             ('ibo-player', 'IBO Player'), ('iptv-vlc', 'IPTV mit VLC'), ('iptv-web-player', 'IPTV im Browser'),
             ('iptv-downloader', 'Downloader App')],
    'devices': [('iptv-geraete', 'Alle IPTV Geräte'), ('beste-iptv-box', 'Beste IPTV Box 2026'),
                ('iptv-set-top-box', 'IPTV Set-Top-Box'), ('mag-box-modelle', 'MAG Box Modelle'),
                ('formuler-tv-box', 'Formuler TV Box'), ('tvip-s-box', 'TVIP S-Box'), ('iptv-8k', 'IPTV 8K')],
    'firetv': [('iptv-smarters-pro-fire-tv-stick', 'Smarters Pro auf dem Fire TV Stick'),
               ('tivimate-fire-tv-stick', 'TiviMate auf dem Fire TV Stick'),
               ('iptv-downloader', 'Downloader App installieren'), ('beste-iptv-box', 'Beste IPTV Box 2026'),
               ('iptv-geraete', 'Alle IPTV Geräte')],
    'samsung': [('iptv-smarters-pro-samsung-tv', 'Smarters Pro auf Samsung TV'),
                ('tivimate-samsung-tv', 'TiviMate auf Samsung TV'), ('smart-iptv-samsung', 'Smart IPTV auf Samsung'),
                ('ibo-player', 'IBO Player'), ('iptv-geraete', 'Alle IPTV Geräte')],
    'apple': [('iptv-smarters-pro-apple-tv', 'Smarters auf iPhone & Apple TV'),
              ('tivimate-apple-tv', 'TiviMate-Alternativen für Apple TV'), ('ibo-player', 'IBO Player'),
              ('iptv-geraete', 'Alle IPTV Geräte')],
    'pc': [('iptv-smarters-pro-windows', 'Smarters Pro für Windows & Mac'), ('iptv-vlc', 'IPTV mit VLC'),
           ('iptv-web-player', 'IPTV im Browser'), ('iptv-jellyfin', 'IPTV in Jellyfin')],
    'm3u': [('iptv-m3u8', 'M3U & M3U8 erklärt'), ('iptv-liste', 'IPTV Liste richtig nutzen'),
            ('iptv-vlc', 'M3U in VLC öffnen'), ('smart-iptv-playlist-hochladen', 'Playlist in Smart IPTV hochladen'),
            ('iptv-server', 'IPTV Server erklärt')],
    'mediacenter': [('iptv-jellyfin', 'IPTV in Jellyfin'), ('iptv-aufnehmen', 'IPTV aufnehmen'),
                    ('iptv-vlc', 'IPTV mit VLC'), ('iptv-m3u8', 'M3U & M3U8 erklärt')],
    'sky': [('sky-q-iptv-box', 'Sky Q IPTV Box erklärt'), ('tv-und-internet', 'TV und Internet im Vergleich')],
    'isp': [('tv-und-internet', 'TV und Internet: Telekom, Vodafone, 1&1, O2'), ('iptv-server', 'IPTV Server erklärt'),
            ('iptv-8k', 'IPTV 8K')],
    'community': [('iptv-ex-yu', 'IP televizija – Ex-YU & Balkan'), ('iptv-rumaenisch', 'IPTV Rumänisch'),
                  ('iptv-georgisch', 'IPTV Georgisch'), ('iptv-england', 'IPTV England / UK')],
    'providers': [('iptv-anbieter-alternativen', 'IPTV Anbieter Alternativen'), ('iptv-lifetime', 'IPTV Lifetime – Vorsicht'),
                  ('iptv-aliexpress', 'IPTV bei Aliexpress kaufen?'), ('iptv-forum', 'IPTV Forum & Reddit')],
    'home': [('iptv-apps', 'IPTV Apps'), ('iptv-geraete', 'IPTV Geräte'), ('bester-iptv-player', 'Bester IPTV Player'),
             ('beste-iptv-box', 'Beste IPTV Box'), ('iptv-anbieter-alternativen', 'Anbieter-Alternativen'),
             ('iptv-ex-yu', 'IP televizija (Ex-YU)'), ('tv-und-internet', 'TV und Internet')],
}

TARGETS = {
    'index.html': 'home',
    'iptv-smarters-pro/index.html': 'smarters', 'iptv-smarters/index.html': 'smarters',
    'iptv-smarters-pro-deutschland/index.html': 'smarters',
    'tivimate/index.html': 'tivimate', 'tivimate-premium/index.html': 'tivimate',
    'iptv-tivimate-deutschland/index.html': 'tivimate', 'iptv-tivimate/index.html': 'tivimate',
    'smart-iptv-deutschland/index.html': 'smartiptv', 'siptv/index.html': 'smartiptv', 'ssiptv/index.html': 'smartiptv',
    'set-iptv/index.html': 'smartiptv',
    'iptv-app/index.html': 'apps', 'beste-iptv-app/index.html': 'apps', 'iptv-player-android/index.html': 'apps',
    'iptvapp/index.html': 'apps', 'xciptv/index.html': 'apps', 'ott-navigator/index.html': 'apps',
    'iptv-box/index.html': 'devices', 'iptv-stick/index.html': 'devices', 'iptv-receiver-deutschland/index.html': 'devices',
    'iptv-mag-box/index.html': 'devices', 'iptv-formuler/index.html': 'devices', 'iptv-box-formuler-mag/index.html': 'devices',
    'iptv-android-box-deutschland/index.html': 'devices', 'iptv-4k/index.html': 'devices', 'iptv-premium-4k/index.html': 'devices',
    'stb-emu/index.html': 'devices', 'iptv-smart-tv/index.html': 'devices',
    'iptv-fire-stick-deutschland/index.html': 'firetv', 'fire-tv-stick-iptv/index.html': 'firetv',
    'iptv-firestick/index.html': 'firetv', 'iptv-fire-stick-deutschland/index.html': 'firetv',
    'iptv-samsung-tv-deutschland/index.html': 'samsung', 'iptv-samsung-qled/index.html': 'samsung',
    'iptv-samsung-frame/index.html': 'samsung', 'iptv-lg-tv-deutschland/index.html': 'samsung',
    'iptv-apple-tv/index.html': 'apple', 'iptv-iphone/index.html': 'apple', 'iptv-ipad/index.html': 'apple',
    'iptv-apple-tv-4k/index.html': 'apple',
    'iptv-pc/index.html': 'pc', 'iptv-macbook/index.html': 'pc', 'iptv-windows-11/index.html': 'pc',
    'iptv-windows-10/index.html': 'pc', 'iptv-linux/index.html': 'pc',
    'iptv-m3u/index.html': 'm3u', 'iptv-playlist/index.html': 'm3u', 'iptv-m3u-playlist-deutschland/index.html': 'm3u',
    'iptv-playlist-deutsch/index.html': 'm3u', 'xtream-iptv/index.html': 'm3u', 'iptv-line/index.html': 'm3u',
    'iptv-kodi/index.html': 'mediacenter', 'iptv-kodi-deutschland/index.html': 'mediacenter', 'iptv-plex/index.html': 'mediacenter',
    'iptv-catchup/index.html': 'mediacenter',
    'iptv-sky/index.html': 'sky', 'iptv-sky-sport/index.html': 'sky', 'iptv-sky-alternative/index.html': 'sky',
    'iptv-telekom/index.html': 'isp', 'iptv-magenta-tv/index.html': 'isp', 'iptv-vodafone-internet/index.html': 'isp',
    'iptv-glasfaser/index.html': 'isp', 'iptv-vs-kabel/index.html': 'isp', 'was-ist-iptv/index.html': 'isp',
    'ip-television/index.html': 'isp',
    'iptv-alle-sender/index.html': 'community', 'iptv-albanisch/index.html': 'community', 'iptv-europe/index.html': 'community',
    'iptv-polnisch/index.html': 'community', 'iptv-russisch/index.html': 'community',
    'iptv-anbieter-vergleich/index.html': 'providers', 'bester-iptv-anbieter/index.html': 'providers',
    'iptv-vergleich/index.html': 'providers', 'iptv-test/index.html': 'providers', 'iptv-anbieter/index.html': 'providers',
    'best-iptv-provider/index.html': 'providers', 'iptv-legal/index.html': 'providers',
}

START, END = '<!-- seo-cluster-links -->', '<!-- /seo-cluster-links -->'


def block(links):
    items = ''.join(
        f'<a href="/{s}/" style="background:#0d0d0d;border:1px solid #1e1e1e;border-radius:8px;padding:12px 16px;'
        f'color:#aaa;font-size:0.88rem;display:block">→ {n}</a>' for s, n in links)
    return (f'{START}<div style="max-width:900px;margin:32px auto;padding:28px;background:#111;border:1px solid #1e1e1e;'
            f'border-radius:12px"><h2 style="font-size:1.1rem;font-weight:700;margin-bottom:16px;color:#fff">Mehr zum Thema</h2>'
            f'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px">{items}</div></div>{END}')


def inject_cluster(path, key):
    s = open(path, encoding='utf-8').read()
    s = re.sub(re.escape(START) + '.*?' + re.escape(END), '', s, flags=re.S)
    b = block(CLUSTERS[key])
    if '<div class="cta-block">' in s:
        s = s.replace('<div class="cta-block">', b + '\n<div class="cta-block">', 1)
    else:
        m = re.search(r'<footer\b', s)
        if not m:
            return False
        s = s[:m.start()] + b + '\n' + s[m.start():]
    open(path, 'w', encoding='utf-8').write(s)
    return True


def inject_footer(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'(<h3>Navigation</h3>)(.*?)(</div>)', s, re.S)
    if not m or '/iptv-apps/' in m.group(2):
        return False
    s = s[:m.end(2)] + HUB_LINKS + s[m.end(2):]
    open(path, 'w', encoding='utf-8').write(s)
    return True


def main():
    n_footer = sum(inject_footer(f) for f in glob.glob(os.path.join(PUBLIC, '**', '*.html'), recursive=True))
    done, missing = 0, []
    for rel, key in TARGETS.items():
        p = os.path.join(PUBLIC, rel)
        if os.path.exists(p) and inject_cluster(p, key):
            done += 1
        else:
            missing.append(rel)
    print(f'footer links added to {n_footer} pages; cluster blocks on {done} pages; skipped {missing}')


if __name__ == '__main__':
    main()
