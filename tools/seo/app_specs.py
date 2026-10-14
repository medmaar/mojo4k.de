"""Content for app_pages.py: one guide per player app (SEO audit 2026-10-13).

Facts about third-party apps are kept to what the apps' own stores and websites describe; prices, trial
lengths and supported platforms change, so the copy points readers to the developer's site for those.
MOJO4K.DE facts are the ones the site states elsewhere (prices, 24h test, up to 10 devices, support).
"""

NO_CONTENT = ('{name} ist ein Player: Die App selbst enthält keine Sender, Filme oder Serien. Sie spielt ab, was Sie ihr '
              'als Playlist geben, also einen M3U-Link oder (wenn die App es unterstützt) einen Xtream-Codes-Login '
              'Ihres IPTV-Anbieters. Wie gut das Bild ist und wie stabil Sender laufen, hängt deshalb vom Anbieter und '
              'von Ihrer Internetleitung ab, nicht von der App.')

MAC_STEPS = [
    'App auf dem Fernseher oder der Box installieren und einmal öffnen. Auf dem Startbildschirm zeigt sie die '
    '<strong>MAC-Adresse</strong> (bei manchen Apps zusätzlich einen Device Key).',
    'Die Website des App-Entwicklers am Handy oder PC öffnen und den Bereich zum Hochladen der Playlist wählen.',
    'MAC-Adresse (und ggf. Device Key) eintragen, dann den M3U-Link oder die Xtream-Zugangsdaten Ihres Anbieters einfügen.',
    'Speichern, die App am Fernseher neu starten: Die Senderliste wird geladen.',
    'Nach der Testphase der App bei Bedarf die Lizenz auf der Entwickler-Website kaufen. Diese Lizenz bezahlt nur die '
    'App, nicht das IPTV-Abo.',
]

LOGIN_STEPS = [
    'App aus dem offiziellen Store Ihres Geräts installieren.',
    'Neue Playlist bzw. neues Profil anlegen und <strong>Xtream Codes</strong> wählen.',
    'Server-URL, Benutzername und Passwort aus der Bestätigung Ihres Anbieters eintragen.',
    'Speichern: Die App lädt Live-TV, Filme, Serien und den EPG.',
    'Alternativ den M3U-Link als Playlist-URL einfügen, falls die App kein Xtream-Login anbietet.',
]


def no_content(name):
    return ('note', NO_CONTENT.format(name=name))


def mojo_fit(name, how):
    return [
        ('p', f'MOJO4K.DE ist kein App-Entwickler, sondern liefert den IPTV-Zugang, den Sie in {name} laden. {how}'),
        ('ul', [
            'Zugang als Xtream-Codes-Login und als M3U-Link, beides in der Bestätigung',
            '24 Stunden kostenlos testen über <a href="/kostenlos-testen">das Testformular</a>',
            'Pakete: 9 € für 1 Monat, 29 € für 3 Monate, 39 € für 6 Monate, 49 € für 12 Monate (1 Gerät)',
            'Bis zu 10 Geräte gleichzeitig mit einem Mehrgeräte-Paket, siehe <a href="/preise/">Preise</a>',
            'Hilfe bei der Einrichtung per WhatsApp und an info@mojo4k.de',
        ]),
    ]


