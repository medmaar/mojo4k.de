import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Welche IPTV App läuft auf LG Smart TV?', acceptedAnswer: { '@type': 'Answer', text: 'SS IPTV ist die empfohlene App für LG webOS – direkt im LG Content Store verfügbar. Beide unterstützen M3U-Playlisten und Xtream Codes.' } },
    { '@type': 'Question', name: 'Unterstützt LG webOS IPTV nativ?', acceptedAnswer: { '@type': 'Answer', text: 'Ja. LG Smart TVs mit webOS (ab 2016) unterstützen IPTV-Apps direkt über den LG Content Store. Sie benötigen weder Fire Stick noch externe Hardware.' } },
    { '@type': 'Question', name: 'Kann ich 4K IPTV auf meinem LG TV nutzen?', acceptedAnswer: { '@type': 'Answer', text: 'Ja, sofern Ihr LG TV 4K-fähig ist und Sie eine Internetverbindung mit mindestens 25 Mbit/s haben. MOJO4K bietet ausgewählte Kanäle in 4K Ultra HD.' } },
    { '@type': 'Question', name: 'Funktioniert IPTV auch auf älteren LG Smart TVs?', acceptedAnswer: { '@type': 'Answer', text: 'Ältere LG Modelle (vor 2016) können IPTV über einen externen HDMI-Stick wie den Amazon Fire TV Stick nutzen, auf dem IPTV Smarters Pro installiert wird.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV LG TV Deutschland', item: 'https://mojo4k.de/iptv-lg-tv-deutschland' },
  ],
}

const steps = [
  { n: '01', title: 'LG TV mit Internet verbinden', desc: 'Stellen Sie sicher, dass Ihr LG Smart TV mit dem WLAN oder per LAN-Kabel mit dem Internet verbunden ist.' },
  { n: '02', title: 'SS IPTV aus dem LG Content Store laden', desc: 'Öffnen Sie den LG Content Store auf Ihrem TV, suchen Sie nach "SS IPTV" und installieren Sie die App kostenlos.' },
  { n: '03', title: 'MOJO4K Abonnement kaufen', desc: 'Wählen Sie Ihr MOJO4K-Paket und erhalten Sie M3U-URL oder Xtream Codes per WhatsApp innerhalb von Minuten.' },
  { n: '04', title: 'URL in SS IPTV eingeben & loslegen', desc: 'Öffnen Sie SS IPTV → Playlist hinzufügen → URL eingeben → Fertig. Sofort 50.000+ Kanäle auf Ihrem LG TV.' },
]

const apps = [
  { name: 'SS IPTV', tag: 'Empfohlen für LG', desc: 'Direkt im LG Content Store. Unterstützt M3U und Xtream Codes. Kostenlos, einfache Einrichtung.' },
  { name: 'Smart IPTV', tag: 'Beliebt', desc: 'Für LG webOS verfügbar. Übersichtliches Interface, EPG-Unterstützung.' },
  { name: 'TiviMate (via Stick)', tag: 'Premium', desc: 'Falls Ihr LG TV kein webOS hat: Fire TV Stick + TiviMate für das beste IPTV-Erlebnis.' },
]

