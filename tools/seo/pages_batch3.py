# Batch 3 (keyword gap pass, Oct 2026): LG Smarters, Enigma2, SAT>IP, support, Panasonic, Toshiba.
from pages_batch1 import TRIAL, PRICES

DEVICE_REL = ['iptv-geraete', 'iptv-smart-tv', 'iptv-fire-stick-deutschland', 'tivimate-fire-tv-stick',
              'iptv-smarters-pro', 'beste-iptv-box', 'preise']

PAGES = [
{
 'slug': 'iptv-smarters-pro-lg-tv', 'crumb': 'Smarters Pro auf LG TV', 'parent': 'iptv-apps',
 'title': 'IPTV Smarters Pro auf LG TV (webOS) – Anleitung 2026',
 'desc': 'IPTV Smarters Pro auf dem LG Smart TV: Ist die App im LG Content Store, welche webOS-Version brauchen Sie, und welche Alternativen laufen sicher?',
 'keywords': ['iptv smarters lg', 'iptv smarters lg tv', 'iptv smarters pro lg', 'iptv lg webos', 'iptv for lg webos', 'smart iptv lg', 'xciptv lg'],
 'badge': '📺 Anleitung · LG webOS',
 'h1': '<span class="hl">IPTV Smarters Pro</span> auf dem LG TV',
 'intro': 'Suchen Sie nach <strong>IPTV Smarters LG</strong>, <strong>IPTV Smarters LG TV</strong> oder <strong>IPTV Smarters Pro LG</strong>? Hier steht, ob die App auf Ihrem LG-Fernseher läuft, wie Sie sie einrichten und was Sie tun, wenn sie im Store fehlt.',
 'info': 'Kurz gesagt: Ob Smarters Pro im LG Content Store erscheint, hängt von webOS-Version und Region ab. Fehlt die App, sind IBO Player, Smart IPTV oder ein Fire TV Stick die sichere Lösung.',
 'sections': [
  ('Ist Smarters Pro im LG Content Store?', [
   ('p', 'LG-Fernseher nutzen webOS, nicht Android. Die Android-Version von Smarters Pro lässt sich deshalb nicht installieren. Der Entwickler hat zeitweise eine eigene Smart-TV-Version für LG angeboten; ob sie in Ihrem Content Store auftaucht, hängt vom Modelljahr und vom Land ab. Prüfen Sie es in einer Minute: Content Store öffnen, Lupe wählen, „Smarters" eingeben.'),
   ('p', 'Finden Sie eine App mit ähnlichem Namen, aber einem anderen Entwickler, ist Vorsicht angebracht. Nachbauten verlangen oft eine Aktivierung, ohne dass klar ist, wer dahintersteht.'),
  ]),
  ('Einrichtung, wenn die App verfügbar ist', [
   ('steps', [
    ('App installieren', 'Im LG Content Store „IPTV Smarters Pro" installieren und öffnen.'),
    ('Login-Art wählen', '„Login with Xtream Codes API" wählen. Das ist schneller als eine M3U-Playlist.'),
    ('Zugangsdaten eintragen', 'Name frei wählen, dann Benutzername, Passwort und Server-URL von MOJO4K eingeben.'),
    ('Sender laden', 'Die App lädt Live-TV, Filme, Serien und den Programmführer. Beim ersten Start kann das eine Minute dauern.'),
   ]),
  ]),
  ('Wenn Smarters fehlt: die besten Alternativen auf webOS', [
   ('table', ['App', 'Kosten', 'Stärke'], [
    ['IBO Player', 'Testphase, dann Aktivierung', 'moderne Oberfläche, Xtream & M3U'],
    ['<strong>Smart IPTV LG</strong>', 'Testphase, dann einmalig', 'bewährt, Upload über MAC-Adresse'],
    ['SS IPTV', 'kostenlos', 'einfach, Upload per Code'],
    ['Fire TV Stick + Smarters', 'Kaufpreis Stick', 'volle Smarters- oder TiviMate-Oberfläche'],
   ]),
   ('p', 'Auch <strong>XCIPTV LG</strong> wird oft gesucht. XCIPTV ist eine Android-App und auf webOS nicht nativ verfügbar – auch hier hilft ein Stick am HDMI-Port.'),
  ]),
  ('IPTV for LG webOS: Tipps für flüssiges Bild', [
   ('ul', ['LG per LAN-Kabel verbinden, wenn der Router weiter weg steht. Viele LG-Fernseher haben nur WLAN-Module mittlerer Leistung.',
           'Unter „Allgemein → Geräte → TV-Verwaltung" ungenutzte Apps schließen. webOS hält Apps im Hintergrund offen.',
           'Für Sport die Bewegungsglättung (TruMotion) testen: Manche finden das Bild damit ruhiger, andere unnatürlich.',
           'Bei sehr großen Senderlisten Gruppen ausblenden – das beschleunigt jede TV-App.']),
   ('p', 'Probieren Sie es ohne Risiko aus: ' + TRIAL + '.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTV Smarters Pro für LG Smart TVs?', 'Zeitweise ja, aber nicht in jedem Land und nicht für jede webOS-Version. Prüfen Sie den LG Content Store. Fehlt die App, nutzen Sie IBO Player, Smart IPTV oder einen Fire TV Stick.'),
  ('Kann ich die Android-APK von Smarters auf einem LG TV installieren?', 'Nein. LG nutzt webOS, Android-Apps lassen sich darauf nicht installieren.'),
  ('Welche IPTV App ist auf LG webOS kostenlos?', 'SS IPTV ist kostenlos. IBO Player und Smart IPTV haben eine Testphase und verlangen danach eine Aktivierung.'),
  ('Brauche ich für LG eine M3U-Playlist oder Xtream Codes?', 'Beides funktioniert. Xtream Codes ist bequemer, weil Sender, Filme und Programmführer getrennt geladen werden. MOJO4K liefert beide Varianten.'),
 ],
 'related': ['iptv-lg-tv-deutschland', 'iptv-smarters-pro', 'iptv-smarters-pro-samsung-tv', 'ibo-player', 'smart-iptv-deutschland', 'ssiptv', 'iptv-apps', 'preise'],
},
{
 'slug': 'iptv-enigma2', 'crumb': 'IPTV auf Enigma2', 'parent': 'iptv-geraete',
 'title': 'IPTV auf Enigma2-Receivern: GigaBlue, VU+ & Dreambox',
 'desc': 'IPTV auf dem Enigma2-Receiver: So bringen Sie M3U und Xtream Codes auf GigaBlue, VU+, Dreambox und Edision – plus Dreamlink T2 und T3 im Vergleich.',
 'keywords': ['iptv enigma2', 'gigablue iptv', 'dreamlink t3', 'dreamlink t2', 'edision ping', 'iptv for receiver', 'vu+ iptv'],
 'badge': '🛰️ Anleitung · Linux-Receiver',
 'h1': '<span class="hl">IPTV auf Enigma2</span>-Receivern',
 'intro': 'Viele Haushalte haben schon einen Linux-Receiver für Satellit oder Kabel. Mit dem passenden Plugin zeigt er auch IPTV-Sender – in derselben Senderliste, mit derselben Fernbedienung. So geht <strong>IPTV Enigma2</strong> auf GigaBlue, VU+, Dreambox und Edision.',
 'sections': [
  ('Welche Receiver laufen mit Enigma2?', [
   ('p', 'Enigma2 ist ein Linux-Betriebssystem für Receiver. Es läuft auf Geräten von Dreambox, VU+, GigaBlue, Edision, Octagon und Zgemma. Die meisten Nutzer installieren ein Community-Image wie OpenATV oder OpenPLi, weil diese regelmäßig Updates bekommen. Wer gezielt nach <strong>GigaBlue IPTV</strong> sucht: GigaBlue-Receiver laufen ab Werk mit Enigma2 und eignen sich deshalb besonders gut.'),
   ('table', ['Hersteller', 'Beispiel', 'IPTV-tauglich?'], [
    ['<strong>GigaBlue</strong>', 'UHD Trio 4K', 'ja, mit OpenATV'],
    ['VU+', 'Uno 4K SE, Duo 4K SE', 'ja'],
    ['Dreambox', 'DM920, DM900', 'ja, mit Dreambox OS oder Community-Image'],
    ['<strong>Edision</strong>', 'OS mio 4K, <strong>Edision Ping</strong>', 'ja; Ping ist als reiner IPTV-Receiver gedacht'],
   ]),
  ]),
  ('Drei Wege, IPTV auf Enigma2 zu bringen', [
   ('ol', ['<strong>Bouquet-Import</strong>: Ein Plugin (z. B. „e2m3u2bouquet" oder „IPTV Bouquet Maker") wandelt Ihre M3U-Playlist in eine Enigma2-Senderliste um. Die IPTV-Sender erscheinen dann neben Ihren Sat-Sendern.',
           '<strong>Xtream-Plugins</strong>: Plugins wie „XStreamity" oder „Jedi Maker Xtream" lesen Xtream-Codes-Daten und zeigen Live-TV, Filme und Serien in eigenen Menüs.',
           '<strong>ServiceApp</strong>: Installieren Sie zusätzlich ServiceApp mit exteplayer3. Das verbessert die Wiedergabe vieler Streams deutlich.']),
   ('p', 'Plugins installieren Sie über den Plugin-Browser Ihres Images (grüne Taste in OpenATV). Für den Bouquet-Import tragen Sie nur Ihre M3U-Adresse ein.'),
  ]),
  ('Dreamlink T2 und T3: keine Enigma2-Boxen', [
   ('p', 'Die <strong>Dreamlink T2</strong> und die <strong>Dreamlink T3</strong> werden oft mit Enigma2-Receivern verwechselt. Sie sind reine IPTV-Boxen mit Linux und arbeiten vor allem mit Portal-Zugängen (ähnlich wie MAG-Boxen). Wenn Ihr Anbieter Xtream Codes oder M3U liefert, ist eine Android-Box oder ein Fire TV Stick meist die einfachere Wahl.'),
  ]),
  ('Vor- und Nachteile von IPTV auf dem Sat-Receiver', [
   ('cards', [
    ('Vorteil: eine Fernbedienung', 'Sat- und IPTV-Sender in einer Liste, ohne HDMI-Umschalten.'),
    ('Vorteil: Aufnahme', 'Viele Receiver nehmen IPTV-Sender auf die interne Festplatte auf.'),
    ('Nachteil: Einrichtung', 'Plugins und Images brauchen etwas Technikverständnis.'),
    ('Nachteil: Leistung', 'Ältere Receiver haben schwache Prozessoren; große VOD-Listen laden langsam.'),
   ]),
   ('p', 'Testen Sie den Zugang erst auf dem Receiver: ' + TRIAL + '. Wenn das Bild dort ruckelt, liegt es oft am Player. Dann ServiceApp installieren.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV auf meinem GigaBlue-Receiver nutzen?', 'Ja. Mit OpenATV und einem Plugin wie XStreamity oder einem Bouquet-Import laufen IPTV-Sender neben den Sat-Sendern.'),
  ('Was ist besser: Bouquet-Import oder Xtream-Plugin?', 'Der Bouquet-Import ist ideal für Live-TV in der gewohnten Senderliste. Xtream-Plugins sind besser, wenn Sie auch Filme und Serien nutzen wollen.'),
  ('Ist die Dreamlink T3 ein Enigma2-Receiver?', 'Nein. Dreamlink T2 und T3 sind Linux-IPTV-Boxen, die vor allem mit Portal-Zugängen arbeiten.'),
  ('Warum ruckeln IPTV-Sender auf meinem Enigma2-Receiver?', 'Häufig liegt es am Standard-Player. Installieren Sie ServiceApp mit exteplayer3 und stellen Sie IPTV-Sender darauf um. Prüfen Sie außerdem die Netzwerkverbindung.'),
 ],
 'related': ['iptv-set-top-box', 'mag-box-modelle', 'formuler-tv-box', 'iptv-m3u', 'xtream-iptv', 'iptv-geraete', 'sat-ip', 'preise'],
},
{
 'slug': 'sat-ip', 'crumb': 'SAT>IP vs. IPTV', 'parent': 'iptv-geraete',
 'title': 'SAT>IP erklärt: Sat-TV im Heimnetz vs. IPTV (2026)',
 'desc': 'SAT>IP verteilt Satellitenfernsehen per WLAN im Haus. Wie es funktioniert, welche Geräte Sie brauchen und wann IPTV die bessere Lösung ist.',
 'keywords': ['sat ip tv', 'sat>ip', 'sat ip', 'sat ip server', 'sat ip vs iptv'],
 'badge': '📡 Ratgeber · Technik',
 'h1': '<span class="hl">SAT>IP</span> – Satellitenfernsehen im Heimnetz',
 'intro': '<strong>SAT IP TV</strong> klingt nach IPTV, ist aber etwas anderes: Das Signal kommt weiter von Ihrer Satellitenschüssel und wird nur im Haus über das Netzwerk verteilt. Hier erfahren Sie, wie SAT>IP funktioniert und wann sich IPTV mehr lohnt.',
 'sections': [
  ('So funktioniert SAT>IP', [
   ('p', 'Ein SAT>IP-Server hängt am Kabel Ihrer Satellitenschüssel. Er wandelt das Satellitensignal in Datenpakete um und schickt sie über LAN oder WLAN an Fernseher, Tablets und Handys im Haus. Die Geräte brauchen dafür keinen eigenen Sat-Anschluss, nur eine SAT>IP-fähige App oder einen SAT>IP-fähigen Fernseher.'),
   ('p', 'Der Standard wurde vom Satellitenbetreiber SES (Astra) ins Leben gerufen. Bekannte Server gibt es zum Beispiel von Telestar (Digibit), Kathrein und Triax. Manche Multischalter und Receiver haben SAT>IP eingebaut.'),
  ]),
  ('SAT>IP vs. IPTV im Vergleich', [
   ('table', ['Merkmal', 'SAT>IP', 'IPTV'], [
    ['Signalquelle', 'eigene Satellitenschüssel', 'Internet'],
    ['Programme', 'frei empfangbare Sat-Sender (und Pay-TV mit Karte)', 'je nach Anbieter, viele Länder'],
    ['Außer Haus nutzbar', 'nein, nur im Heimnetz', 'ja, überall mit Internet'],
    ['Internet nötig', 'nein', 'ja, ca. 10–25 Mbit/s pro Stream'],
    ['Einmalkosten', 'Server ca. 100–300 €', 'Stick ca. 40–70 €'],
    ['Laufende Kosten', 'keine (Free-TV)', 'Abo, bei MOJO4K ' + PRICES],
   ]),
  ]),
  ('Für wen sich SAT>IP lohnt', [
   ('ul', ['Sie haben bereits eine Schüssel und wollen Sat-TV auf mehreren Geräten ohne neue Kabel.',
           'Sie schauen vor allem frei empfangbare deutsche Sender.',
           'Ihre Internetleitung ist langsam, Ihr Heimnetz aber gut.']),
   ('p', 'IPTV passt besser, wenn Sie keine Schüssel haben (Mietwohnung, Denkmalschutz), unterwegs schauen wollen oder Sender aus vielen Ländern suchen.'),
  ]),
  ('Kombinieren: SAT>IP und IPTV in einer App', [
   ('p', 'Einige Apps und Enigma2-Receiver können beides: SAT>IP-Sender aus dem Heimnetz und IPTV-Sender aus dem Internet in einer gemeinsamen Liste. Auf Enigma2 funktioniert das mit Bouquets, siehe <a href="/iptv-enigma2/">IPTV auf Enigma2</a>. Unterscheiden Sie dabei klar zwischen beiden Quellen, damit Sie bei Problemen wissen, wo Sie suchen müssen.'),
   ('p', 'Ausprobieren kostet nichts: ' + TRIAL + '.'),
  ]),
 ],
 'faq': [
  ('Ist SAT>IP dasselbe wie IPTV?', 'Nein. SAT>IP verteilt Satellitenfernsehen aus Ihrer eigenen Schüssel im Heimnetz. IPTV kommt komplett über das Internet.'),
  ('Brauche ich für SAT>IP Internet?', 'Nein. SAT>IP nutzt nur Ihr Heimnetz. Internet brauchen Sie lediglich für App-Updates.'),
  ('Kann ich SAT>IP unterwegs nutzen?', 'In der Regel nein, SAT>IP ist für das Heimnetz gedacht. Für Fernsehen unterwegs eignet sich IPTV.'),
  ('Wie viele Geräte können gleichzeitig SAT>IP schauen?', 'So viele, wie der Server Tuner hat. Typische Server haben zwei bis acht Tuner, also zwei bis acht gleichzeitige Sender.'),
 ],
 'related': ['iptv-vs-satellit', 'iptv-vs-kabel', 'iptv-enigma2', 'iptv-set-top-box', 'was-ist-iptv', 'iptv-geraete', 'iptv-router', 'preise'],
},
{
 'slug': 'iptv-kundenservice', 'crumb': 'IPTV Kundenservice',
 'title': 'IPTV Kundenservice: Wer hilft bei App- und Senderproblemen?',
 'desc': 'IPTV Smarters Customer Service, App-Entwickler oder Anbieter? So finden Sie den richtigen Ansprechpartner bei IPTV-Problemen – mit Checkliste.',
 'keywords': ['iptv customer service', 'iptv smarters customer service', 'iptv smarters com', 'iptv support', 'iptv kundenservice'],
 'badge': '🛟 Ratgeber · Hilfe & Support',
 'h1': '<span class="hl">IPTV Kundenservice</span> – an wen Sie sich wenden',
 'intro': 'Ein Sender läuft nicht, die App stürzt ab, der Programmführer ist leer: Bei IPTV sind oft zwei Firmen beteiligt – der App-Entwickler und der Anbieter der Sender. Wer den richtigen <strong>IPTV Customer Service</strong> anschreibt, bekommt schneller eine Lösung.',
 'info': 'Faustregel: Probleme mit Sendern, Login oder Programmführer → Ihr IPTV-Anbieter. Probleme mit Abstürzen, Updates oder App-Aktivierung → der App-Entwickler.',
 'sections': [
  ('App oder Anbieter: Wer ist zuständig?', [
   ('table', ['Problem', 'Zuständig', 'Warum'], [
    ['Sender schwarz oder ruckelt', 'IPTV-Anbieter', 'Die Streams kommen von seinen Servern'],
    ['„Login fehlgeschlagen"', 'IPTV-Anbieter', 'Er verwaltet Ihre Zugangsdaten'],
    ['Programmführer leer', 'meist IPTV-Anbieter', 'Er liefert die EPG-Daten'],
    ['App stürzt ab, startet nicht', 'App-Entwickler', 'Fehler in der App selbst'],
    ['Aktivierung (z. B. Smart IPTV, IBO)', 'App-Entwickler', 'Die Lizenz verkauft der Entwickler'],
    ['Premium-Funktionen (z. B. TiviMate)', 'App-Entwickler', 'Premium ist ein App-Kauf'],
   ]),
  ]),
  ('IPTV Smarters Customer Service und iptvsmarters.com', [
   ('p', 'Beim <strong>IPTV Smarters Customer Service</strong> erwarten viele Hilfe bei Sendern. Der Entwickler WHMCS Smarters stellt aber nur die App bereit und liefert keine Inhalte. Auf der Website (oft als „<strong>IPTV Smarters com</strong>" gesucht, offiziell iptvsmarters.com) finden Sie Downloads und ein Kontaktformular für App-Fehler. Fragen zu Sendern, Zahlung oder Zugangsdaten beantwortet dort niemand – dafür ist Ihr Anbieter zuständig.'),
  ]),
  ('Checkliste: So bekommen Sie schneller Hilfe', [
   ('ol', ['Gerät und App nennen, zum Beispiel „Fire TV Stick 4K, TiviMate 5.x".',
           'Genauen Sender und Uhrzeit angeben, an dem das Problem auftrat.',
           'Fehlermeldung abfotografieren oder abschreiben.',
           'Schon probiert? Gerät neu starten, Playlist aktualisieren, anderes Netzwerk testen.',
           'Nur Ihren Benutzernamen nennen, nie das Passwort in öffentliche Foren posten.']),
  ]),
  ('So erreichen Sie den Support von MOJO4K', [
   ('p', 'MOJO4K-Kunden schreiben dem Support über die <a href="/kontakt/">Kontaktseite</a> oder per WhatsApp. Wir helfen bei Zugangsdaten, Senderproblemen und der Einrichtung auf Ihrem Gerät – auch wenn das Problem in der App liegt, sagen wir Ihnen, was zu tun ist. Noch kein Kunde? ' + TRIAL + ' und den Support gleich mittesten.'),
  ]),
 ],
 'faq': [
  ('Hilft der IPTV Smarters Kundenservice bei Senderproblemen?', 'Nein. WHMCS Smarters liefert nur die App. Für Sender, Login und Programmführer ist Ihr IPTV-Anbieter zuständig.'),
  ('Wie erreiche ich den MOJO4K Support?', 'Über die Kontaktseite oder per WhatsApp. Halten Sie Gerät, App und Benutzernamen bereit.'),
  ('Was mache ich, wenn mein IPTV-Anbieter nicht antwortet?', 'Prüfen Sie zuerst die Kontaktwege im Impressum. Bei PayPal-Zahlungen können Sie über den Käuferschutz eine Klärung anstoßen. Wählen Sie künftig einen Anbieter, den Sie vorher testen können.'),
  ('Wer hilft bei einer fehlgeschlagenen App-Aktivierung?', 'Der App-Entwickler, zum Beispiel siptv.eu bei Smart IPTV oder der IBO-Player-Support. Der IPTV-Anbieter hat darauf keinen Zugriff.'),
 ],
 'related': ['kontakt', 'iptv-smarters-pro', 'iptv-ruckelt-buffering', 'iptv-epg-probleme', 'iptv-wlan-probleme', 'iptv-apps', 'iptv-forum', 'preise'],
},
{
 'slug': 'iptv-panasonic-tv', 'crumb': 'IPTV Panasonic TV', 'parent': 'iptv-geraete',
 'title': 'IPTV auf Panasonic TV: Fire TV, My Home Screen & Apps',
 'desc': 'IPTV auf dem Panasonic-Fernseher: Was auf neuen Fire-TV-Modellen geht, was auf My Home Screen fehlt und welche App Sie in 5 Minuten einrichten.',
 'keywords': ['iptv panasonic', 'iptv panasonic tv', 'panasonic smart tv iptv', 'panasonic fire tv iptv'],
 'badge': '📺 Anleitung · Panasonic',
 'h1': '<span class="hl">IPTV auf Panasonic</span>-Fernsehern',
 'intro': 'Bei <strong>IPTV Panasonic</strong> kommt es auf das Baujahr an. Neuere Panasonic-Fernseher laufen teilweise mit Fire TV und damit mit den gängigen IPTV-Apps. Ältere Modelle mit „My Home Screen" haben kaum passende Apps – dort hilft ein Stick.',
 'sections': [
  ('Welches System hat Ihr Panasonic?', [
   ('table', ['System', 'Typische Modelle', 'IPTV-Apps'], [
    ['Fire TV (Fire OS)', 'neuere Modelle ab 2024, z. B. Serien mit „Fire TV" im Namen', 'TiviMate, Smarters Pro (per Downloader)'],
    ['My Home Screen', 'die meisten Modelle bis etwa 2023', 'kaum IPTV-Apps, Stick empfohlen'],
    ['Android TV', 'einzelne Modelle', 'TiviMate, Smarters Pro aus dem Play Store'],
   ]),
   ('p', 'Das System finden Sie unter „Menü → Hilfe" oder am Startbildschirm: Fire TV zeigt die bekannte Amazon-Oberfläche, My Home Screen eine Leiste mit großen Kacheln.'),
  ]),
  ('Panasonic mit Fire TV: Einrichtung', [
   ('steps', [
    ('TiviMate installieren', 'Im Startmenü „Suchen" wählen, „TiviMate" eingeben, installieren.'),
    ('Playlist hinzufügen', 'In TiviMate „Playlist hinzufügen" → „Xtream Codes" wählen.'),
    ('MOJO4K-Daten eingeben', 'Server-URL, Benutzername und Passwort eintragen, dann „Weiter".'),
    ('Programmführer laden', 'TiviMate lädt Sender und EPG automatisch. Fertig.'),
   ]),
   ('p', 'Lieber Smarters Pro? Installieren Sie die Downloader-App und laden Sie Smarters von der offiziellen Website, siehe <a href="/iptv-smarters-pro-fire-tv-stick/">Smarters auf Fire TV</a> – der Weg ist identisch.'),
  ]),
  ('Panasonic mit My Home Screen: der Stick-Weg', [
   ('p', 'My Home Screen hat einen kleinen App-Marktplatz ohne bekannte IPTV-Player. Statt sich mit Browser-Lösungen zu quälen, stecken Sie einen Fire TV Stick oder Google TV Streamer in einen freien HDMI-Port. Über HDMI-CEC steuern Sie den Stick oft sogar mit der Panasonic-Fernbedienung.'),
   ('ul', ['HDMI-CEC heißt bei Panasonic „VIERA Link" – im Menü einschalten.',
           'Den Stick an einen HDMI-Port mit 4K/HDR-Unterstützung stecken (meist HDMI 1 oder 2).',
           'Für HDR-Inhalte in den Bildeinstellungen „HDMI Auto" bzw. erweiterten HDMI-Modus aktivieren.']),
  ]),
  ('Bildeinstellungen für Sport und Filme', [
   ('p', 'Panasonic-Fernseher sind für ihre natürliche Bildabstimmung bekannt. Für IPTV empfehlen wir den Bildmodus „Normal" oder „Kino" bei Filmen und „Sport" bei Fußball. Schalten Sie die Rauschunterdrückung bei HD-Sendern eher niedrig; zu starke Filter lassen Rasenflächen verwaschen wirken.'),
   ('p', 'Testen Sie die Kombination aus Fernseher und App vor dem Kauf: ' + TRIAL + '.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV auf einem Panasonic Smart TV nutzen?', 'Auf Panasonic-Modellen mit Fire TV oder Android TV ja, direkt mit TiviMate oder Smarters Pro. Auf Modellen mit My Home Screen nutzen Sie einen Fire TV Stick.'),
  ('Welche IPTV App ist die beste für Panasonic mit Fire TV?', 'TiviMate, weil die App im Amazon Appstore steht und den übersichtlichsten Programmführer hat.'),
  ('Funktioniert Smart IPTV auf Panasonic?', 'Auf Fire-TV-Modellen als APK von siptv.eu, auf My Home Screen in der Regel nicht.'),
  ('Kann ich den Fire TV Stick mit der Panasonic-Fernbedienung steuern?', 'Oft ja, wenn VIERA Link (HDMI-CEC) aktiviert ist. Die Grundfunktionen wie Navigation und OK funktionieren dann.'),
 ],
 'related': ['iptv-toshiba-tv', 'iptv-smart-tv', 'iptv-sony-tv', 'iptv-philips-tv'] + DEVICE_REL,
},
{
 'slug': 'iptv-toshiba-tv', 'crumb': 'IPTV Toshiba TV', 'parent': 'iptv-geraete',
 'title': 'IPTV auf Toshiba TV: Fire TV, VIDAA & Android TV',
 'desc': 'IPTV auf dem Toshiba-Fernseher: Welche App auf Fire TV, VIDAA und Android TV läuft und wann ein Stick die bessere Lösung ist – mit Anleitung.',
 'keywords': ['iptv toshiba', 'iptv toshiba tv', 'toshiba smart tv iptv', 'toshiba fire tv iptv', 'toshiba vidaa iptv'],
 'badge': '📺 Anleitung · Toshiba',
 'h1': '<span class="hl">IPTV auf Toshiba</span>-Fernsehern',
 'intro': 'Toshiba-Fernseher gibt es mit drei Systemen: Fire TV, VIDAA und Android TV. Für <strong>IPTV Toshiba</strong> ist das die wichtigste Frage, denn davon hängt ab, ob Sie TiviMate direkt installieren können oder einen Stick brauchen.',
 'sections': [
  ('Toshiba-Systeme im Überblick', [
   ('table', ['System', 'Erkennen', 'IPTV-Weg'], [
    ['Fire TV Edition', 'Amazon-Oberfläche, Alexa-Fernbedienung', 'TiviMate direkt, Smarters per Downloader'],
    ['VIDAA', 'eigene Startleiste mit VIDAA-Logo', 'wenige Apps, meist Stick nötig'],
    ['Android TV', 'Google-Startbildschirm, Play Store', 'TiviMate oder Smarters aus dem Play Store'],
   ]),
   ('p', 'Viele neuere Toshiba-Modelle laufen mit VIDAA, dem System, das auch Hisense nutzt. Die Fire-TV-Modelle sind in Deutschland ebenfalls verbreitet.'),
  ]),
  ('Toshiba mit Fire TV oder Android TV', [
   ('steps', [
    ('App suchen', 'Auf Fire TV: Suche → „TiviMate". Auf Android TV: Play Store → „TiviMate".'),
    ('Installieren und öffnen', 'App installieren, „Playlist hinzufügen" wählen.'),
    ('Zugangsdaten eintragen', 'Xtream Codes wählen und die MOJO4K-Daten eingeben.'),
    ('Fertig', 'Sender, Filme und Programmführer erscheinen nach kurzer Ladezeit.'),
   ]),
  ]),
  ('Toshiba mit VIDAA: was geht', [
   ('p', 'Auf VIDAA ist die App-Auswahl klein. Schauen Sie im VIDAA Store, ob ein M3U-Player angeboten wird. Viele Nutzer kommen schneller zum Ziel, wenn sie einen Fire TV Stick anschließen. Mehr zu VIDAA lesen Sie auf unserer Seite zu <a href="/iptv-hisense-tv/">IPTV auf Hisense</a>, denn beide Marken nutzen dasselbe System.'),
  ]),
  ('Tipps für ein ruhiges Bild', [
   ('ul', ['Toshiba-Modelle der Einstiegsklasse haben oft nur 2,4-GHz-WLAN. Ein Stick mit 5-GHz-WLAN oder ein LAN-Kabel hilft gegen Ruckler.',
           'Bewegungsglättung bei Sport ausprobieren, bei Filmen eher ausschalten.',
           'Ungenutzte Sendergruppen in der App ausblenden – das beschleunigt den Programmführer.']),
   ('p', 'Probieren Sie es mit Ihrem Fernseher aus: ' + TRIAL + '.'),
  ]),
 ],
 'faq': [
  ('Kann ich TiviMate auf einem Toshiba-Fernseher installieren?', 'Auf Modellen mit Fire TV oder Android TV ja, direkt aus dem jeweiligen Store. Auf VIDAA-Modellen brauchen Sie einen Fire TV Stick.'),
  ('Ist VIDAA auf Toshiba dasselbe wie auf Hisense?', 'Ja, beide Marken nutzen das System VIDAA. Tipps für Hisense gelten deshalb auch für Toshiba-Modelle mit VIDAA.'),
  ('Welcher Stick passt zu einem Toshiba mit VIDAA?', 'Ein Fire TV Stick 4K oder ein Google TV Streamer. Beide lassen sich per HDMI-CEC oft mit der Toshiba-Fernbedienung steuern.'),
  ('Brauche ich für IPTV auf Toshiba eine Satellitenschüssel?', 'Nein. IPTV kommt komplett über das Internet. Sie brauchen nur eine stabile Verbindung von etwa 10 Mbit/s für HD.'),
 ],
 'related': ['iptv-panasonic-tv', 'iptv-hisense-tv', 'iptv-smart-tv', 'iptv-tcl-tv'] + DEVICE_REL,
},
]