APPS = {
    'flix-iptv': {
        'name': 'Flix IPTV',
        'title': 'Flix IPTV 2026 – App einrichten, MAC aktivieren | MOJO4K.DE',
        'desc': 'Flix IPTV (FlixIPTV) ist ein Player für Smart TVs und Android: so aktivieren Sie die MAC-Adresse, laden Ihre M3U-Playlist hoch und lösen typische Fehler.',
        'badge': 'App-Anleitung 2026',
        'h1': 'Flix IPTV einrichten: FlixIPTV App auf Smart TV, Fire TV und Android',
        'intro': 'Flix IPTV ist eine Player-App, kein Senderpaket. Hier steht, auf welchen Geräten sie läuft, wie Sie die MAC-Adresse aktivieren und eine Playlist hochladen, und woher Sie den IPTV-Zugang bekommen, den die App abspielt.',
        'sections': [
            ('Was ist Flix IPTV?', [
                ('p', 'Flix IPTV (auch FlixIPTV oder „Flix IP TV“ geschrieben) ist ein IPTV-Player, der vor allem auf Smart TVs mit Tizen (Samsung) und webOS (LG) beliebt ist und auch für Android TV und Fire TV angeboten wird. Die Oberfläche ist an Streaming-Dienste angelehnt: Live-TV, Filme und Serien liegen in getrennten Bereichen, dazu kommen Favoriten, ein EPG und verschiedene Designs.'),
                no_content('Flix IPTV'),
                ('p', 'Wie die meisten Smart-TV-Player wird Flix IPTV über die MAC-Adresse des Geräts freigeschaltet. Nach einer Testphase verlangt der Entwickler eine einmalige Lizenzgebühr pro Gerät; den aktuellen Preis und die Testdauer nennt die Website des Entwicklers.'),
            ]),
            ('Auf welchen Geräten läuft Flix IPTV?', [
                ('table', ['Gerät', 'Bezugsquelle', 'Hinweis'], [
                    ['Samsung Smart TV (Tizen)', 'Samsung App-Store', 'Modelle ab etwa 2017'],
                    ['LG Smart TV (webOS)', 'LG Content Store', 'Modelle mit webOS 3 oder neuer'],
                    ['Android TV / Google TV', 'Google Play oder APK des Entwicklers', 'je nach Region'],
                    ['Amazon Fire TV Stick', 'per Downloader-App', 'siehe <a href="/iptv-firestick/">Fire TV Anleitung</a>'],
                ]),
                ('p', 'Welche Modelle genau unterstützt werden, ändert sich mit jedem App-Update. Prüfen Sie im Store Ihres Fernsehers, ob die App angezeigt wird. Wenn nicht, ist ein <a href="/iptv-stick/">IPTV-Stick</a> meist die einfachere Lösung.'),
            ]),
            ('Flix IPTV einrichten in 5 Schritten', [
                ('ol', MAC_STEPS),
                ('p', 'Wenn der Upload nicht klappt, liegt es fast immer an einem Tippfehler in der MAC-Adresse (0 und O, 1 und l) oder an einem abgelaufenen Test des Anbieters. Eine ausführliche Fehlerliste finden Sie unter <a href="/iptv-einrichten/">IPTV einrichten</a>.'),
            ]),
            ('Flix IPTV mit MOJO4K.DE nutzen', mojo_fit('Flix IPTV', 'Für Flix IPTV laden Sie den M3U-Link aus Ihrer Bestätigung auf der Website des Entwicklers hoch; der EPG wird dabei mitgeliefert.')),
        ],
        'faq': [
            ('Ist Flix IPTV kostenlos?', 'Die App lässt sich zunächst kostenlos testen. Danach verlangt der Entwickler eine einmalige Lizenzgebühr pro Gerät. Die Sender selbst kommen von Ihrem IPTV-Anbieter und kosten extra.'),
            ('Wo finde ich die MAC-Adresse in Flix IPTV?', 'Sie steht auf dem Startbildschirm der App und im Menü unter Einstellungen bzw. Benutzerkonto.'),
            ('Warum zeigt Flix IPTV keine Sender?', 'Meist wurde noch keine Playlist hochgeladen, die MAC-Adresse wurde falsch eingetragen oder der Zugang des Anbieters ist abgelaufen. Starten Sie die App nach dem Upload neu.'),
            ('Funktioniert Flix IPTV auf dem Fire TV Stick?', 'Ja, die App lässt sich über die Downloader-App installieren. Auf dem Fire TV sind aber TiviMate oder IPTV Smarters Pro oft einfacher, weil sie direkt mit dem Xtream-Login arbeiten.'),
        ],
    },
    'hot-iptv': {
        'name': 'Hot IPTV',
        'title': 'Hot IPTV App 2026 – Einrichten auf Samsung & LG | MOJO4K.DE',
        'desc': 'Hot IPTV ist ein Player für Smart TVs und Android. So aktivieren Sie die App per MAC-Adresse, laden eine M3U-Playlist hoch und finden den passenden IPTV-Zugang.',
        'badge': 'App-Anleitung 2026',
        'h1': 'Hot IPTV App: Einrichtung auf Samsung, LG und Android',
        'intro': 'Hot IPTV ist eine Player-App für Smart TVs und Android-Geräte. Diese Anleitung zeigt, wie Sie sie per MAC-Adresse freischalten, Ihre Playlist hochladen und was Sie tun, wenn keine Sender erscheinen.',
        'sections': [
            ('Was ist Hot IPTV?', [
                ('p', 'Hot IPTV (oft auch „Hot Player“ genannt) ist ein Player für Samsung- und LG-Fernseher sowie Android-Geräte. Er gehört zur Gruppe der Smart-TV-Apps, die über die MAC-Adresse des Geräts aktiviert werden. Die Playlist laden Sie nicht am Fernseher, sondern bequem auf der Website des Entwicklers hoch.'),
                no_content('Hot IPTV'),
                ('p', 'Typisch für diese Apps: eine kostenlose Testphase, danach eine kleine einmalige Gebühr oder ein Jahrespreis pro Gerät. Die aktuellen Konditionen stehen auf der Website des Entwicklers; sie sind unabhängig vom Preis Ihres IPTV-Abos.'),
            ]),
            ('Hot IPTV oder andere Smart-TV-Player?', [
                ('table', ['App', 'Aktivierung', 'Playlist laden'], [
                    ['Hot IPTV', 'MAC-Adresse', 'Website des Entwicklers'],
                    ['<a href="/set-iptv/">Set IPTV</a>', 'MAC-Adresse', 'Website des Entwicklers'],
                    ['<a href="/smartone-iptv/">SmartOne IPTV</a>', 'MAC-Adresse', 'Website des Entwicklers'],
                    ['<a href="/ibo-player/">IBO Player</a>', 'MAC + Device Key', 'Website des Entwicklers'],
                    ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'keine', 'Xtream-Login direkt in der App'],
                ]),
                ('p', 'Ob eine App auf Ihrem Fernseher im Store erscheint, hängt von Modell und Region ab. Wer beim Fernseher keine passende App findet, nutzt einen Fire TV Stick oder eine Android Box: Dort laufen alle gängigen Player.'),
            ]),
            ('Hot IPTV einrichten', [
                ('ol', MAC_STEPS),
                ('h3', 'Keine Sender nach dem Upload?'),
                ('ul', [
                    'App vollständig schließen und neu starten, bei Samsung auch den Fernseher kurz vom Strom trennen',
                    'MAC-Adresse Zeichen für Zeichen vergleichen',
                    'Den M3U-Link einmal im Browser öffnen: lädt eine Datei, ist der Zugang aktiv',
                    'Bei Fehlern im EPG hilft <a href="/iptv-epg-probleme/">EPG-Probleme lösen</a>',
                ]),
            ]),
            ('Hot IPTV mit MOJO4K.DE nutzen', mojo_fit('Hot IPTV', 'Für Hot IPTV verwenden Sie den M3U-Link aus Ihrer Bestätigung und laden ihn auf der Website des Entwicklers für Ihre MAC-Adresse hoch.')),
        ],
        'faq': [
            ('Ist Hot IPTV ein IPTV-Anbieter?', 'Nein. Hot IPTV ist ein Player. Sender, Filme und Serien kommen von dem IPTV-Anbieter, dessen Playlist Sie in die App laden.'),
            ('Kostet Hot IPTV etwas?', 'Nach der Testphase verlangt der Entwickler eine Gebühr pro Gerät. Die aktuellen Preise stehen auf seiner Website.'),
            ('Wie lade ich eine Playlist in Hot IPTV?', 'Auf der Website des Entwicklers die MAC-Adresse aus der App eintragen, den M3U-Link einfügen und speichern. Danach die App neu starten.'),
            ('Gibt es Hot IPTV für den Fire TV Stick?', 'Android-Versionen lassen sich meist per Downloader installieren. Bequemer sind auf dem Fire TV Apps mit Xtream-Login wie TiviMate oder IPTV Smarters Pro.'),
        ],
    },
    'set-iptv': {
        'name': 'Set IPTV',
        'title': 'Set IPTV 2026 – App einrichten & Playlist hochladen | MOJO4K.DE',
        'desc': 'Set IPTV (Set IP TV) für Samsung, LG und Android: MAC-Adresse finden, M3U-Playlist auf der Website hochladen, Fehler beheben. Anleitung Schritt für Schritt.',
        'badge': 'App-Anleitung 2026',
        'h1': 'Set IPTV einrichten: Set IP TV App auf Samsung, LG und Android',
        'intro': 'Set IPTV ist eine der bekanntesten Smart-TV-Apps für IPTV. Sie lädt Ihre Playlist über die MAC-Adresse des Fernsehers. Hier lesen Sie, wie das geht und was Sie dafür brauchen.',
        'sections': [
            ('Was ist Set IPTV?', [
                ('p', 'Set IPTV (auch „Set IP TV“ oder „SetIPTV“) ist ein IPTV-Player für Samsung- und LG-Fernseher, der außerdem für Android und einige Set-Top-Boxen erhältlich ist. Die App zeigt beim Start die MAC-Adresse des Geräts an. Über diese Adresse ordnen Sie auf der Website des Entwicklers Ihre Playlist dem Fernseher zu.'),
                no_content('Set IPTV'),
                ('p', 'Set IPTV unterstützt M3U-Playlists mit EPG und bietet Kategorien, Favoriten und eine Kindersicherung. Nach einer Testphase wird eine Aktivierungsgebühr pro Gerät fällig, die direkt an den Entwickler geht.'),
            ]),
            ('Was Sie für Set IPTV brauchen', [
                ('cards', [
                    ('Ein unterstütztes Gerät', 'Samsung Smart TV (Tizen), LG Smart TV (webOS) oder ein Android-Gerät. Ältere Fernseher finden die App teils nicht im Store.'),
                    ('Die MAC-Adresse', 'Steht auf dem Startbildschirm der App. Notieren Sie sie genau, Groß- und Kleinschreibung spielt keine Rolle.'),
                    ('Einen IPTV-Zugang', 'Einen M3U-Link Ihres Anbieters. Ohne ihn zeigt die App nur einen leeren Bildschirm.'),
                    ('Handy oder PC', 'Zum Hochladen der Playlist auf der Website des Entwicklers.'),
                ]),
            ]),
            ('Set IPTV einrichten: Schritt für Schritt', [
                ('ol', MAC_STEPS),
                ('p', 'Ändert sich später Ihr Zugang, laden Sie den neuen Link auf derselben Seite hoch und überschreiben den alten. Ausführlich mit Bildern: <a href="/iptv-samsung-tv-deutschland/">IPTV auf Samsung TV</a> und <a href="/iptv-lg-tv-deutschland/">IPTV auf LG TV</a>.'),
            ]),
            ('Set IPTV mit MOJO4K.DE nutzen', mojo_fit('Set IPTV', 'Für Set IPTV nehmen Sie den M3U-Link aus Ihrer Bestätigung. Wenn Sie lieber direkt am Fernseher mit Benutzername und Passwort arbeiten, ist <a href="/iptv-smarters-pro-samsung-tv/">IPTV Smarters Pro auf Samsung</a> eine Alternative.')),
        ],
        'faq': [
            ('Ist Set IPTV kostenlos?', 'Set IPTV kann zunächst kostenlos getestet werden, danach ist eine Aktivierungsgebühr pro Gerät fällig. Das IPTV-Abo bezahlen Sie getrennt beim Anbieter.'),
            ('Wo lade ich die Playlist für Set IPTV hoch?', 'Auf der Website des Set-IPTV-Entwicklers. Dort tragen Sie die MAC-Adresse aus der App ein und fügen den M3U-Link Ihres Anbieters ein.'),
            ('Set IPTV zeigt „Playlist not found“, was tun?', 'Prüfen Sie die MAC-Adresse, laden Sie die Playlist erneut hoch und starten Sie den Fernseher neu. Öffnen Sie den M3U-Link testweise im Browser, um zu sehen, ob der Zugang aktiv ist.'),
            ('Was ist der Unterschied zwischen Set IPTV und Smart IPTV?', 'Beide werden per MAC-Adresse aktiviert und bekommen die Playlist über eine Website. Sie unterscheiden sich in Oberfläche, Preis und unterstützten Geräten; die Sender kommen in beiden Fällen vom IPTV-Anbieter.'),
        ],
    },
    'smartone-iptv': {
        'name': 'SmartOne IPTV',
        'title': 'SmartOne IPTV 2026 – App einrichten auf Samsung & LG | MOJO4K.DE',
        'desc': 'SmartOne IPTV (Smart One IPTV) für Samsung, LG und Android: MAC-Adresse, Playlist-Upload und typische Fehler, Schritt für Schritt erklärt.',
        'badge': 'App-Anleitung 2026',
        'h1': 'SmartOne IPTV einrichten: Smart One App auf Samsung, LG und Android',
        'intro': 'SmartOne IPTV ist ein Player für Smart TVs, der Ihre Playlist über die MAC-Adresse lädt. Diese Seite erklärt die Einrichtung und woher die Sender kommen, die die App abspielt.',
        'sections': [
            ('Was ist SmartOne IPTV?', [
                ('p', 'SmartOne IPTV (auch „Smart One IPTV“ oder „SmartOneIPTV“) ist eine IPTV-App für Samsung- und LG-Fernseher sowie Android-Geräte. Sie gehört zu den Playern, die die Playlist nicht in der App selbst, sondern über eine Website des Entwicklers bekommen: Sie tragen dort die MAC-Adresse des Fernsehers ein und hinterlegen Ihren M3U-Link.'),
                no_content('SmartOne IPTV'),
                ('p', 'Die App bietet getrennte Bereiche für Live-TV, Filme und Serien, einen EPG und Favoritenlisten. Nach einer Testphase wird eine Lizenz pro Gerät fällig; Preis und Laufzeit nennt der Entwickler auf seiner Website.'),
            ]),
            ('SmartOne IPTV einrichten', [
                ('ol', MAC_STEPS),
                ('h3', 'Tipps für einen stabilen Empfang'),
                ('ul', [
                    'Fernseher wenn möglich per LAN-Kabel anschließen, WLAN schwankt stärker',
                    'Für 4K-Sender mindestens 50 Mbit/s einplanen, mehr dazu unter <a href="/iptv-4k/">IPTV 4K</a>',
                    'Ruckelt es, helfen die Tipps unter <a href="/iptv-ruckelt/">IPTV ruckelt</a>',
                ]),
            ]),
            ('SmartOne IPTV im Vergleich mit anderen Playern', [
                ('table', ['App', 'Geräte', 'Login-Art'], [
                    ['SmartOne IPTV', 'Samsung, LG, Android', 'MAC-Adresse + Website'],
                    ['<a href="/siptv/">Smart IPTV (SIPTV)</a>', 'Samsung, LG, Android', 'MAC-Adresse + Website'],
                    ['<a href="/duplecast-iptv/">Duplecast</a>', 'Samsung, LG, Android, Fire TV', 'Device ID + Website'],
                    ['<a href="/tivimate/">TiviMate</a>', 'Android TV, Fire TV', 'Xtream-Login in der App'],
                ]),
            ]),
            ('SmartOne IPTV mit MOJO4K.DE nutzen', mojo_fit('SmartOne IPTV', 'Für SmartOne IPTV laden Sie den M3U-Link aus Ihrer Bestätigung auf der Website des Entwicklers hoch.')),
        ],
        'faq': [
            ('Ist SmartOne IPTV ein Anbieter?', 'Nein, SmartOne IPTV ist eine Player-App. Die Sender liefert Ihr IPTV-Anbieter über eine Playlist.'),
            ('Wie aktiviere ich SmartOne IPTV?', 'Die App zeigt beim Start die MAC-Adresse. Diese tragen Sie auf der Website des Entwicklers ein, laden den M3U-Link hoch und kaufen nach der Testphase bei Bedarf die Lizenz.'),
            ('Läuft SmartOne IPTV auf jedem Samsung-Fernseher?', 'Nicht auf jedem. Ob die App im Store erscheint, hängt vom Modelljahr und der Region ab. Ältere Modelle nutzen besser einen Fire TV Stick.'),
            ('Kann ich SmartOne IPTV mit mehreren Fernsehern nutzen?', 'Jeder Fernseher hat eine eigene MAC-Adresse und braucht eine eigene App-Lizenz. Beim IPTV-Abo brauchen Sie ein Paket für die passende Anzahl gleichzeitiger Geräte.'),
        ],
    },
    'duplecast-iptv': {
        'name': 'Duplecast',
        'title': 'Duplecast IPTV 2026 – Player einrichten | MOJO4K.DE',
        'desc': 'Duplecast IPTV für Samsung, LG, Android und Fire TV: Device ID finden, Playlist auf der Website hinzufügen, Fehler beheben. Anleitung mit passendem IPTV-Zugang.',
        'badge': 'App-Anleitung 2026',
        'h1': 'Duplecast IPTV einrichten: Player für Smart TV, Android und Fire TV',
        'intro': 'Duplecast ist ein IPTV-Player, der Playlists über eine Website auf Ihr Gerät bringt. Hier erfahren Sie, wie die Einrichtung abläuft und was die App leistet.',
        'sections': [
            ('Was ist Duplecast?', [
                ('p', 'Duplecast ist eine Player-App für Samsung- und LG-Fernseher, Android-Geräte und den Fire TV Stick. Beim ersten Start zeigt sie eine Geräte-ID (Device ID) und einen Schlüssel. Mit diesen Daten fügen Sie auf der Website von Duplecast Ihre Playlist hinzu, die App lädt sie anschließend automatisch.'),
                no_content('Duplecast'),
                ('p', 'Duplecast unterstützt M3U-Playlists und Xtream-Zugänge, einen EPG und mehrere Playlists pro Gerät. Nach der Testphase verlangt der Entwickler eine Gebühr; die aktuellen Konditionen stehen auf der Website.'),
            ]),
            ('Duplecast einrichten', [
                ('ol', [
                    'Duplecast im App-Store des Fernsehers oder auf dem Android-Gerät installieren.',
                    'App öffnen und Device ID sowie Device Key notieren.',
                    'Auf der Website von Duplecast den Bereich zum Verwalten der Playlist öffnen und die Geräte-Daten eintragen.',
                    'Playlist hinzufügen: M3U-Link oder Xtream-Server, Benutzername und Passwort.',
                    'App neu starten: Live-TV, Filme und Serien erscheinen.',
                ]),
                ('p', 'Wer mehrere Anbieter oder Profile nutzt, kann mehrere Playlists anlegen und in der App zwischen ihnen wechseln.'),
            ]),
            ('Für wen eignet sich Duplecast?', [
                ('cards', [
                    ('Mehrere Geräte im Haushalt', 'Dieselbe App auf Fernseher und Fire TV, verwaltet über eine Website.'),
                    ('Xtream oder M3U', 'Beide Login-Arten werden unterstützt, der EPG kommt mit.'),
                    ('Kein Tippen am Fernseher', 'Zugangsdaten werden bequem am Handy eingegeben.'),
                ]),
                ('p', 'Wer lieber alles direkt in der App eingibt, findet unter <a href="/iptv-apps/">IPTV Apps</a> Player mit eigenem Login-Bildschirm.'),
            ]),
            ('Duplecast mit MOJO4K.DE nutzen', mojo_fit('Duplecast', 'Für Duplecast tragen Sie auf der Website entweder den M3U-Link oder die Xtream-Daten aus Ihrer Bestätigung ein.')),
        ],
        'faq': [
            ('Ist Duplecast kostenlos?', 'Duplecast lässt sich zunächst testen; danach verlangt der Entwickler eine Gebühr. Das IPTV-Abo ist davon unabhängig.'),
            ('Wo finde ich die Device ID in Duplecast?', 'Die App zeigt Device ID und Key auf dem Startbildschirm bzw. in den Einstellungen.'),
            ('Unterstützt Duplecast Xtream Codes?', 'Ja, neben M3U-Links lassen sich Xtream-Zugänge mit Server, Benutzername und Passwort hinterlegen.'),
            ('Duplecast lädt die Playlist nicht, was tun?', 'Device ID und Key prüfen, die Playlist auf der Website erneut speichern und die App neu starten. Ist der Zugang abgelaufen, lädt keine App Sender.'),
        ],
    },
    'implayer': {
        'name': 'iMPlayer',
        'title': 'iMPlayer 2026 – IPTV Player einrichten | MOJO4K.DE',
        'desc': 'iMPlayer ist ein moderner IPTV-Player für Android, Fire TV, Apple TV und Smart TVs. So richten Sie ihn mit Xtream-Login oder M3U ein und was er kann.',
        'badge': 'App-Anleitung 2026',
        'h1': 'iMPlayer einrichten: IPTV Player für Fire TV, Android, Apple und Smart TV',
        'intro': 'iMPlayer ist ein IPTV-Player mit moderner Oberfläche, der auf vielen Plattformen läuft. Hier steht, wie Sie ihn mit Ihrem IPTV-Zugang verbinden und welche Funktionen er bietet.',
        'sections': [
            ('Was ist iMPlayer?', [
                ('p', 'iMPlayer ist eine Player-App, die für Android-Geräte, Fire TV, Apple-Geräte und mehrere Smart-TV-Plattformen angeboten wird. Sie ist für eine aufgeräumte Oberfläche mit Postern für Filme und Serien bekannt und kann Xtream-Zugänge und M3U-Playlists laden.'),
                no_content('iMPlayer'),
                ('p', 'Zu den Funktionen gehören je nach Plattform ein EPG, Catch-up, Favoriten, Kindersicherung und die gleichzeitige Anzeige mehrerer Sender. Ein Teil der Funktionen ist an eine kostenpflichtige Premium-Version gebunden; Details nennt der Entwickler.'),
            ]),
            ('iMPlayer einrichten', [
                ('ol', LOGIN_STEPS),
                ('p', 'Auf Smart TVs mit MAC-Aktivierung kann die Einrichtung stattdessen über die Website des Entwicklers laufen. Die Schritte stehen in der App.'),
            ]),
            ('iMPlayer, TiviMate oder Smarters?', [
                ('table', ['App', 'Stärke', 'Plattformen'], [
                    ['iMPlayer', 'moderne Oberfläche, viele Plattformen', 'Android, Fire TV, Apple, Smart TV'],
                    ['<a href="/tivimate/">TiviMate</a>', 'bester EPG auf Android TV', 'Android TV, Fire TV'],
                    ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'einfacher Einstieg', 'fast alle Geräte'],
                    ['<a href="/ott-navigator/">OTT Navigator</a>', 'viele Einstellungen', 'Android, Fire TV'],
                ]),
                ('p', 'Alle vier Apps spielen dieselben Sender ab, wenn Sie denselben Zugang laden. Die Wahl ist eine Frage der Bedienung. Mehr Auswahl unter <a href="/bester-iptv-player/">Bester IPTV Player</a>.'),
            ]),
            ('Wenn iMPlayer nicht lädt', [
                ('ul', [
                    '<strong>Anmeldung schlägt fehl:</strong> Server-URL mit <code>http://</code> und Port genau so übernehmen, wie sie in der Bestätigung steht.',
                    '<strong>Sender laden, Filme nicht:</strong> In den Einstellungen die Inhalte neu laden; große Bibliotheken brauchen beim ersten Mal etwas Zeit.',
                    '<strong>Kein Programmguide:</strong> EPG in der App aktualisieren, bei M3U die EPG-URL ergänzen.',
                    '<strong>Bild ruckelt:</strong> Zwischen Hardware- und Software-Decoder wechseln und die Tipps unter <a href="/iptv-buffer/">IPTV Buffering</a> prüfen.',
                ]),
            ]),
            ('iMPlayer mit MOJO4K.DE nutzen', mojo_fit('iMPlayer', 'In iMPlayer wählen Sie Xtream Codes und tragen Server, Benutzername und Passwort aus Ihrer Bestätigung ein.')),
        ],
        'faq': [
            ('Ist iMPlayer ein IPTV-Anbieter?', 'Nein, iMPlayer ist ein Player. Er braucht einen Zugang eines IPTV-Anbieters, um Sender abzuspielen.'),
            ('Unterstützt iMPlayer Xtream Codes?', 'Ja, iMPlayer lädt Xtream-Zugänge mit Server, Benutzername und Passwort sowie M3U-Playlists.'),
            ('Gibt es iMPlayer für den Fire TV Stick?', 'Ja, iMPlayer läuft auf Fire TV und Android TV.'),
            ('Ist iMPlayer kostenlos?', 'Die Grundfunktionen lassen sich nutzen bzw. testen, für den vollen Funktionsumfang bietet der Entwickler eine kostenpflichtige Version an.'),
        ],
    },
    'iptvx': {
        'name': 'IPTVX',
        'title': 'IPTVX App 2026 – Player für Apple TV & iPhone | MOJO4K.DE',
        'desc': 'IPTVX ist ein IPTV-Player für Apple TV, iPhone, iPad und Mac. So laden Sie Ihren Xtream-Zugang oder M3U-Link und nutzen EPG, Filme und Serien.',
        'badge': 'App-Anleitung 2026',
        'h1': 'IPTVX einrichten: IPTV Player für Apple TV, iPhone, iPad und Mac',
        'intro': 'IPTVX ist eine Player-App aus dem Apple-Umfeld. Hier lesen Sie, wie Sie Ihren IPTV-Zugang hinzufügen, welche Geräte unterstützt werden und wie IPTVX sich von anderen Playern unterscheidet.',
        'sections': [
            ('Was ist IPTVX?', [
                ('p', 'IPTVX ist ein IPTV-Player, der im App Store für Apple TV, iPhone, iPad und Mac angeboten wird. Die App ist an die Bedienung von tvOS angepasst und lädt Xtream-Zugänge und M3U-Playlists inklusive EPG.'),
                no_content('IPTVX'),
                ('p', 'Die App kann kostenlos geladen werden; einige Funktionen oder die Nutzung über eine Testphase hinaus setzen einen In-App-Kauf voraus. Aktuelle Preise stehen im App Store.'),
            ]),
            ('IPTVX einrichten', [
                ('ol', LOGIN_STEPS),
                ('p', 'Auf dem Apple TV tippen Sie die Daten mit der Fernbedienung oder über die Tastatur Ihres iPhones ein. Eine allgemeine Anleitung für Apple-Geräte finden Sie unter <a href="/iptv-apple-tv/">IPTV auf Apple TV</a> und <a href="/iptv-iphone/">IPTV auf dem iPhone</a>.'),
            ]),
            ('IPTVX oder andere Apps für Apple-Geräte?', [
                ('table', ['App', 'Apple TV', 'iPhone / iPad', 'Mac'], [
                    ['IPTVX', 'ja', 'ja', 'ja'],
                    ['<a href="/gse-iptv/">GSE Smart IPTV</a>', 'ja', 'ja', 'teilweise'],
                    ['<a href="/iptv-smarters-pro-apple-tv/">IPTV Smarters Pro</a>', 'ja', 'ja', 'über iPad-Version'],
                    ['<a href="/iptv-vlc/">VLC</a>', 'ja', 'ja', 'ja (nur M3U)'],
                ]),
            ]),
            ('IPTVX mit MOJO4K.DE nutzen', mojo_fit('IPTVX', 'In IPTVX wählen Sie Xtream Codes und tragen Server, Benutzername und Passwort aus Ihrer Bestätigung ein.')),
        ],
        'faq': [
            ('Ist IPTVX ein IPTV-Anbieter?', 'Nein, IPTVX ist ein Player für Apple-Geräte. Die Sender kommen von Ihrem IPTV-Anbieter.'),
            ('Gibt es IPTVX für Android?', 'IPTVX ist vor allem für Apple-Geräte gedacht. Auf Android und Fire TV sind TiviMate oder IPTV Smarters Pro die üblichen Alternativen.'),
            ('Unterstützt IPTVX einen EPG?', 'Ja, bei Xtream-Zugängen wird der EPG automatisch geladen, bei M3U-Playlists über eine EPG-URL.'),
            ('Was kostet IPTVX?', 'Die App ist im App Store erhältlich; für den vollen Funktionsumfang gibt es In-App-Käufe. Das IPTV-Abo bezahlen Sie getrennt.'),
        ],
    },
    'gse-iptv': {
        'name': 'GSE Smart IPTV',
        'title': 'GSE Smart IPTV 2026 – Einrichten auf iPhone & Co. | MOJO4K.DE',
        'desc': 'GSE Smart IPTV (GSEIPTV) einrichten: Xtream-Login oder M3U-Playlist hinzufügen, EPG laden, Tipps für iPhone, Apple TV und Android. Mit passendem IPTV-Zugang.',
        'badge': 'App-Anleitung 2026',
        'h1': 'GSE Smart IPTV einrichten: Anleitung für iPhone, Apple TV und Android',
        'intro': 'GSE Smart IPTV ist einer der ältesten IPTV-Player für iOS und Android. Diese Anleitung zeigt, wie Sie Ihren Zugang hinzufügen und den EPG einrichten.',
        'sections': [
            ('Was ist GSE Smart IPTV?', [
                ('p', 'GSE Smart IPTV ist ein Player für iPhone, iPad, Apple TV und Android. Er unterstützt M3U-Playlists, Xtream-Codes-Zugänge und EPG-Daten im XMLTV-Format und bietet eine Kindersicherung, Favoriten und die Wiedergabe vieler Stream-Formate.'),
                no_content('GSE Smart IPTV'),
                ('p', 'Die App ist im App Store und bei Google Play erhältlich. Einige Funktionen oder werbefreie Nutzung sind an einen In-App-Kauf gebunden.'),
            ]),
            ('GSE Smart IPTV einrichten', [
                ('h3', 'Mit Xtream Codes'),
                ('ol', [
                    'App öffnen, Menü aufrufen und „Xtream Codes API“ wählen.',
                    'Mit „+“ einen neuen Eintrag anlegen.',
                    'Namen vergeben, Server-URL, Benutzername und Passwort eintragen.',
                    'Speichern und den Eintrag antippen: Kategorien und Sender werden geladen.',
                ]),
                ('h3', 'Mit M3U-Link'),
                ('ol', [
                    'Im Menü „Remote Playlists“ wählen.',
                    'Mit „+“ „Add M3U URL“ wählen, Namen vergeben und den Link einfügen.',
                    'Für den Programmguide unter „EPG Sources“ die EPG-URL Ihres Anbieters hinzufügen.',
                ]),
            ]),
            ('Typische Probleme mit GSE Smart IPTV', [
                ('ul', [
                    '<strong>Kein EPG:</strong> Bei M3U muss die EPG-Quelle separat hinterlegt werden, bei Xtream kommt sie automatisch. Mehr unter <a href="/iptv-epg/">IPTV EPG</a>.',
                    '<strong>Sender starten nicht:</strong> Im Player-Menü einen anderen Player (z. B. den Hardware-Decoder) wählen.',
                    '<strong>Ruckeln:</strong> WLAN prüfen und die Tipps unter <a href="/iptv-ruckelt/">IPTV ruckelt</a> durchgehen.',
                ]),
            ]),
            ('GSE Smart IPTV mit MOJO4K.DE nutzen', mojo_fit('GSE Smart IPTV', 'In GSE wählen Sie „Xtream Codes API“ und tragen die Daten aus Ihrer Bestätigung ein; der EPG wird dann automatisch geladen.')),
        ],
        'faq': [
            ('Ist GSE Smart IPTV kostenlos?', 'Die App kann kostenlos geladen werden, einige Funktionen kosten per In-App-Kauf. Sender bekommen Sie nur über einen IPTV-Anbieter.'),
            ('Funktioniert GSE Smart IPTV auf dem Apple TV?', 'Ja, GSE gibt es für tvOS. Viele Nutzer richten die Playlist auf dem iPhone ein und nutzen dieselbe App auf dem Apple TV.'),
            ('Wie füge ich einen EPG in GSE hinzu?', 'Bei Xtream-Zugängen wird der EPG automatisch geladen. Bei M3U-Playlists fügen Sie unter „EPG Sources“ die EPG-URL Ihres Anbieters hinzu.'),
            ('Was bedeutet GSEIPTV?', 'GSEIPTV ist eine verbreitete Schreibweise für GSE Smart IPTV, die Player-App des Entwicklers GSE.'),
        ],
    },
    'iptvpro': {
        'name': 'IPTV Pro',
        'title': 'IPTV Pro App 2026 – Android Player einrichten | MOJO4K.DE',
        'desc': 'IPTV Pro (IPTVPro) ist ein Player für Android: so fügen Sie eine M3U-Playlist hinzu, laden den EPG und wählen den richtigen Player. Mit passendem IPTV-Zugang.',
        'badge': 'App-Anleitung 2026',
        'h1': 'IPTV Pro einrichten: der Android-Player für M3U-Playlists',
        'intro': 'IPTV Pro ist die Bezahlversion eines bekannten Android-Players für M3U-Playlists. Hier steht, wie Sie ihn einrichten und für wen er sich eignet.',
        'sections': [
            ('Was ist IPTV Pro?', [
                ('p', 'IPTV Pro (oft „IPTVPro“ geschrieben) ist ein Player für Android-Smartphones, Tablets und Android TV. Er ist die werbefreie Kaufversion der kostenlosen App „IPTV“ im Google Play Store und spielt M3U- und XSPF-Playlists ab, mit EPG, Favoriten und einer Auswahl zwischen internem und externem Player.'),
                no_content('IPTV Pro'),
                ('p', 'Die App ist bewusst schlicht: eine Senderliste, ein Programmguide, wenige Menüs. Filme und Serien aus einem Xtream-Zugang zeigt sie nicht so übersichtlich wie spezialisierte Apps.'),
            ]),
            ('IPTV Pro einrichten', [
                ('ol', [
                    'IPTV Pro im Google Play Store kaufen und installieren.',
                    'App öffnen und „Playlist hinzufügen“ bzw. „URL hinzufügen“ wählen.',
                    'Den M3U-Link Ihres Anbieters einfügen und einen Namen vergeben.',
                    'In den Einstellungen die EPG-Quelle (TV-Programm) eintragen, falls sie nicht in der Playlist steckt.',
                    'Unter „Player“ zwischen internem Player und z. B. VLC wählen, falls ein Sender nicht startet.',
                ]),
            ]),
            ('Für wen eignet sich IPTV Pro?', [
                ('cards', [
                    ('Gut für', 'Live-TV am Android-Handy oder Tablet, schlanke Bedienung, M3U-Playlists.'),
                    ('Weniger gut für', 'Große Film- und Serienbibliotheken, Catch-up und Fernbedienungs-Bedienung am Fernseher.'),
                    ('Alternative am TV', '<a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> mit Xtream-Login.'),
                ]),
                ('p', 'Einen Überblick über Android-Player finden Sie unter <a href="/iptv-player-android/">IPTV Player Android</a>.'),
            ]),
            ('IPTV Pro mit MOJO4K.DE nutzen', mojo_fit('IPTV Pro', 'In IPTV Pro fügen Sie den M3U-Link aus Ihrer Bestätigung als Playlist-URL hinzu.')),
        ],
        'faq': [
            ('Ist IPTV Pro ein IPTV-Anbieter?', 'Nein, IPTV Pro ist ein Player für Android. Er spielt die Playlist ab, die Sie von Ihrem Anbieter bekommen.'),
            ('Was ist der Unterschied zwischen IPTV und IPTV Pro?', 'IPTV Pro ist die kostenpflichtige Version ohne Werbung und mit zusätzlichen Funktionen. Die Bedienung ist gleich.'),
            ('Unterstützt IPTV Pro Xtream Codes?', 'IPTV Pro arbeitet mit Playlist-URLs. Nutzen Sie den M3U-Link Ihres Anbieters; für Xtream-Logins eignen sich TiviMate oder Smarters besser.'),
            ('Läuft IPTV Pro auf dem Fire TV Stick?', 'Die App lässt sich auf Fire TV installieren, ist aber für Touch-Bedienung gebaut. Am Fernseher sind TV-Apps angenehmer.'),
        ],
    },
    'iptv-streamplayer': {
        'name': 'IPTV Streamplayer',
        'title': 'IPTV Streamplayer 2026 – Player-Apps einrichten | MOJO4K.DE',
        'desc': 'IPTV Streamplayer: welche Player-App passt zu Fire TV, Smart TV und Handy, wie Sie Xtream-Login oder M3U-Link eintragen und worauf es beim Abspielen ankommt.',
        'badge': 'Ratgeber 2026',
        'h1': 'IPTV Streamplayer: die richtige Player-App finden und einrichten',
        'intro': 'Ein IPTV Streamplayer ist die App, die Ihre IPTV-Sender abspielt. Hier lesen Sie, welche Player es gibt, wie Sie Ihren Zugang eintragen und welcher Player zu welchem Gerät passt.',
        'sections': [
            ('Was ist ein IPTV Streamplayer?', [
                ('p', 'Als IPTV Streamplayer bezeichnet man Apps, die IPTV-Streams abspielen: Sie laden eine Playlist, sortieren die Sender in Kategorien, zeigen den Programmguide und spielen den gewählten Stream ab. Unter dem Namen „IPTV Stream Player“ werden außerdem einzelne Apps in den Stores angeboten.'),
                no_content('Ein Streamplayer'),
            ]),
            ('Welcher Streamplayer für welches Gerät?', [
                ('table', ['Gerät', 'Empfehlung', 'Login'], [
                    ['Fire TV Stick', '<a href="/tivimate-fire-tv-stick/">TiviMate</a>, <a href="/iptv-smarters-pro-fire-tv-stick/">Smarters Pro</a>', 'Xtream'],
                    ['Android TV / Box', '<a href="/tivimate/">TiviMate</a>, <a href="/ott-navigator/">OTT Navigator</a>', 'Xtream'],
                    ['Samsung / LG TV', '<a href="/set-iptv/">Set IPTV</a>, <a href="/ibo-player/">IBO Player</a>, <a href="/iptv-smarters-pro-samsung-tv/">Smarters</a>', 'MAC oder Xtream'],
                    ['iPhone / Apple TV', '<a href="/gse-iptv/">GSE Smart IPTV</a>, <a href="/iptvx/">IPTVX</a>', 'Xtream'],
                    ['PC / Mac', '<a href="/iptv-vlc/">VLC</a>, <a href="/iptv-smarters-pro-windows/">Smarters für Windows</a>', 'M3U oder Xtream'],
                ]),
            ]),
            ('So richten Sie einen Streamplayer ein', [
                ('ol', LOGIN_STEPS),
                ('p', 'Bei Smart-TV-Apps mit MAC-Aktivierung laden Sie die Playlist stattdessen auf der Website des Entwicklers hoch. Die Unterschiede erklärt <a href="/iptv-apps/">IPTV Apps</a>.'),
            ]),
            ('Worauf es beim Abspielen ankommt', [
                ('ul', [
                    '<strong>Decoder:</strong> Hardware-Decoding schont schwache Geräte. Startet ein Sender nicht, hilft oft der Wechsel auf Software-Decoding.',
                    '<strong>Puffer:</strong> Einige Player erlauben einen größeren Puffer. Das verzögert den Start etwas, gleicht aber kurze Schwankungen aus.',
                    '<strong>Bandbreite:</strong> Wir empfehlen mindestens 25 Mbit/s für HD und 50 Mbit/s für 4K.',
                    '<strong>EPG:</strong> Bei Xtream automatisch, bei M3U über eine separate EPG-URL.',
                ]),
            ]),
            ('Streamplayer mit MOJO4K.DE nutzen', mojo_fit('jedem dieser Player', 'Sie bekommen Xtream-Daten und einen M3U-Link, damit funktionieren alle genannten Apps.')),
        ],
        'faq': [
            ('Was ist der beste IPTV Streamplayer?', 'Auf Fire TV und Android TV gilt TiviMate als besonders komfortabel, IPTV Smarters Pro läuft auf den meisten Geräten. Am Ende entscheidet die Bedienung, die Sender sind dieselben.'),
            ('Brauche ich für einen Streamplayer ein Abo?', 'Ja, der Player selbst enthält keine Sender. Sie brauchen den Zugang eines IPTV-Anbieters.'),
            ('Ist ein IPTV Streamplayer legal?', 'Player-Apps sind legal. Entscheidend ist, ob die Inhalte, die Sie abspielen, rechtmäßig angeboten werden.'),
            ('Kann ich mehrere Player gleichzeitig nutzen?', 'Ja, Sie können denselben Zugang in mehreren Apps eintragen. Wie viele Geräte gleichzeitig streamen dürfen, hängt von Ihrem Paket ab.'),
        ],
    },
    'siptv': {
        'name': 'Smart IPTV (SIPTV)',
        'title': 'SIPTV 2026 – Smart IPTV einrichten & Playlist laden | MOJO4K.DE',
        'desc': 'SIPTV (Smart IPTV) auf Samsung, LG und Android: MAC-Adresse, Playlist auf siptv.app hochladen, „My List“ verstehen und Fehler beheben. Schritt für Schritt.',
        'badge': 'App-Anleitung 2026',
        'h1': 'SIPTV einrichten: Smart IPTV App mit Playlist auf Samsung, LG und Android',
        'intro': 'SIPTV ist die Kurzform von Smart IPTV, einer der ältesten Smart-TV-Apps für IPTV. Hier steht, wie Sie die App aktivieren, Ihre Playlist auf siptv.app hochladen und was „My List“ bedeutet.',
        'sections': [
            ('Was ist SIPTV?', [
                ('p', 'Smart IPTV, kurz SIPTV, ist eine Player-App für Samsung- und LG-Fernseher sowie Android-Geräte. Die Playlist wird nicht in der App eingegeben, sondern auf der offiziellen Website siptv.app der MAC-Adresse des Fernsehers zugeordnet. Die App lädt sie beim nächsten Start.'),
                no_content('SIPTV'),
                ('p', 'Nach einer kostenlosen Testphase verlangt der Entwickler eine einmalige Aktivierungsgebühr pro Gerät, die auf siptv.app bezahlt wird.'),
            ]),
            ('SIPTV einrichten', [
                ('ol', [
                    'Smart IPTV aus dem App-Store des Fernsehers installieren und öffnen. Die MAC-Adresse steht auf dem Startbildschirm.',
                    'Am Handy oder PC siptv.app öffnen und die Seite zum Hochladen der Playlist wählen.',
                    'MAC-Adresse eintragen und den M3U-Link Ihres Anbieters als URL einfügen.',
                    'Optional eine EPG-URL hinzufügen, dann „Send“ bzw. Speichern.',
                    'Die App am Fernseher neu starten. Die Sender erscheinen in der Liste.',
                ]),
                ('p', 'Eine Anleitung mit Bildern finden Sie unter <a href="/smart-iptv-playlist-hochladen/">Smart IPTV Playlist hochladen</a>, speziell für Samsung unter <a href="/smart-iptv-samsung/">Smart IPTV auf Samsung</a>.'),
            ]),
            ('SIPTV My List, SIPTV List und typische Fehler', [
                ('p', '„My List“ ist der Name, unter dem SIPTV eine hochgeladene Playlist anzeigt, wenn Sie ihr keinen eigenen Namen geben. Wer nach „siptv my list“ oder „siptv list“ sucht, will meist wissen, warum diese Liste leer bleibt.'),
                ('ul', [
                    '<strong>Liste leer:</strong> MAC-Adresse prüfen, Playlist erneut hochladen, Fernseher neu starten.',
                    '<strong>„Playlist not found“:</strong> Der M3U-Link ist falsch oder der Zugang abgelaufen. Den Link testweise im Browser öffnen.',
                    '<strong>Kein TV-Programm:</strong> EPG-URL auf siptv.app ergänzen. Mehr unter <a href="/iptv-epg-probleme/">EPG-Probleme</a>.',
                    '<strong>App nicht im Store:</strong> Ältere Fernseher werden nicht mehr unterstützt; ein <a href="/iptv-stick/">IPTV-Stick</a> ist dann die Lösung.',
                ]),
            ]),
            ('SIPTV mit MOJO4K.DE nutzen', mojo_fit('SIPTV', 'Für SIPTV laden Sie den M3U-Link aus Ihrer Bestätigung auf siptv.app für die MAC-Adresse Ihres Fernsehers hoch.')),
        ],
        'faq': [
            ('Ist SIPTV ein IPTV-Anbieter?', 'Nein. SIPTV (Smart IPTV) ist ein Player. Die Sender kommen aus der Playlist Ihres IPTV-Anbieters.'),
            ('Was kostet SIPTV?', 'Nach der Testphase ist eine einmalige Aktivierungsgebühr pro Gerät fällig, zu zahlen auf siptv.app. Der aktuelle Betrag steht dort.'),
            ('Wo lade ich die Playlist für SIPTV hoch?', 'Auf der offiziellen Website siptv.app, über die MAC-Adresse Ihres Fernsehers.'),
            ('Funktioniert SIPTV auf Samsung-Fernsehern?', 'Auf vielen Modellen ja. Ob die App im Store angeboten wird, hängt vom Modell und der Region ab.'),
        ],
    },
    'iptv-line': {
        'name': 'IPTV Lines',
        'title': 'IPTV Line 2026 – Formate, Verbindungen & Test | MOJO4K.DE',
        'desc': 'Was ist eine IPTV Line? Xtream-Login, M3U-Link oder MAG-Portal erklärt, Verbindungen pro Line, Line vs. Testline und wie Sie eine IPTV Line kostenlos testen.',
        'badge': 'Ratgeber 2026',
        'h1': 'IPTV Line: was eine IPTV Line ist und wie Sie sie nutzen',
        'intro': 'Eine IPTV Line ist Ihr persönlicher Zugang zu einem IPTV-Dienst. Hier lesen Sie, in welchen Formaten eine Line geliefert wird, was „Verbindungen“ bedeuten und wie Sie eine Line vor dem Kauf testen.',
        'sections': [
            ('Was ist eine IPTV Line?', [
                ('p', 'Als IPTV Line (auch „IPTV Linie“ oder Plural „IPTV Lines“) bezeichnet man die Zugangsdaten, mit denen eine Player-App die Sender eines Anbieters lädt. Technisch ist eine Line ein Benutzerkonto auf dem Server des Anbieters mit Laufzeit und einer festen Zahl gleichzeitiger Verbindungen.'),
                ('p', 'Die Line selbst ist unabhängig vom Gerät: Dieselben Daten funktionieren in TiviMate auf dem Fire TV, in Smarters am Handy oder in VLC am PC.'),
            ]),
            ('In welchen Formaten wird eine IPTV Line geliefert?', [
                ('table', ['Format', 'Was Sie bekommen', 'Geeignet für'], [
                    ['Xtream Codes', 'Server-URL, Benutzername, Passwort', '<a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">Smarters</a>, <a href="/implayer/">iMPlayer</a>'],
                    ['M3U-Link', 'eine URL, die die Senderliste enthält', '<a href="/siptv/">SIPTV</a>, <a href="/set-iptv/">Set IPTV</a>, <a href="/iptv-vlc/">VLC</a>'],
                    ['MAG / Portal', 'Portal-URL, Freischaltung über die MAC-Adresse', '<a href="/iptv-mag-box/">MAG-Boxen</a>, <a href="/stb-emu/">STB Emu</a>'],
                ]),
                ('p', 'Xtream ist meist die bequemste Variante: Live-TV, Filme, Serien und EPG werden getrennt geladen. Mehr dazu unter <a href="/xtream-iptv/">Xtream IPTV</a> und <a href="/iptv-m3u/">IPTV M3U</a>.'),
            ]),
            ('Verbindungen: wie viele Geräte pro Line?', [
                ('p', 'Jede Line erlaubt eine bestimmte Zahl gleichzeitiger Streams. Bei einer Line für 1 Gerät läuft immer nur ein Stream; startet ein zweites Gerät, bricht meist der erste Stream ab. Sie können die Daten auf mehreren Geräten speichern, nur nicht gleichzeitig schauen.'),
                ('p', 'Bei MOJO4K.DE gibt es Pakete für 1 bis 10 gleichzeitige Geräte, siehe <a href="/preise/">Preise</a> und zum Beispiel <a href="/iptv-2-geraete/">IPTV für 2 Geräte</a>.'),
            ]),
            ('IPTV Line oder IPTV Testline?', [
                ('p', 'Eine Testline ist eine IPTV Line mit kurzer Laufzeit, die Anbieter zum Ausprobieren vergeben. Sie hat dieselben Formate wie eine bezahlte Line, läuft aber nach wenigen Stunden ab. So prüfen Sie vor dem Kauf, ob Ihre App, Ihr Gerät und Ihre Leitung zusammenpassen.'),
                ('p', 'MOJO4K.DE vergibt eine 24-Stunden-Testline über <a href="/kostenlos-testen">das Testformular</a>. Mehr zum Ablauf unter <a href="/iptv-testline/">IPTV Testline</a>.'),
            ]),
            ('IPTV Line bei MOJO4K.DE', mojo_fit('Ihre App', 'Ihre Line kommt als Xtream-Login und als M3U-Link.')),
        ],
        'faq': [
            ('Was ist eine IPTV Line?', 'Eine IPTV Line ist Ihr persönlicher Zugang zu einem IPTV-Dienst: Zugangsdaten mit Laufzeit und einer festen Zahl gleichzeitiger Verbindungen, nutzbar in einer Player-App.'),
            ('Was ist der Unterschied zwischen IPTV Line und Testline?', 'Eine Testline ist eine IPTV Line mit kurzer Laufzeit zum Ausprobieren. Technisch funktioniert sie genauso wie die bezahlte Line.'),
            ('Kann ich eine IPTV Line auf mehreren Geräten nutzen?', 'Speichern ja, gleichzeitig schauen nur so viele Geräte wie Verbindungen gebucht sind.'),
            ('In welcher App nutze ich meine IPTV Line?', 'In jeder IPTV-App: Xtream-Daten in TiviMate oder Smarters, den M3U-Link in SIPTV, Set IPTV oder VLC.'),
            ('Wie bekomme ich eine IPTV Line bei MOJO4K.DE?', 'Zum Testen über das Formular auf der Seite „Kostenlos testen“, als Abo über die Preisseite. Die Zugangsdaten kommen per E-Mail bzw. WhatsApp.'),
        ],
    },
    'cloud-stream': {
        'name': 'CloudStream',
        'title': 'CloudStream App 2026 – Was ist das, ist es legal? | MOJO4K.DE',
        'desc': 'CloudStream erklärt: Open-Source-App für Android, wie Erweiterungen funktionieren, rechtliche Risiken und wann ein IPTV-Zugang besser passt.',
        'badge': 'Ratgeber 2026',
        'h1': 'CloudStream: was die App ist und wann IPTV die bessere Wahl ist',
        'intro': 'CloudStream ist eine Open-Source-App für Android, die Inhalte aus Erweiterungen lädt. Hier lesen Sie, wie sie funktioniert, worauf Sie rechtlich achten sollten und wie sie sich von einem IPTV-Zugang unterscheidet.',
        'sections': [
            ('Was ist CloudStream?', [
                ('p', 'CloudStream (oft „Cloud Stream“ geschrieben) ist eine quelloffene App für Android-Geräte, die nicht im Google Play Store, sondern über GitHub verteilt wird. Die App selbst enthält keine Inhalte. Sie lädt Filme, Serien und teils Live-TV über Erweiterungen (Repositories), die von Dritten gepflegt werden.'),
                ('p', 'Welche Inhalte eine Erweiterung liefert und woher sie stammen, kontrolliert weder die App noch der Nutzer. Viele Erweiterungen greifen auf Websites zu, die Inhalte ohne Lizenz anbieten.'),
            ]),
            ('Ist CloudStream legal?', [
                ('p', 'Die App als Software ist nicht verboten. Rechtlich entscheidend ist, was Sie damit abspielen. Nach dem Urteil des EuGH zur Rechtssache C-527/15 („Filmspeler“) kann bereits das Streamen offensichtlich rechtswidrig angebotener Inhalte eine Urheberrechtsverletzung sein. In Deutschland gilt das <a href="https://www.gesetze-im-internet.de/urhg/" target="_blank" rel="noopener">Urheberrechtsgesetz</a>.'),
                ('note', 'Wenn eine Erweiterung aktuelle Kinofilme oder Pay-TV gratis zeigt, ist das ein starkes Zeichen für eine unlizenzierte Quelle. Mehr dazu unter <a href="/iptv-legal/">Ist IPTV legal?</a>'),
            ]),
            ('CloudStream oder IPTV-Zugang?', [
                ('table', ['', 'CloudStream', 'IPTV-Zugang mit Player-App'], [
                    ['Inhalte', 'aus Erweiterungen Dritter', 'vom IPTV-Anbieter'],
                    ['Live-TV', 'je nach Erweiterung', 'Kernfunktion, mit EPG'],
                    ['Geräte', 'Android, Android TV', 'Fire TV, Smart TV, Apple, PC, Handy'],
                    ['Installation', 'APK von GitHub', 'App aus dem Store'],
                    ['Ansprechpartner bei Problemen', 'keiner', 'Support des Anbieters'],
                ]),
                ('p', 'Wer vor allem Live-TV mit Programmguide sehen will, ist mit einer IPTV-App wie <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> und einem Abo besser bedient. Für Mediatheken öffentlich-rechtlicher und privater Sender gibt es außerdem die offiziellen Apps der Sender.'),
            ]),
            ('Offizielle Mediatheken als Alternative', [
                ('p', 'Viele Sendungen gibt es legal und kostenlos in den Mediatheken der Sender. Die Apps laufen auf Fire TV, Smart TVs und Smartphones:'),
                ('ul', [
                    'ARD Mediathek und ZDF-Mediathek für das öffentlich-rechtliche Programm, siehe <a href="/iptv-ard-zdf/">ARD und ZDF per IPTV</a>',
                    'Joyn für ProSieben, SAT.1, kabel eins und weitere Sender',
                    'RTL+ für RTL, VOX und n-tv, teils mit Bezahlinhalten',
                ]),
                ('p', 'Wer alle Sender in einer App mit einheitlichem Programmguide sehen möchte, nutzt dafür IPTV.'),
            ]),
            ('IPTV mit MOJO4K.DE', mojo_fit('Ihrer Player-App', 'Statt Erweiterungen zu suchen, tragen Sie einmal Ihre Zugangsdaten ein.')),
        ],
        'faq': [
            ('Was ist CloudStream?', 'Eine Open-Source-App für Android, die Inhalte über Erweiterungen Dritter lädt. Die App selbst enthält keine Filme oder Sender.'),
            ('Gibt es CloudStream im Play Store?', 'Nein, die App wird über GitHub als APK verteilt.'),
            ('Ist CloudStream legal?', 'Die Software ist erlaubt. Das Abspielen offensichtlich rechtswidrig angebotener Inhalte kann aber eine Urheberrechtsverletzung sein.'),
            ('Ist CloudStream dasselbe wie IPTV?', 'Nein. CloudStream lädt Inhalte aus Erweiterungen, IPTV liefert Sender über den Zugang eines Anbieters, den Sie in einer Player-App eintragen.'),
        ],
        'cta_h2': 'Live-TV mit Programmguide testen',
    },
}