export default function IPTVLgTv() {
  return (
    <>
      <Head>
        <title>IPTV LG Smart TV Deutschland 2026 – Einrichtung & Anleitung | MOJO4K.DE</title>
        <meta name="description" content="IPTV auf LG Smart TV einrichten 2026. Komplette Anleitung für webOS: SS IPTV installieren, M3U-URL eingeben. 50.000+ Kanäle in 4K. Kostenlos testen bei MOJO4K.DE!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/iptv-lg-tv-deutschland" />
        <meta property="og:title" content="IPTV LG Smart TV Deutschland 2026 – Einrichtung & Anleitung | MOJO4K.DE" />
        <meta property="og:description" content="IPTV auf LG Smart TV einrichten 2026. Komplette Anleitung für webOS: SS IPTV installieren, M3U-URL eingeben. 50.000+ Kanäle in 4K." />
        <meta property="og:url" content="https://mojo4k.de/iptv-lg-tv-deutschland" />
        <meta property="og:type" content="article" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      </Head>

      <div style={{ background: '#0a0a0a', minHeight: '100vh', color: '#fff' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, height: '64px', display: 'flex', alignItems: 'center' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>MOJO4K</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <div style={{ display: 'flex', gap: '32px' }} className="hidden-mobile">
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([h, l]) => (
                <Link key={h} href={h} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{l}</Link>
              ))}
            </div>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+IPTV+auf+meinem+LG+Smart+TV+einrichten`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
              Kostenlos testen
            </a>
          </div>
        </nav>

        <div style={{ maxWidth: '900px', margin: '0 auto', padding: '100px 16px 80px' }}>
          <nav aria-label="Breadcrumb" style={{ marginBottom: '32px' }}>
            <ol style={{ listStyle: 'none', display: 'flex', gap: '8px', fontSize: '0.82rem', color: '#555' }}>
              <li><Link href="/" style={{ color: '#555', textDecoration: 'none' }}>Startseite</Link></li>
              <li>›</li>
              <li style={{ color: '#e53935' }}>IPTV LG TV Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>📺 LG Smart TV Guide 2026</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            IPTV auf <span style={{ color: '#e53935' }}>LG Smart TV</span> einrichten – Komplette Anleitung für Deutschland 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            Mit MOJO4K können Sie direkt auf Ihrem LG Smart TV über 50.000+ Kanäle in 4K streamen – ohne externe Hardware. Diese Anleitung erklärt die komplette Einrichtung auf LG webOS mit SS IPTV.
          </p>

          <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px', marginBottom: '48px' }}>
            <p style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '10px' }}>Kurzübersicht</p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '16px' }}>
              {[
                { label: 'Empfohlene App', val: 'SS IPTV' },
                { label: 'webOS Version', val: 'Ab 2016 (webOS 3+)' },
                { label: 'Einrichtungszeit', val: 'Unter 5 Minuten' },
                { label: 'Kanäle verfügbar', val: '50.000+ in 4K' },
              ].map(i => (
                <div key={i.label}>
                  <div style={{ color: '#555', fontSize: '0.78rem', marginBottom: '4px' }}>{i.label}</div>
                  <div style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>{i.val}</div>
                </div>
              ))}
            </div>
          </div>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>IPTV auf LG TV in 4 Schritten</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {steps.map(s => (
                <div key={s.n} style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                  <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>{s.n}</div>
                  <div>
                    <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>{s.title}</h3>
                    <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>{s.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Empfohlene IPTV Apps für LG TV</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '16px' }}>
              {apps.map(a => (
                <div key={a.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '22px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                    <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>{a.name}</h3>
                    <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>{a.tag}</span>
                  </div>
                  <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>{a.desc}</p>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>LG TV Kompatibilität nach Modell</h2>
            <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', overflow: 'hidden' }}>
              {[
                { model: 'LG OLED/QNED 2020–2026', webos: 'webOS 5–24', method: 'SS IPTV direkt aus Content Store', status: '✅ Beste Wahl' },
                { model: 'LG NanoCell / UHD 2018–2019', webos: 'webOS 4', method: 'SS IPTV oder Smart IPTV', status: '✅ Funktioniert' },
                { model: 'LG Smart TV 2016–2017', webos: 'webOS 3', method: 'SS IPTV (ältere Version)', status: '✅ Funktioniert' },
                { model: 'LG Smart TV vor 2016', webos: 'webOS 1–2', method: 'Fire TV Stick HDMI + Smarters Pro', status: '⚠️ Externer Stick nötig' },
              ].map((r, i) => (
                <div key={r.model} style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr 1.5fr 1fr', gap: '12px', padding: '16px 22px', borderBottom: i < 3 ? '1px solid #1a1a1a' : 'none', alignItems: 'center' }}>
                  <div>
                    <div style={{ color: '#fff', fontSize: '0.88rem', fontWeight: 600 }}>{r.model}</div>
                    <div style={{ color: '#555', fontSize: '0.78rem' }}>{r.webos}</div>
                  </div>
                  <div style={{ color: '#8c8c8c', fontSize: '0.82rem' }}>{r.method}</div>
                  <div style={{ color: r.status.includes('✅') ? '#4caf50' : '#ff9800', fontSize: '0.85rem', fontWeight: 600 }}>{r.status}</div>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen – IPTV auf LG TV</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {faqSchema.mainEntity.map((f: any) => (
                <div key={f.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>{f.name}</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{f.acceptedAnswer.text}</p>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '48px' }}>
            <h2 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '16px' }}>Weitere Geräte-Anleitungen</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
              {[['/iptv-samsung-tv-deutschland', '📺 Samsung TV'], ['/iptv-fire-stick-deutschland', '🔥 Fire Stick'], ['/iptv-android-box-deutschland', '📦 Android Box'], ['/iptv-smarters-pro-deutschland', '⚡ Smarters Pro']].map(([h, l]) => (
                <Link key={h} href={h} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '8px', padding: '9px 16px', color: '#aaa', textDecoration: 'none', fontSize: '0.88rem' }}>{l}</Link>
              ))}
            </div>
          </section>

          <div style={{ background: 'linear-gradient(135deg, #1a0000, #0a0a0a)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '16px', padding: '40px', textAlign: 'center' }}>
            <h2 style={{ color: '#fff', fontWeight: 900, fontSize: '1.6rem', marginBottom: '12px' }}>Bereit zum Starten?</h2>
            <p style={{ color: '#aaa', marginBottom: '28px', lineHeight: 1.7 }}>Kostenlos testen – kein Vertrag, keine Kreditkarte. Aktivierung in Minuten per WhatsApp.</p>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+IPTV+auf+meinem+LG+Smart+TV+kostenlos+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 36px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block' }}>
              Kostenlos testen – LG TV
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
