import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Welche IPTV Receiver sind die besten für Deutschland?', acceptedAnswer: { '@type': 'Answer', text: 'MAG 522w3 und MAG 524w3 sind die empfohlenen IPTV Receiver für Deutschland 2026. Sie bieten 4K-Unterstützung, HEVC-Dekodierung und eingebautes WLAN. Für Enigma2-Nutzer sind VU+ und GigaBlue empfehlenswert.' } },
    { '@type': 'Question', name: 'Was ist der Unterschied zwischen MAG Box und Android Box?', acceptedAnswer: { '@type': 'Answer', text: 'MAG Boxen sind speziell für IPTV optimiert und laufen auf Linux – sehr stabil, aber keine App-Installation möglich. Android Boxen sind flexibler (Apps, Netflix, YouTube), aber etwas aufwendiger in der Einrichtung.' } },
    { '@type': 'Question', name: 'Funktioniert MOJO4K mit Enigma2?', acceptedAnswer: { '@type': 'Answer', text: 'Ja. MOJO4K liefert M3U-Playlisten und Xtream Codes, die vollständig mit Enigma2-Receivern (Dreambox, VU+, GigaBlue) kompatibel sind. Die Einrichtung erfolgt via Plugin oder M3U-Import.' } },
    { '@type': 'Question', name: 'Brauche ich für die MAG Box ein IPTV-Abonnement?', acceptedAnswer: { '@type': 'Answer', text: 'Ja. Die MAG Box ist nur die Hardware. Für Inhalte benötigen Sie ein IPTV-Abonnement wie MOJO4K. Nach dem Kauf erhalten Sie die Portal-URL, die Sie in der MAG Box eintragen.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV Receiver Deutschland', item: 'https://mojo4k.de/iptv-receiver-deutschland' },
  ],
}

const receivers = [
  { name: 'MAG 524w3', tag: 'Testsieger', desc: '4K Ultra HD, HEVC, eingebautes Dual-Band WLAN 5GHz. Meistverkaufter IPTV Receiver in Deutschland. Ca. 90 Euro.' },
  { name: 'MAG 522w3', tag: 'Preis-Leistung', desc: '4K Ultra HD, HEVC, WLAN 2.4/5GHz. Identische Leistung wie 524w3 zu günstigerem Preis. Ca. 75 Euro.' },
  { name: 'Formuler Z10 Pro', tag: 'Premium', desc: 'Android 9 + MyTVOnline 2. Beste Kombination aus IPTV-Receiver und Android TV Box. Ca. 120 Euro.' },
  { name: 'Enigma2 / VU+', tag: 'Für Profis', desc: 'Für erfahrene Nutzer. Voll kompatibel mit MOJO4K via M3U-Plugin. Beste DVB-S2-Kombination (Satellit + IPTV).' },
]

const steps = [
  { n: '01', title: 'MAG Box einschalten', desc: 'Schließen Sie die MAG Box per HDMI an Ihren TV und per LAN oder WLAN an das Internet an.' },
  { n: '02', title: 'MOJO4K Abonnement kaufen', desc: 'Wählen Sie Ihr Paket – Sie erhalten die Portal-URL, Benutzername und Passwort per WhatsApp.' },
  { n: '03', title: 'Portal-URL eintragen', desc: 'In der MAG Box: Einstellungen → Server → Portals → Portal 1 URL eintragen → Speichern.' },
  { n: '04', title: 'Neu starten & genießen', desc: 'Nach dem Neustart lädt die MAG Box automatisch alle Kanäle. Sofort 50.000+ Kanäle verfügbar.' },
]

export default function IPTVReceiver() {
  return (
    <>
      <Head>
        <title>IPTV Receiver Deutschland 2026 – MAG Box | MOJO4K.DE</title>
        <meta name="description" content="Bester IPTV Receiver 2026: MAG Box, Enigma2 & Formuler im Vergleich. Einrichtung Schritt für Schritt. 50.000+ Kanäle in 4K mit MOJO4K. Kostenlos testen!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/iptv-receiver-deutschland/" />
        <meta property="og:title" content="IPTV Receiver Deutschland 2026 – MAG Box | MOJO4K.DE" />
        <meta property="og:description" content="Bester IPTV Receiver 2026: MAG Box, Enigma2 & Formuler im Vergleich. 50.000+ Kanäle in 4K mit MOJO4K. Kostenlos testen!" />
        <meta property="og:url" content="https://mojo4k.de/iptv-receiver-deutschland/" />
        <meta property="og:type" content="article" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="IPTV Receiver MAG Box Deutschland – MOJO4K" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="IPTV Receiver Deutschland 2026 – MAG Box | MOJO4K.DE" />
        <meta name="twitter:description" content="Bester IPTV Receiver 2026: MAG Box, Enigma2 & Formuler im Vergleich. 50.000+ Kanäle in 4K mit MOJO4K." />
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
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+IPTV+auf+meinem+Receiver+einrichten`} target="_blank" rel="noopener noreferrer"
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
              <li style={{ color: '#e53935' }}>IPTV Receiver Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>📡 MAG Box & Receiver Guide 2026</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            <span style={{ color: '#e53935' }}>IPTV Receiver</span> & MAG Box Deutschland – Vergleich & Einrichtung 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            IPTV Receiver wie die MAG Box oder Enigma2-Geräte sind die professionellste Lösung für IPTV in Deutschland. Sie bieten maximale Stabilität und sind perfekt kompatibel mit MOJO4K – 50.000+ Kanäle in 4K Ultra HD.
          </p>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '28px' }}>Beste IPTV Receiver 2026 im Vergleich</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '16px' }}>
              {receivers.map(r => (
                <div key={r.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '22px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                    <h3 style={{ color: '#fff', fontWeight: 800, fontSize: '1rem' }}>{r.name}</h3>
                    <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>{r.tag}</span>
                  </div>
                  <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.7 }}>{r.desc}</p>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>MAG Box einrichten – Schritt für Schritt</h2>
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
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '20px' }}>Enigma2 / Dreambox einrichten</h2>
            <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px' }}>
              <p style={{ color: '#aaa', lineHeight: 1.8, marginBottom: '20px', fontSize: '0.95rem' }}>
                Für Enigma2-Receiver (VU+, GigaBlue, Dreambox) gibt es zwei Möglichkeiten MOJO4K einzurichten:
              </p>
              {[
                { method: 'Via M3U-Import', desc: 'MOJO4K sendet Ihnen eine M3U-URL. In Enigma2: Plugin "E2m3u2bouquet" installieren → URL eingeben → Kanalliste automatisch erstellen lassen.' },
                { method: 'Via Xtream Plugin', desc: 'Das Plugin "Xtream Editor" ermöglicht direkten Xtream-Codes-Import mit VOD und EPG-Unterstützung.' },
              ].map((m, i) => (
                <div key={m.method} style={{ marginBottom: i === 0 ? '16px' : 0, paddingBottom: i === 0 ? '16px' : 0, borderBottom: i === 0 ? '1px solid #1a1a1a' : 'none' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#e53935" strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
                    <span style={{ color: '#fff', fontWeight: 700, fontSize: '0.92rem' }}>{m.method}</span>
                  </div>
                  <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65, paddingLeft: '22px' }}>{m.desc}</p>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen</h2>
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
