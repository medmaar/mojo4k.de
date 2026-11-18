#!/usr/bin/env python3
"""Build public/de/index.html from the home page's shared chrome (CSS, nav, footer) plus its own content."""
import json, re, sys, os

ROOT = sys.argv[1]  # path to public/
src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()

def between(s, start, end, inclusive=True):
    i = s.index(start)
    j = s.index(end, i) + len(end)
    return s[i:j] if inclusive else s[i + len(start):j - len(end)]

main_css = between(src, '<style>\n*{box-sizing', '</style>')
wa_css = between(src, '<style>\n.whatsapp-float', '</style>')
nav = between(src, '<nav id="nav">', '</nav>')
mobile = between(src, '<div class="mobile-menu" id="mobileMenu">', '</div>')
footer = between(src, '<footer>', '</footer>')
beacon = re.search(r'<script defer src="https://static\.cloudflareinsights\.com[^>]*></script>', src).group(0)
wa_float = between(src, '<a href="/support/nachricht?msg=Hallo%2C+ich+interessiere+mich+f%C3%BCr+IPTV" class="whatsapp-float"', '</a>')

URL = 'https://mojo4k.de/de/'
TITLE = 'MOJO4K Deutschland – IPTV Abo ab 9 € mit 24h Test | MOJO4K.DE'
DESC = "MOJO4K Deutschland: IPTV ab 9 € im Monat für 1 bis 5 Geräte, Aktivierung per WhatsApp und 24 Stunden kostenlos testen. Preise, Geräte und FAQ."

faqs = [
    ("Was bekomme ich bei MOJO4K Deutschland?",
     "Sie erhalten einen persönlichen IPTV-Zugang mit Live-TV, Filmen und Serien sowie EPG (elektronischer Programmführer). "
     "Die Zugangsdaten funktionieren in gängigen Apps wie IPTV Smarters Pro, TiviMate oder IBO Player."),
    ("Wie schnell ist mein Zugang aktiv?",
     "In der Regel innerhalb weniger Minuten nach der Bestellung. Server-Adresse, Benutzername und Passwort bekommen Sie per WhatsApp oder E-Mail."),
    ("Kann ich vor dem Kauf testen?",
     "Ja. Über das Formular auf der Testseite können Sie einen kostenlosen 24-Stunden-Test anfordern. "
     "Der Test endet automatisch, es entsteht kein Abo und keine Zahlungspflicht."),
    ("Was kostet ein Abo für ein Gerät?",
     "Für ein Gerät kostet 1 Monat 9 €, 3 Monate 29 €, 6 Monate 39 € und 12 Monate 49 €. "
     "Pakete für 2 bis 5 Geräte finden Sie auf der Preisseite."),
    ("Gibt es eine Mindestlaufzeit oder automatische Verlängerung?",
     "Nein. Sie zahlen einmal für den gewählten Zeitraum. Danach entscheiden Sie selbst, ob Sie verlängern möchten."),
    ("Auf welchen Geräten funktioniert MOJO4K?",
     "Auf Amazon Fire TV Stick, Android-TV-Boxen, Samsung- und LG-Smart-TVs, MAG-Receivern, Smartphones, Tablets, PC und Mac. "
     "Für jedes Gerät gibt es eine Schritt-für-Schritt-Anleitung."),
    ("Wie viele Geräte kann ich gleichzeitig nutzen?",
     "Das hängt vom Paket ab: Sie wählen 1, 2, 3, 4 oder 5 Geräte. Jedes gebuchte Gerät kann gleichzeitig streamen."),
    ("Welche Internetgeschwindigkeit brauche ich?",
     "Für HD reichen meist 16 Mbit/s, für 4K empfehlen wir mindestens 25 Mbit/s pro Gerät. Ein LAN-Kabel ist stabiler als WLAN."),
    ("Wie erreiche ich den Support?",
     "Per WhatsApp oder über die Kontaktseite. Der Support hilft auf Deutsch bei Einrichtung, App-Wahl und Störungen."),
]

prices = [  # 1 device, from the pricing table on the home page
    ("1 Monat", 9, "/1-monat-1-gerat"),
    ("3 Monate", 29, "/3-monate-1-gerat"),
    ("6 Monate", 39, "/6-monate-1-gerat"),
    ("12 Monate", 49, "/1-jahr-1-gerat"),
]

