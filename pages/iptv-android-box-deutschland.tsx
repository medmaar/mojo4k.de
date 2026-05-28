import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    {"@type":"Question","name":"Welche Android Box ist die beste für IPTV in Deutschland?","acceptedAnswer":{"@type":"Answer","text":"Nvidia Shield TV Pro, Xiaomi Mi Box S (2. Gen) und Amazon Fire TV Cube sind die Top-Empfehlungen für 4K IPTV in Deutschland. Alle drei laufen stabil mit TiviMate und IPTV Smarters Pro."}},
    {"@type":"Question","name":"Benötige ich ein Google-Konto für die Android Box?","acceptedAnswer":{"@type":"Answer","text":"Ja, für den Zugriff auf den Google Play Store benötigen Sie ein Google-Konto. Die IPTV-Nutzung selbst funktioniert aber auch mit direkt installierten APK-Dateien."}},
    {"@type":"Question","name":"Kann ich mit der Android Box IPTV in 4K streamen?","acceptedAnswer":{"@type":"Answer","text":"Ja, mit einer 4K-fähigen Android Box (z.B. Nvidia Shield, Mi Box S) und einer Internetverbindung von mindestens 25 Mbit/s können Sie MOJO4K in 4K Ultra HD genießen."}}
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV Android Box Deutschland', item: 'https://mojo4k.de/iptv-android-box-deutschland' },
  ],
}

export default function Page() {
  return (
    <>
      <Head>
        <title>IPTV Android Box Deutschland 2026 – Beste Box & Einrichtung | MOJO4K.DE</title>
        <meta name="description" content="Die beste IPTV Android Box für Deutschland 2026. Einrichtung, empfohlene Boxen und Apps. 50.000+ Kanäle in 4K Ultra HD. Kostenlos testen bei MOJO4K.DE!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/iptv-android-box-deutschland" />
        <meta property="og:title" content="IPTV Android Box Deutschland 2026 – Beste Box & Einrichtung | MOJO4K.DE" />
        <meta property="og:description" content="Die beste IPTV Android Box für Deutschland 2026. Einrichtung, empfohlene Boxen und Apps. 50.000+ Kanäle in 4K Ultra HD. Kostenlos testen bei MOJO4K.DE!" />
        <meta property="og:url" content="https://mojo4k.de/iptv-android-box-deutschland" />
        <meta property="og:type" content="article" />
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
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+möchte+IPTV+auf+meiner+Android+Box+einrichten`} target="_blank" rel="noopener noreferrer"
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
              <li style={{ color: '#e53935' }}>IPTV Android Box Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>📦 Android Box Guide</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            IPTV <span style={{ color: '#e53935' }}>Android Box</span> Deutschland – Beste Box & komplette Einrichtung 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            Eine Android TV Box ist die flexibelste Lösung für IPTV in Deutschland. Sie erhalten Zugang zu allen IPTV Apps wie TiviMate und IPTV Smarters Pro – und können über 50.000 Kanäle in 4K streamen.
          </p>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>Einrichtung in 4 Schritten</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div key="01" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>01</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>Android Box einrichten</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Schließen Sie die Box an Ihren TV (HDMI) und das Internet (WLAN oder LAN) an.</p>
                </div>
              </div>
              <div key="02" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>02</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>TiviMate oder Smarters Pro installieren</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Öffnen Sie den Google Play Store und installieren Sie TiviMate Player oder IPTV Smarters Pro.</p>
                </div>
              </div>
              <div key="03" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>03</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>MOJO4K Abonnement kaufen</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Wählen Sie Ihr Paket und erhalten Sie die Zugangsdaten per WhatsApp innerhalb von Minuten.</p>
                </div>
              </div>
              <div key="04" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>04</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>Xtream-Daten eingeben</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Geben Sie Server-URL, Benutzername und Passwort ein und starten Sie mit dem Streaming.</p>
                </div>
              </div>
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Empfohlene Apps</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '16px' }}>
              <div key="TiviMate" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>TiviMate</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Beste Wahl</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Bestes Layout für Android Boxen. EPG, Aufnahme, Multi-Screen. Kostenlose Version verfügbar.</p>
              </div>
              <div key="IPTV Smarters Pro" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>IPTV Smarters Pro</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Empfohlen</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Professionelle Oberfläche, Xtream Codes und M3U unterstützt. Kostenlos.</p>
              </div>
              <div key="GSE Smart IPTV" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>GSE Smart IPTV</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Flexibel</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Sehr flexibel, unterstützt alle Formate. Ideal für fortgeschrittene Nutzer.</p>
              </div>
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <div key="Welche Android Box ist die bes" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Welche Android Box ist die beste für IPTV in Deutschland?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>Nvidia Shield TV Pro, Xiaomi Mi Box S (2. Gen) und Amazon Fire TV Cube sind die Top-Empfehlungen für 4K IPTV in Deutschland. Alle drei laufen stabil mit TiviMate und IPTV Smarters Pro.</p>
            </div>
            <div key="Benötige ich ein Google-Konto " style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Benötige ich ein Google-Konto für die Android Box?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>Ja, für den Zugriff auf den Google Play Store benötigen Sie ein Google-Konto. Die IPTV-Nutzung selbst funktioniert aber auch mit direkt installierten APK-Dateien.</p>
            </div>
            <div key="Kann ich mit der Android Box I" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Kann ich mit der Android Box IPTV in 4K streamen?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>Ja, mit einer 4K-fähigen Android Box (z.B. Nvidia Shield, Mi Box S) und einer Internetverbindung von mindestens 25 Mbit/s können Sie MOJO4K in 4K Ultra HD genießen.</p>
            </div>
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
