import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Ist TiviMate kostenlos?', acceptedAnswer: { '@type': 'Answer', text: 'TiviMate ist kostenlos mit grundlegenden Funktionen. TiviMate Premium (ca. 4,99 €/Jahr) schaltet EPG-Aufnahmen, Multi-Screen und erweiterte Features frei.' } },
    { '@type': 'Question', name: 'Auf welchen Geräten läuft TiviMate?', acceptedAnswer: { '@type': 'Answer', text: 'TiviMate läuft auf Amazon Fire TV Stick, Android TV Boxen und Android-Geräten mit Google Play Zugang. Es ist nicht nativ für iOS oder Samsung/LG webOS verfügbar.' } },
    { '@type': 'Question', name: 'Wie verbinde ich TiviMate mit MOJO4K?', acceptedAnswer: { '@type': 'Answer', text: 'Öffnen Sie TiviMate → Playlist hinzufügen → Xtream Codes API wählen → Server-URL, Benutzername und Passwort von MOJO4K eingeben. Fertig in unter 2 Minuten.' } },
    { '@type': 'Question', name: 'Was ist der Unterschied zwischen TiviMate und IPTV Smarters Pro?', acceptedAnswer: { '@type': 'Answer', text: 'TiviMate hat das bessere UI/EPG-Design und ist die erste Wahl für Fire Stick und Android Box. Smarters Pro ist kostenlos auf mehr Plattformen verfügbar (inkl. iPhone). Beide funktionieren perfekt mit MOJO4K.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'TiviMate IPTV Deutschland', item: 'https://mojo4k.de/iptv-tivimate-deutschland' },
  ],
}

const steps = [
  { n: '01', title: 'TiviMate installieren', desc: 'Öffnen Sie den Google Play Store oder Amazon App Store und suchen Sie nach "TiviMate IPTV Player". Die kostenlose Version ist sofort verfügbar.' },
  { n: '02', title: 'MOJO4K Abonnement kaufen', desc: 'Wählen Sie Ihr MOJO4K-Paket und erhalten Sie Server-URL, Benutzername und Passwort innerhalb von Minuten per WhatsApp.' },
  { n: '03', title: 'Playlist in TiviMate hinzufügen', desc: 'TiviMate öffnen → "Playlist hinzufügen" → "Xtream Codes API" wählen → die 3 Zugangsdaten eingeben → Laden.' },
  { n: '04', title: 'EPG aktivieren & genießen', desc: 'Einstellungen → EPG → URL eingeben. Dann haben Sie vollständiges TV-Programm für alle 50.000+ Kanäle.' },
]

const features = [
  { title: 'EPG TV-Guide', desc: 'Vollständiges elektronisches TV-Programm für alle Kanäle. Bis zu 14 Tage Vorschau.' },
  { title: 'Aufnahmefunktion', desc: 'Sendungen direkt auf USB-Stick oder internen Speicher aufnehmen (Premium-Feature).' },
  { title: 'Multi-Screen', desc: 'Bis zu 4 Kanäle gleichzeitig im Bild-in-Bild-Modus anzeigen.' },
  { title: 'Favoriten & Gruppen', desc: 'Eigene Kanal-Favoriten anlegen und Gruppen nach Themen organisieren.' },
  { title: 'Catch-Up TV', desc: 'Verpasste Sendungen im Nachhinein abrufen – sofern vom IPTV-Anbieter unterstützt.' },
  { title: 'Kindersicherung', desc: 'Einzelne Kanäle oder Gruppen mit PIN sperren.' },
]