ld = [
    {"@context": "https://schema.org", "@type": "WebPage", "@id": URL + "#webpage", "url": URL,
     "name": TITLE, "description": DESC, "inLanguage": "de-DE",
     "isPartOf": {"@id": "https://mojo4k.de/#website"}, "about": {"@id": "https://mojo4k.de/#organization"},
     "breadcrumb": {"@id": URL + "#breadcrumb"}},
    {"@context": "https://schema.org", "@type": "WebSite", "@id": "https://mojo4k.de/#website",
     "name": "MOJO4K.DE", "url": "https://mojo4k.de/", "inLanguage": "de-DE",
     "publisher": {"@id": "https://mojo4k.de/#organization"}},
    {"@context": "https://schema.org", "@type": "Organization", "@id": "https://mojo4k.de/#organization",
     "name": "MOJO4K.DE", "url": "https://mojo4k.de/", "logo": "https://mojo4k.de/favicon.svg",
     "areaServed": ["DE", "AT", "CH"],
     "contactPoint": {"@type": "ContactPoint", "contactType": "customer support",
                      "availableLanguage": "German", "url": "https://mojo4k.de/kontakt-de"},
     "sameAs": ["https://t.me/mojo4kdeutschland"]},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "@id": URL + "#breadcrumb",
     "itemListElement": [
         {"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://mojo4k.de/"},
         {"@type": "ListItem", "position": 2, "name": "MOJO4K Deutschland", "item": URL}]},
    {"@context": "https://schema.org", "@type": "FAQPage", "@id": URL + "#faq",
     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
]
ld_html = '\n'.join('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + '</script>' for o in ld)

page_css = """<style>
.de-wrap{max-width:1100px;margin:0 auto;padding:0 20px}
.de-hero{padding:130px 0 60px;background:radial-gradient(ellipse 70% 60% at 20% 40%,rgba(255,82,102,.14),transparent 70%),radial-gradient(ellipse 60% 50% at 85% 20%,rgba(4,63,255,.16),transparent 70%),#140438}
.de-crumb{font-size:13px;color:rgba(255,255,255,.55);margin-bottom:18px}.de-crumb a{color:rgba(255,255,255,.75)}
.de-hero h1{font-size:clamp(28px,4.6vw,46px);font-weight:900;line-height:1.12;margin-bottom:18px}
.de-lead{color:rgba(255,255,255,.78);font-size:17px;line-height:1.75;max-width:760px;margin-bottom:26px}
.de-btns{display:flex;gap:12px;flex-wrap:wrap}
.de-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:40px;list-style:none}
.de-facts li{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:16px 18px;font-size:14px;color:rgba(255,255,255,.8)}
.de-facts b{display:block;color:#fff;font-size:17px;margin-bottom:2px}
.de-sec{padding:64px 0;border-top:1px solid rgba(255,255,255,.06)}
.de-sec:nth-of-type(even){background:#0f0330}
.de-sec h2{font-size:clamp(22px,3vw,32px);font-weight:900;margin-bottom:14px}
.de-sec>.de-wrap>p{color:rgba(255,255,255,.72);max-width:820px;line-height:1.8;margin-bottom:14px}
.de-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:26px;counter-reset:st;list-style:none}
.de-steps li{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:22px;position:relative}
.de-steps li::before{counter-increment:st;content:counter(st);display:inline-flex;width:34px;height:34px;border-radius:50%;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--gfrom),var(--gto));font-weight:900;margin-bottom:12px}
.de-steps h3{font-size:17px;margin-bottom:6px}.de-steps p{color:rgba(255,255,255,.68);font-size:14px}
.de-table-wrap{overflow-x:auto;margin-top:22px}
.de-table{width:100%;min-width:520px;border-collapse:collapse;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.1);border-radius:12px;overflow:hidden}
.de-table th,.de-table td{padding:14px 16px;text-align:left;border-bottom:1px solid rgba(255,255,255,.08);font-size:15px}
.de-table th{background:rgba(255,255,255,.06);font-size:13px;text-transform:uppercase;letter-spacing:.5px;color:rgba(255,255,255,.7)}
.de-table td a{color:#ff9a3e;font-weight:700}
.de-note{font-size:13px;color:rgba(255,255,255,.55);margin-top:12px}
.de-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:24px}
.de-card{display:block;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:18px 20px;transition:border-color .2s}
.de-card:hover{border-color:rgba(255,154,62,.6)}
.de-card h3{font-size:16px;margin-bottom:4px}.de-card p{font-size:13.5px;color:rgba(255,255,255,.65)}
.de-faq details{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:12px;padding:16px 18px;margin-top:10px}
.de-faq summary{cursor:pointer;font-weight:700;font-size:16px}
.de-faq details p{color:rgba(255,255,255,.72);margin-top:10px;line-height:1.75}
.de-cta{text-align:center}.de-cta .de-btns{justify-content:center;margin-top:18px}
@media(max-width:600px){.de-hero{padding:110px 0 44px}.de-sec{padding:48px 0}}
</style>"""


def card(href, title, text):
    return f'<a class="de-card" href="{href}"><h3>{title}</h3><p>{text}</p></a>'

devices = [
    ("/iptv-fire-stick-deutschland-de", "Amazon Fire TV Stick", "App installieren, Zugangsdaten eingeben, fertig."),
    ("/iptv-samsung-tv-deutschland/", "Samsung Smart TV", "Einrichtung über eine App aus dem Samsung-Store."),
    ("/iptv-lg-tv-deutschland/", "LG Smart TV", "So läuft MOJO4K auf webOS-Fernsehern."),
    ("/iptv-android-box-deutschland-de", "Android-TV-Box", "Für Boxen mit Android TV oder Google TV."),
    ("/iptv-receiver-deutschland-de", "MAG-Receiver", "Portal-Adresse eintragen und starten."),
    ("/iptv-smarters-pro-deutschland-de", "IPTV Smarters Pro", "Die meistgenutzte App, Schritt für Schritt."),
    ("/iptv-tivimate-deutschland-de", "TiviMate", "Für alle, die einen komfortablen TV-Guide wollen."),
    ("/iptv-m3u-playlist-deutschland-de", "M3U-Playlist", "Für VLC, Kodi und andere Player."),
]

topics = [
    ("/preise-de", "Alle Preise", "Pakete für 1 bis 5 Geräte und 1 bis 12 Monate."),
    ("/kostenlos-testen-de", "24h kostenlos testen", "Testzugang anfordern, ohne Zahlungsdaten."),
    ("/iptv-kaufen-de", "IPTV kaufen", "Worauf Sie beim Kauf eines IPTV-Zugangs achten sollten."),
    ("/iptv-abo-de", "IPTV Abo", "Laufzeiten, Verlängerung und Gerätewechsel erklärt."),
    ("/bester-iptv-anbieter-de", "Bester IPTV Anbieter", "Kriterien, an denen Sie einen guten Anbieter erkennen."),
    ("/iptv-anbieter-vergleich-de", "Anbieter-Vergleich", "Anbieter nach Preis, Geräten und Support verglichen."),
    ("/iptv-stick-de", "IPTV Stick", "Welche Sticks sich für IPTV eignen."),
    ("/iptv-box-de", "IPTV Box", "Android-Boxen und Receiver im Überblick."),
    ("/iptv-oesterreich/", "IPTV Österreich", "MOJO4K in Österreich nutzen."),
    ("/iptv-schweiz/", "IPTV Schweiz", "MOJO4K in der Schweiz nutzen."),
    ("/was-ist-iptv/", "Was ist IPTV?", "Die Technik kurz und verständlich erklärt."),
    ("/faqs-de", "Alle FAQs", "Weitere Antworten zu Bestellung, Technik und Zahlung."),
]

price_rows = '\n'.join(
    f'<tr><td>{d}</td><td><strong>{p} €</strong></td><td>{round(p / int(d.split()[0]), 2):.2f} €'.replace('.', ',') +
    f'</td><td><a href="{u}">Bestellen →</a></td></tr>'
    for d, p, u in prices)

faq_html = '\n'.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)

