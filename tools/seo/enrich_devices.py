# Enrichment for device / hardware pages.
T = '<a href="/kostenlos-testen-de">24 Stunden kostenlos testen</a>'

ENRICH = {
'fire-tv-stick-iptv/index.html': {
 'sections': [
  ('Fire TV IPTV: Amazon Fire Stick in der Praxis', [
   ('p', 'Für <strong>Fire TV IPTV</strong> brauchen Sie drei Dinge: einen Fire TV Stick, eine IPTV-App und ein Abo. Bei Suchen wie <strong>Amazon Fire Stick IPTV</strong> oder <strong>IPTV Amazon Stick</strong> geht es meist um die Frage, welcher Stick reicht. Unsere Erfahrung: Der Fire TV Stick 4K ist das beste Preis-Leistungs-Verhältnis, der 4K Max hat mehr Speicher und das schnellere WLAN.'),
   ('ol', ['TiviMate oder IPTV Smarters Pro installieren (TiviMate direkt aus dem Appstore, Smarters per Downloader).',
           'MOJO4K-Zugangsdaten eintragen.',
           'Bei Rucklern: Stick per HDMI-Verlängerung vom Fernseher weg positionieren oder den Ethernet-Adapter von Amazon nutzen.']),
  ]),
 ],
 'faq': [
  ('Welcher Amazon Fire Stick ist der beste für IPTV?', 'Der Fire TV Stick 4K Max: genug Speicher für große Senderlisten, Wi-Fi 6E und 4K mit HDR. Für reine Full-HD-Nutzung reicht der einfache Fire TV Stick.'),
 ],
},
'iptv-fire-stick-deutschland/index.html': {
 'sections': [
  ('IPTV for Firestick: die kürzeste Anleitung', [
   ('p', 'Wer <strong>IPTV for Firestick</strong> sucht, will meist nur wissen, wie es am schnellsten geht. In drei Sätzen: TiviMate im Amazon Appstore installieren. Unter „Playlist hinzufügen" die Xtream-Codes-Daten von MOJO4K eintragen. Fertig – Programmführer und Sender laden automatisch. Probieren Sie es ' + T.replace('24 Stunden kostenlos testen', '24 Stunden kostenlos') + ' aus.'),
  ]),
 ],
 'faq': [
  ('Muss ich den Fire TV Stick für IPTV „jailbreaken"?', 'Nein. TiviMate gibt es im Amazon Appstore. Nur für Apps außerhalb des Stores erlauben Sie in den Entwickleroptionen die Installation für die Downloader-App.'),
 ],
},
'iptv-lg-tv-deutschland/index.html': {
 'sections': [
  ('IPTV LG TV: webOS-Versionen und passende Apps', [
   ('p', 'LG-Fernseher laufen mit webOS. Für <strong>IPTV LG TV</strong>, <strong>IPTV LG webOS</strong> und <strong>IPTV for LG webOS</strong> kommen die Apps aus dem LG Content Store. Bewährt haben sich IBO Player, Smart IPTV und SS IPTV. Ob IPTV Smarters Pro im Store erscheint, hängt von webOS-Version und Region ab – Details in unserer Anleitung <a href="/iptv-smarters-pro-lg-tv/">Smarters Pro auf LG TV</a>.'),
   ('table', ['webOS', 'Typische Baujahre', 'Hinweis'], [
    ['webOS 3.x–4.x', 'ca. 2016–2019', 'Apps laufen, Store-Auswahl kleiner'],
    ['webOS 5–6', 'ca. 2020–2021', 'gute App-Auswahl'],
    ['webOS 22–25', 'ab 2022', 'aktuellste Apps, auch Re:New-Updates'],
   ]),
  ]),
 ],
 'faq': [
  ('Welche IPTV App ist die beste für LG webOS?', 'IBO Player bietet die modernste Oberfläche, Smart IPTV ist bewährt, SS IPTV ist kostenlos. Alle drei funktionieren mit MOJO4K.'),
 ],
},
'iptv-hisense-tv/index.html': {
 'sections': [
  ('IPTV Hisense VIDAA: was geht, was nicht', [
   ('p', 'Die meisten Hisense-Fernseher nutzen VIDAA. Der VIDAA-Store hat weniger Apps als Google oder LG. Für <strong>IPTV Hisense VIDAA</strong> heißt das: Prüfen Sie im Store, ob ein IPTV-Player wie IBO Player oder ein M3U-Player angeboten wird. <strong>Smart IPTV Hisense VIDAA</strong> ist auf vielen Modellen nicht verfügbar.'),
   ('p', 'Einige Hisense-Modelle laufen mit Google TV statt VIDAA – dort installieren Sie TiviMate direkt aus dem Play Store. Bei VIDAA ist ein Fire TV Stick die sichere Lösung.'),
  ]),
 ],
 'faq': [
  ('Woran erkenne ich, ob mein Hisense VIDAA oder Google TV hat?', 'Schauen Sie auf den Startbildschirm: VIDAA zeigt eine eigene Leiste mit „VIDAA"-Logo, Google TV die typischen Tabs „Für dich" und „Apps". Alternativ steht es in den Einstellungen unter „Systeminformationen".'),
 ],
},
'iptv-sony-tv/index.html': {
 'sections': [
  ('IPTV Sony Bravia: Google TV macht es einfach', [
   ('p', 'Aktuelle <strong>Sony Bravia</strong>-Fernseher laufen mit Google TV, ältere mit Android TV. Für <strong>IPTV Sony Bravia</strong> installieren Sie TiviMate oder IPTV Smarters Pro direkt aus dem Play Store – ohne Stick und ohne Umweg. Für 4K-Sender empfehlen wir LAN statt WLAN, weil Sony-Fernseher oft weit vom Router entfernt stehen.'),
  ]),
 ],
 'faq': [
  ('Brauche ich für IPTV auf einem Sony Bravia einen Stick?', 'Nein, wenn Ihr Bravia Android TV oder Google TV nutzt. Dann installieren Sie die App direkt aus dem Play Store.'),
 ],
},
'iptv-chromecast-google-tv/index.html': {
 'sections': [
  ('IPTV Google TV, Smarters Chromecast und TiviMate Chromecast', [
   ('p', 'Bei <strong>IPTV Google TV</strong> ist die Lage einfach: Chromecast mit Google TV und der neuere Google TV Streamer sind vollwertige Android-TV-Geräte. TiviMate und Smarters Pro laufen dort nativ.'),
   ('p', 'Anders beim Streamen vom Handy: <strong>IPTV Smarters Chromecast</strong> funktioniert, wenn die Smarters-App in Ihrer Version ein Cast-Symbol zeigt. <strong>TiviMate Chromecast</strong> im Sinne von „vom Handy auf den Fernseher casten" gibt es nicht, weil TiviMate keine Handy-App ist. Installieren Sie TiviMate stattdessen direkt auf dem Google-TV-Gerät.'),
  ]),
 ],
 'faq': [
  ('Kann ich TiviMate auf Chromecast nutzen?', 'Ja, auf Chromecast mit Google TV und dem Google TV Streamer läuft TiviMate direkt aus dem Play Store. Auf ältere Chromecasts ohne Fernbedienung lässt sich TiviMate nicht casten.'),
 ],
},
'iptv-android-box/index.html': {
 'sections': [
  ('IPTV TV Box Android: worauf es ankommt', [
   ('p', 'Bei <strong>IPTV TV Box Android</strong>, <strong>Box Android IPTV</strong> oder <strong>Box IPTV Android</strong> lohnt der Blick auf das Betriebssystem. Boxen mit offiziellem Android TV bzw. Google TV (zum Beispiel Nvidia Shield, Google TV Streamer, Homatics) bekommen Updates und haben den Play Store. Günstige <strong>IPTV Box Android</strong>-Geräte mit „Android 12 AOSP" haben oft keine Lizenz für Netflix in HD und keine Updates.'),
   ('table', ['Merkmal', 'Gute Box', 'Billig-Box'], [
    ['System', 'Android TV / Google TV', 'AOSP ohne Zertifizierung'],
    ['Updates', 'regelmäßig', 'selten oder nie'],
    ['Streaming-Apps', 'Netflix & Co. in HD/4K', 'oft nur SD'],
    ['IPTV-Apps', 'TiviMate, Smarters Pro', 'laufen, oft langsamer'],
   ]),
  ]),
 ],
 'faq': [
  ('Welche Android Box ist für IPTV am besten?', 'Eine zertifizierte Android-TV- oder Google-TV-Box wie Nvidia Shield, Homatics oder der Google TV Streamer. Sie laufen schnell und bekommen Updates.'),
 ],
},
'iptv-roku/index.html': {
 'sections': [
  ('IPTV on Roku TV und Smarters Pro auf Roku', [
   ('p', '<strong>IPTV on Roku TV</strong> bzw. <strong>IPTV Roku TV</strong> ist in Deutschland ein Sonderfall: Roku-Fernseher und -Sticks erlauben keine Android-Apps. <strong>IPTV Smarters Pro Roku</strong> gibt es nicht im Roku Channel Store. Was bleibt, sind einfache M3U-Player aus dem Store oder ein zweiter Stick am HDMI-Port.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTV Smarters Pro für Roku?', 'Nein. Auf Roku laufen nur Apps aus dem Roku Channel Store, Smarters ist dort nicht gelistet. Ein Fire TV Stick am zweiten HDMI-Port ist die einfachste Lösung.'),
 ],
},
'iptv-smart-tv/index.html': {
 'sections': [
  ('IP TV Smart TV: so finden Sie die passende App', [
   ('p', 'Ob Sie <strong>IP TV Smart TV</strong>, <strong>Smart IP TV</strong>, <strong>IPTV for Smart</strong> TV oder <strong>IPTV Smart Net</strong> suchen: Entscheidend ist das Betriebssystem Ihres Fernsehers.'),
   ('table', ['System', 'Hersteller', 'Empfohlene App'], [
    ['Tizen', 'Samsung', 'IBO Player, Smart IPTV'],
    ['webOS', 'LG', 'IBO Player, SS IPTV'],
    ['Google TV / Android TV', 'Sony, Philips, TCL, Xiaomi', 'TiviMate, Smarters Pro'],
    ['VIDAA', 'Hisense, Toshiba', 'Fire TV Stick'],
    ['Fire TV', 'Panasonic (neuere), Toshiba, Grundig', 'TiviMate, Smarters Pro'],
   ]),
   ('p', '„Smart Net" ist kein eigenes System, sondern ein Begriff aus Werbeanzeigen. Fragen Sie sich nur: Welches System hat mein Fernseher? Dann wählen Sie die App aus der Tabelle.'),
  ]),
 ],
 'faq': [
  ('Wie finde ich heraus, welches System mein Smart TV hat?', 'In den Einstellungen unter „Info" oder „Systeminformationen". Alternativ verrät es der Startbildschirm: Samsung nutzt Tizen, LG webOS, Sony und Philips meist Google TV.'),
 ],
},
'beste-iptv-box/index.html': {
 'sections': [
  ('IPTV Box Test, Preis und Amazon: was Sie zahlen sollten', [
   ('p', 'Für unseren <strong>IPTV Box Test</strong> zählen Geschwindigkeit, WLAN und Updates. Beim <strong>IPTV Box Price</strong> gilt: 40 bis 70 Euro für einen Fire TV Stick oder Google TV Streamer reichen für die meisten Haushalte. 150 bis 200 Euro lohnen sich nur für Technikfans, etwa für eine Nvidia Shield. Wenn Sie eine <strong>IPTV Box kaufen</strong> möchten, ist eine <strong>IPTV Box Amazon</strong>-Bestellung bei bekannten Marken unproblematisch – meiden Sie aber Boxen mit „vorinstallierten Sendern".'),
   ('p', '<strong>IPTV Box WiFi</strong>: Achten Sie auf Wi-Fi 6 oder besser. Ältere Boxen mit 2,4-GHz-WLAN sind der häufigste Grund für Ruckler bei 4K.'),
  ]),
 ],
 'faq': [
  ('Wie viel sollte eine gute IPTV Box kosten?', 'Für die meisten reichen 40 bis 70 Euro, etwa für einen Fire TV Stick 4K oder einen Google TV Streamer. Teurere Boxen lohnen sich für sehr große Senderlisten oder Gaming.'),
 ],
},
'iptv-set-top-box/index.html': {
 'sections': [
  ('IPTV for Receiver: 4K-Receiver im Test', [
   ('p', 'Wer <strong>IPTV for Receiver</strong> sucht, hat meist schon einen Satelliten- oder Kabelreceiver und möchte IPTV dazunehmen. Linux-Receiver mit Enigma2 können das, siehe <a href="/iptv-enigma2/">IPTV auf Enigma2-Receivern</a>. Für einen <strong>IPTV Receiver 4K</strong> ohne Satellit sind Android-Boxen und Formuler die einfachere Wahl.'),
   ('p', 'In unserem <strong>IPTV Receiver Test</strong> achten wir auf drei Punkte: Startet die App in unter fünf Sekunden? Lädt der Programmführer für 1.000+ Sender ohne Hänger? Läuft 4K über WLAN ruckelfrei? Ein Fire TV Stick 4K Max, eine Formuler Z11 und eine Nvidia Shield schaffen das.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV auf meinem Sat-Receiver nutzen?', 'Bei Linux-Receivern mit Enigma2 (z. B. GigaBlue, VU+, Dreambox) ja, mit Plugin oder Bouquet-Import. Bei einfachen Sat-Receivern ohne Netzwerkfunktionen nicht.'),
 ],
},
'mag-box-modelle/index.html': {
 'sections': [
  ('Infomir MAG 254, MAG 322 und neuere MAG IPTV Boxes', [
   ('p', 'Hersteller der MAG-Boxen ist Infomir. Viele Suchanfragen nennen ältere Modelle: Die <strong>Infomir MAG 254</strong> und die <strong>MAG 256</strong> gehören zur Generation um 2014–2016, die <strong>Infomir MAG 322</strong> bzw. <strong>MAG Box 322</strong> brachte H.265 und gilt bis heute als solide Full-HD-Box. Für 4K sind die 4xx- und 5xx-Modelle gedacht.'),
   ('p', 'Eine <strong>MAG IPTV</strong>-Box arbeitet mit einem Portal-Link statt einer App. Das macht <strong>MAG IPTV Boxes</strong> und jede <strong>MAG TV Box</strong> besonders einfach für ältere Nutzer: Einschalten, Senderliste erscheint wie beim Kabelfernsehen. Fragen Sie vor dem Kauf, ob Ihr Anbieter ein Portal für MAG bereitstellt.'),
  ]),
 ],
 'faq': [
  ('Lohnt sich eine gebrauchte MAG 254 noch?', 'Für Full HD in Einzelfällen, aber sie bekommt keine Updates mehr und unterstützt kein H.265. Für einen Neukauf empfehlen wir eine MAG 5xx oder einen Fire TV Stick.'),
 ],
},
'formuler-tv-box/index.html': {
 'sections': [
  ('Formuler Z7, Z8 Pro, Z10 Pro 4K, Z Nano und Z Neo', [
   ('p', 'Viele suchen gezielt nach einzelnen Modellen. Kurz eingeordnet:'),
   ('ul', ['<strong>Formuler Z7</strong> und <strong>Formuler Z7+</strong>: ältere 4K-Boxen, laufen noch, aber mit langsamerem Prozessor.',
           '<strong>Formuler Z8 Pro</strong>: Android 10, 4K, Dualband-WLAN – gute Mittelklasse.',
           '<strong>Formuler Z10 Pro 4K</strong>: schneller, mit mehr Speicher; ideal für große Senderlisten.',
           '<strong>Formuler Z Nano</strong> und <strong>Formuler Z Neo</strong> (Z+ Neo): kompakte Einstiegsmodelle, für Full HD ausreichend.']),
   ('p', 'Alle Modelle nutzen die vorinstallierte App MyTVOnline, die mit Xtream-Codes- und Portal-Zugängen arbeitet.'),
  ]),
 ],
 'faq': [
  ('Welche Formuler ist die beste für 4K?', 'Aktuell die Z10 Pro Max oder Z11 Pro Max. Die Z8 Pro reicht für 4K, wenn Sie keine sehr großen Senderlisten nutzen.'),
 ],
},
'tvip-s-box/index.html': {
 'sections': [
  ('TVIP 605: die S-Box v.605 als IPTV Box 4K', [
   ('p', 'Die <strong>TVIP S-Box 605</strong> (auch <strong>TVIP 605</strong>) ist eine kompakte <strong>IPTV Box 4K</strong> mit H.265 und HDR. Sie kann zwischen Linux-Modus (Portal) und Android TV umschalten. Das macht sie flexibler als eine MAG-Box, aber weniger verbreitet als Fire TV oder Formuler.'),
  ]),
 ],
 'faq': [
  ('Kann die TVIP 605 4K wiedergeben?', 'Ja, die S-Box v.605 unterstützt 4K mit HDR und H.265. Für stabile 4K-Wiedergabe empfehlen wir LAN.'),
 ],
},
'iptv-8k/index.html': {
 'sections': [
  ('IPTV8K und IPTV12K: was hinter den Namen steckt', [
   ('p', '<strong>IPTV8K</strong> und <strong>IPTV12K</strong> sind Marketingnamen von Anbietern, keine technischen Standards. 12K-Fernsehen gibt es nicht, und echtes 8K-Programm sendet in Deutschland niemand regelmäßig. Was zählt, ist stabiles 4K mit HDR – und das erreicht man mit einer guten Leitung und einem 4K-fähigen Gerät.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTV in 12K?', 'Nein. „IPTV12K" ist ein Anbietername, keine Auflösung. Selbst 8K-Sender gibt es in Deutschland nicht regelmäßig.'),
 ],
},
'iptv-geraete/index.html': {
 'sections': [
  ('IPTV Fernseher und Set-Top-Box IPTV: Kurzüberblick', [
   ('p', 'Ein <strong>IPTV Fernseher</strong> ist jeder Smart TV, auf dem sich eine IPTV-App installieren lässt – also praktisch jedes Gerät ab Baujahr 2017. Eine <strong>Set Top Box IPTV</strong> ist ein separates Kästchen am HDMI-Port, etwa eine MAG, Formuler oder Android-Box. Die Box lohnt sich, wenn der Fernseher alt ist oder die Lieblings-App nicht anbietet.'),
  ]),
 ],
 'faq': [
  ('Brauche ich eine Set-Top-Box, wenn ich einen Smart TV habe?', 'Nicht unbedingt. Wenn Ihr Fernseher die gewünschte App anbietet, reicht er. Eine Box oder ein Stick lohnt sich bei älteren Fernsehern oder für TiviMate.'),
 ],
},
'sky-q-iptv-box/index.html': {
 'sections': [
  ('Sky Q IPTV Box: Preis und UHD', [
   ('p', 'Die <strong>Sky Q IPTV Box</strong> wird von Sky gestellt und ist an ein Sky-Abo gebunden. Einen festen <strong>Sky Q IPTV Box Preis</strong> zum Kaufen gibt es daher nicht; Sky berechnet je nach Tarif eine Leihgebühr oder einen Einrichtungsbetrag. Die <strong>Sky Q IPTV Box UHD</strong>-Funktion setzt ein UHD-Paket voraus. Wer <strong>Sky IP TV</strong> nur über das Internet empfangen möchte, braucht bei Sky eine Leitung mit ausreichender Bandbreite.'),
  ]),
 ],
 'faq': [
  ('Kann ich die Sky Q IPTV Box ohne Sky-Abo nutzen?', 'Nein. Die Box ist an einen Sky-Vertrag gebunden. Für IPTV ohne Vertrag brauchen Sie ein eigenes Gerät wie einen Fire TV Stick.'),
 ],
},
}
