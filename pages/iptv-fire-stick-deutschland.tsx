import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const steps = [
  { n: '01', title: 'Fire Stick einrichten', desc: 'Schließen Sie den Amazon Fire TV Stick an Ihren TV an und verbinden Sie ihn mit dem Internet.' },
  { n: '02', title: 'IPTV App installieren', desc: 'Öffnen Sie den Amazon App Store oder Downloader und installieren Sie IPTV Smarters Pro oder TiviMate.' },
  { n: '03', title: 'Abonnement kaufen', desc: 'Wählen Sie ein IPTVV-Paket und erhalten Sie Ihre Zugangsdaten innerhalb von Minuten per WhatsApp.' },
  { n: '04', title: 'Einloggen & Genießen', desc: 'Geben Sie Ihre Zugangsdaten in die App ein und streamen Sie sofort über 50.000 Kanäle in 4K.' },
]

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Wie installiere ich IPTV auf dem Amazon Fire Stick?', acceptedAnswer: { '@type': 'Answer', text: 'Installieren Sie IPTV Smarters Pro oder TiviMate aus dem App Store, kaufen Sie ein IPTVV-Abonnement, und geben Sie die Zugangsdaten in die App ein. Die Einrichtung dauert unter 5 Minuten.' } },
    { '@type': 'Question', name: 'Welche IPTV App ist die beste für Fire Stick?', acceptedAnswer: { '@type': 'Answer', text: 'IPTV Smarters Pro und TiviMate sind die beliebtesten IPTV Apps für den Amazon Fire TV Stick. Beide sind kostenlos verfügbar und bieten eine übersichtliche Benutzeroberfläche.' } },
    { '@type': 'Question', name: 'Kann ich 4K IPTV auf dem Fire Stick 4K streamen?', acceptedAnswer: { '@type': 'Answer', text: 'Ja! Mit dem Amazon Fire TV Stick 4K Max und einem IPTVV-Abonnement können Sie über 50.000 Kanäle in bis zu 4K Ultra HD-Qualität streamen.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://iptvv.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV Fire Stick Deutschland', item: 'https://iptvv.de/iptv-fire-stick-deutschland' },
  ],
}

export default function IPTVFireStick() {
  return (
    <>
      <Head>
        <title>IPTV Fire Stick Deutschland 2026 – Anleitung & Setup | IPTVV.DE</title>
        <meta name="description" content="IPTV auf Amazon Fire TV Stick in Deutschland einrichten. Schritt-für-Schritt Anleitung für IPTV Smarters Pro & TiviMate. 50.000+ Kanäle in 4K. Kostenlos testen!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://iptvv.de/iptv-fire-stick-deutschland" />
        <meta property="og:title" content="IPTV Fire Stick Deutschland 2026 – Anleitung & Setup | IPTVV.DE" />
        <meta property="og:description" content="IPTV auf dem Amazon Fire TV Stick einrichten. Schritt-für-Schritt Anleitung auf Deutsch." />
        <meta property="og:url" content="https://iptvv.de/iptv-fire-stick-deutschland" />
        <meta property="og:type" content="article" />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      </Head>

      <div style={{ background: '#0a0a0a', minHeight: '100vh', color: '#fff' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, height: '64px', display: 'flex', alignItems: 'center' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>IPTVV</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+möchte+IPTV+auf+meinem+Fire+Stick+einrichten`} target="_blank" rel="noopener noreferrer"
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
              <li style={{ color: '#e53935' }}>IPTV Fire Stick Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>🔥 Fire Stick Anleitung 2026</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            IPTV auf <span style={{ color: '#e53935' }}>Amazon Fire TV Stick</span> einrichten – Komplette Anleitung für Deutschland
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            Mit dem Amazon Fire TV Stick und IPTVV können Sie über 50.000 Kanäle in 4K Ultra HD auf Ihrem Fernseher genießen – ganz ohne Kabel oder Satellit. Diese Schritt-für-Schritt-Anleitung erklärt den kompletten Einrichtungsprozess.
          </p>

          <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '32px', marginBottom: '48px' }}>
            <p style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '8px' }}>Schnellstart</p>
            <p style={{ color: '#ccc', fontSize: '0.95rem', lineHeight: 1.7 }}>
              Fire Stick an TV anschließen → IPTV Smarters Pro installieren → IPTVV Abonnement kaufen → Zugangsdaten eingeben → Fertig in unter 5 Minuten.
            </p>
          </div>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>
              Installation in 4 Schritten
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
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
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Empfohlene IPTV Apps für Fire Stick</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '16px' }}>
              {[
                { name: 'IPTV Smarters Pro', desc: 'Die beliebteste IPTV App. Übersichtlich, stabil, kostenlos im App Store.', tag: 'Empfohlen' },
                { name: 'TiviMate', desc: 'Premium-Optik mit EPG-Guide. Beste Wahl für Bundesliga und Sport.', tag: 'Für Sport' },
                { name: 'GSE Smart IPTV', desc: 'Flexibel und leicht, gut für M3U-Playlisten. Kostenlose Version verfügbar.', tag: 'Gratis' },
              ].map(a => (
                <div key={a.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
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
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen – IPTV Fire Stick</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {faqSchema.mainEntity.map((f: any) => (
                <div key={f.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>{f.name}</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{f.acceptedAnswer.text}</p>
                </div>
              ))}
            </div>
          </section>

          <div style={{ background: 'linear-gradient(135deg, #1a0000, #0a0a0a)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '16px', padding: '40px', textAlign: 'center' }}>
            <h2 style={{ color: '#fff', fontWeight: 900, fontSize: '1.6rem', marginBottom: '12px' }}>Bereit zum Starten?</h2>
            <p style={{ color: '#aaa', marginBottom: '28px', lineHeight: 1.7 }}>Kostenlos testen – kein Vertrag, keine Kreditkarte. Aktivierung in Minuten.</p>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+möchte+IPTV+auf+meinem+Fire+Stick+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 36px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block' }}>
              Kostenlos testen – Fire Stick
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
