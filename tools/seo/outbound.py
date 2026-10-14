#!/usr/bin/env python3
"""Links to official / authoritative sources on pages where a reader benefits (SEO audit 2026-10-13).

Inserted just above the "Verwandte Themen" block. Idempotent.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402

START, END = '<!-- seo-sources -->', '<!-- /seo-sources -->'

WIKI_IPTV = ('https://de.wikipedia.org/wiki/Internet_Protocol_Television', 'Internet Protocol Television (Wikipedia)')
SMARTERS = ('https://www.iptvsmarters.com/', 'offizielle Website von IPTV Smarters')
TIVIMATE = ('https://play.google.com/store/apps/details?id=ar.tvplayer.tv', 'TiviMate im Google Play Store')
SIPTV = ('https://siptv.app/', 'offizielle Website von Smart IPTV')
VLC = ('https://www.videolan.org/vlc/', 'VLC media player (VideoLAN)')
KODI = ('https://kodi.wiki/view/Add-on:PVR_IPTV_Simple_Client', 'PVR IPTV Simple Client im Kodi-Wiki')
SPEED = ('https://breitbandmessung.de/', 'Breitbandmessung der Bundesnetzagentur')
M3U = ('https://de.wikipedia.org/wiki/M3U', 'M3U-Format (Wikipedia)')
EPG = ('https://de.wikipedia.org/wiki/Elektronischer_Programmf%C3%BChrer', 'Elektronischer Programmführer (Wikipedia)')
URHG = ('https://www.gesetze-im-internet.de/urhg/', 'Urheberrechtsgesetz (gesetze-im-internet.de)')
EUGH = ('https://curia.europa.eu/juris/liste.jsf?num=C-527/15', 'EuGH-Urteil C-527/15 „Filmspeler“')
JOYN = ('https://www.joyn.de/', 'Joyn (Mediathek von ProSieben, SAT.1 & Co.)')
RTLPLUS = ('https://plus.rtl.de/', 'RTL+')

SOURCES = {
    'was-ist-iptv': [WIKI_IPTV], 'ip-television': [WIKI_IPTV], 'blog/was-ist-iptv-erklaert': [WIKI_IPTV],
    'iptv-smarters-pro': [SMARTERS], 'iptv-smarters': [SMARTERS], 'iptv-smarters-pro-deutschland': [SMARTERS],
    'iptv-smarters-pro-windows': [SMARTERS], 'iptv-smarters-lite': [SMARTERS], 'iptv-smarters-pro-premium': [SMARTERS],
    'blog/iptv-smarters-pro-anleitung': [SMARTERS],
    'tivimate': [TIVIMATE], 'iptv-tivimate': [TIVIMATE], 'iptv-tivimate-deutschland': [TIVIMATE],
    'tivimate-premium': [TIVIMATE], 'tivimate-fire-tv-stick': [TIVIMATE], 'blog/tivimate-einrichten-anleitung': [TIVIMATE],
    'smart-iptv-deutschland': [SIPTV], 'siptv': [SIPTV], 'smart-iptv-download': [SIPTV],
    'smart-iptv-playlist-hochladen': [SIPTV], 'smart-iptv-samsung': [SIPTV],
    'ssiptv': [('https://ss-iptv.com/', 'offizielle Website von SS IPTV')],
    'ibo-player': [('https://iboplayer.com/', 'offizielle Website des IBO Players')],
    'ott-navigator': [('https://play.google.com/store/apps/details?id=studio.scillarium.ottnavigator', 'OTT Navigator im Google Play Store')],
    'iptv-vlc': [VLC], 'iptv-pc': [VLC], 'iptv-linux': [VLC], 'iptv-macbook': [VLC],
    'iptv-kodi': [('https://kodi.tv/', 'offizielle Kodi-Website'), KODI], 'iptv-kodi-deutschland': [('https://kodi.tv/', 'offizielle Kodi-Website'), KODI],
    'iptv-plex': [('https://www.plex.tv/', 'Plex'), ('https://jellyfin.org/', 'Jellyfin')],
    'iptv-jellyfin': [('https://jellyfin.org/docs/', 'Jellyfin-Dokumentation')],
    'iptv-raspberry-pi': [('https://www.raspberrypi.com/', 'Raspberry Pi Foundation')],
    'iptv-mag-box': [('https://www.infomir.eu/', 'Infomir (Hersteller der MAG-Boxen)')],
    'mag-box-modelle': [('https://www.infomir.eu/', 'Infomir (Hersteller der MAG-Boxen)')],
    'iptv-formuler': [('https://formuler.tv/', 'Formuler')], 'formuler-tv-box': [('https://formuler.tv/', 'Formuler')],
    'iptv-nvidia-shield': [('https://www.nvidia.com/de-de/shield/', 'NVIDIA SHIELD TV')],
    'iptv-apple-tv': [('https://www.apple.com/de/apple-tv-4k/', 'Apple TV 4K bei Apple')],
    'iptv-apple-tv-4k': [('https://www.apple.com/de/apple-tv-4k/', 'Apple TV 4K bei Apple')],
    'iptv-samsung-tv-deutschland': [('https://www.samsung.com/de/support/', 'Samsung Support Deutschland')],
    'iptv-lg-tv-deutschland': [('https://www.lg.com/de/support/', 'LG Support Deutschland')],
    'iptv-fritzbox': [('https://avm.de/service/', 'AVM Service für FRITZ!Box')],
    'iptv-ruckelt': [SPEED], 'iptv-ruckelt-buffering': [SPEED], 'iptv-buffer': [SPEED], 'iptv-wlan-probleme': [SPEED],
    'iptv-glasfaser': [SPEED], 'iptv-mobile-daten': [SPEED], 'iptv-4k': [SPEED],
    'iptv-m3u': [M3U], 'iptv-m3u8': [M3U, ('https://datatracker.ietf.org/doc/html/rfc8216', 'HLS-Spezifikation RFC 8216')],
    'iptv-playlist': [M3U], 'iptv-liste': [M3U],
    'iptv-epg': [EPG], 'iptv-epg-probleme': [EPG],
    'iptv-legal': [URHG, EUGH], 'iptv-legal-deutschland': [URHG, EUGH], 'iptv-legal-sicher': [URHG, EUGH],
    'iptv-bundesliga': [('https://www.bundesliga.com/de', 'bundesliga.com')],
    'iptv-2-bundesliga': [('https://www.bundesliga.com/de/2bundesliga', '2. Bundesliga auf bundesliga.com')],
    'iptv-champions-league': [('https://de.uefa.com/uefachampionsleague/', 'UEFA Champions League')],
    'iptv-europa-league': [('https://de.uefa.com/uefaeuropaleague/', 'UEFA Europa League')],
    'iptv-f1': [('https://www.formula1.com/', 'Formel 1 (formula1.com)')],
    'iptv-ard-zdf': [('https://www.ardmediathek.de/', 'ARD Mediathek'), ('https://www.zdf.de/', 'ZDF')],
    'iptv-arte': [('https://www.arte.tv/de/', 'ARTE')], 'iptv-3sat': [('https://www.3sat.de/', '3sat')],
    'iptv-br': [('https://www.br.de/', 'BR')], 'iptv-hr': [('https://www.hr.de/', 'hr')],
    'iptv-mdr': [('https://www.mdr.de/', 'MDR')], 'iptv-ndr': [('https://www.ndr.de/', 'NDR')],
    'iptv-swr': [('https://www.swr.de/', 'SWR')], 'iptv-wdr': [('https://www1.wdr.de/', 'WDR')],
    'iptv-ntv': [('https://www.n-tv.de/', 'n-tv')], 'iptv-rtl': [RTLPLUS], 'iptv-rtl-plus': [RTLPLUS], 'iptv-vox': [RTLPLUS],
    'iptv-prosieben': [JOYN], 'iptv-prosieben-maxx': [JOYN], 'iptv-sat1': [JOYN], 'iptv-sat1-gold': [JOYN],
    'iptv-kabel-1': [JOYN], 'iptv-sixx': [JOYN],
    'iptv-sky': [('https://www.sky.de/', 'Sky Deutschland')], 'iptv-sky-go': [('https://www.sky.de/', 'Sky Deutschland')],
    'iptv-dazn': [('https://www.dazn.com/de-DE', 'DAZN')],
    'iptv-zattoo': [('https://zattoo.com/de', 'Zattoo')],
    'iptv-magenta-tv': [('https://www.telekom.de/magenta-tv', 'MagentaTV der Telekom')],
    'iptv-telekom': [('https://www.telekom.de/magenta-tv', 'MagentaTV der Telekom')],
}


def block(links):
    a = ', '.join(f'<a href="{u}" target="_blank" rel="noopener" style="color:#e53935">{t}</a>' for u, t in links)
    return (f'{START}<div style="max-width:900px;margin:24px auto 0;padding:0 4px"><p style="color:#8c8c8c;font-size:0.85rem;'
            f'line-height:1.7">Offizielle Informationen: {a}.</p></div>{END}')


def main():
    n = 0
    for slug, links in SOURCES.items():
        p = os.path.join(audit.PUB, slug, 'index.html')
        if not os.path.exists(p):
            print('missing', slug)
            continue
        s0 = s = open(p, encoding='utf-8').read()
        s = re.sub(re.escape(START) + '.*?' + re.escape(END) + r'\n?', '', s, flags=re.S)
        b = block(links) + '\n'
        if '<!-- seo-related -->' in s:
            s = s.replace('<!-- seo-related -->', b + '<!-- seo-related -->', 1)
        elif '<div class="cta-block">' in s:
            s = s.replace('<div class="cta-block">', b + '<div class="cta-block">', 1)
        else:
            continue
        if s != s0:
            open(p, 'w', encoding='utf-8').write(s)
            n += 1
    print('sources added on', n, 'pages')


if __name__ == '__main__':
    main()
