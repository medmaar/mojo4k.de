# Batch 2: info guides, receivers, ISP comparison, community pages.
from pages_batch1 import TRIAL, PRICES

PAGES = [
{
 'slug': 'iptv-lifetime', 'crumb': 'IPTV Lifetime', 'parent': 'iptv-anbieter-alternativen',
 'title': 'IPTV Lifetime Angebote 2026: Warum Vorsicht geboten ist',
 'desc': 'IPTV Lifetime für einmalig 50 bis 200 Euro? Warum lebenslange IPTV-Abos fast nie halten, welche Risiken es gibt und wie Sie stattdessen sparen.',
 'keywords': ['iptv lifetime', 'lifetime iptv', 'iptv lebenslang', 'iptv einmalzahlung', 'iptv deals', 'iptv sale', 'iptv promotions'],
 'badge': '⚠️ Ratgeber · Lifetime-Angebote',
 'h1': '<span class="hl">IPTV Lifetime</span> – warum „lebenslang" selten lange hält',
 'intro': 'Angebote wie „IPTV Lifetime für einmalig 99 €" klingen verlockend: einmal zahlen, nie wieder kümmern. In der Praxis enden solche Zugänge oft nach wenigen Monaten. Hier erklären wir, warum – und wie Sie trotzdem günstig fernsehen.',
 'sections': [
  ('Warum Lifetime-IPTV wirtschaftlich nicht aufgeht', [
   ('p', 'Ein IPTV-Dienst hat laufende Kosten: Server, Bandbreite, Personal für Support. Diese Kosten fallen jeden Monat an. Wer nur einmal Geld einnimmt, muss ständig neue Kunden gewinnen, um alte zu finanzieren. Hört der Zustrom auf, wird der Dienst eingestellt – und mit ihm Ihr „lebenslanger" Zugang.'),
   ('p', '„Lifetime" bezieht sich deshalb in der Praxis meist auf die Lebensdauer des Dienstes, nicht auf Ihre. Eine Rückerstattung gibt es dann in der Regel nicht.'),
  ]),
  ('Typische Warnsignale', [
   ('ul', ['Kein Impressum, nur ein Telegram- oder WhatsApp-Kontakt',
           'Zahlung nur per Krypto, Gutscheinkarte oder Freunde-Überweisung ohne Käuferschutz',
           'Unrealistische Versprechen: „alle Sender der Welt", „nie wieder Ruckler"',
           'Kein Test möglich oder Test nur gegen Gebühr',
           'Countdown-Timer und „nur noch heute"-Rabatte']),
  ]),
  ('Rechenbeispiel: Lifetime vs. Jahresabo', [
   ('table', ['Modell', 'Einmalig / jährlich', 'Risiko'], [
    ['„Lifetime" für 150 €', '150 € einmalig', 'Totalverlust, wenn Dienst nach 6–12 Monaten endet'],
    ['MOJO4K 1 Jahr, 1 Gerät', '€49 pro Jahr', 'Max. 1 Jahr im Voraus gezahlt'],
    ['MOJO4K 1 Monat, 1 Gerät', '€9 pro Monat', 'Monatlich kündbar'],
   ]),
   ('p', 'Selbst wenn ein Lifetime-Angebot drei Jahre hält, zahlen Sie mit einem Jahresabo kaum mehr – tragen aber nur das Risiko eines Jahres. Und Sie können jederzeit wechseln, wenn die Qualität nicht mehr passt.'),
  ]),
  ('So sparen Sie seriös', [
   ('ol', ['Erst <a href="/kostenlos-testen-de">24 Stunden kostenlos testen</a>.',
           'Dann einen Monat buchen und zur Primetime prüfen.',
           'Erst danach das <a href="/iptv-12-monate/">Jahresabo</a> wählen – es ist pro Monat am günstigsten.',
           'Mit der Familie ein Paket für mehrere Geräte teilen statt mehrere Einzelabos.']),
  ]),
 ],
 'faq': [
  ('Gibt es seriöse IPTV Lifetime Angebote?', 'Uns ist kein IPTV-Dienst bekannt, der „lebenslang" dauerhaft einlösen kann. Die laufenden Serverkosten machen Einmalzahlungen wirtschaftlich riskant.'),
  ('Was passiert, wenn der Lifetime-Anbieter verschwindet?', 'Ihr Zugang funktioniert nicht mehr, und eine Rückerstattung ist meist nicht möglich – besonders bei Zahlung ohne Käuferschutz.'),
  ('Bietet MOJO4K ein Lifetime-Abo an?', 'Nein. Die längste Laufzeit ist ein Jahr (ab €49). So zahlen Sie nie mehr als ein Jahr im Voraus.'),
  ('Wie bekomme ich IPTV am günstigsten?', 'Mit dem Jahresabo – pro Monat gerechnet etwa €4. Vorher kostenlos testen.'),
 ],
 'related': ['iptv-anbieter-alternativen', 'iptv-anbieter-vergleich', 'iptv-12-monate', 'iptv-abo', 'iptv-test', 'iptv-legal', 'iptv-aliexpress', 'preise'],
},
{
 'slug': 'iptv-aliexpress', 'crumb': 'IPTV Aliexpress & Alibaba', 'parent': 'iptv-anbieter-alternativen',
 'title': 'IPTV bei Aliexpress & Alibaba kaufen? Risiken 2026',
 'desc': 'IPTV bei Aliexpress, Alibaba oder Amazon-Marktplatz kaufen: Was hinter Billig-Abos und Boxen mit „vorinstallierten Sendern" steckt und was Sie stattdessen tun.',
 'keywords': ['iptv aliexpress', 'alibaba iptv', 'iptv amazon', 'iptv box amazon', 'iptv m3u kaufen', 'iptv shop', 'iptv account'],
 'badge': '🛒 Ratgeber · Marktplätze',
 'h1': '<span class="hl">IPTV bei Aliexpress</span> & Alibaba kaufen – lohnt sich das?',
 'intro': 'Auf Aliexpress, Alibaba und anderen Marktplätzen finden sich IPTV-Abos für wenige Euro und Boxen mit „20.000 Sendern inklusive". Wir erklären, was Sie dort tatsächlich kaufen und warum der vermeintliche Schnäppchenpreis oft teuer wird.',
 'sections': [
  ('Was dort verkauft wird', [
   ('table', ['Angebot', 'Was es wirklich ist', 'Risiko'], [
    ['„IPTV 12 Monate 5 €"', 'Zugang eines unbekannten Wiederverkäufers', 'Hoch: oft nach Wochen tot'],
    ['Android-Box mit Abo', 'Billig-Hardware + Zugang unbekannter Herkunft', 'Hoch: Hardware veraltet, Abo endet'],
    ['„M3U Liste lifetime"', 'Geteilte Liste vieler Käufer', 'Sehr hoch: überlastet, schnell gesperrt'],
    ['Neutrale Box ohne Abo', 'Nur Hardware', 'Gering, wenn Marke & Updates stimmen'],
   ]),
  ]),
  ('Die fünf häufigsten Probleme', [
   ('ol', ['<strong>Kein Ansprechpartner:</strong> Der Händler ist oft nur Vermittler und kennt den Server nicht.',
           '<strong>Keine deutsche Senderzusammenstellung:</strong> Listen sind für andere Märkte gebaut, EPG fehlt.',
           '<strong>Rückgabe schwierig:</strong> Digitale Güter sind von Rücknahmen meist ausgeschlossen.',
           '<strong>Sicherheitslücken:</strong> No-Name-Boxen bekommen selten Updates.',
           '<strong>Rechtliche Grauzone:</strong> Bei unklarer Herkunft wissen Sie nicht, was Sie da eigentlich nutzen – lesen Sie unseren Beitrag <a href="/iptv-legal/">Ist IPTV legal?</a>']),
  ]),
  ('Hardware: Wann ein Marktplatz-Kauf okay ist', [
   ('p', 'Die Box selbst kann man auch auf Marktplätzen kaufen – wenn es ein Markengerät ohne vorinstalliertes Abo ist. Achten Sie auf Google-Zertifizierung, aktuelle Android-Version, 2 GB RAM oder mehr und einen Händler mit EU-Lager (Garantie, Zoll). Für die meisten Haushalte ist ein Fire TV Stick aus dem regulären Handel die unkompliziertere Wahl. Kaufberatung: <a href="/beste-iptv-box/">Beste IPTV Box 2026</a>.'),
  ]),
  ('Die Alternative: Abo mit Test und deutschem Support', [
   ('p', 'Bei MOJO4K.DE testen Sie zuerst 24 Stunden kostenlos, bekommen Zugangsdaten für alle Apps (Xtream Codes und M3U) und einen Support, der Deutsch spricht. Preise ' + PRICES + ', Jahresabo €49.'),
  ]),
 ],
 'faq': [
  ('Kann man IPTV bei Aliexpress kaufen?', 'Angebote gibt es, aber meist von unbekannten Wiederverkäufern ohne Support. Viele Zugänge funktionieren nur kurz.'),
  ('Sind Boxen mit vorinstallierten Sendern empfehlenswert?', 'Nein. Kaufen Sie Hardware und IPTV-Abo getrennt, damit Sie bei Problemen den Anbieter wechseln können.'),
  ('Was ist an IPTV von Amazon-Marktplatzhändlern anders?', 'Für digitale IPTV-Zugänge gelten oft dieselben Probleme. Neutrale Hardware wie Fire TV Sticks ist dagegen unproblematisch.'),
  ('Wie teste ich einen IPTV-Anbieter sicher?', 'Mit einem kostenlosen Test ohne Zahlungsdaten und danach einem Monatsabo – erst dann länger buchen.'),
 ],
 'related': ['iptv-anbieter-alternativen', 'iptv-lifetime', 'beste-iptv-box', 'iptv-kaufen', 'iptv-legal', 'iptv-test', 'preise'],
},
{
 'slug': 'iptv-8k', 'crumb': 'IPTV 8K', 'parent': 'iptv-geraete',
 'title': 'IPTV 8K 2026: Gibt es 8K-Sender wirklich?',
 'desc': 'IPTV 8K – was steckt hinter 8K-Angeboten? Welche Inhalte es wirklich in 8K gibt, welche Bandbreite und Geräte nötig sind und warum 4K heute die Grenze ist.',
 'keywords': ['iptv 8k', 'iptv8k', 'iptv12k', '8k iptv', 'iptv 8k sender', 'iptv uhd'],
 'badge': '🖥️ Ratgeber · 8K',
 'h1': '<span class="hl">IPTV 8K</span> – Marketing oder echte Bildqualität?',
 'intro': 'Immer mehr IPTV-Angebote werben mit „8K" oder gar „12K". Ehrliche Antwort: Echte 8K-Fernsehsender gibt es in Deutschland nicht. Was dahintersteckt und welche Qualität Sie realistisch erwarten können, lesen Sie hier.',
 'sections': [
  ('Gibt es 8K-Fernsehen in Deutschland?', [
   ('p', 'Nein. Die öffentlich-rechtlichen und privaten Sender in Deutschland strahlen in HD aus, einzelne Sport- und Spielfilm-Angebote in 4K (UHD). Regelmäßige 8K-Übertragungen gibt es hierzulande nicht. 8K-Inhalte findet man vor allem als Demo-Videos und vereinzelt auf Videoplattformen.'),
   ('p', '„12K" ist im TV-Bereich reines Marketing – weder Fernseher noch Sender unterstützen eine solche Auflösung für den Heimgebrauch.'),
  ]),
  ('Was „8K IPTV" in der Praxis bedeutet', [
   ('ul', ['<strong>Hochskaliert:</strong> 4K- oder HD-Signal wird künstlich auf 8K gerechnet – das bringt keine echte Schärfe.',
           '<strong>Demo-Kanäle:</strong> Ein, zwei Endlosschleifen mit 8K-Naturaufnahmen.',
           '<strong>Werbebegriff:</strong> „8K" steht für „sehr gut", ohne technische Grundlage.']),
  ]),
  ('Was Sie für echtes 4K brauchen', [
   ('table', ['Baustein', 'Empfehlung'], [
    ['Internet', 'Mind. 25–50 Mbit/s pro 4K-Stream'],
    ['Verbindung', 'LAN oder Wi-Fi 6 in Routernähe'],
    ['Gerät', 'Fire TV Stick 4K Max, Google TV, Nvidia Shield, Apple TV 4K'],
    ['Codec', 'HEVC (H.265) muss unterstützt werden'],
    ['Fernseher', 'UHD-Panel, idealerweise mit HDR'],
   ]),
   ('p', 'Bei MOJO4K.DE gibt es eigene 4K-Kategorien. Mehr dazu: <a href="/iptv-4k/">IPTV 4K</a> und <a href="/iptv-premium-4k/">IPTV Premium 4K</a>.'),
  ]),
  ('Lohnt sich ein 8K-Fernseher für IPTV?', [
   ('p', 'Für IPTV nicht. Ein guter 4K-Fernseher mit hochwertiger Bildverarbeitung bringt sichtbar mehr als ein 8K-Panel, das HD-Fernsehen hochrechnen muss. Investieren Sie lieber in eine stabile Internetverbindung und ein schnelles Abspielgerät – siehe <a href="/beste-iptv-box/">Beste IPTV Box</a>.'),
  ]),
 ],
 'faq': [
  ('Gibt es IPTV in 8K?', 'Echte 8K-Sender gibt es in Deutschland nicht. „8K IPTV" bedeutet meist hochskalierte 4K- oder HD-Signale.'),
  ('Welche Internetgeschwindigkeit brauche ich für 8K?', 'Echte 8K-Streams bräuchten rund 80–100 Mbit/s. Für die realistisch verfügbaren 4K-Sender reichen 25–50 Mbit/s.'),
  ('Bietet MOJO4K 4K-Sender?', 'Ja, es gibt eigene 4K-Kategorien. Die genaue Auswahl sehen Sie im kostenlosen 24h-Test.'),
  ('Was ist IPTV 12K?', 'Ein Werbebegriff ohne technische Grundlage. Kein gängiger Fernseher oder Sender nutzt 12K.'),
 ],
 'related': ['iptv-4k', 'iptv-premium-4k', 'iptv-geraete', 'beste-iptv-box', 'iptv-glasfaser', 'iptv-ruckelt-buffering', 'preise'],
},
{
 'slug': 'iptv-server', 'crumb': 'IPTV Server', 'parent': 'was-ist-iptv',
 'title': 'IPTV Server erklärt: So funktioniert IPTV-Streaming',
 'desc': 'Was ist ein IPTV Server? Wie Xtream Codes, M3U und Portale funktionieren, warum Server-Qualität über Ruckler entscheidet und woran Sie gute Server erkennen.',
 'keywords': ['iptv server', 'iptv servers', 'iptv server url', 'xtream codes server', 'iptv portal url', 'iptv service', 'iptv ip'],
 'badge': '🖧 Technik · IPTV Server',
 'h1': '<span class="hl">IPTV Server</span> – was hinter Ihrem Stream steckt',
 'intro': 'Jeder IPTV-Stream kommt von einem Server: einem Rechenzentrum, das Sender empfängt, umwandelt und an Ihre App schickt. Wie gut dieser Server ist, entscheidet über Umschaltzeit, Bildqualität und Ruckler – viel mehr als die App.',
 'sections': [
  ('So kommt der Sender auf Ihren Fernseher', [
   ('steps', [
    ('Einspeisung', 'Der Anbieter empfängt das Programm und wandelt es in einen Internet-Stream um.'),
    ('Server & Load-Balancer', 'Mehrere Server verteilen die Zuschauer, damit keiner überlastet wird.'),
    ('Auslieferung', 'Ihr Stream geht über das Internet zu Ihrem Router – meist als MPEG-TS oder HLS (m3u8).'),
    ('Wiedergabe', 'Die App (TiviMate, Smarters, IBO …) puffert ein paar Sekunden und zeigt das Bild.'),
   ]),
  ]),
  ('Die drei Zugangsarten zum Server', [
   ('table', ['Zugang', 'Sieht so aus', 'Genutzt von'], [
    ['Xtream Codes API', 'Server-URL + Benutzername + Passwort', 'Smarters, TiviMate, IBO, XCIPTV'],
    ['M3U-Playlist', 'Ein langer Link oder eine .m3u-Datei', 'VLC, Kodi, Smart IPTV, fast alle Apps'],
    ['Stalker-Portal', 'Portal-URL + MAC-Adresse', 'MAG-Boxen, STB Emu, Formuler'],
   ]),
   ('p', 'Bei MOJO4K.DE bekommen Sie alle drei Varianten. Mehr zu M3U: <a href="/iptv-m3u/">IPTV M3U</a>, zu MAG: <a href="/iptv-mag-box/">MAG Box</a>.'),
  ]),
  ('Woran Sie einen guten IPTV Server erkennen', [
   ('cards', [
    ('Schnelles Umschalten', 'Unter 2 Sekunden von Sender zu Sender ist ein gutes Zeichen.'),
    ('Stabil zur Primetime', 'Samstag 15:30 und Champions-League-Abende sind der Härtetest.'),
    ('Ehrliche Verbindungen', 'Die Anzahl gleichzeitiger Geräte ist klar geregelt.'),
    ('Aktueller EPG', 'Programmführer stimmt und reicht mehrere Tage im Voraus.'),
   ]),
  ]),
  ('Probleme, die am Server liegen – und welche nicht', [
   ('table', ['Symptom', 'Wahrscheinliche Ursache'], [
    ['Alle Sender ruckeln, auch per LAN', 'Server überlastet'],
    ['Nur im WLAN ruckelt es', 'Heimnetz (<a href="/iptv-wlan-probleme/">WLAN-Tipps</a>)'],
    ['Einzelner Sender schwarz', 'Quelle des Senders gestört'],
    ['Abends schlechter als tagsüber', 'Server oder Internetanbieter überlastet (<a href="/iptv-vpn/">VPN kann helfen</a>)'],
   ]),
  ]),
 ],
 'faq': [
  ('Was ist ein IPTV Server?', 'Ein Rechner im Rechenzentrum, der TV-Sender als Internet-Streams an Ihre App ausliefert.'),
  ('Kann ich einen eigenen IPTV Server betreiben?', 'Technisch ja, etwa für eigene Kameras oder freie Sender. Für Pay-TV-Inhalte brauchen Sie aber die Rechte der Sender.'),
  ('Was ist die Server-URL bei Xtream Codes?', 'Die Adresse des Anbieter-Servers, meist mit http:// und einer Portnummer. Sie steht in Ihren Zugangsdaten.'),
  ('Warum ruckelt IPTV trotz schnellem Internet?', 'Entweder ist der Server überlastet oder das Heimnetz (WLAN) die Schwachstelle. Testen Sie per LAN-Kabel.'),
 ],
 'related': ['was-ist-iptv', 'iptv-m3u', 'xtream-iptv', 'iptv-line', 'iptv-ruckelt-buffering', 'iptv-vpn', 'iptv-epg', 'preise'],
},
{
 'slug': 'iptv-forum', 'crumb': 'IPTV Forum & Reddit', 'parent': 'iptv-anbieter-alternativen',
 'title': 'IPTV Forum & Reddit: Empfehlungen richtig einordnen',
 'desc': 'IPTV Forum, Reddit & Co.: Wo Nutzer über IPTV-Anbieter und Apps sprechen, wie Sie Empfehlungen richtig bewerten und welche Fragen Sie dort stellen sollten.',
 'keywords': ['iptv forum', 'iptvforum', 'iptv anbieter forum', 'iptv reddit', 'best iptv reddit', 'best iptv provider reddit', 'reddit best iptv', 'kodinerds iptv', 'szenebox iptv', 'tivimate reddit', 'iptv smarters reddit', 'iptv trustpilot'],
 'badge': '💬 Ratgeber · Foren & Reddit',
 'h1': '<span class="hl">IPTV Forum</span> & Reddit – Empfehlungen richtig lesen',
 'intro': 'Bevor sie ein IPTV-Abo kaufen, suchen viele nach „best IPTV Reddit" oder in deutschen Foren. Das ist klug – wenn man weiß, wie man die Beiträge einordnet. Hier zeigen wir, wo Nutzer diskutieren und wie Sie echte Erfahrungen von Werbung unterscheiden.',
 'sections': [
  ('Wo über IPTV gesprochen wird', [
   ('table', ['Plattform', 'Gut für', 'Hinweis'], [
    ['Reddit (z. B. r/IPTV, r/TiviMate)', 'App-Fragen, Technik', 'Anbieternamen sind in vielen Subreddits verboten'],
    ['Kodi-Foren (z. B. kodinerds, forum.kodi.tv)', 'Kodi, PVR, Enigma2', 'Fokus auf Technik, nicht auf Anbieter'],
    ['Allgemeine Technik-Foren', 'Router, Fire TV, Smart TV', 'Gute Hilfe bei Netzwerkproblemen'],
    ['Trustpilot & Bewertungsportale', 'Erster Eindruck', 'Bewertungen kritisch lesen'],
   ]),
  ]),
  ('So erkennen Sie gekaufte Empfehlungen', [
   ('ul', ['Neue Accounts, die nur einen einzigen Anbieter loben',
           'Direktnachrichten mit „Schreib mir, ich hab den besten Anbieter"',
           'Beiträge ohne konkrete Details (Gerät, App, Uhrzeit, Spiel)',
           'Viele 5-Sterne-Bewertungen in kurzer Zeit mit ähnlichem Wortlaut',
           'Druck: „Nur heute", „Letzte Plätze"']),
   ('p', 'Echte Erfahrungsberichte nennen Gerät, App, Internetanbieter und konkrete Situationen („Champions League am Dienstag lief stabil per LAN, im WLAN ruckelte es").'),
  ]),
  ('Die richtigen Fragen im Forum', [
   ('ol', ['„Läuft Anbieter X bei euch stabil zur Primetime?"',
           '„Welche App nutzt ihr auf Gerät Y?"',
           '„Wie schnell antwortet der Support?"',
           '„Wie lange gibt es den Anbieter schon?"',
           '„Gibt es einen kostenlosen Test?"']),
   ('p', 'Am Ende ersetzt kein Forum den eigenen Test. Deshalb bieten wir einen <a href="/kostenlos-testen-de">kostenlosen 24h-Test</a> an – testen Sie zu der Uhrzeit, zu der Sie wirklich schauen.'),
  ]),
  ('Häufige Forenthemen – unsere Anleitungen dazu', [
   ('ul', ['<a href="/tivimate-premium/">TiviMate Premium – lohnt es sich?</a>', '<a href="/bester-iptv-player/">Welcher IPTV Player ist der beste?</a>',
           '<a href="/iptv-ruckelt-buffering/">Warum ruckelt IPTV?</a>', '<a href="/iptv-legal/">Ist IPTV legal?</a>',
           '<a href="/iptv-vpn/">Brauche ich ein VPN?</a>', '<a href="/iptv-lifetime/">Lifetime-Angebote</a>']),
  ]),
 ],
 'faq': [
  ('Welcher IPTV-Anbieter wird auf Reddit empfohlen?', 'In vielen IPTV-Subreddits ist das Nennen von Anbietern verboten, um Spam zu verhindern. Empfehlungen per Direktnachricht sind oft Werbung.'),
  ('Gibt es ein deutsches IPTV Forum?', 'Ja, technische Fragen werden etwa in Kodi-Foren und allgemeinen Technik-Foren diskutiert. Anbieter-Empfehlungen sollten Sie dort kritisch lesen.'),
  ('Kann ich Trustpilot-Bewertungen zu IPTV trauen?', 'Teilweise. Achten Sie auf Details, Datum und Verteilung der Bewertungen. Ein eigener Test ist aussagekräftiger.'),
  ('Wie teste ich einen Anbieter am besten?', 'Zur Uhrzeit, zu der Sie normalerweise schauen, auf Ihrem eigenen Gerät, einmal per WLAN und einmal per LAN.'),
 ],
 'related': ['iptv-anbieter-alternativen', 'iptv-anbieter-vergleich', 'bester-iptv-anbieter', 'iptv-test', 'iptv-lifetime', 'bester-iptv-player', 'preise'],
},
{
 'slug': 'iptv-m3u8', 'crumb': 'IPTV M3U8', 'parent': 'iptv-m3u',
 'title': 'IPTV M3U8: Format, Unterschied zu M3U & Nutzung',
 'desc': 'IPTV M3U8 erklärt: Was eine m3u8-Liste ist, wie sie sich von M3U unterscheidet, wann HLS besser ist und wie Sie m3u8-Links in Apps und VLC nutzen.',
 'keywords': ['iptv m3u8', 'm3u8 iptv', 'iptv m3u8 list', 'm3u8 list', 'm3u8 liste', 'm.m3u iptv', 'mu3 iptv', 'm3u lista'],
 'badge': '📄 Technik · M3U8',
 'h1': '<span class="hl">IPTV M3U8</span> – was das Format bedeutet',
 'intro': 'M3U8 begegnet Ihnen bei IPTV an zwei Stellen: als Playlist-Datei im UTF-8-Format und als Stream-Format (HLS). Hier erklären wir beides verständlich – und wann Sie m3u8 statt ts wählen sollten.',
 'sections': [
  ('M3U vs. M3U8 – der Unterschied', [
   ('table', ['', 'M3U', 'M3U8'], [
    ['Zeichensatz', 'oft Latin-1', 'UTF-8 (Umlaute korrekt)'],
    ['Typischer Einsatz', 'Senderliste', 'Senderliste und HLS-Stream'],
    ['Umlaute in Sendernamen', 'manchmal kaputt (ä → Ã¤)', 'korrekt'],
    ['Unterstützt von', 'fast allen Apps', 'fast allen Apps'],
   ]),
   ('p', 'Kurz: Eine .m3u8-Datei ist eine M3U-Datei in UTF-8. Inhaltlich sind beide gleich aufgebaut – eine Liste mit Sendernamen und Stream-Adressen. Grundlagen in <a href="/iptv-m3u/">IPTV M3U erklärt</a>.'),
  ]),
  ('M3U8 als Stream-Format (HLS)', [
   ('p', 'Beim Streaming steht „m3u8" für HLS (HTTP Live Streaming). Der Sender wird in kurze Stücke geteilt, die App lädt sie nacheinander. Alternativ gibt es MPEG-TS (.ts), einen durchgehenden Datenstrom.'),
   ('table', ['Format', 'Vorteil', 'Nachteil', 'Ideal für'], [
    ['HLS (m3u8)', 'Robust bei schwankendem Netz, browserfreundlich', 'Etwas mehr Verzögerung', 'Handy, Browser, WLAN'],
    ['MPEG-TS (ts)', 'Schnelles Umschalten, wenig Verzögerung', 'Empfindlicher bei Paketverlust', 'TV-Box per LAN'],
   ]),
   ('p', 'In vielen Apps (TiviMate, Smarters) können Sie das Format umstellen. Ruckelt es im WLAN, probieren Sie HLS.'),
  ]),
  ('So sieht eine M3U8-Liste aus', [
   ('p', 'Jeder Sender besteht aus zwei Zeilen: einer Info-Zeile mit Name, Logo und Gruppe und der Stream-Adresse. Die Datei beginnt immer mit <strong>#EXTM3U</strong>; jede Info-Zeile mit <strong>#EXTINF</strong>, gefolgt von Attributen wie tvg-id (für den EPG), tvg-logo und group-title (Kategorie).'),
   ('p', '„M.m3u" oder „mu3" in Suchanfragen sind übrigens meist Tippfehler für m3u – gemeint ist dasselbe Format.'),
  ]),
  ('M3U8-Link nutzen', [
   ('ul', ['<a href="/iptv-vlc/">VLC</a>: Medien → Netzwerkstream öffnen → Link einfügen',
           '<a href="/smart-iptv-playlist-hochladen/">Smart IPTV</a>: Link auf der Upload-Seite eintragen',
           '<a href="/iptv-kodi/">Kodi</a>: PVR IPTV Simple Client → M3U-URL',
           '<a href="/tivimate/">TiviMate</a>: Playlist hinzufügen → M3U-Playlist']),
  ]),
 ],
 'faq': [
  ('Was ist der Unterschied zwischen M3U und M3U8?', 'M3U8 ist eine M3U-Datei im UTF-8-Zeichensatz. Dadurch werden Umlaute und Sonderzeichen korrekt angezeigt.'),
  ('Soll ich m3u8 oder ts als Stream-Format wählen?', 'Per LAN auf einer TV-Box ist ts meist schneller. Im WLAN, auf dem Handy oder im Browser ist m3u8 (HLS) robuster.'),
  ('Wo bekomme ich eine M3U8-Liste?', 'Von Ihrem IPTV-Anbieter. MOJO4K.DE liefert M3U-Links in beiden Varianten.'),
  ('Kann ich eine M3U8-Liste bearbeiten?', 'Ja, mit einem Texteditor, der UTF-8 speichert. Achten Sie darauf, die Zweizeilen-Struktur nicht zu zerstören.'),
 ],
 'related': ['iptv-m3u', 'iptv-liste', 'iptv-m3u-playlist-deutschland', 'iptv-playlist', 'iptv-vlc', 'iptv-epg', 'iptv-server', 'preise'],
},
{
 'slug': 'iptv-liste', 'crumb': 'IPTV Liste', 'parent': 'iptv-m3u',
 'title': 'IPTV Liste 2026: M3U-Senderliste richtig nutzen',
 'desc': 'IPTV Liste und M3U Liste erklärt: woher seriöse Senderlisten kommen, warum „kostenlose IPTV Listen" riskant sind und wie Sie Ihre Liste sortieren.',
 'keywords': ['iptv liste', 'iptv list', 'iptv m3u liste', 'iptv m3u list', 'beste m3u liste', 'iptv m3u 1 jahr', 'iptv m3u test', 'iptv checker', 'iptv checker online'],
 'badge': '📋 Ratgeber · IPTV Liste',
 'h1': '<span class="hl">IPTV Liste</span> – Senderliste finden, prüfen & sortieren',
 'intro': 'Eine IPTV Liste ist eine M3U-Datei mit allen Sendern Ihres Abos. Im Netz werden „kostenlose IPTV Listen" und „beste M3U Listen" geteilt – die meisten sind nach Stunden tot oder rechtlich problematisch. So kommen Sie an eine Liste, die dauerhaft funktioniert.',
 'sections': [
  ('Kostenlose IPTV Listen: Warum sie selten funktionieren', [
   ('ul', ['<strong>Überlastet:</strong> Tausende nutzen denselben Link – Ruckeln und Abbrüche sind die Folge.',
           '<strong>Schnell gesperrt:</strong> Geteilte Zugänge werden vom Server-Betreiber deaktiviert.',
           '<strong>Rechtlich heikel:</strong> Geteilte Pay-TV-Zugänge verletzen in der Regel Urheberrechte (<a href="/iptv-legal/">mehr dazu</a>).',
           '<strong>Sicherheitsrisiko:</strong> Downloads aus dubiosen Quellen enthalten manchmal Schadsoftware.']),
   ('p', 'Legal und kostenlos sind dagegen frei empfangbare Mediatheken und offizielle Live-Streams der Sender – diese finden Sie auf den Websites der Sender selbst.'),
  ]),
  ('Ihre persönliche IPTV Liste', [
   ('p', 'Mit einem Abo bekommen Sie einen persönlichen M3U-Link, der nur für Sie gilt. Bei MOJO4K.DE erhalten Sie Link und Xtream-Codes-Daten nach der Bestellung oder dem <a href="/kostenlos-testen-de">kostenlosen Test</a>. Der Link enthält Benutzername und Passwort – teilen Sie ihn deshalb nicht.'),
   ('table', ['Laufzeit', 'Preis (1 Gerät)'], [['1 Monat', '€9'], ['3 Monate', '€29'], ['6 Monate', '€39'], ['1 Jahr', '€49']]),
  ]),
  ('IPTV Liste prüfen (IPTV Checker)', [
   ('p', 'Ein „IPTV Checker" testet, ob die Links in einer Liste erreichbar sind. Für Ihre eigene Liste reicht meist der einfachste Test: Link in <a href="/iptv-vlc/">VLC</a> öffnen und ein paar Sender anklicken. Online-Checker, bei denen Sie Ihren Link auf fremde Websites hochladen, geben Ihre Zugangsdaten preis – nutzen Sie sie nicht mit Ihrem bezahlten Zugang.'),
  ]),
  ('Liste sortieren und aufräumen', [
   ('steps', [
    ('Favoriten statt Riesenliste', 'In TiviMate, Smarters oder IBO eine Favoriten-Gruppe mit den 20–30 Sendern anlegen, die Sie wirklich schauen.'),
    ('Kategorien ausblenden', 'Länder und Bereiche, die Sie nicht brauchen, in der App ausblenden – das macht auch langsame Geräte schneller.'),
    ('EPG zuordnen', 'Fehlt das Programm bei einzelnen Sendern, hilft der Artikel <a href="/iptv-epg-probleme/">EPG-Probleme lösen</a>.'),
   ]),
  ]),
 ],
 'faq': [
  ('Wo bekomme ich eine funktionierende IPTV Liste?', 'Von einem IPTV-Anbieter mit persönlichem Zugang. Öffentlich geteilte Listen funktionieren selten lange.'),
  ('Ist eine kostenlose M3U Liste legal?', 'Listen mit frei empfangbaren, offiziell gestreamten Sendern ja. Geteilte Pay-TV-Listen verletzen in der Regel Urheberrechte.'),
  ('Wie teste ich, ob meine IPTV Liste funktioniert?', 'Öffnen Sie den Link in VLC oder Ihrer IPTV-App und testen Sie einige Sender. Laden Sie ihn nicht auf unbekannte Online-Checker hoch.'),
  ('Was kostet eine IPTV M3U Liste für 1 Jahr?', 'Bei MOJO4K.DE €49 für ein Gerät, inklusive Xtream Codes und IBO-Player-Aktivierung.'),
 ],
 'related': ['iptv-m3u', 'iptv-m3u8', 'iptv-m3u-playlist-deutschland', 'iptv-playlist', 'iptv-playlist-deutsch', 'iptv-vlc', 'iptv-legal', 'preise'],
},
{
 'slug': 'iptv-jellyfin', 'crumb': 'IPTV Jellyfin', 'parent': 'iptv-apps',
 'title': 'IPTV Jellyfin: Live TV mit M3U & EPG einrichten',
 'desc': 'IPTV in Jellyfin einrichten: M3U-Tuner und XMLTV-Programmführer hinzufügen, Live TV aufnehmen und auf allen Geräten schauen. Anleitung für Jellyfin 10.x.',
 'keywords': ['jellyfin iptv', 'iptv jellyfin', 'jellyfin live tv', 'jellyfin m3u', 'iptv dvr', 'plex iptv'],
 'badge': '🟣 Jellyfin · Live TV',
 'h1': '<span class="hl">IPTV in Jellyfin</span> – Live TV & Aufnahmen einrichten',
 'intro': 'Jellyfin ist ein kostenloser, quelloffener Medienserver. Neben Filmen und Serien kann er Live-TV aus einer M3U-Liste einbinden, mit Programmführer und Aufnahmefunktion. So wird Ihr Heimserver zum eigenen IPTV-Receiver für die ganze Familie.',
 'sections': [
  ('Voraussetzungen', [
   ('ul', ['Ein laufender Jellyfin-Server (PC, NAS oder Raspberry Pi 4/5)',
           'Ihr M3U-Link und der EPG-Link (XMLTV) von MOJO4K.DE',
           'Für Aufnahmen: genug Speicherplatz (HD ≈ 2–3 GB pro Stunde)',
           'Für Transcoding auf schwachen Geräten: ein Server mit Hardware-Beschleunigung']),
  ]),
  ('Einrichtung Schritt für Schritt', [
   ('steps', [
    ('Live TV öffnen', 'Dashboard → Live TV (unter „Live TV" im Menü).'),
    ('Tuner hinzufügen', 'Bei „Tuner-Geräte" auf + klicken → Typ „M3U Tuner" → Ihren M3U-Link einfügen → Speichern.'),
    ('Programmführer hinzufügen', 'Bei „TV-Programmdaten-Anbieter" auf + → „XMLTV" → EPG-Link einfügen.'),
    ('Sender zuordnen', 'Jellyfin ordnet Sender per tvg-id zu. Fehlende Zuordnungen lassen sich manuell korrigieren.'),
    ('Aktualisieren', 'Unter „Geplante Aufgaben" den Guide aktualisieren. Danach erscheint der Bereich „Live TV".'),
   ]),
  ]),
  ('Tipps für große Senderlisten', [
   ('p', 'Eine komplette IPTV-Liste mit Zehntausenden Einträgen macht Jellyfin langsam. Besser: eine gefilterte Liste nur mit den Sendern, die Sie schauen. Bitten Sie unseren Support um eine kompakte Liste oder filtern Sie selbst mit einem M3U-Editor. Begrenzen Sie außerdem in den Tuner-Einstellungen die gleichzeitigen Streams auf die Anzahl Ihrer Paket-Verbindungen.'),
  ]),
  ('Aufnehmen mit Jellyfin (DVR)', [
   ('p', 'Im Programmführer eine Sendung auswählen → „Aufnehmen". Serienaufnahmen sind ebenfalls möglich. Aufnahmen landen im eingestellten Aufnahme-Ordner und erscheinen in der Mediathek. Beachten Sie: Aufnahmen sind nur für den privaten Gebrauch erlaubt.'),
   ('table', ['Lösung', 'Live TV', 'Aufnahme', 'Kosten'], [
    ['Jellyfin', '✅', '✅', 'Kostenlos'],
    ['<a href="/iptv-plex/">Plex</a>', '✅', '✅ mit Plex Pass', 'Teilweise kostenpflichtig'],
    ['<a href="/iptv-kodi/">Kodi</a>', '✅', '✅ mit Backend', 'Kostenlos'],
    ['<a href="/tivimate/">TiviMate</a>', '✅', '✅ Premium', 'Premium kostenpflichtig'],
   ]),
  ]),
 ],
 'faq': [
  ('Kann Jellyfin IPTV abspielen?', 'Ja, über einen M3U-Tuner im Bereich Live TV. Mit XMLTV gibt es auch einen Programmführer.'),
  ('Kann ich mit Jellyfin IPTV aufnehmen?', 'Ja, Jellyfin hat eine eingebaute DVR-Funktion für Einzel- und Serienaufnahmen.'),
  ('Ist Jellyfin kostenlos?', 'Ja, Jellyfin ist vollständig kostenlos und Open Source.'),
  ('Jellyfin oder Plex für IPTV?', 'Jellyfin bietet Live TV und Aufnahmen ohne Abo. Plex ist bequemer, verlangt für DVR aber den Plex Pass.'),
 ],
 'related': ['iptv-apps', 'iptv-plex', 'iptv-kodi', 'iptv-m3u', 'iptv-epg', 'iptv-aufnehmen', 'iptv-raspberry-pi', 'preise'],
},
{
 'slug': 'iptv-aufnehmen', 'crumb': 'IPTV aufnehmen', 'parent': 'iptv-apps',
 'title': 'IPTV aufnehmen: Sendungen speichern mit App & DVR',
 'desc': 'IPTV aufnehmen: Mit TiviMate, Kodi, Jellyfin, VLC & Formuler Sendungen speichern. Was Sie brauchen, wo Aufnahmen landen und was rechtlich erlaubt ist.',
 'keywords': ['iptv aufnehmen', 'iptv dvr', 'iptv aufnahme', 'iptv recording', 'iptv catchup', 'iptv vod', 'iptv series'],
 'badge': '⏺️ Ratgeber · Aufnehmen',
 'h1': '<span class="hl">IPTV aufnehmen</span> – so speichern Sie Sendungen',
 'intro': 'Wer früher mit dem Festplattenreceiver aufgenommen hat, kann das auch mit IPTV – mit der richtigen App. Oft ist eine Aufnahme aber gar nicht nötig: Catch-Up und die VOD-Bibliothek decken vieles ab.',
 'sections': [
  ('Erst prüfen: Brauche ich überhaupt eine Aufnahme?', [
   ('table', ['Funktion', 'Was es ist', 'Wann sinnvoll'], [
    ['<a href="/iptv-catchup/">Catch-Up</a>', 'Sendungen der letzten Tage nachträglich abrufen', 'Spiel verpasst, Serie gestern'],
    ['VOD', 'Filme & Serien auf Abruf', 'Kein festes Sendedatum nötig'],
    ['Aufnahme (DVR)', 'Sendung als Datei speichern', 'Dauerhaft behalten, offline schauen'],
   ]),
  ]),
  ('Apps mit Aufnahmefunktion', [
   ('table', ['App / Gerät', 'Aufnahme', 'Speicherort'], [
    ['<a href="/tivimate/">TiviMate</a> (Premium)', 'Einzeln & geplant', 'Interner Speicher, USB, Netzwerk'],
    ['<a href="/iptv-formuler/">Formuler</a> (MyTVOnline)', 'Einzeln & geplant', 'USB-Stick / Festplatte'],
    ['<a href="/iptv-kodi/">Kodi</a> + Backend', 'Geplant, Serien', 'Server-Festplatte'],
    ['<a href="/iptv-jellyfin/">Jellyfin</a>', 'Geplant, Serien', 'Server-Festplatte'],
    ['<a href="/iptv-vlc/">VLC</a>', 'Manuell', 'PC'],
    ['Smarters Pro / IBO', 'Nein bzw. eingeschränkt', '–'],
   ]),
  ]),
  ('Aufnehmen mit TiviMate – Schritt für Schritt', [
   ('steps', [
    ('Speicherort festlegen', 'Einstellungen → Aufnahme → Ordner wählen. Für Fire TV Sticks empfiehlt sich ein USB-Stick per OTG-Adapter oder ein Netzwerkordner.'),
    ('Sendung im TV-Guide wählen', 'Im Programmführer auf die Sendung → „Aufnehmen".'),
    ('Puffer einstellen', 'Vor- und Nachlauf (z. B. 2 und 10 Minuten) einstellen – Sport dauert oft länger.'),
    ('Aufnahme ansehen', 'Menü → Aufnahmen.'),
   ]),
   ('p', 'Wichtig: Eine Aufnahme belegt eine Verbindung. Wer gleichzeitig aufnehmen und etwas anderes schauen will, braucht ein Paket mit mindestens zwei Geräten.'),
  ]),
  ('Was ist rechtlich erlaubt?', [
   ('p', 'In Deutschland dürfen Sie Sendungen für den privaten Gebrauch aufzeichnen (Privatkopie), sofern die Quelle nicht offensichtlich rechtswidrig ist. Weitergeben, hochladen oder öffentlich vorführen ist nicht erlaubt. Mehr: <a href="/iptv-legal/">Ist IPTV legal?</a>'),
  ]),
 ],
 'faq': [
  ('Kann man IPTV aufnehmen?', 'Ja, mit Apps wie TiviMate Premium, Kodi, Jellyfin oder Receivern wie Formuler.'),
  ('Kann ich auf dem Fire TV Stick aufnehmen?', 'Ja, mit TiviMate Premium. Wegen des kleinen Speichers empfiehlt sich ein USB-Stick per OTG-Adapter oder ein Netzwerkordner.'),
  ('Brauche ich für Aufnahmen mehrere Verbindungen?', 'Nur, wenn Sie gleichzeitig aufnehmen und etwas anderes schauen wollen.'),
  ('Kann Smarters Pro aufnehmen?', 'Smarters Pro hat keine vollwertige Aufnahmefunktion. Dafür eignen sich TiviMate, Kodi oder Jellyfin.'),
 ],
 'related': ['iptv-catchup', 'tivimate-premium', 'iptv-jellyfin', 'iptv-kodi', 'iptv-formuler', 'iptv-apps', 'preise'],
},
{
 'slug': 'iptv-roku', 'crumb': 'IPTV Roku', 'parent': 'iptv-geraete',
 'title': 'IPTV auf Roku TV: Was geht & bessere Alternativen',
 'desc': 'IPTV auf Roku und Roku TV: warum TiviMate und Smarters dort fehlen, welche Wege funktionieren und welches Gerät für IPTV in Deutschland besser geeignet ist.',
 'keywords': ['iptv roku', 'iptv roku tv', 'iptv on roku tv', 'iptv smarters pro roku', 'roku iptv'],
 'badge': '🟪 Roku',
 'h1': '<span class="hl">IPTV auf Roku</span> – geht das?',
 'intro': 'Roku-Geräte und Fernseher mit Roku TV sind für Streamingdienste gebaut, nicht für freie IPTV-Apps. Die bekannten Player TiviMate, Smarters Pro oder IBO Player gibt es dort nicht im Store. Es gibt Umwege – aber meist ist ein anderes Gerät die bessere Wahl.',
 'sections': [
  ('Warum IPTV auf Roku schwierig ist', [
   ('p', 'Roku lässt nur Apps aus dem eigenen Channel Store zu. Android-Apps lassen sich nicht installieren, und Roku entfernt IPTV-Player regelmäßig aus dem Store. Deshalb finden Sie dort weder TiviMate noch Smarters Pro.'),
  ]),
  ('Was trotzdem funktioniert', [
   ('table', ['Weg', 'Wie', 'Bewertung'], [
    ['M3U-Player aus dem Roku-Store', 'Nach „M3U" suchen, Link eintragen', 'Wechselnde Verfügbarkeit, oft ohne EPG'],
    ['Bildschirm spiegeln', 'Vom Android-Handy auf Roku spiegeln', 'Akku- und Qualitätsverlust'],
    ['Streaming-Stick am zweiten HDMI', 'Fire TV Stick an den Roku TV', 'Beste Lösung'],
   ]),
  ]),
  ('Unsere Empfehlung', [
   ('p', 'Wer einen Roku TV besitzt, steckt am besten einen Fire TV Stick oder Google TV Streamer an einen freien HDMI-Port. Dort laufen <a href="/tivimate-fire-tv-stick/">TiviMate</a> und <a href="/iptv-smarters-pro-fire-tv-stick/">Smarters Pro</a> ohne Einschränkungen. In Deutschland sind Fire TV und Google TV ohnehin weiter verbreitet und bekommen mehr App-Support.'),
   ('p', 'Kaufberatung: <a href="/beste-iptv-box/">Beste IPTV Box 2026</a> und <a href="/iptv-stick-de">IPTV Stick</a>.'),
  ]),
  ('Checkliste vor dem Kauf eines neuen Fernsehers', [
   ('ul', ['Google TV (Sony, Philips, TCL, Hisense-Modelle) – alle Android-Apps inkl. TiviMate',
           'Samsung Tizen / LG webOS – IBO Player, Smart IPTV',
           'Roku TV / Fire TV Edition – nur mit Einschränkungen bzw. per Sideload (Fire TV)',
           'Unabhängig vom TV: Ein Stick für 30–70 € löst fast jedes App-Problem.']),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV Smarters Pro auf Roku installieren?', 'Nein. Smarters Pro ist im Roku-Store nicht verfügbar, und Roku erlaubt keine Android-Apps.'),
  ('Gibt es TiviMate für Roku?', 'Nein. TiviMate gibt es nur für Android TV, Google TV und Fire TV.'),
  ('Wie schaue ich IPTV am Roku TV?', 'Am einfachsten mit einem Fire TV Stick oder Google TV Streamer an einem freien HDMI-Anschluss.'),
  ('Funktioniert MOJO4K auf Roku?', 'Nur über einzelne M3U-Player aus dem Roku-Store, deren Verfügbarkeit wechselt. Wir empfehlen einen Stick.'),
 ],
 'related': ['iptv-geraete', 'beste-iptv-box', 'iptv-stick', 'tivimate-fire-tv-stick', 'iptv-smarters-pro-fire-tv-stick', 'iptv-smart-tv', 'preise'],
},
{
 'slug': 'tv-und-internet', 'crumb': 'TV und Internet', 'parent': 'iptv-deutschland',
 'title': 'TV und Internet: Telekom, Vodafone, 1&1, O2 vs. IPTV',
 'desc': 'Fernsehen über Internet in Deutschland: MagentaTV, GigaTV, 1&1 TV und O2 TV im Überblick – und wann ein unabhängiges IPTV-Abo die flexiblere Lösung ist.',
 'keywords': ['television and internet', 'tv und internet', 'fernsehen über telekom', '1&1 tv pakete', 'o2 iptv', 'telekom ip tv', 'vodafone ip tv', 'vodafone iptv', 'magenta iptv', 'magenta tv iptv'],
 'badge': '🌐 Vergleich · TV über Internet',
 'h1': '<span class="hl">TV und Internet</span> – die Anbieter im Überblick',
 'intro': 'Fast jeder Internetanbieter in Deutschland verkauft inzwischen auch Fernsehen: Telekom mit MagentaTV, Vodafone mit GigaTV, 1&1 mit eigenen TV-Paketen, O2 mit O2 TV. Wir zeigen, wie diese Angebote funktionieren und wann ein unabhängiges IPTV-Abo besser passt.',
 'sections': [
  ('Die TV-Angebote der Internetanbieter', [
   ('table', ['Anbieter', 'TV-Produkt', 'Empfang', 'Bindung'], [
    ['Telekom', 'MagentaTV', 'IPTV über Telekom-Anschluss bzw. App', 'An Telekom-Tarif oder MagentaTV-Abo'],
    ['Vodafone', 'GigaTV', 'Kabel bzw. App', 'An Vodafone-Tarif'],
    ['1&1', '1&1 TV-Pakete', 'App / Receiver über Internet', 'An 1&1-Tarif'],
    ['O2', 'O2 TV', 'App (in Kooperation mit waipu.tv)', 'Zubuchoption'],
   ]),
   ('p', 'Preise und Paketinhalte ändern sich häufig – die aktuellen Konditionen finden Sie direkt bei den Anbietern. Mehr zu den Einzelheiten: <a href="/iptv-telekom/">IPTV und Telekom</a>, <a href="/iptv-magenta-tv/">MagentaTV vs. IPTV</a>, <a href="/iptv-vodafone-internet/">IPTV mit Vodafone-Internet</a>.'),
  ]),
  ('Fernsehen über Telekom: So funktioniert es', [
   ('p', 'Die Telekom liefert MagentaTV über den eigenen Anschluss als IPTV aus – mit reservierter Bandbreite im Netz der Telekom. Das macht das Bild sehr stabil. MagentaTV gibt es außerdem als App für Kunden anderer Internetanbieter. Wichtig: Das ist ein geschlossenes System; Sie nutzen die Telekom-Apps oder den Telekom-Receiver.'),
  ]),
  ('Wann ein unabhängiges IPTV-Abo besser passt', [
   ('cards', [
    ('Anbieter wechseln', 'Ihr TV hängt nicht am Internetvertrag. Sie können Ihren DSL- oder Glasfaser-Anbieter frei wechseln.'),
    ('Alle Geräte', 'Fire TV, Smart TV, Handy, PC – mit den Apps Ihrer Wahl.'),
    ('Monatlich kündbar', 'Keine 24-Monats-Bindung, Test vorab.'),
    ('Internationale Sender', 'Viele Länderkategorien in einem Paket.'),
   ]),
   ('p', 'Ein IPTV-Abo wie MOJO4K.DE läuft über jeden Anschluss – Telekom, Vodafone, 1&1, O2 oder Glasfaser von Stadtwerken. Für HD reichen 16 Mbit/s, für 4K 25–50 Mbit/s pro Gerät. Mehr: <a href="/iptv-glasfaser/">IPTV mit Glasfaser</a>.'),
  ]),
  ('Kombination: Internet vom Anbieter, TV von uns', [
   ('p', 'Viele Kunden behalten ihren Internetvertrag und buchen das Fernsehen separat. So sparen Sie sich den teuren Receiver-Mietvertrag und schauen auf Geräten, die Sie schon haben. ' + TRIAL.capitalize() + ' und vergleichen Sie selbst.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV mit jedem Internetanbieter nutzen?', 'Ja. Ein unabhängiges IPTV-Abo funktioniert mit Telekom, Vodafone, 1&1, O2 und allen anderen Anschlüssen.'),
  ('Was ist der Unterschied zwischen MagentaTV und IPTV?', 'MagentaTV ist das IPTV-Angebot der Telekom, gebunden an Telekom-Apps und -Receiver. Unabhängige IPTV-Abos laufen in frei wählbaren Apps.'),
  ('Brauche ich für TV über Internet einen Receiver?', 'Nein. Smart-TV-Apps oder ein Streaming-Stick reichen in der Regel aus.'),
  ('Welche Internetgeschwindigkeit brauche ich?', 'Rund 16 Mbit/s für HD und 25–50 Mbit/s für 4K pro gleichzeitig genutztem Gerät.'),
  ('Was bietet O2 beim Fernsehen?', 'O2 TV ist eine App-Lösung in Kooperation mit waipu.tv. Details und Preise nennt O2.'),
 ],
 'related': ['iptv-telekom', 'iptv-magenta-tv', 'iptv-vodafone-internet', 'iptv-glasfaser', 'iptv-vs-kabel', 'iptv-vs-satellit', 'iptv-deutschland', 'preise'],
},
{
 'slug': 'mag-box-modelle', 'crumb': 'MAG Box Modelle', 'parent': 'iptv-geraete',
 'title': 'MAG Box Modelle 2026: MAG 254, 322, 424, 524 im Vergleich',
 'desc': 'Infomir MAG Box Modelle im Vergleich: MAG 250, 254, 256, 322, 410, 420, 424, 524 – welche Box 4K und HEVC kann, welche veraltet ist und wie Sie einrichten.',
 'keywords': ['mag box', 'mag iptv', 'infomir mag', 'mag 254', 'mag 322', 'mag 424', 'mag 524', 'mag 250', 'mag 256', 'mag 410', 'mag 420', 'infomir mag 322', 'infomir mag 254', 'mag tv box', 'mag iptv boxes', 'mag box 322'],
 'badge': '🗄️ Infomir MAG · Modellvergleich',
 'h1': '<span class="hl">MAG Box Modelle</span> – welche MAG passt 2026?',
 'intro': 'MAG-Boxen von Infomir sind die Klassiker unter den IPTV-Receivern: einschalten, Sender wählen, fertig. Es gibt viele Generationen – von der veralteten MAG 250 bis zu aktuellen 4K-Modellen. Diese Übersicht hilft bei Kauf und Einrichtung.',
 'sections': [
  ('Die Modelle im Überblick', [
   ('table', ['Modell', 'Auflösung', 'HEVC (H.265)', 'Einschätzung 2026'], [
    ['MAG 250', 'Full HD', '❌', 'Veraltet – nicht mehr kaufen'],
    ['MAG 254 / 256', 'Full HD', '❌', 'Veraltet, für alte HD-Streams'],
    ['MAG 322', 'Full HD', '✅', 'Solide Einsteiger-Box'],
    ['MAG 410', '4K', '✅', 'Android-basiert'],
    ['MAG 420 / 424', '4K', '✅', 'Gute 4K-Linux-Boxen'],
    ['MAG 524', '4K', '✅', 'Aktuelles Linux-Modell, Wi-Fi'],
   ]),
   ('p', 'Faustregel: Für 4K-Sender und moderne Streams muss die Box HEVC können. Modelle ohne HEVC (250, 254, 256) zeigen viele aktuelle Sender nicht oder nur ruckelnd an.'),
  ]),
  ('MAG Box mit MOJO4K einrichten', [
   ('steps', [
    ('MAC-Adresse ablesen', 'Auf dem Aufkleber unter der Box oder unter Einstellungen → Geräteinfo (beginnt mit 00:1A:79).'),
    ('MAC an uns senden', 'Über das <a href="/kontakt-de">Kontaktformular</a> – wir schalten die Box frei und senden die Portal-URL.'),
    ('Portal eintragen', 'Einstellungen → Server → Portale → Portal 1 Name: MOJO4K, Portal 1 URL: die URL von uns.'),
    ('Neustarten', 'Box neu starten – sie lädt direkt das Portal mit Sendern, Filmen und Serien.'),
   ]),
  ]),
  ('Vorteile & Nachteile von MAG-Boxen', [
   ('table', ['Vorteile', 'Nachteile'], [
    ['Sehr einfache Bedienung wie Kabel-TV', 'Wenig App-Auswahl'],
    ['Fernbedienung mit Zifferntasten', 'Linux-Modelle ohne Google Play'],
    ['Schneller Start ins Portal', 'Ältere Modelle ohne HEVC'],
    ['Ideal für Senioren', 'Weniger Funktionen als TiviMate'],
   ]),
   ('p', 'Wer mehr Apps möchte, schaut sich <a href="/formuler-tv-box/">Formuler-Boxen</a> oder <a href="/beste-iptv-box/">Android-Boxen</a> an. Eine MAG am Smartphone nachbilden geht mit <a href="/stb-emu/">STB Emu</a>.'),
  ]),
 ],
 'faq': [
  ('Welche MAG Box ist die beste?', 'Für 4K die MAG 524 oder MAG 424. Für reines HD reicht die MAG 322. MAG 250/254/256 sind veraltet.'),
  ('Funktioniert MOJO4K auf der MAG 254?', 'Grundsätzlich ja, aber ohne HEVC laufen manche moderne Streams nicht. Wir empfehlen ein neueres Modell.'),
  ('Wo finde ich die MAC-Adresse der MAG Box?', 'Auf dem Aufkleber unter dem Gerät oder in den Einstellungen unter Geräteinfo.'),
  ('Kann ich auf der MAG Box Apps installieren?', 'Linux-MAGs haben nur wenige eingebaute Apps. Android-basierte Modelle wie die MAG 410 bieten mehr.'),
 ],
 'related': ['iptv-mag-box', 'iptv-receiver-deutschland', 'iptv-set-top-box', 'formuler-tv-box', 'iptv-box-formuler-mag', 'stb-emu', 'iptv-geraete', 'preise'],
},
{
 'slug': 'formuler-tv-box', 'crumb': 'Formuler TV Box', 'parent': 'iptv-geraete',
 'title': 'Formuler TV Box 2026: Z-Modelle & MyTVOnline erklärt',
 'desc': 'Formuler TV Box Modelle im Überblick: Z+, Z7+, Z8, Z8 Pro, Z10 Pro, Z10 Pro Max, Z11 Pro Max, Z Nano & Z Neo – mit MyTVOnline-Einrichtung für MOJO4K.',
 'keywords': ['formuler tv box', 'formuler iptv box', 'formuler z10 pro 4k', 'formuler z10 pro max 4k', 'formuler z8', 'formuler z8 pro', 'formuler z7', 'formuler z7+', 'formuler z+', 'formuler z nano', 'formuler z neo'],
 'badge': '📦 Formuler · Z-Serie',
 'h1': '<span class="hl">Formuler TV Box</span> – Modelle & Einrichtung',
 'intro': 'Formuler-Boxen verbinden Android TV mit einer eigenen IPTV-Oberfläche namens MyTVOnline. Dazu kommt eine Fernbedienung mit Zifferntasten – das fühlt sich an wie ein klassischer Receiver, bietet aber die App-Vielfalt von Android.',
 'sections': [
  ('Die Formuler Z-Modelle im Überblick', [
   ('table', ['Generation', 'Modelle', 'Einschätzung'], [
    ['Ältere Modelle', 'Z+, Z7+, Z8', 'Für HD okay, Software teils veraltet'],
    ['Pro-Generation', 'Z8 Pro, Z10 Pro', '4K, flüssige Bedienung'],
    ['Aktuelle Spitzenmodelle', 'Z10 Pro Max, Z11 Pro Max', '4K, viel Speicher, schnellstes MyTVOnline'],
    ['Kompakt', 'Z Nano, Z Neo', 'Günstig, einfacher, für Zweitgeräte'],
   ]),
   ('p', 'Die genauen technischen Daten unterscheiden sich je nach Revision. Achten Sie beim Kauf auf die Android-Version und darauf, dass MyTVOnline in der aktuellen Version (MyTVOnline 3) unterstützt wird.'),
  ]),
  ('MyTVOnline mit MOJO4K einrichten', [
   ('steps', [
    ('MyTVOnline öffnen', 'Auf dem Startbildschirm die App MyTVOnline 3 starten.'),
    ('Portal hinzufügen', '„Add Portal" → Verbindungsart „Xtream Codes" (oder Portal-URL, falls Sie MAC-Freischaltung wünschen).'),
    ('Daten eintragen', 'Name: MOJO4K, Server-URL, Benutzername und Passwort eintragen.'),
    ('Laden lassen', 'Sender, EPG, Filme und Serien werden geladen. Danach mit „OK" und den Zifferntasten umschalten.'),
   ]),
  ]),
  ('Was Formuler besser macht – und was nicht', [
   ('table', ['Stärken', 'Schwächen'], [
    ['Zifferntasten wie beim Kabelreceiver', 'Teurer als ein Fire TV Stick'],
    ['MyTVOnline mit Aufnahme auf USB', 'Nicht jedes Modell Google-zertifiziert'],
    ['Zusätzlich TiviMate & Smarters möglich', 'Updates je nach Modell unterschiedlich'],
    ['LAN-Anschluss', 'Ältere Modelle langsam bei großen Listen'],
   ]),
   ('p', 'Vergleich mit der Konkurrenz: <a href="/iptv-box-formuler-mag/">Formuler vs. MAG</a> und <a href="/mag-box-modelle/">MAG Box Modelle</a>.'),
  ]),
 ],
 'faq': [
  ('Welche Formuler Box ist die beste?', 'Aktuell die Z11 Pro Max bzw. Z10 Pro Max: schnell, 4K-fähig und mit der neuesten MyTVOnline-Version.'),
  ('Funktioniert MOJO4K mit Formuler?', 'Ja, per Xtream Codes in MyTVOnline oder in jeder Android-App wie TiviMate.'),
  ('Kann ich mit Formuler aufnehmen?', 'Ja, MyTVOnline kann auf USB-Speicher aufnehmen.'),
  ('Lohnt sich ein altes Modell wie Z7+ noch?', 'Für HD-Sender ja, für 4K und große Senderlisten empfehlen wir ein aktuelles Modell.'),
 ],
 'related': ['iptv-formuler', 'iptv-box-formuler-mag', 'mag-box-modelle', 'iptv-set-top-box', 'beste-iptv-box', 'iptv-aufnehmen', 'iptv-geraete', 'preise'],
},
{
 'slug': 'tvip-s-box', 'crumb': 'TVIP S-Box', 'parent': 'iptv-geraete',
 'title': 'TVIP S-Box v.605: IPTV Box mit Linux & Android',
 'desc': 'TVIP S-Box v.605 für IPTV: Was die 4K-Box mit Linux- und Android-Modus kann, wie Sie MOJO4K per Portal oder M3U einrichten und für wen sie sich lohnt.',
 'keywords': ['tvip s box', 'tvip 605', 'tvip s box 605', 'tvip s box v 605', 'tvip iptv', 'iptv box 4k'],
 'badge': '📦 TVIP S-Box',
 'h1': '<span class="hl">TVIP S-Box</span> – die IPTV-Box mit zwei Systemen',
 'intro': 'Die TVIP S-Box v.605 ist eine kompakte 4K-Box, die speziell für IPTV gebaut wurde. Ihre Besonderheit: Sie kann im schnellen Linux-Modus (ähnlich einer MAG) oder im Android-Modus mit Apps laufen.',
 'sections': [
  ('Was die TVIP S-Box auszeichnet', [
   ('cards', [
    ('Zwei Betriebssysteme', 'Linux für einfache Portal-Bedienung, Android für Apps wie TiviMate oder Smarters.'),
    ('4K & HEVC', 'Moderne Codecs für 4K-Sender.'),
    ('Kompakt', 'Kleines Gehäuse, lässt sich hinter dem Fernseher verstecken.'),
    ('Portal & M3U', 'Unterstützt Stalker-Portale (MAC) und M3U-Listen.'),
   ]),
   ('p', 'Ausstattungsdetails (WLAN-Standard, Speicher) unterscheiden sich je nach Revision – prüfen Sie das Datenblatt des Händlers.'),
  ]),
  ('Einrichtung im Linux-Modus (Portal)', [
   ('steps', [
    ('MAC-Adresse notieren', 'Steht auf der Unterseite bzw. in den Einstellungen.'),
    ('Freischaltung anfragen', 'MAC über das <a href="/kontakt-de">Kontaktformular</a> an MOJO4K senden; Sie erhalten die Portal-URL.'),
    ('Portal eintragen', 'Einstellungen → TV-Anbieter → Stalker/Portal → URL eintragen.'),
    ('Neustart', 'Die Box lädt das Portal mit allen Sendern.'),
   ]),
  ]),
  ('Einrichtung im Android-Modus (App)', [
   ('p', 'Im Android-Modus installieren Sie eine App Ihrer Wahl – wir empfehlen <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro-android/">Smarters Pro</a> – und melden sich mit Ihren Xtream Codes an. Das ist die richtige Wahl, wenn Sie Aufnahmen, mehrere Playlists oder zusätzliche Streaming-Apps nutzen wollen.'),
  ]),
  ('TVIP vs. MAG vs. Formuler', [
   ('table', ['Box', 'System', 'Für wen?'], [
    ['TVIP S-Box v.605', 'Linux + Android', 'Wer flexibel bleiben will'],
    ['<a href="/mag-box-modelle/">MAG 524</a>', 'Linux', 'Wer es maximal einfach will'],
    ['<a href="/formuler-tv-box/">Formuler Z10/Z11</a>', 'Android + MyTVOnline', 'Wer Receiver-Gefühl mit Apps will'],
   ]),
  ]),
 ],
 'faq': [
  ('Was ist die TVIP S-Box v.605?', 'Eine kompakte 4K-IPTV-Box, die wahlweise mit Linux (Portal-Bedienung) oder Android (Apps) läuft.'),
  ('Funktioniert MOJO4K auf der TVIP-Box?', 'Ja, im Linux-Modus per Portal-URL mit MAC-Freischaltung, im Android-Modus per App mit Xtream Codes.'),
  ('Linux- oder Android-Modus – was ist besser?', 'Linux ist schneller und einfacher, Android bietet mehr Apps und Aufnahmen.'),
  ('Ist die TVIP S-Box besser als ein Fire TV Stick?', 'Sie ist auf IPTV spezialisiert und hat LAN. Ein Fire TV Stick ist günstiger und bietet mehr Streaming-Apps.'),
 ],
 'related': ['iptv-set-top-box', 'mag-box-modelle', 'formuler-tv-box', 'beste-iptv-box', 'iptv-receiver-deutschland', 'iptv-geraete', 'preise'],
},
{
 'slug': 'iptv-rumaenisch', 'crumb': 'IPTV Rumänisch', 'parent': 'iptv-alle-sender',
 'title': 'IPTV Rumänisch: Canale românești in Deutschland',
 'desc': 'Canale românești IPTV in Deutschland: Rumänisches Fernsehen über Internet auf Smart TV, Fire TV & Handy. Einrichtung, Geräte und 24h-Test auf Deutsch erklärt.',
 'keywords': ['canale romanesti iptv', 'iptv rumänisch', 'iptv romania', 'rumänisches fernsehen deutschland', 'iptv romanesc'],
 'badge': '🇷🇴 IPTV Rumänisch',
 'h1': '<span class="hl">IPTV Rumänisch</span> – canale românești in Deutschland',
 'intro': 'Bun venit! Hunderttausende Menschen mit rumänischen Wurzeln leben in Deutschland. Mit IPTV schauen Sie Programme aus der Heimat ohne Satellitenschüssel – zusammen mit deutschen Sendern in einer App.',
 'info': '🔎 Welche rumänischen Sender aktuell im Paket sind, sehen Sie am zuverlässigsten im ' + TRIAL + '.',
 'sections': [
  ('Warum IPTV für rumänische Sender?', [
   ('ul', ['<strong>Keine Schüssel nötig:</strong> In Mietwohnungen oft die einzige Möglichkeit.',
           '<strong>Alles in einer App:</strong> Deutsche und rumänische Sender, Filme und Serien.',
           '<strong>Auf allen Geräten:</strong> Smart TV, Fire TV Stick, Handy, Tablet.',
           '<strong>Zeitzone beachten:</strong> Rumänien ist eine Stunde voraus – der Programmführer zeigt die Zeiten in der Regel automatisch passend an.']),
  ]),
  ('Einrichtung in 3 Schritten', [
   ('steps', [
    ('Kostenlos testen', 'Testformular ausfüllen – Zugangsdaten kommen per E-Mail.'),
    ('App wählen', 'Smart TV: <a href="/ibo-player/">IBO Player</a>. Fire TV: <a href="/tivimate-fire-tv-stick/">TiviMate</a>. Handy: <a href="/iptv-smarters-pro-android/">Smarters Pro</a>.'),
    ('Kategorie Rumänien öffnen', 'Rumänische Sender als Favoriten speichern – so haben Sie sie immer oben.'),
   ]),
  ]),
  ('Pakete und Preise', [
   ('table', ['Laufzeit', '1 Gerät', 'Hinweis'], [
    ['1 Monat', '€9', 'Zum Kennenlernen'], ['6 Monate', '€39', 'Beliebt'], ['1 Jahr', '€49', 'Inkl. IBO-Player-Aktivierung'],
   ]),
   ('p', 'Für Familien mit mehreren Fernsehern gibt es Pakete für 2–10 Geräte: <a href="/preise-de">alle Preise</a>.'),
  ]),
  ('Tipps für die Familie', [
   ('p', 'Für Eltern und Großeltern ist eine <a href="/mag-box-modelle/">MAG Box</a> mit Zifferntasten oft am einfachsten. Wer viel Sport schaut, sollte den Fernseher per LAN-Kabel verbinden. Und wer am Handy unterwegs schaut, stellt die Qualität auf HD, um Datenvolumen zu sparen.'),
  ]),
 ],
 'faq': [
  ('Kann ich in Deutschland rumänisches Fernsehen schauen?', 'Ja, über IPTV mit Internetanschluss. Welche Sender aktuell im MOJO4K-Paket sind, sehen Sie im kostenlosen Test.'),
  ('Brauche ich eine Satellitenschüssel?', 'Nein, nur Internet und ein Gerät mit IPTV-App.'),
  ('Was kostet IPTV mit rumänischen Sendern?', 'Bei MOJO4K.DE ab €9 im Monat oder €49 im Jahr für ein Gerät.'),
  ('Welche App ist für Smart TVs am besten?', 'IBO Player für Samsung und LG. Er ist im MOJO4K-Jahrespaket inklusive.'),
 ],
 'related': ['iptv-alle-sender', 'iptv-ex-yu', 'iptv-polnisch', 'iptv-italienisch', 'iptv-europe', 'iptv-apps', 'iptv-test', 'preise'],
},
{
 'slug': 'iptv-georgisch', 'crumb': 'IPTV Georgisch', 'parent': 'iptv-alle-sender',
 'title': 'IPTV Georgisch: Georgisches Fernsehen in Deutschland',
 'desc': 'Georgisches Fernsehen in Deutschland per IPTV: Was „iptv ge" bedeutet, welche Geräte Sie brauchen und wie Sie das Angebot 24 Stunden kostenlos testen.',
 'keywords': ['iptv ge', 'iptv ge live', 'iptv ge imedi', 'imedi tv live iptv ge', 'iptv ge rustavi2', 'iptv georgisch', 'georgisches fernsehen'],
 'badge': '🇬🇪 IPTV Georgisch',
 'h1': '<span class="hl">IPTV Georgisch</span> – georgisches Fernsehen in Deutschland',
 'intro': 'Wer nach „iptv ge" sucht, meint meist georgische IPTV-Angebote – die Endung .ge steht für Georgien. Für Georgierinnen und Georgier in Deutschland ist IPTV der einfachste Weg, Nachrichten und Shows großer georgischer Sender wie Imedi oder Rustavi 2 zu verfolgen.',
 'info': '🔎 Ob einzelne georgische Sender aktuell im MOJO4K-Paket sind, prüfen Sie im ' + TRIAL + '. Senderlisten ändern sich, deshalb versprechen wir hier keine feste Liste.',
 'sections': [
  ('Was bedeutet „iptv ge"?', [
   ('p', 'In Georgien bieten die großen Telekommunikationsunternehmen IPTV im Inland an, und viele Sender haben eigene Live-Streams auf ihren Websites. Außerhalb Georgiens sind diese Angebote teils nicht oder nur eingeschränkt verfügbar. Ein internationaler IPTV-Dienst bündelt Sender aus verschiedenen Ländern in einer App.'),
   ('p', 'Kostenlose offizielle Streams einzelner Sender können Sie natürlich auch direkt auf deren Websites nutzen, sofern sie für Deutschland freigeschaltet sind.'),
  ]),
  ('So schauen Sie in Deutschland', [
   ('steps', [
    ('Gerät wählen', 'Smart TV mit <a href="/ibo-player/">IBO Player</a>, Fire TV Stick mit <a href="/tivimate-fire-tv-stick/">TiviMate</a> oder Handy mit Smarters.'),
    ('Testen', '24 Stunden kostenlos – Zugangsdaten per E-Mail.'),
    ('Länderkategorien durchsuchen', 'Nach Georgien bzw. internationalen Kategorien suchen und Favoriten anlegen.'),
   ]),
  ]),
  ('Technische Tipps', [
   ('table', ['Thema', 'Empfehlung'], [
    ['Internet', 'Mind. 16 Mbit/s für HD'],
    ['Zeitzone', 'Georgien liegt 2–3 Stunden vor Deutschland – die meisten Apps rechnen den EPG automatisch um'],
    ['Sprache der App', 'Apps sind meist auf Deutsch oder Englisch einstellbar'],
    ['Mehrere Fernseher', 'Paket mit mehreren Geräten wählen'],
   ]),
  ]),
  ('Pakete', [
   ('p', 'MOJO4K.DE gibt es ab €9 im Monat, das Jahrespaket kostet €49 und enthält die IBO-Player-Aktivierung. Alle Optionen auf der <a href="/preise-de">Preisseite</a>.'),
  ]),
 ],
 'faq': [
  ('Was ist iptv ge?', 'Damit sind meist georgische IPTV-Angebote gemeint; .ge ist die Länderendung Georgiens.'),
  ('Kann ich Imedi oder Rustavi 2 in Deutschland sehen?', 'Viele Sender bieten eigene Live-Streams an. Ob sie im MOJO4K-Paket enthalten sind, prüfen Sie im kostenlosen Test.'),
  ('Welche Geräte funktionieren?', 'Smart TVs, Fire TV Stick, Android-Boxen, iPhone, Android-Handys und PCs.'),
  ('Was kostet das?', 'Ab €9 im Monat oder €49 im Jahr für ein Gerät.'),
 ],
 'related': ['iptv-alle-sender', 'iptv-russisch', 'iptv-ex-yu', 'iptv-europe', 'iptv-apps', 'iptv-test', 'preise'],
},
{
 'slug': 'iptv-england', 'crumb': 'IPTV England / UK', 'parent': 'iptv-alle-sender',
 'title': 'IPTV England: Britisches Fernsehen in Deutschland',
 'desc': 'Britisches Fernsehen in Deutschland: BBC, ITV & UK-Sport per IPTV. Was offiziell geht, was geoblockt ist und wie Sie englischsprachiges TV einfach empfangen.',
 'keywords': ['iptv england', 'iptv bbc', 'iptv uk', 'uk iptv deutschland', 'english tv germany', 'iptv premier league'],
 'badge': '🇬🇧 IPTV England / UK',
 'h1': '<span class="hl">IPTV England</span> – britisches Fernsehen in Deutschland',
 'intro': 'Expats aus Großbritannien, Studierende und Fans der Premier League suchen britisches Fernsehen in Deutschland. Offizielle Dienste wie BBC iPlayer sind außerhalb des UK gesperrt. Was es für Möglichkeiten gibt – ehrlich erklärt.',
 'sections': [
  ('Was offiziell gilt', [
   ('ul', ['<strong>BBC iPlayer</strong> ist nur im Vereinigten Königreich verfügbar und setzt dort eine TV-Lizenz voraus.',
           '<strong>ITVX, Channel 4</strong> und andere UK-Mediatheken sind ebenfalls geoblockt.',
           '<strong>BBC News</strong> (international) ist über viele Wege auch in Deutschland frei verfügbar.',
           '<strong>Premier League</strong> wird in Deutschland von deutschen Rechteinhabern übertragen.']),
   ('p', 'Ein VPN ändert Ihren virtuellen Standort, ersetzt aber nicht die Nutzungsbedingungen der Dienste. Mehr zum Thema VPN: <a href="/iptv-vpn/">IPTV und VPN</a>.'),
  ]),
  ('Englischsprachiges TV mit MOJO4K', [
   ('p', 'Das MOJO4K-Paket enthält internationale Kategorien, darunter englischsprachige Sender. Welche UK-Sender aktuell verfügbar sind, sehen Sie im ' + TRIAL + ' – wir nennen hier bewusst keine feste Liste, weil sich das Angebot ändert.'),
   ('cards', [
    ('News', 'Internationale Nachrichtensender auf Englisch.'),
    ('Sport', 'Fußball und weitere Sportarten – siehe <a href="/iptv-premier-league/">IPTV Premier League</a>.'),
    ('Filme & Serien', 'Viele VOD-Titel in Originalsprache.'),
    ('App-Sprache', 'Smarters, TiviMate und IBO lassen sich auf Englisch stellen.'),
   ]),
  ]),
  ('Setup for English speakers', [
   ('steps', [
    ('Free trial', 'Fill in the trial form – your login arrives by e-mail within minutes.'),
    ('Install an app', 'Fire TV: <a href="/tivimate-fire-tv-stick/">TiviMate</a>. Samsung/LG: <a href="/ibo-player/">IBO Player</a>. iPhone: <a href="/iptv-smarters-pro-apple-tv/">Smarters Player Lite</a>.'),
    ('Find UK categories', 'Browse the international categories and save your favourites.'),
   ]),
   ('p', 'Unser Support antwortet auch auf Englisch: <a href="/kontakt-de">Kontakt</a>.'),
  ]),
 ],
 'faq': [
  ('Kann ich BBC iPlayer in Deutschland schauen?', 'Offiziell nicht. BBC iPlayer ist auf das Vereinigte Königreich beschränkt und setzt dort eine TV-Lizenz voraus.'),
  ('Gibt es bei MOJO4K englische Sender?', 'Ja, es gibt internationale Kategorien mit englischsprachigen Sendern. Die aktuelle Auswahl sehen Sie im kostenlosen Test.'),
  ('Do you offer English support?', 'Yes, our support team also answers in English.'),
  ('Was kostet IPTV mit UK-Sendern?', 'Ab €9 im Monat oder €49 im Jahr für ein Gerät.'),
 ],
 'related': ['iptv-alle-sender', 'iptv-premier-league', 'iptv-europe', 'iptv-vpn', 'iptv-sport', 'iptv-apps', 'iptv-test', 'preise'],
},
]

# Extra sections that give the shorter pages more depth.
_EXTRA = {
 'iptv-8k': ('Häufige Missverständnisse rund um 8K', [
  ('p', 'Viele verwechseln Auflösung mit Bildqualität. Ein gut komprimierter Full-HD-Stream mit hoher Bitrate sieht oft besser aus als ein schlecht komprimierter 4K-Stream. Entscheidend sind Bitrate, Codec und eine stabile Verbindung. Wenn Sie Ihre Bildqualität verbessern wollen, prüfen Sie zuerst die Verbindung per LAN, dann die Einstellungen des Fernsehers (Bewegungsglättung, Bildmodus) und erst danach die Hardware.'),
 ]),
 'iptv-jellyfin': ('Jellyfin-Apps für jedes Gerät', [
  ('p', 'Jellyfin hat Clients für Android TV, Fire TV, iOS, Android, Web-Browser, Samsung und LG (teils über Community-Projekte). Live TV aus dem Server ist damit in jedem Raum verfügbar, und alle Familienmitglieder teilen sich Programmführer und Aufnahmen. Beachten Sie: Jeder gleichzeitig geschaute Sender belegt eine Verbindung Ihres IPTV-Pakets.'),
 ]),
 'iptv-aufnehmen': ('Speicherplatz richtig planen', [
  ('p', 'Eine Stunde HD belegt je nach Sender etwa 2 bis 3 GB, eine Stunde 4K deutlich mehr. Für regelmäßige Serienaufnahmen ist eine externe Festplatte oder ein NAS sinnvoll. Löschen Sie gesehene Aufnahmen regelmäßig und nutzen Sie für verpasste Sendungen der letzten Tage lieber Catch-Up – das spart Platz und funktioniert ohne Planung.'),
 ]),
 'iptv-roku': ('Was ist mit Fire TV Edition und anderen Systemen?', [
  ('p', 'Fernseher mit Fire TV Edition (Fire OS) verhalten sich wie ein Fire TV Stick: Apps wie TiviMate lassen sich per Downloader installieren. Bei Fernsehern mit eigenem System (z. B. VIDAA bei Hisense oder Titan OS bei Philips) ist die Auswahl kleiner. In allen Fällen gilt: Ein externer Stick macht Sie unabhängig vom Betriebssystem des Fernsehers.'),
 ]),
 'formuler-tv-box': ('Für wen sich eine Formuler lohnt', [
  ('p', 'Eine Formuler ist ideal für Haushalte, die vom Kabel- oder Sat-Receiver kommen und die gewohnte Bedienung mit Zifferntasten, Senderliste und Aufnahme behalten wollen. Wer dagegen hauptsächlich Streaming-Apps wie Netflix oder Disney+ nutzt, ist mit einem Google-TV-Gerät oder Fire TV Stick günstiger unterwegs, weil diese Apps dort offiziell unterstützt werden.'),
 ]),
 'tvip-s-box': ('Tipps für den Alltag', [
  ('p', 'Verbinden Sie die Box per LAN-Kabel – das ist bei Live-Sport stabiler als WLAN. Halten Sie die Firmware aktuell; TVIP liefert Updates über das Einstellungsmenü. Wechseln Sie den Modus (Linux/Android) nur, wenn nötig: Nach einem Wechsel muss das Portal bzw. die App neu eingerichtet werden. Bei Problemen mit einzelnen Sendern hilft oft ein Neustart der Box.'),
 ]),
 'iptv-rumaenisch': ('Rumänische Filme und Serien auf Abruf', [
  ('p', 'Neben Live-TV bietet die VOD-Bibliothek viele Filme und Serien, teils mit Untertiteln. Durchsuchen Sie in der App die Kategorien nach Sprache oder Land. Tipp: In TiviMate und IBO Player können Sie Kategorien ausblenden, die Sie nicht brauchen – dann bleibt die Liste übersichtlich und die App reagiert schneller, gerade auf älteren Fernsehern.'),
 ]),
 'iptv-georgisch': ('Für Familien mit mehreren Sprachen', [
  ('p', 'In vielen Familien schauen die Eltern Heimatsender und die Kinder deutsche Programme. Mit einem Paket für mehrere Geräte kann jeder auf seinem Gerät schauen, ohne dass sich die Streams gegenseitig blockieren. Legen Sie in der App für jedes Familienmitglied eigene Favoriten an und nutzen Sie die Kindersicherung für Kategorien, die nicht für Kinder gedacht sind.'),
 ]),
 'iptv-england': ('Tipps für englischsprachige Zuschauer', [
  ('p', 'Viele Apps lassen sich komplett auf Englisch umstellen, ebenso der Programmführer, sofern der Sender englische EPG-Daten liefert. Für Fußball am Wochenende empfehlen wir eine LAN-Verbindung und ein Paket mit zwei Geräten, falls parallel noch jemand anderes schaut. Wer zwischen Deutschland und dem UK pendelt, kann sein MOJO4K-Abo auf Reisen innerhalb Europas weiter nutzen, sofern die Internetverbindung ausreicht.'),
 ]),
}
for _p in PAGES:
    if _p['slug'] in _EXTRA:
        _p['sections'].append(_EXTRA[_p['slug']])
