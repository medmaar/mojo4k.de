# Enrichment for topic, buying-guide, provider, sport and community pages.
T = '<a href="/kostenlos-testen.html">24 Stunden kostenlos testen</a>'

ENRICH = {
# ── Grundlagen ───────────────────────────────────────────────────────────────
'was-ist-iptv/index.html': {
 'sections': [
  ('What is Internet Protocol Television? IPTV Television in einem Satz', [
   ('p', 'Auf Englisch gefragt – „<strong>what is Internet Protocol Television</strong>?" – lautet die Antwort: Fernsehen, das über das Internetprotokoll statt über Antenne, Satellit oder Kabel zu Ihnen kommt. <strong>IPTV Television</strong> und <strong>Television IPTV</strong> meinen dasselbe. Sender werden als Datenstrom übertragen und von einer App, einer Box oder dem Smart TV abgespielt.'),
   ('table', ['Empfangsweg', 'Signal', 'Gerät'], [
    ['Satellit (DVB-S2)', 'Funk vom Satelliten', 'Schüssel + Receiver'],
    ['Kabel (DVB-C)', 'Koaxialkabel', 'Kabelanschluss'],
    ['Antenne (DVB-T2)', 'Funk vom Sendemast', 'Antenne + Receiver'],
    ['IPTV', 'Internet (IP)', 'App, Stick, Box, Smart TV'],
   ]),
  ]),
 ],
 'faq': [
  ('Was bedeutet Internet Protocol Television?', 'Internet Protocol Television (IPTV) bedeutet Fernsehen über das Internetprotokoll. Die Sender kommen als Datenstrom über Ihren Internetanschluss statt über Satellit, Kabel oder Antenne.'),
 ],
},
'ip-television/index.html': {
 'sections': [
  ('IP TV Streaming: Kosten, Box, Stick und Receiver', [
   ('p', '„IP TV" mit Leerzeichen ist dieselbe Technik wie IPTV. Häufige Fragen dazu:'),
   ('ul', ['<strong>IP TV Kosten</strong>: Legale Pakete von Internetanbietern kosten meist 5 bis 20 Euro im Monat zusätzlich. Unabhängige Anbieter wie MOJO4K starten ab €9 im Monat.',
           '<strong>IP TV Streaming</strong>: Sie brauchen etwa 10 Mbit/s für HD und 25 Mbit/s für 4K pro Gerät.',
           '<strong>IP TV Box</strong>, <strong>IP TV Stick</strong> oder <strong>IP TV Receiver</strong>: Ein Fire TV Stick reicht für die meisten. Eine Box lohnt sich für LAN-Anschluss und viel Speicher.',
           '<strong>IP TV Smarters</strong>: die meistgenutzte App für Ihre Zugangsdaten, kostenlos für Android, iPhone und PC.']),
  ]),
  ('Premium IP TV und IP TV Subscription: worauf achten?', [
   ('p', 'Unter <strong>Premium IP TV</strong> bzw. <strong>IP TV Premium</strong> versprechen viele Anbieter „alles in 4K". Prüfen Sie lieber selbst. Ein gutes <strong>IP TV Subscription</strong>-Angebot erkennen Sie an einem kostenlosen Test, monatlicher Kündbarkeit, einem Impressum und erreichbarem Support. Die Frage nach dem „<strong>IP TV best</strong>" Anbieter beantwortet am Ende nur Ihr eigener Test zur Primetime – deshalb können Sie MOJO4K ' + T + '.'),
  ]),
 ],
 'faq': [
  ('Was kostet IP TV im Monat?', 'Bei Internetanbietern meist 5 bis 20 Euro zusätzlich zum Anschluss, bei MOJO4K ab €9 im Monat ohne Vertragslaufzeit.'),
  ('Brauche ich eine IP TV Box?', 'Nicht zwingend. Ein Smart TV mit passender App oder ein Fire TV Stick reicht. Eine Box lohnt sich für LAN-Anschluss oder ältere Fernseher.'),
 ],
},
'iptv-einrichten/index.html': {
 'sections': [
  ('Setting IPTV: die wichtigsten Einstellungen', [
   ('p', 'Wer nach „<strong>setting IPTV</strong>" sucht, meint die Einstellungen nach der Installation. Diese vier lohnen sich auf jedem Gerät:'),
   ('ol', ['<strong>Puffer</strong> auf „mittel" oder „groß" stellen – weniger Ruckler bei schwankendem WLAN.',
           '<strong>Programmführer (EPG)</strong> einmal täglich aktualisieren lassen.',
           '<strong>Decoder</strong> auf „Hardware" stellen; nur bei Bildfehlern auf „Software" wechseln.',
           '<strong>Favoriten</strong> anlegen und ungenutzte Ländergruppen ausblenden – die App wird spürbar schneller.']),
  ]),
 ],
 'faq': [
  ('Welche Einstellungen helfen gegen IPTV-Ruckler?', 'Puffer erhöhen, Hardware-Decoder nutzen und das Gerät per LAN oder 5-GHz-WLAN verbinden. Mehr in unserer Anleitung zu IPTV-Rucklern.'),
 ],
},
'iptv-playlist/index.html': {
 'sections': [
  ('IPTV Play List: Schreibweise und Bedeutung', [
   ('p', '„<strong>IPTV Play List</strong>" ist dasselbe wie IPTV Playlist: eine Liste mit Senderadressen, meist im M3U-Format. Ihre persönliche Playlist bekommen Sie vom Anbieter als Link. Diesen Link tragen Sie in die App ein – Sie müssen die Datei nicht herunterladen.'),
  ]),
 ],
 'faq': [
  ('Muss ich die IPTV Playlist herunterladen?', 'Nein. Fügen Sie den Playlist-Link direkt in die App ein. So bleibt die Liste automatisch aktuell.'),
 ],
},
'iptv-m3u/index.html': {
 'sections': [
  ('M3U IP TV und M3U IPTV: kurz erklärt', [
   ('p', '<strong>M3U IP TV</strong> und <strong>M3U IPTV</strong> bezeichnen IPTV-Zugänge im Playlist-Format M3U. Die Datei ist eine einfache Textliste: Jede Zeile beginnt mit „#EXTINF" und dem Sendernamen, darunter steht die Stream-Adresse. Fast jede App versteht das Format – von VLC über Kodi bis TiviMate.'),
  ]),
 ],
 'faq': [
  ('Was ist besser: M3U oder Xtream Codes?', 'Xtream Codes lädt Sender, Filme und Programmführer getrennt und ist meist schneller. M3U ist universeller und funktioniert auch in Apps ohne Xtream-Unterstützung.'),
 ],
},
'iptv-m3u-playlist-deutschland/index.html': {
 'sections': [
  ('IPTV M3U Playlist Deutsch: nur deutsche Sender anzeigen', [
   ('p', 'Viele möchten eine <strong>IPTV M3U Playlist deutsch</strong>, also ohne tausende Auslandssender. Statt eine eigene Liste zu bauen, blenden Sie in der App einfach Gruppen aus: In TiviMate unter „Gruppen verwalten", in Smarters Pro über „Kategorien bearbeiten". So bleibt die Liste vom Anbieter aktuell, und Sie sehen trotzdem nur deutsche Sender.'),
  ]),
 ],
 'faq': [
  ('Kann ich nur deutsche Sender in meiner M3U-Playlist anzeigen?', 'Ja. Blenden Sie in TiviMate oder Smarters Pro alle anderen Gruppen aus. Die Playlist selbst bleibt unverändert und aktualisiert sich weiter.'),
 ],
},
'iptv-liste/index.html': {
 'sections': [
  ('Beste M3U Liste? Warum es die nicht zum Download gibt', [
   ('p', 'Wer nach „<strong>beste M3U Liste</strong>", „<strong>IPTV List</strong>", „<strong>IPTV M3U List</strong>", „<strong>IPTV M3U Liste</strong>" oder „<strong>M3U List</strong>" sucht, findet vor allem öffentliche Sammlungen. Die funktionieren selten lange. Eine dauerhafte Liste ist immer an ein Abo gebunden.'),
   ('ul', ['<strong>IPTV M3U Test</strong>: Seriöse Anbieter geben einen persönlichen Test-Link, bei MOJO4K für 24 Stunden.',
           '<strong>IPTV M3U 1 Jahr</strong>: Ein Jahreszugang ist pro Monat am günstigsten – erst nach dem Test buchen.',
           '<strong>IPTV Checker Online</strong>: Online-Checker zeigen, ob Links erreichbar sind. Geben Sie dort aber nie Ihre persönliche Liste ein, weil die Seite die Zugangsdaten speichern kann.']),
  ]),
 ],
 'faq': [
  ('Ist ein IPTV Checker online sicher?', 'Für öffentliche Testlisten ja, für Ihre persönliche Playlist nicht: Der Link enthält Benutzername und Passwort. Testen Sie Ihre Liste lieber direkt in VLC oder Ihrer App.'),
 ],
},
'iptv-m3u8/index.html': {
 'sections': [
  ('M3U8 List, M3U8 Liste und „mu3"', [
   ('p', 'Eine <strong>M3U8 List</strong> oder <strong>M3U8 Liste</strong> ist eine M3U-Datei in UTF-8-Kodierung – wichtig für Sendernamen mit Umlauten. Bei <strong>IPTV M3U8 List</strong> sind zusätzlich oft HLS-Streams gemeint. Tippfehler wie „<strong>mu3 IPTV</strong>" oder „<strong>m.m3u IPTV</strong>" meinen dasselbe Format; die spanische Form „<strong>M3U Lista</strong>" ebenso.'),
  ]),
 ],
 'faq': [
  ('Ist „mu3" ein eigenes Format?', 'Nein, „mu3" ist ein Tippfehler für M3U. Gemeint ist die Playlist-Datei mit Senderadressen.'),
 ],
},
'xtream-iptv/index.html': {
 'sections': [
  ('Xtream IPTV M3U: beide Zugänge aus einem Konto', [
   ('p', 'Bei <strong>Xtream IPTV M3U</strong> geht es um die Frage, ob man aus Xtream-Codes-Daten eine M3U-Adresse machen kann. Ja: Die M3U-Adresse setzt sich aus Server, Benutzername und Passwort zusammen. MOJO4K liefert Ihnen beide Varianten direkt mit, sodass Sie nichts selbst zusammenbauen müssen.'),
  ]),
 ],
 'faq': [
  ('Kann ich mit Xtream-Codes-Daten auch eine M3U-Playlist nutzen?', 'Ja. Die M3U-Adresse wird aus denselben Daten gebildet. Bei MOJO4K erhalten Sie beide Formate mit Ihrem Zugang.'),
 ],
},
'iptv-server/index.html': {
 'sections': [
  ('IPTV Servers: Was „mehrere Server" bedeutet', [
   ('p', 'Anbieter werben gern mit vielen <strong>IPTV Servers</strong>. Für Sie zählt nicht die Anzahl, sondern ob ein Server in Ihrer Nähe steht und abends genug Kapazität hat. Ein Server in Westeuropa mit Lastverteilung ist für Deutschland meist besser als zehn Server auf anderen Kontinenten.'),
  ]),
 ],
 'faq': [
  ('Sind mehr IPTV Server besser?', 'Nicht automatisch. Wichtiger sind die Nähe zu Deutschland und genügend Kapazität zur Primetime. Prüfen Sie das im kostenlosen Test am Abend.'),
 ],
},
# ── Kaufen, Test, Abo ────────────────────────────────────────────────────────
'iptv-kaufen/index.html': {
 'sections': [
  ('IPTV Angebote, Packages und Plans im Überblick', [
   ('p', 'Unter <strong>IPTV Angebote</strong>, <strong>IPTV Packages</strong> und <strong>IPTV Plans</strong> findet man sehr unterschiedliche Preise. Für einen fairen <strong>IPTV Preisvergleich</strong> rechnen Sie immer auf den Monatspreis um und vergleichen gleiche Laufzeiten und Gerätezahlen.'),
   ('table', ['Laufzeit', '1 Gerät bei MOJO4K', 'Für wen?'], [
    ['1 Monat', '€9', 'zum Ausprobieren nach dem Gratistest'],
    ['12 Monate (<strong>IPTV 12 Months</strong>)', '€49', 'günstigster Monatspreis'],
   ]),
   ('p', 'Alle Laufzeiten und Mehrgeräte-Pakete finden Sie auf der <a href="/preise/">Preisseite</a>.'),
  ]),
  ('IPTV Buy, IPTV Service, IPTV Account: so läuft der Kauf', [
   ('p', 'Egal ob Sie „<strong>IPTV buy</strong>", „<strong>IP TV kaufen</strong>" oder vertippt „<strong>IPTV kaufe</strong>" suchen – der Ablauf ist bei MOJO4K immer gleich:'),
   ('ol', ['Paket wählen und bezahlen.',
           'Ihr <strong>IPTV Account</strong> wird angelegt: Sie erhalten Xtream-Codes-Daten und eine M3U-Adresse.',
           'Zugangsdaten in Ihre App eintragen – der <strong>IPTV Service</strong> läuft sofort.']),
   ('p', 'Ein Hinweis zu „<strong>IPTV M3U kaufen</strong>" und „<strong>Smart IPTV kaufen</strong>": Sie kaufen kein M3U-File und keine App, sondern einen Zugang. Die App Smart IPTV wird separat beim Entwickler aktiviert.'),
  ]),
 ],
 'faq': [
  ('Was ist der Unterschied zwischen einem IPTV Account und einer M3U-Liste?', 'Der Account ist Ihr Zugang beim Anbieter. Die M3U-Liste ist eine von zwei Formen, ihn in einer App zu nutzen; die andere sind Xtream-Codes-Daten.'),
  ('Welches IPTV Angebot ist am günstigsten?', 'Auf den Monat gerechnet das Jahrespaket. Buchen Sie es aber erst, nachdem Sie den Dienst kostenlos getestet haben.'),
 ],
},
'iptv-testline/index.html': {
 'sections': [
  ('IPTV 24h Test, IPTV Test 24 und IPTV Free Test', [
   ('p', 'Ein <strong>IPTV 24h Test</strong> (auch <strong>IPTV Test 24</strong> oder <strong>IPTV Free Test</strong>) ist der wichtigste Schritt vor jedem Kauf. Eine <strong>Testline IPTV</strong> – oft auch „<strong>IPTV Linie</strong>" genannt – ist ein zeitlich begrenzter Zugang mit denselben Sendern wie im Abo.'),
   ('p', 'So nutzen Sie einen <strong>IPTV Line Test</strong> richtig: Testen Sie abends zwischen 20 und 22 Uhr, wenn die Server am stärksten ausgelastet sind. Schauen Sie ein Live-Spiel, prüfen Sie den Programmführer und starten Sie einen Film. Wer einen „<strong>Test IP TV</strong>" nur am Vormittag macht, sieht nicht, wie der Dienst zur Primetime läuft.'),
  ]),
 ],
 'faq': [
  ('Wann sollte ich einen IPTV 24h Test machen?', 'Am besten am Abend oder am Wochenende während eines Live-Spiels. Dann sind die Server am stärksten ausgelastet.'),
 ],
},
'iptv-free-trial/index.html': {
 'sections': [
  ('IPTV Trial: was ein guter Test enthalten sollte', [
   ('p', 'Ein faires <strong>IPTV Trial</strong> enthält alle Sender des Abos, den Programmführer und Filme – nicht nur eine Auswahl. Es läuft ohne Zahlungsdaten und endet automatisch. Bei MOJO4K können Sie ' + T + '.'),
  ]),
 ],
 'faq': [
  ('Muss ich für ein IPTV Trial Zahlungsdaten angeben?', 'Bei MOJO4K nicht. Der Test endet nach 24 Stunden automatisch, ohne Abo-Falle.'),
 ],
},
'iptv-premium/index.html': {
 'sections': [
  ('IPTV Premium Test und Premium Subscription', [
   ('p', 'Ein <strong>IPTV Premium Test</strong> sollte zeigen, ob „Premium" mehr ist als ein Wort. Prüfen Sie: Laufen 4K-Sender ruckelfrei? Stimmt der Programmführer? Antwortet der Support schnell? Erst dann lohnt eine <strong>IPTV Premium Subscription</strong>. Auch <strong>Premium IP TV</strong> und <strong>IP TV Premium</strong> sollten Sie mit diesen drei Fragen prüfen.'),
  ]),
 ],
 'faq': [
  ('Woran erkenne ich echtes Premium-IPTV?', 'An stabilem 4K zur Primetime, einem vollständigen Programmführer und erreichbarem Support. Testen Sie das vor dem Kauf.'),
 ],
},
'iptv-subscription/index.html': {
 'sections': [
  ('IPTV Sub, Subscribe und IP TV Subscription', [
   ('p', '„<strong>IPTV sub</strong>" ist die Kurzform für IPTV Subscription. Wer „<strong>IPTV subscribe</strong>" sucht, will meist direkt abschließen. Bei MOJO4K geht das ohne Vertrag: Monats- oder Jahrespaket wählen, Zugangsdaten erhalten, fertig. Eine <strong>IP TV Subscription</strong> verlängert sich bei uns nicht automatisch.'),
  ]),
 ],
 'faq': [
  ('Verlängert sich das MOJO4K-Abo automatisch?', 'Nein. Sie verlängern selbst, wenn Sie möchten. Es gibt keine Kündigungsfrist.'),
 ],
},
'iptv-per-paypal/index.html': {
 'sections': [
  ('IPTV mit Paysafecard bezahlen?', [
   ('p', 'Viele suchen nach <strong>IPTV Paysafecard</strong>, weil die Karte anonym ist. Bedenken Sie: Paysafecard bietet keinen Käuferschutz. Zahlen Sie damit an einen unseriösen Anbieter, ist das Geld weg. PayPal und Kreditkarte schützen Sie besser. Welche Zahlungsarten MOJO4K aktuell anbietet, beantwortet der Support per WhatsApp.'),
  ]),
 ],
 'faq': [
  ('Ist Paysafecard für IPTV sicher?', 'Paysafecard ist anonym, bietet aber keinen Käuferschutz. Für Abos ist PayPal sicherer, weil Sie bei Problemen eine Erstattung beantragen können.'),
 ],
},
'iptv-reseller/index.html': {
 'sections': [
  ('Reseller for IPTV: was Sie vorher wissen sollten', [
   ('p', 'Wer als <strong>Reseller for IPTV</strong> starten möchte, kauft Guthaben (Credits) und richtet damit Zugänge für eigene Kunden ein. Rechnen Sie vorher: Credits kosten Geld im Voraus, und Sie übernehmen den Support für Ihre Kunden. In Deutschland brauchen Sie für einen regelmäßigen Weiterverkauf außerdem ein Gewerbe.'),
  ]),
 ],
 'faq': [
  ('Brauche ich als IPTV Reseller ein Gewerbe?', 'Wenn Sie regelmäßig und mit Gewinnabsicht verkaufen, in Deutschland in der Regel ja. Lassen Sie sich im Zweifel steuerlich beraten.'),
 ],
},
# ── Anbieter & Vergleich ─────────────────────────────────────────────────────
'iptv-anbieter/index.html': {
 'sections': [
  ('Anbieter IPTV, IPTV Providers und IPTV Stream Anbieter', [
   ('p', 'Ob <strong>Anbieter IPTV</strong>, <strong>Provider IPTV</strong>, <strong>IPTV Providers</strong> oder <strong>IPTV Stream Anbieter</strong>: Gemeint sind Dienste, die Sender über das Internet liefern. Es gibt zwei Arten:'),
   ('table', ['Art', 'Beispiele', 'Typisch'], [
    ['Internetanbieter mit TV', 'Telekom MagentaTV, Vodafone GigaTV', 'an den Anschluss gebunden'],
    ['Streaming-TV-Apps', 'Zattoo, waipu.tv, Joyn', 'deutsche Sender, Monatsabo'],
    ['Unabhängige IPTV-Dienste', 'MOJO4K', 'App + Zugangsdaten, viele Länder'],
   ]),
   ('p', 'Vergleichen Sie Anbieter immer mit einem Test zur Primetime. Mehr dazu im <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>.'),
  ]),
 ],
 'faq': [
  ('Welche Arten von IPTV Anbietern gibt es?', 'Internetanbieter mit TV-Paket (z. B. MagentaTV), Streaming-TV-Apps (z. B. Zattoo, waipu.tv) und unabhängige IPTV-Dienste mit App und Zugangsdaten.'),
 ],
},
'bester-iptv-anbieter/index.html': {
 'sections': [
  ('IPTV Best, Bestenliste und „besser IPTV": so lesen Sie Rankings', [
   ('p', 'Suchen wie „<strong>IPTV best</strong>", „<strong>bes IPTV</strong>", „<strong>besser IPTV</strong>" oder „<strong>IPTV Bestenliste</strong>" führen zu vielen Ranglisten. Fragen Sie bei jeder Liste: Wer hat getestet, wann, und wie? Eine Bestenliste ohne Datum und ohne Methode ist Werbung. Die verlässlichste Bestenliste ist Ihr eigener Test zur Primetime.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV-Bestenlisten im Internet trauen?', 'Nur wenn Testmethode und Datum genannt sind. Viele Listen sind bezahlte Platzierungen. Ein eigener 24-Stunden-Test ist aussagekräftiger.'),
 ],
},
'iptv-forum/index.html': {
 'sections': [
  ('Reddit, Trustpilot und Kodinerds: was die Quellen taugen', [
   ('p', 'Bei „<strong>best IPTV Reddit</strong>", „<strong>reddit best IPTV</strong>" oder „<strong>best IPTV provider Reddit</strong>" stoßen Sie auf Threads, in denen Anbieter selten beim Namen genannt werden – viele Subreddits verbieten das. <strong>IPTV Reddit</strong> ist trotzdem nützlich für App-Fragen, etwa unter <strong>TiviMate Reddit</strong> oder <strong>IPTV Smarters Reddit</strong>.'),
   ('ul', ['<strong>IPTV Trustpilot</strong>: Bewertungen lassen sich kaufen. Achten Sie auf das Verhältnis von Ein-Sterne- zu Fünf-Sterne-Bewertungen und auf konkrete Details.',
           '<strong>Kodinerds IPTV</strong>: das größte deutschsprachige Kodi-Forum, gut für Technikfragen zu Kodi.',
           '<strong>Szenebox IPTV</strong>, <strong>IPTVForum</strong> und ein <strong>IPTV Anbieter Forum</strong>: Hier werben oft Anbieter selbst. Empfehlungen ohne Erfahrungsbericht sind wenig wert.']),
  ]),
 ],
 'faq': [
  ('Warum werden auf Reddit keine IPTV-Anbieter genannt?', 'Viele Subreddits verbieten Anbieternamen, um Werbung und Rechtsprobleme zu vermeiden. Für App- und Technikfragen sind sie trotzdem hilfreich.'),
 ],
},
'iptv-anbieter-alternativen/index.html': {
 'sections': [
  ('Weitere Namen aus der Suche: FoxIPTV, Dragon IPTV, Quzu & Co.', [
   ('p', 'Auch diese Namen tauchen in Suchanfragen auf. Wir haben keine überprüfbaren Informationen zu Betreibern, Preisen oder Qualität und empfehlen keinen davon. Prüfen Sie jeden Dienst mit der Checkliste oben.'),
   ('table', ['Gesuchter Name', 'Was wir wissen', 'Unser Rat'], [
    ['<strong>FoxIPTV</strong>', 'Anbietername; nicht mit dem Sender FOX verbunden', 'Impressum und Test prüfen'],
    ['<strong>Dragon IPTV</strong> / <strong>DragonIPTV</strong>', 'Anbietername, mehrere Websites', 'Herkunft der Website prüfen'],
    ['<strong>Quzu IPTV</strong> / <strong>Quzu TV</strong>', 'Anbieter- bzw. App-Name', 'nur mit Käuferschutz zahlen'],
    ['<strong>IPTV One</strong>', 'mehrdeutig: Anbieter- und App-Namen', 'genau prüfen, wer dahintersteht'],
    ['<strong>BesserIPTV</strong>', 'Anbietername', 'Impressum suchen'],
    ['<strong>AnbieterIPTV</strong>', 'meist Suchbegriff, kein bestimmter Dienst', 'siehe <a href="/iptv-anbieter-vergleich/">Anbieter-Vergleich</a>'],
    ['<strong>My IPTV</strong>', 'meist der Name einer Player-App', 'App nur aus offiziellen Stores'],
    ['<strong>Rapid Swiss IPTV</strong>', 'Anbietername', 'Testphase nutzen'],
    ['<strong>TV Team IPTV</strong>', 'Anbietername', 'Testphase nutzen'],
   ]),
   ('p', '<strong>Internet Protocol TV Providers</strong> gibt es viele. Ein seriöser erkennt man an Impressum, Test ohne Zahlungsdaten und erreichbarem Support.'),
  ]),
 ],
 'faq': [
  ('Ist FoxIPTV ein Angebot des Senders FOX?', 'Nein. Der Name hat nichts mit dem US-Sender FOX zu tun. Prüfen Sie Impressum und Zahlungswege, bevor Sie dort bestellen.'),
 ],
},
'iptv-lifetime/index.html': {
 'sections': [
  ('IPTV Deals, Sale und Promotions richtig einordnen', [
   ('p', '<strong>IPTV Deals</strong>, ein <strong>IPTV Sale</strong> oder <strong>IPTV Promotions</strong> mit 70 % Rabatt sind oft mit „<strong>Lifetime IPTV</strong>" verbunden. Rechnen Sie den Rabatt auf den Monatspreis um und fragen Sie: Wie lange gibt es den Anbieter schon? Gibt es eine Rückerstattung? Ein ehrlicher Rabatt ist zum Beispiel ein günstigerer Jahrespreis gegenüber dem Monatspreis.'),
  ]),
 ],
 'faq': [
  ('Sind IPTV Deals mit hohem Rabatt seriös?', 'Manchmal, aber oft nicht. Prüfen Sie Impressum, Rückerstattung und wie lange es den Anbieter gibt. Testen Sie vorher kostenlos.'),
 ],
},
'iptv-aliexpress/index.html': {
 'sections': [
  ('Alibaba IPTV, IPTV Amazon und IPTV Shop', [
   ('p', 'Neben Aliexpress tauchen auch <strong>Alibaba IPTV</strong>-Angebote auf – meist Großhandelsboxen mit vorinstallierten Apps. Unter <strong>IPTV Amazon</strong> finden Sie dagegen vor allem Hardware wie Fire TV Sticks und Android-Boxen, das ist unproblematisch. Ein <strong>IPTV Shop</strong> mit Abos ohne Impressum ist dagegen ein Warnsignal.'),
  ]),
 ],
 'faq': [
  ('Kann ich IPTV bei Amazon kaufen?', 'Hardware ja, etwa Fire TV Sticks. IPTV-Abos werden bei Amazon nicht seriös verkauft. Kaufen Sie das Abo direkt beim Anbieter mit Test und Impressum.'),
 ],
},
'flix-iptv/index.html': {
 'sections': [
  ('Flix IP TV oder FlixIPTV: App oder Anbieter?', [
   ('p', '„<strong>Flix IP TV</strong>" meint meist die Player-App Flix IPTV für Smart TVs, manchmal aber auch Anbieter mit ähnlichem Namen. Die App selbst enthält keine Sender und braucht eine Playlist. MOJO4K-Zugangsdaten funktionieren in Flix IPTV wie in jeder anderen M3U-fähigen App.'),
  ]),
 ],
 'faq': [
  ('Enthält die Flix IPTV App Sender?', 'Nein. Flix IPTV ist ein Player. Sie brauchen eine Playlist eines IPTV-Anbieters, zum Beispiel von MOJO4K.'),
 ],
},
'mega-iptv/index.html': {
 'sections': [
  ('Mega IP TV: eine Suche, mehrere Anbieter', [
   ('p', 'Unter „<strong>Mega IP TV</strong>" bzw. MegaIPTV treten mehrere Websites auf, die nicht zusammengehören müssen. Prüfen Sie deshalb die Domain, das Impressum und ob ein kostenloser Test ohne Zahlungsdaten möglich ist, bevor Sie bestellen.'),
  ]),
 ],
 'faq': [
  ('Gibt es nur einen Anbieter namens Mega IPTV?', 'Nein, unter dem Namen treten mehrere Websites auf. Achten Sie auf Domain und Impressum.'),
 ],
},
'iptv-netflix-alternative/index.html': {
 'sections': [
  ('IPTV Netflix: Ersatz oder Ergänzung?', [
   ('p', 'Bei „<strong>IPTV Netflix</strong>" fragen sich viele, ob IPTV Netflix ersetzt. Die ehrliche Antwort: IPTV ist vor allem für Live-Fernsehen und Sport stark, Netflix für eigene Serien. Viele Haushalte kombinieren beides. Netflix-Eigenproduktionen gibt es nur in der Netflix-App.'),
  ]),
 ],
 'faq': [
  ('Kann ich Netflix über IPTV schauen?', 'Netflix-Serien laufen nur in der Netflix-App. Auf einem Fire TV Stick haben Sie aber beides: Netflix und Ihre IPTV-App.'),
 ],
},
'iptv-streaming-vergleich/index.html': {
 'sections': [
  ('IPTV, Pluto TV und Discovery+: was ist was?', [
   ('p', '<strong>IPTV Pluto TV</strong>: Pluto TV ist ein kostenloser, werbefinanzierter Dienst mit thematischen Kanälen. Er ist legal und gratis, bietet aber keine regulären deutschen Hauptsender. <strong>IPTV Discovery Plus</strong>: discovery+ ist ein Streamingdienst von Warner Bros. Discovery; das Unternehmen baut in Europa zudem seinen Dienst HBO Max aus. Welche Titel in Deutschland wo laufen, ändert sich regelmäßig.'),
   ('table', ['Dienst', 'Kosten', 'Stärke'], [
    ['Pluto TV', 'kostenlos (Werbung)', 'Themenkanäle, Klassiker'],
    ['Netflix, Prime Video', 'Monatsabo', 'Eigenproduktionen auf Abruf'],
    ['Zattoo, waipu.tv', 'Monatsabo', 'deutsche Sender legal live'],
    ['IPTV-Dienst', 'ab €9/Monat bei MOJO4K', 'Live-TV, viele Länder, Sport'],
   ]),
  ]),
 ],
 'faq': [
  ('Ist Pluto TV eine Art IPTV?', 'Technisch ja, Pluto TV überträgt Kanäle über das Internet. Es ist aber ein kostenloser Dienst mit eigenem Programm, nicht mit ARD, ZDF oder RTL.'),
 ],
},
'iptv-hbo/index.html': {
 'sections': [
  ('IPTV HBO Max: wo HBO-Serien in Deutschland laufen', [
   ('p', 'Bei „<strong>IPTV HBO Max</strong>" geht es meist um die Frage, wo HBO-Serien in Deutschland zu sehen sind. Lange liefen sie exklusiv über Sky und WOW. Warner Bros. Discovery baut in Europa seinen eigenen Dienst HBO Max aus, deshalb wandern Rechte nach und nach. Welche Serie wo verfügbar ist, prüfen Sie am besten beim jeweiligen Dienst.'),
  ]),
 ],
 'faq': [
  ('Wo laufen HBO-Serien in Deutschland?', 'Traditionell bei Sky und WOW. Warner Bros. Discovery baut zusätzlich den eigenen Dienst HBO Max aus, der genaue Stand hängt von Serie und Lizenz ab.'),
 ],
},
'iptv-sky/index.html': {
 'sections': [
  ('IP TV Sky und „Sky über IPTV": die offiziellen Wege', [
   ('p', 'Sky selbst bietet Fernsehen über das Internet an: mit der Sky Q IPTV Box am Internetanschluss und mit der Streaming-App WOW. Wer nach <strong>IP TV Sky</strong>, <strong>Sky über IPTV</strong>, <strong>IPTV Anbieter Sky</strong> oder <strong>IPTV Sky Deutschland</strong> sucht, findet dort die offiziellen Wege. Details zur Box lesen Sie unter <a href="/sky-q-iptv-box/">Sky Q IPTV Box</a>.'),
  ]),
 ],
 'faq': [
  ('Bietet Sky selbst IPTV an?', 'Ja. Sky liefert Fernsehen per Internet mit der Sky Q IPTV Box und über die Streaming-App WOW.'),
 ],
},
'tv-und-internet/index.html': {
 'sections': [
  ('Telekom IP TV, Vodafone IP TV, O2 IPTV und 1&1 TV Pakete', [
   ('p', 'Alle großen Internetanbieter verkaufen „<strong>Television and Internet</strong>" im Paket. Ein kurzer Überblick über die Begriffe, unter denen danach gesucht wird:'),
   ('ul', ['<strong>Telekom IP TV</strong>, <strong>Magenta IPTV</strong>, <strong>Magenta TV IPTV</strong>: MagentaTV der Telekom, per App oder MagentaTV One. <strong>Fernsehen über Telekom</strong> geht auch ohne Telekom-Anschluss über die MagentaTV-App.',
           '<strong>Vodafone IP TV</strong>: GigaTV, als App oder mit Box.',
           '<strong>O2 IPTV</strong>: O2 TV, technisch auf Basis von waipu.tv.',
           '<strong>1&1 TV Pakete</strong>: 1&1 HD TV als Zusatzoption zum Internetvertrag.']),
   ('p', 'Die Pakete sind legal und bequem, haben aber oft Laufzeiten von 12 oder 24 Monaten.'),
  ]),
 ],
 'faq': [
  ('Kann ich MagentaTV ohne Telekom-Anschluss nutzen?', 'Ja, die MagentaTV-App funktioniert auch mit Internet von anderen Anbietern. Die Box-Variante ist an den Telekom-Anschluss gebunden.'),
 ],
},
# ── Sport ────────────────────────────────────────────────────────────────────
'iptv-sport/index.html': {
 'sections': [
  ('IPTV Soccer und IPTV ESPN: internationale Suchbegriffe', [
   ('p', '„<strong>IPTV Soccer</strong>" ist das englische Wort für Fußball-IPTV. Wer so sucht, interessiert sich oft für internationale Ligen. „<strong>IPTV ESPN</strong>" betrifft einen US-Sportsender. In Deutschland gibt es keinen eigenen ESPN-Kanal, Sportrechte liegen hier bei Sky, DAZN, MagentaSport, Sat.1 und den Öffentlich-Rechtlichen.'),
  ]),
 ],
 'faq': [
  ('Gibt es ESPN in Deutschland?', 'Einen deutschen ESPN-Sender gibt es nicht. Die großen Sportrechte liegen hier bei Sky, DAZN, MagentaSport und den Free-TV-Sendern.'),
 ],
},
'iptv-sport-live/index.html': {
 'sections': [
  ('IPTV live: was „live" technisch bedeutet', [
   ('p', 'Bei <strong>IPTV live</strong> läuft das Bild meist einige Sekunden hinter Satellit oder Kabel her. Das liegt am Puffer, der Ruckler verhindert. Bei Fußball kann der Nachbar mit Satellit also früher jubeln. Ein kleinerer Puffer verkürzt den Abstand, macht das Bild aber anfälliger für Ruckler.'),
  ]),
 ],
 'faq': [
  ('Warum ist IPTV einige Sekunden später als Satellit?', 'Die App puffert einige Sekunden, damit das Bild nicht ruckelt. Das ist bei allen Internet-TV-Diensten so, auch bei offiziellen Streaming-Apps.'),
 ],
},
'iptv-wm-2026/index.html': {
 'sections': [
  ('IPTV World Cup: Rückblick und die nächsten Turniere', [
   ('p', 'Die WM 2026 in den USA, Kanada und Mexiko fand vom 11. Juni bis 19. Juli 2026 statt. In Deutschland liefen alle 104 Spiele bei MagentaTV, ausgewählte Spiele bei ARD und ZDF. Wer jetzt nach „<strong>IPTV World Cup</strong>" sucht, plant meist für die nächsten Turniere: die Frauen-WM 2027 in Brasilien und die Männer-WM 2030.'),
  ]),
 ],
 'faq': [
  ('Wann ist die nächste Fußball-WM?', 'Die Frauen-WM 2027 findet in Brasilien statt, die nächste Männer-WM 2030.'),
 ],
},
'iptv-bein-sports/index.html': {
 'sections': [
  ('IPTV beIN Sport: Sender und Verfügbarkeit', [
   ('p', '„<strong>IPTV beIN Sport</strong>" (ohne s) meint dieselben Sender wie beIN Sports. beIN überträgt in mehreren Ländern unterschiedliche Rechte, etwa in Frankreich und der Türkei. In Deutschland hat beIN keinen eigenen Kanal im Kabel- oder Satellitenangebot.'),
  ]),
 ],
 'faq': [
  ('Gibt es beIN Sports in Deutschland?', 'Nicht als regulären deutschen Sender. beIN Sports sendet in anderen Ländern mit eigenen Rechten, etwa in Frankreich.'),
 ],
},
# ── Communities (approved markets) ──────────────────────────────────────────
'iptv-albanisch/index.html': {
 'sections': [
  ('Alb Kanale, IPTV Shqip live und IPTV Iliria', [
   ('p', 'Albanisch sprechende Zuschauer suchen oft nach „<strong>Alb Kanal IPTV</strong>", „<strong>AlbKanale IPTV</strong>" (kanale = Kanäle) oder „<strong>IPTV Shqip live</strong>" (shqip = Albanisch). Gemeint sind albanische und kosovarische Sender live in Deutschland. „<strong>IPTV Iliria</strong>" ist der Name eines eigenen Anbieters, mit dem MOJO4K nicht verbunden ist.'),
   ('p', 'Tipp für Familien: Legen Sie in der App eine Favoritenliste „Shqip" an. So finden auch Großeltern die Sender ohne Suchen.'),
  ]),
 ],
 'faq': [
  ('Was bedeutet „IPTV Shqip"?', '„Shqip" heißt Albanisch. Gemeint ist IPTV mit albanischen und kosovarischen Sendern.'),
 ],
},
'iptv-russisch/index.html': {
 'sections': [
  ('RU IPTV und russische IPTV Anbieter vergleichen', [
   ('p', '„<strong>RU IPTV</strong>", „<strong>IPTV russische TV</strong>" und „<strong>russische IPTV Anbieter</strong>" sind typische Suchen der russischsprachigen Community in Deutschland. Achten Sie beim Vergleich auf Zeitversatz-Kanäle (Moskauer Zeit vs. MEZ) und darauf, ob der Programmführer auf Russisch oder Deutsch angezeigt wird.'),
  ]),
 ],
 'faq': [
  ('Kann ich russische Sender zeitversetzt schauen?', 'Viele Sender gibt es in mehreren Zeitzonen-Varianten, und Catch-up erlaubt das Zurückspulen um einige Tage. Prüfen Sie im Test, welche Varianten Sie brauchen.'),
 ],
},
'iptv-ex-yu/index.html': {
 'sections': [
  ('IPTV kanali, ponuda, programi i cena', [
   ('p', 'Häufige Fragen unserer Zuschauer aus dem Balkan: Welche <strong>IPTV kanali</strong> sind dabei, was umfasst die <strong>IPTV ponuda</strong> (Angebot), welche <strong>IPTV programi</strong> (Programme) laufen, und was ist die <strong>IPTV cena</strong> (Preis)? Bei MOJO4K gibt es kein separates Balkan-Paket mit Aufpreis: Internationale Bereiche gehören zum normalen Paket, die Ex-YU-Kategorie prüfen Sie im kostenlosen Test. <strong>IPTV televizija</strong> funktioniert auf Smart TV, Fire TV Stick und Handy.'),
  ]),
 ],
 'faq': [
  ('Gibt es bei MOJO4K ein Balkan-Paket mit Aufpreis?', 'Nein, es gibt nur die normalen Pakete. Welche Sender aus Ex-Jugoslawien darin laufen, prüfen Sie im kostenlosen 24-Stunden-Test.'),
 ],
},
'iptv-georgisch/index.html': {
 'sections': [
  ('IPTV GE live: Imedi, Rustavi 2 und Programmführer', [
   ('p', 'Unter „<strong>IPTV GE live</strong>", „<strong>Imedi TV live IPTV GE</strong>", „<strong>IPTV GE Imedi</strong>" und „<strong>IPTV GE Rustavi2</strong>" suchen Georgierinnen und Georgier in Deutschland ihre Heimatsender. Beachten Sie den Zeitunterschied: Georgien liegt zwei bis drei Stunden vor Deutschland. Mit Catch-up schauen Sie Abendnachrichten zu Ihrer Zeit.'),
  ]),
 ],
 'faq': [
  ('Wie schaue ich georgische Nachrichten trotz Zeitverschiebung?', 'Mit Catch-up: Sender mit Uhr-Symbol lassen sich einige Tage zurückspulen. So sehen Sie die Abendnachrichten aus Tiflis zu Ihrer Zeit.'),
 ],
},
'iptv-rumaenisch/index.html': {
 'sections': [
  ('Canale românești IPTV în Germania', [
   ('p', '„<strong>Canale romanesti IPTV</strong>" ist die häufigste Suche rumänischer Familien in Deutschland. Rumänien liegt eine Stunde vor Deutschland – Hauptnachrichten um 19 Uhr Bukarester Zeit laufen hier um 18 Uhr. Legen Sie die rumänischen Sender als Favoritengruppe an, damit sie direkt nach dem Start erscheinen.'),
  ]),
 ],
 'faq': [
  ('Brauche ich für rumänische Sender ein eigenes Paket?', 'Nein, bei MOJO4K gibt es nur die normalen Pakete. Welche rumänischen Sender laufen, sehen Sie im kostenlosen 24-Stunden-Test.'),
 ],
},
'iptv-england/index.html': {
 'sections': [
  ('IPTV BBC: what is officially available', [
   ('p', 'Bei „<strong>IPTV BBC</strong>" geht es meist um BBC One und BBC Two. Offiziell sind sie über BBC iPlayer nur in Großbritannien abrufbar, und dafür ist eine TV Licence nötig. Außerhalb Großbritanniens zeigt iPlayer keine Live-Sender.'),
  ]),
 ],
 'faq': [
  ('Can I watch BBC iPlayer in Germany?', 'BBC iPlayer is officially only available in the UK and requires a TV Licence. Outside the UK the app does not play live channels.'),
 ],
},
# ── Deutsche Sender / Hauptseiten ────────────────────────────────────────────
'german-iptv/index.html': {
 'sections': [
  ('IPTV German, Germany IPTV, Deutsch IPTV', [
   ('p', 'Many English-speaking searches use „<strong>IPTV German</strong>" or „<strong>Germany IPTV</strong>", while German speakers type „<strong>Deutsch IPTV</strong>". All of them look for the same: German channels like ARD, ZDF, RTL, ProSieben and regional channels via internet. MOJO4K is built for viewers in Germany, Austria and Switzerland, with a German programme guide and German support.'),
  ]),
 ],
 'faq': [
  ('Is there an English-language support for German IPTV?', 'Our support answers in German and English via WhatsApp. The programme guide shows German channel names.'),
 ],
},
'iptv-alle-sender/index.html': {
 'sections': [
  ('IPTV Sender und IPTV Programa: so finden Sie Ihren Kanal', [
   ('p', 'Bei Tausenden <strong>IPTV Sender</strong>n hilft die Suche in der App mehr als jede Liste. Tippen Sie den Sendernamen ein, und die App zeigt alle Varianten (HD, FHD, 4K). Wer auf Spanisch oder Portugiesisch nach „<strong>IPTV Programa</strong>" sucht, meint das Programm bzw. den Programmführer – den zeigt jede gute App unter „EPG" oder „TV-Guide".'),
  ]),
 ],
 'faq': [
  ('Wie finde ich schnell einen bestimmten Sender?', 'Nutzen Sie die Suchfunktion der App und legen Sie häufig genutzte Sender als Favoriten an.'),
 ],
},
'index.html': {
 'sections': [
  ('IPTV kurz erklärt: Sender, Apps und Geräte', [
   ('p', 'Neu bei IPTV? Die drei wichtigsten Seiten für den Einstieg: <a href="/was-ist-iptv/">Was ist IPTV?</a> erklärt die Technik, <a href="/iptv-apps/">IPTV Apps</a> zeigt die passende App für Ihr Gerät, und unter <a href="/iptv-alle-sender/">IPTV alle Sender</a> finden Sie die <strong>IPTV Sender</strong> nach Ländern. Alles ohne Vertrag – zuerst ' + T + '.'),
  ]),
 ],
},
}