export default function TiviMateDeutschland() {
  return (
    <>
      <Head>
        <title>TiviMate IPTV Deutschland 2026 – Einrichtung | MOJO4K.DE</title>
        <meta name="description" content="TiviMate IPTV einrichten 2026. Anleitung für Fire Stick & Android Box. Mit MOJO4K 50.000+ Kanäle, EPG & Aufnahmen. Kostenlos testen!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/iptv-tivimate-deutschland/" />
        <meta property="og:title" content="TiviMate IPTV Deutschland 2026 – Einrichtung | MOJO4K.DE" />
        <meta property="og:description" content="TiviMate IPTV einrichten 2026. Fire Stick & Android Box Anleitung. Mit MOJO4K 50.000+ Kanäle in 4K. Kostenlos testen!" />
        <meta property="og:url" content="https://mojo4k.de/iptv-tivimate-deutschland/" />
        <meta property="og:type" content="article" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="TiviMate IPTV Deutschland – MOJO4K" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="TiviMate IPTV Deutschland 2026 – Einrichtung | MOJO4K.DE" />
        <meta name="twitter:description" content="TiviMate IPTV einrichten 2026. Fire Stick & Android Box Anleitung. Mit MOJO4K 50.000+ Kanäle in 4K. Kostenlos testen!" />
        <meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta name="author" content="MOJO4K.DE" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon.svg" />
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
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+TiviMate+mit+MOJO4K+nutzen`} target="_blank" rel="noopener noreferrer"
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
              <li style={{ color: '#e53935' }}>TiviMate IPTV Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>⭐ Beste IPTV-App für Fire Stick</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            <span style={{ color: '#e53935' }}>TiviMate IPTV</span> einrichten – Komplette Anleitung für Deutschland 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            TiviMate gilt als der beste IPTV-Player in Deutschland – besonders auf dem Amazon Fire TV Stick. Mit übersichtlichem EPG-Guide, Aufnahme-Funktion und bis zu 4 Streams gleichzeitig ist es die erste Wahl für anspruchsvolle IPTV-Nutzer.
          </p>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>TiviMate mit MOJO4K in 4 Schritten einrichten</h2>
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
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>TiviMate Features im Überblick</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '14px' }}>
              {features.map(f => (
                <div key={f.title} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#e53935" strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
                    <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.92rem' }}>{f.title}</h3>
                  </div>
                  <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>{f.desc}</p>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>TiviMate vs. IPTV Smarters Pro</h2>
            <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', overflow: 'hidden' }}>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', background: '#0d0d0d', padding: '14px 22px', borderBottom: '1px solid #1a1a1a' }}>
                <span style={{ color: '#555', fontSize: '0.8rem', fontWeight: 700 }}>Feature</span>
                <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 700 }}>TiviMate</span>
                <span style={{ color: '#888', fontSize: '0.8rem', fontWeight: 700 }}>Smarters Pro</span>
              </div>
              {[
                ['EPG-Design', '⭐⭐⭐⭐⭐ Sehr gut', '⭐⭐⭐⭐ Gut'],
                ['Plattformen', 'Fire Stick, Android TV', 'Fire Stick, Android, iOS, PC'],
                ['Kostenlos', 'Ja (Premium: ~5€/Jahr)', 'Ja, komplett kostenlos'],
                ['Aufnahme', '✅ Ja (Premium)', '❌ Nein'],
                ['Multi-Screen', '✅ Bis zu 4 (Premium)', '❌ Nein'],
                ['iOS/iPhone', '❌ Nicht verfügbar', '✅ Ja'],
              ].map(([feat, tivi, smarters], i) => (
                <div key={feat} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', padding: '14px 22px', borderBottom: i < 5 ? '1px solid #1a1a1a' : 'none' }}>
                  <span style={{ color: '#888', fontSize: '0.85rem' }}>{feat}</span>
                  <span style={{ color: '#ccc', fontSize: '0.85rem' }}>{tivi}</span>
                  <span style={{ color: '#666', fontSize: '0.85rem' }}>{smarters}</span>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen zu TiviMate</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {faqSchema.mainEntity.map((f: any) => (
                <div key={f.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>{f.name}</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{f.acceptedAnswer.text}</p>
                </div>
              ))}
            </div>
          </section>

                    <div style={{ background: 'linear-gradient(135deg, #0d0d0d, #1a0000)', border: '1px solid rgba(229,57,53,0.35)', borderRadius: '16px', padding: '40px', textAlign: 'center', marginTop: '48px' }}>
            <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.78rem', marginBottom: '10px' }}>Abonnement wählen</p>
            <h2 style={{ color: '#fff', fontWeight: 900, fontSize: '1.6rem', marginBottom: '12px' }}>Bereit loszulegen?</h2>
            <p style={{ color: '#aaa', marginBottom: '28px', lineHeight: 1.7, maxWidth: '480px', margin: '0 auto 28px' }}>
              Ab €9/Monat – kein Vertrag, keine Kreditkarte. Wählen Sie Ihr Paket und starten Sie in Minuten.
            </p>
            <div style={{ display: 'flex', gap: '14px', justifyContent: 'center', flexWrap: 'wrap' }}>
              <Link href="/preise" style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 32px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block' }}>
                Jetzt kaufen – Preise ansehen
              </Link>
              <a href={`${WA}`} target="_blank" rel="noopener noreferrer"
                style={{ background: 'transparent', color: '#fff', fontWeight: 700, padding: '14px 32px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block', border: '1px solid rgba(255,255,255,0.2)' }}>
                Kostenlos testen
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}
