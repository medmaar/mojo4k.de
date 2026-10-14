"""Deeper sections for thin keyword pages (used by deepen.py, SEO audit 2026-10-13).

Only facts the site states elsewhere (prices, 24h test, up to 10 devices, WhatsApp/e-mail support) plus
general, verifiable technical background. No ratings, customer counts or competitor figures.
"""

PRICES = ['1 Monat: 9 €', '3 Monate: 29 € (rund 9,67 € pro Monat)', '6 Monate: 39 € (6,50 € pro Monat)',
          '12 Monate: 49 € (rund 4,08 € pro Monat)']
TEST = 'Testen Sie vorher 24 Stunden kostenlos über <a href="/kostenlos-testen">das Testformular</a>.'

DEEPEN = {
    'iptv-smarters': {
        'sections': [
            ('Smarters Pro, Smarters Lite oder Smarters Player?', [
                ('p', 'Unter dem Namen Smarters gibt es mehrere Apps. Für Live-TV mit Filmen und Serien ist <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> die übliche Wahl. <a href="/iptv-smarters-lite/">Smarters Lite</a> ist schlanker und läuft auf schwächeren Geräten flüssiger. Der Smarters Player auf manchen Smart TVs wird teils über eine Website aktiviert statt direkt per Login.'),
                ('table', ['App', 'Stärke', 'Login'], [
                    ['IPTV Smarters Pro', 'volle Oberfläche mit Filmen, Serien, EPG', 'Xtream oder M3U'],
                    ['Smarters Lite', 'läuft auf älteren Geräten', 'Xtream oder M3U'],
                    ['Smarters für Windows', 'Desktop-Version', 'Xtream oder M3U'],
                ]),
            ]),
            ('Die häufigsten Fehler in Smarters und ihre Lösung', [
                ('ul', [
                    '<strong>„Invalid credentials“ / Anmeldung fehlgeschlagen:</strong> Benutzername und Passwort ohne Leerzeichen kopieren, Server-URL mit <code>http://</code> und Port übernehmen.',
                    '<strong>Filme und Serien fehlen:</strong> Im Menü „Inhalte neu laden“ wählen; beim ersten Laden großer Bibliotheken etwas warten.',
                    '<strong>Kein TV-Programm:</strong> „EPG installieren“ bzw. „EPG aktualisieren“ ausführen.',
                    '<strong>Bild friert ein:</strong> In den Einstellungen zwischen Hardware- und Software-Decoder wechseln, siehe <a href="/iptv-ruckelt/">IPTV ruckelt</a>.',
                ]),
                ('p', 'Mehrere Zugänge lassen sich als getrennte Profile anlegen, etwa für zwei Haushaltsmitglieder. Wie viele Geräte gleichzeitig schauen dürfen, legt Ihr Paket fest.'),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu Smarters',
        'faq': [
            ('Ist IPTV Smarters Pro kostenlos?', 'Die App ist auf den meisten Plattformen kostenlos erhältlich. Sie enthält keine Sender; diese kommen von Ihrem IPTV-Anbieter.'),
            ('Kann ich Smarters auf mehreren Geräten nutzen?', 'Ja, Sie können dieselben Zugangsdaten auf mehreren Geräten eintragen. Gleichzeitig streamen dürfen so viele Geräte, wie Ihr Paket erlaubt.'),
        ],
    },
    'iptv-kosten': {
        'sections': [
            ('Was IPTV insgesamt kostet', [
                ('p', 'Die Kosten für IPTV setzen sich aus bis zu vier Teilen zusammen. Nur der erste ist laufend; die anderen fallen einmalig oder gar nicht an.'),
                ('ol', [
                    '<strong>Das Abo</strong> beim IPTV-Anbieter. Bei MOJO4K.DE für 1 Gerät: ' + ', '.join(PRICES) + '.',
                    '<strong>Ein Abspielgerät</strong>, falls Ihr Fernseher keine passende App hat, zum Beispiel ein <a href="/iptv-stick/">IPTV-Stick</a>.',
                    '<strong>Eine App-Lizenz</strong> bei manchen Smart-TV-Playern wie <a href="/set-iptv/">Set IPTV</a> oder <a href="/siptv/">SIPTV</a>; Apps wie IPTV Smarters Pro sind kostenlos.',
                    '<strong>Der Internetanschluss</strong>, den Sie meist ohnehin haben. Wir empfehlen mindestens 25 Mbit/s für HD und 50 Mbit/s für 4K.',
                ]),
            ]),
            ('Monatspreis im Vergleich der Laufzeiten', [
                ('table', ['Laufzeit', 'Preis', 'pro Monat'], [
                    ['1 Monat', '9 €', '9,00 €'], ['3 Monate', '29 €', '9,67 €'], ['6 Monate', '39 €', '6,50 €'], ['12 Monate', '49 €', '4,08 €'],
                ]),
                ('p', 'Pakete für mehrere gleichzeitige Geräte (bis zu 10) kosten entsprechend mehr; die genauen Preise stehen unter <a href="/preise/">Preise</a>. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu den IPTV Kosten',
        'faq': [
            ('Gibt es versteckte Kosten bei IPTV?', 'Beim Abo von MOJO4K.DE zahlen Sie den Paketpreis. Zusätzliche Kosten können nur für ein Abspielgerät oder eine kostenpflichtige Player-App entstehen, die Sie selbst wählen.'),
            ('Welche Laufzeit ist am günstigsten?', 'Pro Monat gerechnet das 12-Monats-Paket mit rund 4,08 € im Monat. Wer erst ausprobieren will, startet mit dem kostenlosen 24h-Test oder einem Monat.'),
        ],
    },
    'iptv-kodi-deutschland': {
        'sections': [
            ('Die wichtigsten Einstellungen im PVR IPTV Simple Client', [
                ('table', ['Einstellung', 'Wert', 'Wozu'], [
                    ['Speicherort', 'Pfad aus dem Internet (URL)', 'Playlist direkt vom Anbieter laden'],
                    ['M3U-Playlist-URL', 'Ihr M3U-Link', 'Senderliste'],
                    ['EPG-Einstellungen → XMLTV-URL', 'EPG-Link des Anbieters', 'Programmguide'],
                    ['M3U zwischenspeichern', 'an', 'schnellerer Start'],
                    ['Kanalsymbole', 'aus der Playlist', 'Senderlogos'],
                ]),
                ('p', 'Nach dem Speichern Kodi einmal neu starten. Die Sender erscheinen dann unter „TV“, das Programm unter „TV → Guide“. Grundlagen zum Add-on stehen im Kodi-Wiki.'),
            ]),
            ('Kodi ruckelt oder lädt keine Sender', [
                ('ul', [
                    'Playlist-URL im Browser öffnen: Lädt eine Datei, ist der Zugang aktiv.',
                    'Unter Einstellungen → PVR & Live-TV „Daten löschen“ wählen und neu laden lassen.',
                    'Auf schwachen Geräten die Hardware-Beschleunigung im Player aktivieren.',
                    'Bei Pufferproblemen hilft eine LAN-Verbindung, mehr unter <a href="/iptv-buffer/">IPTV Buffering</a>.',
                ]),
                ('p', 'Wer Filme und Serien bequem durchsuchen will, ist mit einer IPTV-App wie <a href="/tivimate/">TiviMate</a> oft besser bedient; Kodi spielt seine Stärken bei Live-TV mit Aufnahme-Add-ons und eigener Mediathek aus.'),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu Kodi und IPTV',
        'faq': [
            ('Welches Add-on brauche ich für IPTV in Kodi?', 'Das offizielle Add-on „PVR IPTV Simple Client“. Es ist in Kodi enthalten und muss nur aktiviert und konfiguriert werden.'),
            ('Unterstützt Kodi Xtream Codes?', 'Der Simple Client arbeitet mit M3U-Links. Nutzen Sie dafür den M3U-Link aus Ihren Zugangsdaten.'),
        ],
    },
    'iptv-player-android': {
        'sections': [
            ('Android IPTV Player im Überblick', [
                ('table', ['Player', 'Geeignet für', 'Login'], [
                    ['<a href="/tivimate/">TiviMate</a>', 'Android TV, Fire TV, Boxen', 'Xtream, M3U'],
                    ['<a href="/iptv-smarters-pro-android/">IPTV Smarters Pro</a>', 'Handy, Tablet, TV', 'Xtream, M3U'],
                    ['<a href="/ott-navigator/">OTT Navigator</a>', 'Android TV, Boxen', 'Xtream, M3U'],
                    ['<a href="/xciptv/">XCIPTV</a>', 'Handy, TV', 'Xtream'],
                    ['<a href="/iptvpro/">IPTV Pro</a>', 'Handy, Tablet', 'M3U'],
                    ['<a href="/iptv-vlc/">VLC</a>', 'alle Android-Geräte', 'M3U'],
                ]),
            ]),
            ('Einstellungen, die auf Android den Unterschied machen', [
                ('ul', [
                    '<strong>Decoder:</strong> Hardware-Decoding ist sparsam; bei Bildfehlern auf Software-Decoding umstellen.',
                    '<strong>Puffergröße:</strong> Ein etwas größerer Puffer gleicht kurze Schwankungen im WLAN aus.',
                    '<strong>Energiesparmodus:</strong> Auf dem Handy die Akku-Optimierung für den Player abschalten, sonst bricht der Stream im Hintergrund ab.',
                    '<strong>Mobile Daten:</strong> HD verbraucht grob 1,5 bis 3 GB pro Stunde, siehe <a href="/iptv-mobile-daten/">IPTV mit mobilen Daten</a>.',
                ]),
                ('p', TEST + ' Die Zugangsdaten funktionieren in allen oben genannten Apps.'),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu Android-Playern',
        'faq': [
            ('Welcher IPTV Player ist der beste für Android TV?', 'Auf Android TV und Fire TV gilt TiviMate als besonders komfortabel. Auf Handy und Tablet ist IPTV Smarters Pro verbreitet.'),
            ('Brauche ich Root für einen IPTV Player?', 'Nein. Alle genannten Apps laufen ohne Root aus dem Play Store oder als offizielle APK des Entwicklers.'),
        ],
    },
    'iptv-playlist-deutsch': {
        'sections': [
            ('So ist eine deutsche M3U-Playlist aufgebaut', [
                ('p', 'Eine M3U-Playlist ist eine Textdatei. Sie beginnt mit <code>#EXTM3U</code>; danach folgt für jeden Sender eine Zeile <code>#EXTINF</code> mit Name, Logo und Gruppe und eine Zeile mit der Stream-Adresse.'),
                ('ul', [
                    '<code>tvg-id</code> verknüpft den Sender mit dem Programmguide (EPG).',
                    '<code>tvg-logo</code> liefert das Senderlogo.',
                    '<code>group-title</code> ordnet den Sender einer Gruppe zu, etwa „Deutschland HD“ oder „Sport“.',
                ]),
                ('p', 'Player-Apps sortieren die Sender anhand von <code>group-title</code> in Kategorien. Wer nur deutsche Sender sehen will, blendet die übrigen Gruppen in der App aus.'),
            ]),
            ('Playlist sicher verwenden', [
                ('ul', [
                    'Den M3U-Link nicht weitergeben: Er enthält Ihre Zugangsdaten.',
                    'Den Link direkt in die App laden, statt die Datei herunterzuladen; so bleibt die Liste aktuell.',
                    'Ändert sich etwas am Zugang, einfach den neuen Link hinterlegen.',
                ]),
                ('p', 'Mehr zum Format unter <a href="/iptv-m3u/">IPTV M3U</a> und <a href="/iptv-m3u8/">M3U8</a>. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zur deutschen Playlist',
        'faq': [
            ('Kann ich nur deutsche Sender anzeigen lassen?', 'Ja. In den meisten Apps lassen sich Gruppen ausblenden oder Favoritenlisten anlegen, sodass nur deutsche Sender erscheinen.'),
            ('Funktioniert die Playlist auch in VLC?', 'Ja, VLC öffnet M3U-Links über „Medien → Netzwerkstream öffnen“. Einen Programmguide zeigt VLC allerdings nicht an.'),
        ],
    },
    'iptv-vodafone-internet': {
        'sections': [
            ('IPTV über Vodafone Kabel, DSL oder Glasfaser', [
                ('p', 'IPTV-Dienste wie MOJO4K.DE laufen über jede Internetverbindung, unabhängig vom Anbieter. Sie brauchen kein TV-Paket von Vodafone und keinen GigaTV-Receiver: Der Zugang wird in einer App auf Fire TV, Smart TV oder Handy eingetragen.'),
                ('table', ['Anschluss', 'Worauf achten'], [
                    ['Kabel (DOCSIS)', 'Abends kann die Bandbreite im Wohngebiet schwanken; LAN-Kabel statt WLAN hilft.'],
                    ['DSL / VDSL', 'Für HD sollten es mindestens 25 Mbit/s sein, für 4K mindestens 50 Mbit/s.'],
                    ['Glasfaser', 'Genug Reserve für mehrere 4K-Streams, siehe <a href="/iptv-glasfaser/">IPTV mit Glasfaser</a>.'],
                ]),
            ]),
            ('Router und Leitung prüfen', [
                ('ol', [
                    'Die tatsächliche Geschwindigkeit mit der Breitbandmessung der Bundesnetzagentur testen, am besten abends.',
                    'Den Streaming-Player per LAN am Router anschließen oder einen Repeater nahe am Fernseher nutzen.',
                    'Bei Aussetzern einen anderen DNS-Server im Router oder im Gerät eintragen.',
                    'Ruckelt es weiterhin, die Tipps unter <a href="/iptv-wlan-probleme/">IPTV WLAN-Probleme</a> durchgehen.',
                ]),
                ('p', TEST + ' So sehen Sie vorab, wie stabil IPTV an Ihrem Vodafone-Anschluss läuft.'),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu IPTV mit Vodafone',
        'faq': [
            ('Brauche ich GigaTV für IPTV?', 'Nein. Ein IPTV-Zugang läuft über die Internetverbindung in einer App. GigaTV ist das eigene TV-Angebot von Vodafone und dafür nicht nötig.'),
            ('Reicht Vodafone Kabel für 4K-IPTV?', 'Bei den meisten Kabeltarifen ja. Wir empfehlen mindestens 50 Mbit/s für 4K, am besten per LAN-Kabel.'),
        ],
    },
    'iptv-premium': {
        'sections': [
            ('Woran Sie ein Premium-IPTV erkennen', [
                ('ul', [
                    '<strong>Echte HD- und 4K-Streams</strong> mit ausreichender Bitrate, nicht hochskaliertes SD.',
                    '<strong>Vollständiger EPG</strong> für alle deutschen Hauptsender.',
                    '<strong>Mehrere Formate:</strong> Xtream-Login und M3U-Link, damit jede App funktioniert.',
                    '<strong>Erreichbarer Support</strong> auf Deutsch, bei MOJO4K.DE per WhatsApp und an info@mojo4k.de.',
                    '<strong>Ein Test vor dem Kauf</strong>, bei MOJO4K.DE 24 Stunden kostenlos.',
                ]),
            ]),
            ('Was Ihr Gerät für 4K-Premium braucht', [
                ('p', '4K-Streams werden meist in H.265 (HEVC) übertragen. Das Gerät muss diesen Codec in Hardware decodieren können. Aktuelle Fire TV Sticks mit 4K, Android-TV-Boxen und neuere Smart TVs können das; ältere Full-HD-Sticks nicht.'),
                ('p', 'Dazu kommt die Leitung: wir empfehlen mindestens 50 Mbit/s für 4K. Mehr Details unter <a href="/iptv-4k/">IPTV 4K</a> und <a href="/iptv-premium-4k/">Premium 4K</a>. Pakete ab 9 € im Monat, im Jahr 49 €, siehe <a href="/preise/">Preise</a>.'),
            ]),
        ],
        'faq_title': 'Weitere Fragen zu Premium IPTV',
        'faq': [
            ('Ist Premium IPTV teurer?', 'Bei MOJO4K.DE ist 4K in allen Paketen enthalten. Der Preis hängt nur von Laufzeit und Geräteanzahl ab.'),
            ('Kann ich Premium IPTV vor dem Kauf testen?', 'Ja, mit dem kostenlosen 24-Stunden-Test. Prüfen Sie dabei vor allem die Sender, die Sie am häufigsten sehen.'),
        ],
    },
    'iptv-vergleich': {
        'head': {'title': 'IPTV Vergleich 2026 – Checkliste für den Anbieter-Test | MOJO4K.DE'},
        'sections': [
            ('Checkliste: so vergleichen Sie IPTV-Anbieter selbst', [
                ('ol', [
                    'Gibt es einen kostenlosen Test? Ohne Test kaufen Sie blind.',
                    'Laufen Ihre fünf wichtigsten Sender während des Tests abends stabil?',
                    'Ist der Programmguide (EPG) für deutsche Sender vollständig?',
                    'Werden Xtream-Login und M3U-Link geliefert, damit Ihre App funktioniert?',
                    'Wie viele Geräte dürfen gleichzeitig streamen, und was kostet ein zweites Gerät?',
                    'Ist der Support auf Deutsch erreichbar, und wie schnell kommt eine Antwort?',
                    'Sind Preise und Laufzeit klar angegeben, ohne automatische Verlängerung zu höheren Preisen?',
                ]),
            ]),
            ('Warnsignale bei IPTV-Angeboten', [
                ('ul', [
                    '„Lebenslang“-Angebote zum Einmalpreis: Ein Dienst mit laufenden Serverkosten kann das kaum dauerhaft halten, siehe <a href="/iptv-lifetime/">IPTV Lifetime</a>.',
                    'Kein Impressum, keine Kontaktmöglichkeit, nur ein Telegram-Kanal.',
                    'Kein Test und Vorkasse für ein ganzes Jahr.',
                ]),
                ('p', 'Rechtliche Fragen beantwortet <a href="/iptv-legal/">Ist IPTV legal?</a>. Den ausführlichen Anbietervergleich finden Sie unter <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zum Vergleich',
        'faq': [
            ('Wie lange sollte ich einen IPTV-Anbieter testen?', 'Ein 24-Stunden-Test reicht, wenn Sie ihn abends zur Hauptsendezeit und bei einem Live-Spiel nutzen. Dann zeigt sich, ob Leitung und Server zusammenpassen.'),
            ('Was ist wichtiger: Kanalanzahl oder Stabilität?', 'Stabilität. Entscheidend ist, dass die Sender, die Sie wirklich sehen, ohne Ruckeln laufen.'),
        ],
    },
    'iptv-bundesliga': {
        'sections': [
            ('Bundesliga per IPTV: Technik für den Spieltag', [
                ('p', 'An Spieltagen schauen viele gleichzeitig. Ob das Spiel flüssig läuft, entscheidet sich vor allem bei Ihnen zu Hause: Leitung, WLAN und Gerät.'),
                ('ul', [
                    'Mindestens 25 Mbit/s für HD und 50 Mbit/s für 4K einplanen.',
                    'Den Player per LAN anschließen, vor allem bei der Konferenz am Samstagnachmittag.',
                    'App und Gerät vor dem Anpfiff einmal neu starten.',
                    'Alle Streams laufen einige Sekunden hinter dem Live-Signal. Push-Nachrichten von Ergebnis-Apps können deshalb vorab spoilern.',
                ]),
            ]),
            ('Die passende App für Fußball', [
                ('p', '<a href="/tivimate/">TiviMate</a> zeigt das Programm mehrerer Sender übersichtlich und erlaubt Favoritenlisten für Sportsender. <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> bietet auf vielen Geräten einen Multiscreen-Modus für mehrere Spiele gleichzeitig; dafür brauchen Sie ein Paket mit entsprechend vielen Verbindungen.'),
                ('p', 'Übersicht über weitere Wettbewerbe: <a href="/iptv-2-bundesliga/">2. Bundesliga</a>, <a href="/iptv-champions-league/">Champions League</a> und <a href="/iptv-sport/">IPTV Sport</a>. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zur Bundesliga per IPTV',
        'faq': [
            ('Warum ist mein Stream hinter dem Live-Ergebnis?', 'Jeder Internet-Stream wird gepuffert und läuft einige Sekunden bis eine halbe Minute hinter dem Satellitensignal. Das ist technisch normal.'),
            ('Kann ich zwei Spiele gleichzeitig sehen?', 'Ja, mit einer App mit Multiscreen-Funktion und einem Paket für mindestens zwei gleichzeitige Verbindungen.'),
        ],
    },
    'iptv-champions-league': {
        'sections': [
            ('Champions-League-Abende ohne Ruckeln', [
                ('p', 'Dienstag und Mittwoch laufen viele Spiele parallel um 21 Uhr, dazu Partien am frühen Abend. Für einen stabilen Abend helfen drei Dinge:'),
                ('ol', [
                    'Leitung prüfen: mindestens 25 Mbit/s für HD, 50 Mbit/s für 4K.',
                    'Player per LAN anschließen oder WLAN im 5-GHz-Band nutzen.',
                    'Bei kurzen Aussetzern den Puffer in der App etwas erhöhen, siehe <a href="/iptv-buffer/">IPTV Buffering</a>.',
                ]),
            ]),
            ('Mehrere Spiele parallel verfolgen', [
                ('p', 'Mit einer Multiscreen-fähigen App und einem Paket für mehrere Geräte lassen sich zwei bis vier Spiele gleichzeitig zeigen. Bei MOJO4K.DE gibt es Pakete für bis zu 10 gleichzeitige Geräte, siehe <a href="/preise/">Preise</a>.'),
                ('p', 'Weitere Wettbewerbe: <a href="/iptv-europa-league/">Europa League</a>, <a href="/iptv-bundesliga/">Bundesliga</a>. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zur Champions League per IPTV',
        'faq': [
            ('Welche Internetgeschwindigkeit brauche ich für die Champions League in 4K?', 'Wir empfehlen mindestens 50 Mbit/s, damit auch andere Geräte im Haushalt genug Reserve haben.'),
            ('Kann ich die Champions League unterwegs sehen?', 'Ja, mit einer IPTV-App auf dem Smartphone. Im Mobilfunknetz verbraucht ein HD-Spiel grob 3 bis 5 GB.'),
        ],
    },
    'iptv-abo': {
        'sections': [
            ('Welches IPTV Abo passt zu Ihnen?', [
                ('table', ['Sie möchten …', 'Empfehlung'], [
                    ['erst einmal ausprobieren', '24h kostenlos testen, dann 1 Monat für 9 €'],
                    ['eine Saison Fußball sehen', '6 Monate für 39 € oder 12 Monate für 49 €'],
                    ['am günstigsten pro Monat', '12 Monate für 49 € (rund 4,08 € im Monat)'],
                    ['auf mehreren Fernsehern gleichzeitig schauen', 'Mehrgeräte-Paket, bis zu 10 Geräte'],
                ]),
            ]),
            ('So läuft der Kauf ab', [
                ('ol', [
                    'Paket und Geräteanzahl unter <a href="/preise/">Preise</a> wählen.',
                    'Bestellung abschließen; die Zugangsdaten kommen als Xtream-Login und M3U-Link.',
                    'Daten in Ihrer App eintragen, Anleitungen unter <a href="/iptv-einrichten/">IPTV einrichten</a>.',
                    'Bei Fragen hilft der Support per WhatsApp oder an info@mojo4k.de.',
                ]),
            ]),
        ],
        'faq_title': 'Weitere Fragen zum IPTV Abo',
        'faq': [
            ('Kann ich mein IPTV Abo später auf mehr Geräte erweitern?', 'Sprechen Sie dafür den Support an. Er nennt Ihnen die Möglichkeiten für Ihr bestehendes Paket.'),
            ('Bekomme ich die Zugangsdaten sofort?', 'Die Zugangsdaten werden nach der Bestellung zugestellt; den genauen Ablauf beschreibt die Preisseite.'),
        ],
    },
    'iptv-12-monate': {
        'sections': [
            ('Rechenbeispiel: 12 Monate gegen Monatsabo', [
                ('table', ['Modell', 'Kosten für ein Jahr', 'pro Monat'], [
                    ['12 × 1 Monat', '108 €', '9,00 €'],
                    ['4 × 3 Monate', '116 €', '9,67 €'],
                    ['2 × 6 Monate', '78 €', '6,50 €'],
                    ['1 × 12 Monate', '49 €', '4,08 €'],
                ]),
                ('p', 'Wer ein ganzes Jahr schauen will, zahlt mit dem 12-Monats-Paket weniger als die Hälfte gegenüber zwölf Einzelmonaten.'),
            ]),
            ('Für wen lohnt sich das Jahresabo?', [
                ('ul', [
                    'Wenn der 24h-Test auf Ihren Geräten stabil lief.',
                    'Wenn Sie über eine ganze Fußballsaison schauen wollen.',
                    'Wenn Sie nicht jeden Monat verlängern möchten.',
                ]),
                ('p', 'Wer unsicher ist, startet mit einem Monat und wechselt später. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zum Jahresabo',
        'faq': [
            ('Was kostet IPTV für 12 Monate?', 'Bei MOJO4K.DE 49 € für 12 Monate und 1 Gerät, umgerechnet rund 4,08 € im Monat.'),
            ('Ist 4K im Jahresabo enthalten?', 'Ja, 4K ist in allen Paketen enthalten, unabhängig von der Laufzeit.'),
        ],
    },
    'iptv-stick': {
        'sections': [
            ('Worauf es beim IPTV Stick ankommt', [
                ('table', ['Merkmal', 'Empfehlung', 'Warum'], [
                    ['Auflösung', '4K mit HEVC/H.265', 'nötig für 4K-Sender'],
                    ['Arbeitsspeicher', 'mindestens 2 GB', 'große Senderlisten laden schneller'],
                    ['WLAN', 'WLAN 6 oder 5 GHz', 'stabiler als 2,4 GHz'],
                    ['Betriebssystem', 'Fire OS oder Google TV', 'alle wichtigen IPTV-Apps verfügbar'],
                    ['LAN', 'per Adapter möglich', 'beste Stabilität beim Sport'],
                ]),
            ]),
            ('Fire TV Stick oder Google TV?', [
                ('p', 'Auf dem <a href="/iptv-firestick/">Fire TV Stick</a> werden Apps wie TiviMate über die Downloader-App installiert, die Bedienung ist einfach. Geräte mit <a href="/iptv-chromecast-google-tv/">Google TV</a> haben direkten Zugriff auf den Play Store. Für IPTV eignen sich beide; entscheidend ist ein 4K-Modell mit genügend Speicher.'),
                ('p', 'Einrichtung in wenigen Minuten: App installieren, Xtream-Daten eintragen, fertig. ' + TEST),
            ]),
        ],
        'faq_title': 'Weitere Fragen zum IPTV Stick',
        'faq': [
            ('Brauche ich einen IPTV Stick, wenn ich einen Smart TV habe?', 'Nicht unbedingt. Viele Smart TVs haben passende Apps. Ein Stick lohnt sich, wenn Ihr Fernseher älter ist oder die gewünschte App nicht anbietet.'),
            ('Kann ich einen IPTV Stick per LAN anschließen?', 'Ja, mit einem passenden Ethernet-Adapter. Das ist bei Live-Sport die stabilste Lösung.'),
        ],
    },
}
