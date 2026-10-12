# Enrichment for app / player pages (keywords that were only in meta tags or missing).
T = '<a href="/kostenlos-testen.html">24 Stunden kostenlos testen</a>'

ENRICH = {
# ── IPTV Smarters ────────────────────────────────────────────────────────────
'iptv-smarters-pro/index.html': {
 'sections': [
  ('Smarters Pro, Smarters IPTV, „IP TV Smarters Pro" – alles dieselbe App', [
   ('p', 'Bei Google landen täglich viele Schreibweisen für dieselbe App: <strong>IPTV Smarters Pro</strong>, <strong>Smarters IPTV</strong>, <strong>Smarters Pro IPTV</strong>, <strong>Smarters IPTV Pro</strong>, <strong>TV Smarters</strong> oder <strong>TV Smarters Pro</strong>. Mit Leerzeichen wird daraus schnell <strong>IP TV Smarters Pro</strong> oder <strong>IP TV Smarter Pro</strong>, ohne Leerzeichen <strong>SmartersPro</strong>. Tippfehler wie <strong>IPTV Smarter Pro</strong>, <strong>IP Smarter Pro</strong>, <strong>IPTV Smart Pro</strong> oder <strong>IP TV Smart Pro</strong> meinen fast immer ebenfalls den Player von WHMCS Smarters.'),
   ('p', 'Wichtig ist der Unterschied zwischen App und Inhalt: Die App selbst ist kostenlos und enthält keine Sender. Erst mit Zugangsdaten eines IPTV-Anbieters – zum Beispiel von MOJO4K – zeigt sie Live-TV, Filme und Serien. Wer eine Seite findet, die „Smarters Pro mit allen Sendern" verkauft, kauft in Wahrheit ein IPTV-Abo eines Dritten.'),
  ]),
  ('IPTV Smarters Pro live: Live-TV, Filme und Serien', [
   ('p', 'Nach dem Login zeigt der Startbildschirm drei Bereiche: <strong>Live TV</strong>, <strong>Movies</strong> und <strong>Series</strong>. Unter „Live TV" finden Sie alle Sendergruppen Ihres Anbieters mit Programmführer (EPG). Wer nach <strong>IPTV Smarters Pro live</strong> sucht, will meist genau das: lineares Fernsehen wie am Kabelanschluss, nur über das Internet.'),
   ('ul', ['<strong>Catch-up</strong>: Sender mit Uhr-Symbol lassen sich bis zu einigen Tagen zurückspulen, sofern der Anbieter das unterstützt.',
           '<strong>Multi-Screen</strong>: Bis zu vier Sender gleichzeitig – praktisch am Bundesliga-Samstag.',
           '<strong>Externer Player</strong>: Bei ruckelnden Streams lässt sich VLC oder MX Player als Wiedergabe einstellen.',
           '<strong>Kindersicherung</strong>: Einzelne Kategorien per PIN sperren.']),
   ('p', 'Mit MOJO4K-Zugangsdaten können Sie Smarters Pro vor dem Kauf ' + T + '.'),
  ]),
 ],
 'faq': [
  ('Ist „IPTV Smarter Pro" eine andere App als IPTV Smarters Pro?', 'Nein. „IPTV Smarter Pro", „IP TV Smarters Pro", „SmartersPro" oder „IPTV Smart Pro" sind Schreibvarianten derselben App. Laden Sie sie nur aus dem Play Store, dem App Store oder von der offiziellen Website iptvsmarters.com.'),
  ('Kann ich mit IPTV Smarters Pro live fernsehen?', 'Ja. Im Bereich „Live TV" laufen alle Sender Ihres IPTV-Anbieters mit Programmführer. Die App liefert selbst keine Sender – dafür brauchen Sie ein Abo wie MOJO4K.'),
 ],
 'app': {'name': 'IPTV Smarters Pro', 'os': 'Android, iOS, Windows, macOS, Fire OS', 'free': True, 'publisher': 'WHMCS Smarters'},
},
'iptv-smarters-pro-fire-tv-stick/index.html': {
 'sections': [
  ('IPTV Smarters auf dem Firestick: die Suchbegriffe kurz erklärt', [
   ('p', 'Ob <strong>IPTV Smarters Firestick</strong>, <strong>IPTV Smarters Fire Stick</strong>, <strong>Smarters Pro Firestick</strong>, <strong>IPTV Smarters Pro Firestick</strong> oder <strong>IPTV Smarters Pro Fire Stick</strong> – gemeint ist immer die Installation auf Amazons Fire TV Stick. Smarters Pro steht nicht im Amazon Appstore. Deshalb führt der Weg über die Downloader-App und die offizielle Download-Adresse von iptvsmarters.com.'),
   ('p', 'Wer nach <strong>IPTV Smarters on Firestick</strong> oder allgemein nach <strong>IPTV for Firestick</strong> sucht, sollte zwei Dinge wissen: Erstens muss unter „Mein Fire TV → Entwickleroptionen" die Installation aus unbekannten Quellen für Downloader erlaubt sein. Zweitens reicht der Fire TV Stick 4K (Max) für 4K-Sender aus, der einfache Stick „Lite" nur für Full HD.'),
   ('table', ['Fire-TV-Modell', 'Smarters Pro', 'Empfehlung'], [
    ['Fire TV Stick Lite', 'läuft, nur Full HD', 'für Zweitgeräte'],
    ['Fire TV Stick 4K / 4K Max', 'läuft flüssig, 4K & HDR', 'beste Wahl'],
    ['Fire TV Cube', 'läuft, LAN-Anschluss', 'für große Senderlisten'],
   ]),
  ]),
 ],
 'faq': [
  ('Warum finde ich IPTV Smarters nicht im Amazon Appstore?', 'Smarters Pro wird für Fire TV nicht über den Amazon Appstore verteilt. Installieren Sie die App mit der Downloader-App von der offiziellen Website des Entwicklers.'),
 ],
},
'iptv-smarters-pro-samsung-tv/index.html': {
 'sections': [
  ('IPTV Smarters Samsung: Tizen, Modelle und Alternativen', [
   ('p', 'Samsung-Fernseher laufen mit dem Betriebssystem Tizen. Wer nach <strong>IPTV Smarters Samsung</strong>, <strong>IPTV Smarters Samsung TV</strong> oder <strong>IPTV Samsung Tizen</strong> sucht, stellt schnell fest: Die Android-Version von Smarters lässt sich auf Tizen nicht installieren. Ob eine Tizen-Version im Samsung Smart Hub erscheint, hängt von Modelljahr und Region ab.'),
   ('p', 'Die gute Nachricht: Für <strong>IPTV for Samsung TV</strong> gibt es verlässliche Wege. Auf Tizen funktionieren IBO Player, Smart IPTV und SS IPTV mit einer M3U-Playlist. Wer die volle Smarters-Oberfläche möchte, steckt einen Fire TV Stick in den HDMI-Port – das dauert fünf Minuten und ist oft flüssiger als jede TV-App.'),
  ]),
 ],
 'faq': [
  ('Welche Samsung-Fernseher unterstützen IPTV-Apps?', 'Samsung Smart TVs mit Tizen ab etwa Modelljahr 2017 können IPTV-Apps wie IBO Player oder Smart IPTV aus dem Smart Hub installieren. Ältere Modelle und Fernseher ohne passende App rüsten Sie mit einem Fire TV Stick nach.'),
 ],
},
'iptv-smarters-pro-android/index.html': {
 'sections': [
  ('IPTV Smarters Android, Android TV und Google Play', [
   ('p', 'Auf Smartphones und Tablets ist der Weg am einfachsten: Im Play Store nach „IPTV Smarters Pro" suchen und auf den Entwickler WHMCS Smarters achten. Diese <strong>IPTV Smarters Pro Google Play</strong>-Version ist die sicherste Quelle. Für <strong>IPTV Smarters Android</strong>-Boxen und Fernseher mit <strong>IPTV Smarters Pro Android TV</strong> ist die App je nach Gerät ebenfalls im Play Store gelistet; fehlt sie, hilft die APK von der offiziellen Website.'),
   ('p', 'Wer ganz allgemein eine <strong>Application IPTV Android</strong> sucht, hat neben Smarters gute Alternativen: TiviMate für Android TV, OTT Navigator für viele Filme und Serien oder XCIPTV als schlanken Player. Alle funktionieren mit denselben MOJO4K-Zugangsdaten.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTV Smarters Pro im Google Play Store?', 'Ja, für Android-Smartphones und viele Android-TV-Geräte. Achten Sie auf den Entwickler „WHMCS Smarters". Nachbauten mit ähnlichem Namen sollten Sie meiden.'),
 ],
},
'iptv-smarters-pro-windows/index.html': {
 'sections': [
  ('IPTV Smarters auf PC, Laptop, Mac und MacBook', [
   ('p', 'Für <strong>IPTV Smarters Pro PC</strong> und <strong>Smarters Pro PC</strong> bietet der Entwickler einen Windows-Installer auf iptvsmarters.com an. Auf dem <strong>IPTV Laptop</strong> funktioniert das genauso wie am Desktop – ein stabiles WLAN oder ein LAN-Kabel vorausgesetzt.'),
   ('p', 'Bei <strong>IPTV Smarters Mac</strong>, <strong>IPTV Smarters Pro Mac</strong> und <strong>IPTV Smarters Pro MacBook</strong> lohnt ein Blick in den Mac App Store: Auf Macs mit Apple-Chip (M1 und neuer) lassen sich viele iPad-Apps installieren, darunter die Smarters-Varianten für iOS. Auf älteren Intel-Macs ist VLC mit Ihrer M3U-Adresse der einfachste Weg.'),
  ]),
 ],
 'faq': [
  ('Läuft IPTV Smarters Pro auf einem MacBook?', 'Auf MacBooks mit Apple-Chip meist ja, über die iPad-Version im Mac App Store. Auf Intel-MacBooks nutzen Sie besser VLC oder einen Web Player mit Ihrer M3U-Adresse.'),
 ],
},
'iptv-smarters-pro-apple-tv/index.html': {
 'sections': [
  ('IPTV Smarters Apple TV und IPTV Smarters Pro iPhone', [
   ('p', 'Im App Store heißt die App oft „Smarters Player Lite". Für <strong>IPTV Smarters Pro iPhone</strong> und iPad laden Sie diese Version, melden sich mit Xtream-Codes-Daten an und haben Live-TV, Filme und Serien auf dem Handy. Für <strong>IPTV Smarters Apple TV</strong> gibt es eine tvOS-Variante, deren Funktionsumfang je nach Version schwankt.'),
   ('p', 'Unser Tipp für Apple TV: Testen Sie parallel iPlayTV oder IPTVX. Beide sind für tvOS gebaut und laden große Senderlisten oft schneller.'),
  ]),
 ],
 'faq': [
  ('Heißt Smarters Pro auf dem iPhone anders?', 'Ja, im App Store finden Sie die App meist als „Smarters Player Lite". Die Anmeldung mit Server-URL, Benutzername und Passwort funktioniert genauso wie auf Android.'),
 ],
},
'iptv-smarters-pro-premium/index.html': {
 'sections': [
  ('IPTV Smarters free, Premium und Subscription – was kostet was?', [
   ('p', 'Die Suchbegriffe <strong>IPTV Smarters Premium</strong>, <strong>IPTV Smarters Subscription</strong>, <strong>IPTV Smarters Pro Subscription</strong> und <strong>IPTV Smarters Pro Price</strong> führen oft in die Irre. Die App ist <strong>IPTV Smarters free</strong> – also kostenlos. Was Geld kostet, ist das IPTV-Abo, das Sie in der App eintragen.'),
   ('table', ['Begriff', 'Was gemeint ist', 'Kosten'], [
    ['IPTV Smarters Pro (App)', 'Player von WHMCS Smarters', 'kostenlos'],
    ['„Smarters Premium" / Subscription', 'IPTV-Abo eines Anbieters', 'bei MOJO4K ab €9 im Monat'],
    ['Smarters-Version für Smart TVs', 'TV-App mit Aktivierung', 'je nach Plattform einmalig'],
   ]),
  ]),
 ],
 'faq': [
  ('Ist IPTV Smarters wirklich kostenlos?', 'Ja, die App selbst ist kostenlos. Kosten entstehen nur für das IPTV-Abo, also für die Sender, die Sie in der App abspielen.'),
 ],
},
'iptv-smarters-lite/index.html': {
 'sections': [
  ('Smarters IPTV Lite oder „Smarters TV Pro"?', [
   ('p', '<strong>Smarters IPTV Lite</strong> ist die abgespeckte Variante für schwächere Geräte und für iPhone und iPad, wo sie als „Smarters Player Lite" im App Store steht. <strong>Smarters TV</strong> und <strong>Smarters TV Pro</strong> sind keine offiziellen Produkte, sondern Suchbegriffe, mit denen Nutzer meist die Pro-Version auf dem Fernseher meinen.'),
   ('p', 'Faustregel: Auf einem Fire TV Stick 4K oder einer aktuellen Android-Box nehmen Sie Pro, auf alten Geräten oder Apple-Hardware die Lite-Version.'),
  ]),
 ],
 'faq': [
  ('Gibt es eine App namens „Smarters TV Pro"?', 'Nicht als eigenes offizielles Produkt. Wer danach sucht, meint fast immer IPTV Smarters Pro auf dem Fernseher oder die Lite-Version für Apple-Geräte.'),
 ],
},
'iptv-web-player/index.html': {
 'sections': [
  ('IPTV im Browser: Web Player, Smarters Web und M3U online', [
   ('p', 'Ein <strong>IPTV Browser</strong>-Player spielt Ihre Sender direkt auf einer Website ab, ganz ohne Installation. Gesucht wird das als <strong>IPTV Web Browser</strong>, <strong>IPTV Website</strong> oder schlicht <strong>IPTV Site</strong>. Auch <strong>IPTV Smarters Web</strong> und <strong>IPTV Smarters online</strong> meinen diesen Weg: Manche Anbieter stellen einen Web Player auf Smarters-Basis bereit, in den Sie sich mit Ihren Zugangsdaten einloggen.'),
   ('p', 'Wer <strong>M3U online</strong> abspielen will, kann die Playlist-Adresse auch in einen browserbasierten HLS-Player einfügen. Das klappt bei Sendern im M3U8-Format zuverlässig, bei anderen Formaten nicht immer – dann hilft VLC am PC.'),
   ('info', 'Sicherheit: Geben Sie Zugangsdaten nur in Web Player ein, die Ihr Anbieter selbst nennt. Fremde Seiten können Ihre Daten speichern und weiterverkaufen.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV ohne App im Browser schauen?', 'Ja, mit einem Web Player. Am stabilsten läuft das in Chrome oder Edge. Für dauerhaftes Fernsehen ist eine App auf Stick oder Smart TV aber komfortabler.'),
 ],
},
'iptv-downloader/index.html': {
 'sections': [
  ('IPTV Smarters Downloader und Smart IPTV Downloader', [
   ('p', 'Mit <strong>IPTV Smarters Downloader</strong> ist meist gemeint: Smarters Pro über die Downloader-App auf den Fire TV Stick bringen. Sie tippen in Downloader die offizielle Download-Adresse von iptvsmarters.com ein, laden die APK und installieren sie. Beim <strong>Smart IPTV Downloader</strong> ist es genauso, nur mit der Adresse von siptv.eu.'),
   ('p', 'Kurzcodes aus Videos oder Foren (zum Beispiel „ly73pr") sind bequem, zeigen aber nicht, welche Datei dahintersteckt. Nutzen Sie lieber die vollständige Adresse des Entwicklers.'),
  ]),
 ],
 'faq': [
  ('Ist die Downloader-App selbst sicher?', 'Ja, Downloader von AFTVnews steht im Amazon Appstore. Riskant sind nur die Dateien, die Sie damit laden. Nutzen Sie ausschließlich Adressen der App-Entwickler.'),
 ],
},
'iptv-vlc/index.html': {
 'sections': [
  ('IP TV VLC und VLC IP TV: kurze Antwort', [
   ('p', 'Ob <strong>IP TV VLC</strong> oder <strong>VLC IP TV</strong>: VLC kann jede M3U- oder M3U8-Adresse abspielen. Unter Windows wählen Sie „Medien → Netzwerkstream öffnen", auf dem Mac „Ablage → Netzwerk öffnen". Für Senderlisten mit tausenden Einträgen ist VLC aber unübersichtlich – ohne Programmführer und Favoriten. Für den Alltag empfehlen wir eine IPTV-App, VLC eignet sich zum schnellen Testen.'),
  ]),
 ],
 'faq': [
  ('Zeigt VLC einen Programmführer (EPG) an?', 'Nein, VLC spielt die Sender nur ab. Einen Programmführer bieten IPTV-Apps wie TiviMate oder IPTV Smarters Pro.'),
 ],
},
'iptv-plex/index.html': {
 'sections': [
  ('Plex IPTV oder Jellyfin IPTV?', [
   ('p', 'Bei <strong>Plex IPTV</strong> brauchen Sie einen Umweg: Plex Live TV erwartet einen TV-Tuner, deshalb setzen viele Nutzer einen Proxy wie xTeVe oder Threadfin ein, der die M3U-Liste als Tuner ausgibt. <strong>Jellyfin IPTV</strong> ist einfacher: Jellyfin liest M3U-Listen und XMLTV-EPG direkt ein und ist kostenlos.'),
   ('p', 'Unsere ausführliche Anleitung für Jellyfin finden Sie unter <a href="/iptv-jellyfin/">IPTV in Jellyfin</a>.'),
  ]),
 ],
 'faq': [
  ('Brauche ich Plex Pass für IPTV in Plex?', 'Für Live TV und DVR in Plex ist Plex Pass nötig. Jellyfin bietet Live TV und Aufnahmen kostenlos.'),
 ],
},
'iptv-jellyfin/index.html': {
 'sections': [
  ('IPTV DVR: Aufnehmen mit dem eigenen Server', [
   ('p', 'Ein <strong>IPTV DVR</strong> nimmt Sendungen auf Ihre Festplatte auf, statt sie nur in der Cloud vorzuhalten. Jellyfin bringt diese Funktion ohne Zusatzkosten mit: Im Programmführer eine Sendung wählen, „Aufnehmen" antippen, fertig. Wichtig ist genug Speicher: Eine Stunde Full HD belegt grob 2 bis 4 GB, eine Stunde 4K deutlich mehr.'),
  ]),
 ],
 'faq': [
  ('Wie viele Sendungen kann Jellyfin gleichzeitig aufnehmen?', 'So viele, wie Ihr IPTV-Abo parallele Verbindungen erlaubt. Mit einem Paket für ein Gerät ist es eine Verbindung, für Aufnahme plus Live-TV brauchen Sie mindestens zwei.'),
 ],
},
'iptv-aufnehmen/index.html': {
 'sections': [
  ('IPTV VOD und IPTV Series: Abruf statt Aufnahme', [
   ('p', 'Bevor Sie aufnehmen: Viele Filme und Serien gibt es ohnehin auf Abruf. <strong>IPTV VOD</strong> (Video on Demand) heißt, dass Filme jederzeit startbar sind. <strong>IPTV Series</strong> sind Serien, sortiert nach Staffel und Folge. In IPTV Smarters Pro und OTT Navigator finden Sie dafür eigene Bereiche, in TiviMate zeigt die Premium-Version VOD ebenfalls an.'),
   ('p', 'Aufnehmen lohnt sich vor allem für Live-Sendungen ohne Catch-up, zum Beispiel Spiele zu ungünstigen Zeiten.'),
  ]),
 ],
 'faq': [
  ('Was ist der Unterschied zwischen VOD und Catch-up?', 'VOD sind Filme und Serien, die dauerhaft abrufbar sind. Catch-up ist das Zurückspulen von Live-Sendern für einige Tage, sofern der Sender das unterstützt.'),
 ],
},
# ── TiviMate ─────────────────────────────────────────────────────────────────
'tivimate-premium/index.html': {
 'sections': [
  ('TiviMate Premium Preis, Kosten und Subscription', [
   ('p', 'Die häufigsten Fragen rund um den <strong>TiviMate Premium Preis</strong> (englisch: <strong>TiviMate Premium Price</strong>) – oft auch als „<strong>Tivi Mate Premium</strong>“ gesucht – lauten: Was kostet es, wie lange gilt es, auf wie vielen Geräten? Der <strong>TiviMate Price</strong> bzw. die <strong>TiviMate Kosten</strong> werden vor dem Kauf in der offiziellen Companion-App angezeigt. Es gibt ein Jahresabo und – je nach Angebot – eine einmalige Lifetime-Option. Den genauen Betrag lesen Sie dort ab, weil der Entwickler Preise gelegentlich anpasst; die Angabe oben auf dieser Seite ist ein Richtwert.'),
   ('p', 'Die <strong>TiviMate Subscription</strong> und die <strong>TiviMate Premium Subscription</strong> betreffen nur die App-Funktionen (Aufnahme, Multi-View, Playlist-Updates). Sender sind nicht enthalten – die liefert Ihr IPTV-Abo. Den <strong>TiviMate Premium Cost</strong> bezahlen Sie also zusätzlich zu Ihrem Anbieter.'),
   ('table', ['Frage', 'Antwort'], [
    ['Wo kaufe ich Premium?', 'In der App „TiviMate Companion" (Android-Handy)'],
    ['Auf wie vielen Geräten?', 'Ein Premium-Konto lässt sich auf bis zu 5 Geräten nutzen'],
    ['Sind Sender enthalten?', 'Nein, nur App-Funktionen'],
    ['Kostenlos testen?', 'Ja, Premium hat eine Testphase; MOJO4K lässt sich ' + T],
   ]),
  ]),
  ('TiviMate Account, tivimate.com und „TiviMate Pro"', [
   ('p', 'Ihr <strong>TiviMate Account</strong> bzw. <strong>TiviMate Premium Account</strong> ist das Konto, mit dem Sie in der Companion-App bezahlt haben. Auf dem Fernseher melden Sie sich unter „Einstellungen → TiviMate Premium" mit diesem Konto an. Die offizielle <strong>TiviMate Website</strong> ist <strong>tivimate.com</strong> – nur dort und in den App-Stores bekommen Sie die echte App.'),
   ('p', 'Eine App namens <strong>TiviMate Pro</strong> gibt es offiziell nicht. Angebotene „Pro"-APKs sind meist geknackte Versionen, die Schadsoftware enthalten können und keine Updates bekommen. Auch eine <strong>TiviMate M3U</strong>-Datei kauft man nicht bei TiviMate: Die M3U-Adresse kommt von Ihrem IPTV-Anbieter und wird in TiviMate als Playlist eingetragen.'),
  ]),
 ],
 'faq': [
  ('Was kostet TiviMate Premium aktuell?', 'Den aktuellen Preis zeigt die TiviMate Companion-App vor dem Kauf an. Es gibt ein Jahresabo und je nach Angebot eine Lifetime-Option. Sender sind darin nicht enthalten.'),
  ('Gibt es TiviMate Pro?', 'Nein, offiziell nur TiviMate (kostenlos) und TiviMate Premium. „TiviMate Pro"-Downloads sind inoffizielle, oft manipulierte Dateien.'),
  ('Wie nutze ich meinen TiviMate Premium Account auf einem zweiten Fire TV Stick?', 'TiviMate auf dem zweiten Gerät installieren, unter Einstellungen → TiviMate Premium anmelden und denselben Account wählen. Bis zu fünf Geräte sind möglich.'),
 ],
 'app': {'name': 'TiviMate IPTV Player', 'os': 'Android TV, Fire OS', 'free': True, 'publisher': 'AR Mobile Dev'},
},
'tivimate/index.html': {
 'sections': [
  ('Tivi Mate oder TiviMate: auf welchen Geräten läuft die App?', [
   ('p', 'Ob <strong>Tivi Mate</strong> mit Leerzeichen oder TiviMate – gemeint ist der „TiviMate IPTV Player" des Entwicklers AR Mobile Dev. Die App ist für Fernseher gebaut, nicht für Handys. Das ist die häufigste Überraschung für Einsteiger.'),
   ('table', ['Gerät', 'TiviMate verfügbar?', 'Hinweis'], [
    ['Fire TV Stick, Fire TV Cube', 'ja, Amazon Appstore', '<a href="/tivimate-fire-tv-stick/">Anleitung</a>'],
    ['Android TV / Google TV', 'ja, Play Store', 'Sony, Philips, TCL, Nvidia Shield'],
    ['Samsung (Tizen), LG (webOS)', 'nein', 'Stick nutzen, siehe <a href="/tivimate-samsung-tv/">TiviMate auf Samsung</a>'],
    ['iPhone, iPad, Apple TV', 'nein', '<a href="/tivimate-apple-tv/">Alternativen für Apple</a>'],
    ['Windows, Mac', 'nein', 'VLC oder Smarters Pro'],
   ]),
   ('p', 'Mehr zu Kosten und Funktionen der Bezahlversion lesen Sie unter <a href="/tivimate-premium/">TiviMate Premium</a>.'),
  ]),
 ],
 'faq': [
  ('Gibt es TiviMate für das Handy?', 'Nein. TiviMate ist für Android TV und Fire TV gebaut. Auf dem Handy gibt es nur die Companion-App zum Verwalten von Premium.'),
 ],
},
'tivimate-fire-tv-stick/index.html': {
 'sections': [
  ('TiviMate Firestick: „Tivi Mate", for Firestick, on Firestick', [
   ('p', 'Ob als <strong>Tivi Mate</strong> mit Leerzeichen, <strong>TiviMate Firestick</strong>, <strong>Firestick TiviMate</strong>, <strong>TiviMate for Firestick</strong> oder <strong>TiviMate on Firestick</strong> gesucht: TiviMate steht im Amazon Appstore und lässt sich direkt über die Suche des Fire TV Sticks installieren. Die Downloader-App brauchen Sie dafür nur, wenn die App in Ihrem Land nicht gelistet ist.'),
   ('p', 'Für Premium-Funktionen wie Aufnahme benötigen Sie die TiviMate Companion-App auf einem Android-Handy. Ohne Premium läuft TiviMate trotzdem – mit einer Playlist und Programmführer.'),
  ]),
 ],
 'faq': [
  ('Ist TiviMate im Amazon Appstore für den Fire TV Stick verfügbar?', 'In Deutschland in der Regel ja. Suchen Sie auf dem Fire TV Stick nach „TiviMate" und installieren Sie den „TiviMate IPTV Player".'),
 ],
},
'tivimate-apple-tv/index.html': {
 'sections': [
  ('TiviMate für PC, Mac und Companion auf dem iPhone', [
   ('p', 'Für <strong>TiviMate PC</strong>, <strong>TiviMate for PC</strong> und <strong>TiviMate Mac</strong> gibt es keine offizielle Desktop-Version. Theoretisch läuft TiviMate in einem Android-Emulator, praktisch ist das umständlich und ruckelt oft. Besser sind am Rechner VLC oder IPTV Smarters Pro für Windows.'),
   ('p', 'Die Companion-App gibt es nur für Android – eine <strong>TiviMate Companion iPhone</strong>-Version existiert nicht. Auf dem iPhone lässt sich Premium deshalb nicht kaufen; Sie brauchen dafür kurz ein Android-Gerät oder einen anderen Player.'),
  ]),
 ],
 'faq': [
  ('Gibt es die TiviMate Companion-App für das iPhone?', 'Nein, die Companion-App ist nur für Android erhältlich. Für den Kauf von Premium reicht aber ein beliebiges Android-Handy, zum Beispiel von einem Familienmitglied.'),
 ],
},
# ── Smart IPTV / SIPTV / SS IPTV ─────────────────────────────────────────────
'smart-iptv-deutschland/index.html': {
 'sections': [
  ('Smart IPTV Kosten und Test: was die App verlangt', [
   ('p', '<strong>Smart IPTV Kosten</strong>: Die App von siptv.eu läuft nach der Installation einige Tage als Test. Danach wird eine einmalige Aktivierung pro Fernseher fällig (siehe oben). Der <strong>Smart IPTV Test</strong> eignet sich gut, um mit einem ' + T.replace('24 Stunden kostenlos testen', 'kostenlosen 24h-Test von MOJO4K') + ' gleichzeitig App und Sender auszuprobieren.'),
   ('p', 'Achtung bei <strong>IP Smart IPTV</strong>, „Smart IPTV Pro" und ähnlichen Namen: Im TV-Store gibt es viele Apps mit fast gleichem Namen. Das Original erkennen Sie daran, dass es eine MAC-Adresse anzeigt und auf siptv.eu verweist.'),
  ]),
  ('Smart IPTV auf LG, Sony, Philips und Hisense VIDAA', [
   ('table', ['Fernseher', 'Smart IPTV verfügbar?', 'Alternative'], [
    ['<strong>Smart IPTV LG</strong> (webOS)', 'im LG Content Store', 'SS IPTV, IBO Player'],
    ['<strong>Smart IPTV Sony</strong> (Android/Google TV)', 'als APK von siptv.eu', 'TiviMate aus dem Play Store'],
    ['<strong>Smart IPTV Philips</strong> (Android TV)', 'als APK von siptv.eu', 'TiviMate, Smarters Pro'],
    ['Philips mit Titan OS / Saphi', 'meist nicht', 'Fire TV Stick'],
    ['<strong>Smart IPTV Hisense VIDAA</strong>', 'je nach Modell, oft nicht', 'Fire TV Stick'],
   ]),
   ('p', 'Bei Fernsehern ohne passende App ist ein Fire TV Stick oder ein Google TV Streamer die zuverlässigste Lösung.'),
  ]),
 ],
 'faq': [
  ('Wie lange kann ich Smart IPTV kostenlos testen?', 'Nach der Installation läuft Smart IPTV einige Tage als Test. Danach ist eine einmalige Aktivierung pro Gerät auf siptv.eu nötig.'),
  ('Gibt es Smart IPTV für Hisense VIDAA?', 'Das hängt vom Modell ab, auf vielen VIDAA-Fernsehern fehlt die App. Ein Fire TV Stick am HDMI-Anschluss löst das Problem zuverlässig.'),
 ],
},
'smart-iptv-download/index.html': {
 'sections': [
  ('Smart IPTV auf Android, Android TV und Fire Stick', [
   ('p', 'Die App wurde aus dem Google Play Store entfernt. Für <strong>Smart IPTV Android</strong>, <strong>Smart IPTV Android TV</strong>, <strong>Smart IPTV Fire Stick</strong> bzw. <strong>Smart IPTV Firestick</strong> laden Sie die APK deshalb direkt vom Entwickler. Die offizielle Seite ist siptv.eu – wer nach <strong>Smart IPTV com</strong> oder <strong>IPTV com</strong> sucht, landet oft auf Nachbauten.'),
   ('p', 'Eine <strong>App Smart IPTV</strong> mit dem Zusatz „Pro" oder „Premium" stammt nicht vom Original-Entwickler. <strong>Smart IPTV Pro</strong> und <strong>Smart IPTV Premium</strong> sind meist andere Apps oder ein IPTV-Abo unter fremdem Namen.'),
  ]),
  ('Smart IPTV MAC: die MAC-Adresse finden', [
   ('p', 'Bei <strong>Smart IPTV Mac</strong> geht es fast nie um Apple-Computer, sondern um die MAC-Adresse Ihres Geräts. Sie steht auf dem Startbildschirm der App, zum Beispiel 00:1a:79:xx:xx:xx. Diese Adresse tragen Sie auf siptv.eu ein, zusammen mit Ihrer M3U-Adresse.'),
  ]),
 ],
 'faq': [
  ('Was bedeutet „Smart IPTV MAC"?', 'Gemeint ist die MAC-Adresse Ihres Fernsehers oder Sticks, die Smart IPTV beim Start anzeigt. Mit ihr laden Sie die Playlist auf siptv.eu hoch.'),
  ('Gibt es Smart IPTV Pro?', 'Nicht vom Original-Entwickler. Apps mit „Pro" im Namen sind andere Produkte. Das Original gibt es über siptv.eu und die TV-App-Stores.'),
 ],
},
'smart-iptv-samsung/index.html': {
 'sections': [
  ('Smart IPTV Tizen: Samsung-Fernseher im Überblick', [
   ('p', 'Samsung nutzt Tizen. Für <strong>Smart IPTV Tizen</strong>, <strong>IPTV Tizen</strong> und <strong>SIPTV Samsung</strong> heißt das: Die App kommt aus dem Samsung Smart Hub, nicht aus dem Play Store. Auf jedem <strong>Smart IPTV Samsung Fernseher</strong> ab etwa Baujahr 2017 klappt das in der Regel.'),
   ('p', 'Wer allgemein nach <strong>Smart TV IP TV</strong> sucht: Neben Smart IPTV gibt es auf Samsung auch IBO Player und SS IPTV. Alle drei lesen eine M3U-Playlist, unterscheiden sich aber bei Bedienung und Kosten.'),
  ]),
 ],
 'faq': [
  ('Wo finde ich Smart IPTV auf meinem Samsung-Fernseher?', 'Im Smart Hub unter „Apps" die Suche öffnen und „Smart IPTV" eingeben. Erscheint die App nicht, ist sie für Ihr Modell nicht verfügbar – dann hilft IBO Player oder ein Fire TV Stick.'),
 ],
},
'smart-iptv-playlist-hochladen/index.html': {
 'sections': [
  ('SIPTV List, Smart IPTV My List und SS IPTV M3U', [
   ('p', 'Die Upload-Seite heißt bei Smart IPTV „My List". Wer nach <strong>Smart IPTV My List</strong>, <strong>Smart IPTV List</strong> oder <strong>SIPTV List</strong> sucht, meint siptv.eu/mylist. Dort tragen Sie die MAC-Adresse und Ihre <strong>Smart IPTV M3U</strong>-Adresse ein.'),
   ('p', 'Bei SS IPTV läuft es anders: <strong>SSIPTV List</strong> und <strong>SSIPTV M3U</strong> laden Sie über einen Verbindungscode hoch. Den Code erzeugt die App unter „Einstellungen → Allgemein". Auf ss-iptv.com geben Sie den Code ein und fügen den Link Ihrer Playlist hinzu.'),
  ]),
 ],
 'faq': [
  ('Wie lade ich eine M3U-Liste in SS IPTV hoch?', 'In SS IPTV unter Einstellungen einen Verbindungscode erzeugen, auf ss-iptv.com im Playlist-Editor eingeben und die M3U-Adresse als externe Playlist speichern.'),
 ],
},
'siptv/index.html': {
 'sections': [
  ('My SIPTV, SIP TV und SIPTV: Begriffe sortiert', [
   ('p', '<strong>SIPTV</strong> ist die Kurzform von Smart IPTV. <strong>My SIPTV</strong> bzw. <strong>My SIP TV</strong> meint die Seite „My List" auf siptv.eu, über die Sie Ihre Playlist hochladen. <strong>SIP TV</strong> ohne „I" ist meist ein Tippfehler für dieselbe App – mit Internet-Telefonie (SIP) hat das nichts zu tun.'),
   ('p', 'Die Schritt-für-Schritt-Anleitung finden Sie unter <a href="/smart-iptv-playlist-hochladen/">Smart IPTV Playlist hochladen</a>.'),
  ]),
 ],
 'faq': [
  ('Was ist My SIPTV?', 'Die Upload-Seite „My List" auf siptv.eu. Dort verknüpfen Sie die MAC-Adresse Ihres Fernsehers mit Ihrer M3U-Playlist.'),
 ],
},
'ssiptv/index.html': {
 'sections': [
  ('SSIPTV Android und ssiptv com', [
   ('p', 'SS IPTV ist vor allem für Smart TVs von LG und Samsung gedacht. Wer nach <strong>SSIPTV Android</strong> sucht, findet für Android-Boxen und Fire TV aktuell bessere Alternativen wie TiviMate oder IPTV Smarters Pro. Die offizielle Website schreibt sich mit Bindestrich: ss-iptv.com. Seiten unter <strong>SSIPTV com</strong> ohne Bindestrich gehören nicht zum Entwickler.'),
  ]),
 ],
 'faq': [
  ('Was ist die offizielle Website von SS IPTV?', 'ss-iptv.com mit Bindestrich. Dort finden Sie den Playlist-Editor, in dem Sie mit dem Verbindungscode Ihre M3U-Liste hochladen.'),
 ],
},
# ── weitere Player ───────────────────────────────────────────────────────────
'xciptv/index.html': {
 'sections': [
  ('XCIPTV auf Fire TV Stick, LG und Samsung', [
   ('p', 'Am besten läuft XCIPTV auf Android-Geräten. Für <strong>XCIPTV Fire TV</strong>, <strong>XCIPTV Fire TV Stick</strong> und <strong>XCIPTV Firestick</strong> installieren Sie die App über den Amazon Appstore oder per Downloader. Auf Android TV kommt sie aus dem Play Store.'),
   ('p', '<strong>XCIPTV LG</strong>, <strong>XCIPTV LG TV</strong> und <strong>XCIPTV Samsung</strong> sind häufige Suchanfragen. Eine native Version für webOS bzw. Tizen ist nicht durchgängig verfügbar. Prüfen Sie den App-Store Ihres Fernsehers; fehlt XCIPTV, nehmen Sie dort IBO Player oder Smart IPTV, oder Sie nutzen einen Fire TV Stick.'),
  ]),
  ('XCIPTV free oder XCIPTV Pro?', [
   ('p', '<strong>XCIPTV free</strong>: Die App ist kostenlos. Eine offizielle <strong>XCIPTV Pro</strong>-Version gibt es nicht. XCIPTV wird aber oft von Anbietern mit eigenem Logo verteilt – solche Versionen heißen dann anders, basieren aber auf demselben Player.'),
  ]),
 ],
 'faq': [
  ('Gibt es XCIPTV für LG-Fernseher?', 'Eine native webOS-Version ist nicht durchgängig verfügbar. Auf LG nutzen Sie IBO Player, Smart IPTV oder einen Fire TV Stick mit XCIPTV.'),
  ('Ist XCIPTV kostenlos?', 'Ja, XCIPTV ist kostenlos. Die Sender kommen von Ihrem IPTV-Anbieter, zum Beispiel MOJO4K.'),
 ],
 'app': {'name': 'XCIPTV Player', 'os': 'Android, Android TV, Fire OS', 'free': True},
},
'stb-emu/index.html': {
 'sections': [
  ('STB Emu Pro: lohnt sich die Bezahlversion?', [
   ('p', 'Neben der kostenlosen Version gibt es <strong>STB Emu Pro</strong> (oft auch <strong>STBEmu Pro</strong> geschrieben) als kostenpflichtige App im Play Store. Pro entfernt Werbung und erlaubt mehr Profile – praktisch, wenn Sie mehrere Portale nutzen. Am Empfang von Sendern ändert Pro nichts.'),
   ('p', '<strong>STBEmu IPTV</strong> funktioniert nur mit Anbietern, die ein Stalker-Portal bereitstellen. MOJO4K liefert Xtream-Codes- und M3U-Zugänge; dafür sind TiviMate oder Smarters Pro die bessere Wahl.'),
  ]),
 ],
 'faq': [
  ('Was ist der Unterschied zwischen STB Emu und STB Emu Pro?', 'Pro ist werbefrei und unterstützt mehr Profile. Die Wiedergabe und die Portal-Unterstützung sind gleich.'),
 ],
 'app': {'name': 'STB Emu', 'os': 'Android, Android TV, Fire OS', 'free': True},
},
'iptv-kodi/index.html': {
 'sections': [
  ('Kodi Live TV: was „Kodi IP TV" und „Kodi XBMC IPTV" bedeuten', [
   ('p', '<strong>Kodi Live TV</strong> ist der Bereich, in dem Kodi Sender mit Programmführer anzeigt. Er bleibt leer, bis ein PVR-Client wie der PVR IPTV Simple Client aktiviert ist. Suchanfragen wie <strong>Kodi IP TV</strong> oder <strong>Kodi IPTV</strong> meinen genau diese Einrichtung.'),
   ('p', '<strong>Kodi XBMC IPTV</strong> verweist auf den alten Namen: Bis 2014 hieß Kodi „XBMC". Anleitungen für XBMC funktionieren grundsätzlich weiter, die Menüs heißen heute aber anders. Nutzen Sie die aktuelle Kodi-Version von kodi.tv.'),
  ]),
 ],
 'faq': [
  ('Warum ist der Bereich „TV" in Kodi leer?', 'Es ist noch kein PVR-Client aktiviert. Aktivieren Sie den PVR IPTV Simple Client, tragen Sie Ihre M3U-Adresse ein und starten Sie Kodi neu.'),
  ('Ist XBMC dasselbe wie Kodi?', 'Ja. XBMC wurde 2014 in Kodi umbenannt. Laden Sie immer die aktuelle Version von kodi.tv.'),
 ],
 'app': {'name': 'Kodi', 'os': 'Android, Windows, macOS, Linux, iOS, Fire OS', 'free': True, 'publisher': 'XBMC Foundation'},
},
'ott-navigator/index.html': {
 'sections': [
  ('OTT Navigator Premium: was die Bezahlversion bringt', [
   ('p', '<strong>OTT Navigator Premium</strong> ist ein optionales Abo innerhalb der App. Es schaltet erweiterte Funktionen frei, etwa mehr Anpassungen der Oberfläche und Aufnahme-Optionen, je nach Version. Für Live-TV, Programmführer und Filme reicht die kostenlose Version. Sender sind auch in Premium nicht enthalten – die liefert Ihr IPTV-Abo.'),
  ]),
 ],
 'faq': [
  ('Brauche ich OTT Navigator Premium für MOJO4K?', 'Nein. Die kostenlose Version spielt alle MOJO4K-Sender mit Programmführer ab. Premium ist nur für Zusatzfunktionen nötig.'),
 ],
 'app': {'name': 'OTT Navigator IPTV', 'os': 'Android, Android TV, Fire OS', 'free': True},
},
'iptvx/index.html': {
 'sections': [
  ('IPTVX auf Android und Apple TV', [
   ('p', 'IPTVX ist eine App für Apple-Geräte: iPhone, iPad, Mac und Apple TV. Für <strong>IPTVX Apple TV</strong> laden Sie die App aus dem App Store auf dem Apple TV und tragen Ihre Zugangsdaten ein. <strong>IPTVX Android</strong> gibt es nicht als offizielle Version. Auf Android sind TiviMate und IPTV Smarters Pro die passenden Gegenstücke.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTVX für Android?', 'Nein, IPTVX ist für Apple-Geräte gebaut. Auf Android nutzen Sie TiviMate, IPTV Smarters Pro oder OTT Navigator.'),
 ],
},
'bester-iptv-player/index.html': {
 'sections': [
  ('Best IPTV Player nach Gerät: Android, Windows und Fire TV Stick', [
   ('p', 'Ob „<strong>best IPTV player</strong>", „<strong>best player IPTV</strong>" oder „<strong>IP TV smart player</strong>": Die beste Wahl hängt vom Gerät ab.'),
   ('table', ['Gerät', 'Unsere Wahl', 'Kostenlos?'], [
    ['<strong>Beste IPTV Player Android</strong> (Handy)', 'IPTV Smarters Pro', 'ja'],
    ['Android TV / Google TV', 'TiviMate', 'ja, Premium optional'],
    ['Fire TV Stick', 'TiviMate oder Smarters Pro', 'ja'],
    ['<strong>IPTV Player Win</strong> (Windows)', 'Smarters Pro für Windows oder VLC', 'ja'],
    ['Smart TV (Samsung/LG)', 'IBO Player, Smart IPTV', 'Testphase, dann Aktivierung'],
   ]),
   ('p', 'Unsere Antwort auf den <strong>bester IPTV Player für Fire TV Stick kostenlos deutsch</strong>: TiviMate. Die App ist kostenlos, die Oberfläche auf Deutsch, und sie bringt den besten Programmführer mit. Wer Filme und Serien wichtiger findet, nimmt Smarters Pro. Ein „<strong>Smart Player TV</strong>" ist übrigens kein eigenes Produkt, sondern meist eine Smart-TV-App wie Smart IPTV.'),
  ]),
 ],
 'faq': [
  ('Welcher IPTV Player ist auf dem Fire TV Stick kostenlos und auf Deutsch?', 'TiviMate und IPTV Smarters Pro sind beide kostenlos und auf Deutsch einstellbar. TiviMate hat den übersichtlicheren Programmführer.'),
 ],
},
'iptv-app/index.html': {
 'sections': [
  ('IP TV App und IP TV Smart: welche App ist gemeint?', [
   ('p', 'Mit <strong>IP TV App</strong> suchen die meisten Nutzer nach einem Player für ihr Gerät. Unter „<strong>IP TV Smart</strong>" landen Anfragen für Smart IPTV (Samsung, LG) und für IPTV Smarters. Beide Apps spielen nur ab, was Ihr Anbieter liefert. Eine Übersicht aller Player nach Gerät finden Sie unter <a href="/iptv-apps/">IPTV Apps</a>.'),
  ]),
 ],
 'faq': [
  ('Welche IPTV App ist die einfachste?', 'Für Einsteiger IPTV Smarters Pro: Zugangsdaten eingeben, fertig. Auf Android TV ist TiviMate am übersichtlichsten.'),
 ],
},
'gse-iptv/index.html': {
 'sections': [
  ('GSEIPTV: GSE Smart IPTV kurz erklärt', [
   ('p', '<strong>GSEIPTV</strong> ist die zusammengeschriebene Suchform für GSE Smart IPTV. Die App läuft auf iPhone, iPad, Apple TV und Android und unterstützt M3U-Playlists, Xtream Codes und EPG. Sie wirkt etwas älter als TiviMate oder IPTVX, ist aber auf Apple-Geräten eine solide Wahl.'),
  ]),
 ],
 'faq': [
  ('Ist GSEIPTV dasselbe wie GSE Smart IPTV?', 'Ja, GSEIPTV ist nur die zusammengeschriebene Form. Gemeint ist die App GSE Smart IPTV.'),
 ],
},
}