main = f"""<main id="main-content">
<section class="de-hero">
  <div class="de-wrap">
    <nav class="de-crumb" aria-label="Brotkrumen"><a href="/">Startseite</a> › MOJO4K Deutschland</nav>
    <h1>MOJO4K Deutschland: Ihr IPTV-Zugang für Fernsehen auf jedem Gerät</h1>
    <p class="de-lead">MOJO4K.DE ist ein IPTV-Dienst für Haushalte in Deutschland, Österreich und der Schweiz. Sie buchen einen Zugang für 1 bis 5 Geräte, bekommen Ihre Zugangsdaten in wenigen Minuten und schauen Live-TV, Filme und Serien über Ihre Internetleitung, ohne Satellitenschüssel, Kabelanschluss oder Vertragsbindung.</p>
    <div class="de-btns">
      <a href="/kostenlos-testen-de" class="btn">24 Stunden kostenlos testen</a>
      <a href="/preise-de" class="btn-ol">Preise ansehen</a>
    </div>
    <ul class="de-facts">
      <li><b>ab 9 € / Monat</b>für ein Gerät, einmalige Zahlung</li>
      <li><b>1 bis 5 Geräte</b>gleichzeitig im selben Haushalt</li>
      <li><b>24h Testzugang</b>kostenlos und unverbindlich</li>
      <li><b>Deutscher Support</b>per WhatsApp und Kontaktformular</li>
    </ul>
  </div>
</section>

<section class="de-sec" id="so-funktioniert-es">
  <div class="de-wrap">
    <h2>So starten Sie mit MOJO4K in Deutschland</h2>
    <p>Sie brauchen kein neues Gerät und keinen Techniker. Ein Fernseher mit App-Store, ein Fire TV Stick oder ein Smartphone und eine stabile Internetverbindung genügen.</p>
    <ol class="de-steps">
      <li><h3>Test oder Paket wählen</h3><p>Starten Sie mit dem kostenlosen 24h-Test oder wählen Sie direkt Laufzeit und Anzahl der Geräte.</p></li>
      <li><h3>Zugangsdaten erhalten</h3><p>Server-Adresse, Benutzername und Passwort kommen in der Regel innerhalb weniger Minuten per WhatsApp oder E-Mail.</p></li>
      <li><h3>App einrichten</h3><p>Installieren Sie eine IPTV-App wie Smarters Pro, TiviMate oder IBO Player und tragen Sie die Daten ein.</p></li>
      <li><h3>Fernsehen</h3><p>Senderliste, Programmführer und Mediathek erscheinen sofort. Bei Fragen hilft der Support.</p></li>
    </ol>
  </div>
</section>

<section class="de-sec" id="preise">
  <div class="de-wrap">
    <h2>Preise für ein Gerät</h2>
    <p>Alle Laufzeiten enthalten denselben Umfang. Je länger die Laufzeit, desto niedriger der Monatspreis. Es gibt keine automatische Verlängerung.</p>
    <div class="de-table-wrap">
      <table class="de-table">
        <thead><tr><th>Laufzeit</th><th>Preis</th><th>Pro Monat</th><th></th></tr></thead>
        <tbody>
{price_rows}
        </tbody>
      </table>
    </div>
    <p class="de-note">Pakete für 2, 3, 4 oder 5 Geräte und alle Details stehen auf der <a href="/preise-de" style="color:#ff9a3e">Preisseite</a>. Beim 12-Monats-Paket ist ein IBO-Player-Abo inklusive.</p>
  </div>
</section>

<section class="de-sec" id="inhalte">
  <div class="de-wrap">
    <h2>Was Sie mit MOJO4K schauen</h2>
    <p>Der Zugang bündelt Live-Fernsehen und eine Video-Bibliothek in einer App. Die Senderliste ist nach Ländern und Kategorien sortiert, damit Sie deutsche Programme schnell finden.</p>
    <div class="de-grid">
      <div class="de-card"><h3>Deutsches Fernsehen</h3><p>Öffentlich-rechtliche und private Sender sowie regionale Programme, sortiert nach Bundesland.</p></div>
      <div class="de-card"><h3>Live-Sport</h3><p>Sportkanäle für Fußball, Tennis, Motorsport und mehr. Mehr dazu auf der Seite <a href="/iptv-sport/" style="color:#ff9a3e">IPTV Sport</a>.</p></div>
      <div class="de-card"><h3>Filme &amp; Serien</h3><p>Eine Video-on-Demand-Bibliothek, die laufend ergänzt wird, abrufbar wann Sie wollen.</p></div>
      <div class="de-card"><h3>Programmführer (EPG)</h3><p>Sehen Sie, was gerade läuft und was als Nächstes kommt. <a href="/iptv-epg/" style="color:#ff9a3e">So funktioniert der EPG</a>.</p></div>
      <div class="de-card"><h3>Internationale Sender</h3><p>Programme aus vielen Ländern, zum Beispiel <a href="/iptv-tuerkisch/" style="color:#ff9a3e">türkische Sender</a>.</p></div>
      <div class="de-card"><h3>Bis zu 4K</h3><p>Viele Kanäle in HD, Full HD und 4K, abhängig von Sender und Internetleitung.</p></div>
    </div>
  </div>
</section>

<section class="de-sec" id="vergleich">
  <div class="de-wrap">
    <h2>IPTV, Kabel oder Satellit: der Unterschied</h2>
    <p>Kabel- und Satellitenfernsehen brauchen einen festen Anschluss oder eine Schüssel am Haus. IPTV kommt über das Internet und läuft deshalb auf jedem Bildschirm, auch unterwegs oder in der Ferienwohnung.</p>
    <div class="de-table-wrap">
      <table class="de-table">
        <thead><tr><th></th><th>MOJO4K IPTV</th><th>Kabel-TV</th><th>Satellit</th></tr></thead>
        <tbody>
          <tr><td>Anschluss</td><td>Internet</td><td>Kabeldose</td><td>Schüssel und Receiver</td></tr>
          <tr><td>Geräte</td><td>TV, Stick, Box, Handy, PC</td><td>meist nur der Fernseher</td><td>meist nur der Fernseher</td></tr>
          <tr><td>Bindung</td><td>keine, Laufzeit frei wählbar</td><td>oft Mindestlaufzeit</td><td>Hardware-Kauf</td></tr>
          <tr><td>Test vorab</td><td>24 Stunden kostenlos</td><td>selten</td><td>nein</td></tr>
          <tr><td>Unterwegs</td><td>ja, mit Internet</td><td>nein</td><td>nein</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="de-sec" id="geraete">
  <div class="de-wrap">
    <h2>Anleitungen für Ihr Gerät</h2>
    <p>Wählen Sie Ihr Gerät oder Ihre App. Jede Anleitung zeigt die Einrichtung in wenigen Schritten.</p>
    <div class="de-grid">
      {''.join(card(*d) for d in devices)}
    </div>
  </div>
</section>

<section class="de-sec" id="ratgeber">
  <div class="de-wrap">
    <h2>Ratgeber und weitere Seiten</h2>
    <p>Hier finden Sie die wichtigsten Seiten rund um Kauf, Test und Einrichtung.</p>
    <div class="de-grid">
      {''.join(card(*t) for t in topics)}
    </div>
  </div>
</section>

<section class="de-sec de-faq" id="faq">
  <div class="de-wrap">
    <h2>Häufige Fragen zu MOJO4K Deutschland</h2>
{faq_html}
  </div>
</section>

<section class="de-sec de-cta">
  <div class="de-wrap">
    <h2>Erst testen, dann entscheiden</h2>
    <p style="margin:0 auto">Fordern Sie Ihren kostenlosen 24h-Testzugang an oder schreiben Sie uns, wenn Sie Hilfe bei der Auswahl brauchen.</p>
    <div class="de-btns">
      <a href="/kostenlos-testen-de" class="btn">Kostenlos testen</a>
      <a href="/kontakt-de" class="btn-ol">Kontakt</a>
    </div>
  </div>
</section>
</main>"""

head = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{TITLE}</title>
<meta name="description" content="{DESC}"/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="{URL}"/>
<link rel="alternate" hreflang="de" href="{URL}"/>
<link rel="alternate" hreflang="x-default" href="{URL}"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="MOJO4K.DE"/>
<meta property="og:locale" content="de_DE"/>
<meta property="og:title" content="{TITLE}"/>
<meta property="og:description" content="{DESC}"/>
<meta property="og:url" content="{URL}"/>
<meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{TITLE}"/>
<meta name="twitter:description" content="{DESC}"/>
<meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="/favicon.svg"/>
<meta name="theme-color" content="#140438"/>
{main_css}
{page_css}
{wa_css}
{ld_html}
</head>
<body>
{nav}
{mobile}
"""

out = head + main + '\n\n' + footer + '\n' + beacon + '\n' + wa_float + '\n</body>\n</html>\n'
os.makedirs(os.path.join(ROOT, 'de'), exist_ok=True)
open(os.path.join(ROOT, 'de', 'index.html'), 'w', encoding='utf-8').write(out)
print('wrote', len(out), 'bytes')
