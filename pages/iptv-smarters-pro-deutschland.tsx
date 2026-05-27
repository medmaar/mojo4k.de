import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    {"@type":"Question","name":"Ist IPTV Smarters Pro kostenlos?","acceptedAnswer":{"@type":"Answer","text":"Ja, IPTV Smarters Pro ist vollständig kostenlos. Sie laden die App aus dem jeweiligen App Store und geben dann Ihre MOJO4K-Zugangsdaten ein. Es fallen keine zusätzlichen App-Kosten an."}},
    {"@type":"Question","name":"Auf welchen Geräten läuft IPTV Smarters Pro?","acceptedAnswer":{"@type":"Answer","text":"IPTV Smarters Pro läuft auf Amazon Fire TV Stick, Android TV, Android-Smartphones, iPhone, iPad, Windows PC, Mac und den meisten Smart TVs über den jeweiligen App Store."}},
    {"@type":"Question","name":"Was ist der Unterschied zwischen M3U und Xtream Codes?","acceptedAnswer":{"@type":"Answer","text":"Xtream Codes API ist die empfohlene Methode für MOJO4K – sie ermöglicht schnelleres Laden, VOD-Bibliotheken und EPG. M3U ist eine einfache Playlist-URL. Beides funktioniert mit Smarters Pro."}}
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV Smarters Pro Deutschland', item: 'https://mojo4k.de/iptv-smarters-pro-deutschland' },
  ],
}

export default function Page() {
  return (
    <>
      <Head>
        <title>IPTV Smarters Pro Deutschland – Einrichtung & Anleitung 2026 | MOJO4K.DE</title>
        <meta name="description" content="IPTV Smarters Pro in Deutschland einrichten. Schritt-für-Schritt Anleitung für Fire Stick, Android, iPhone und Smart TV. Mit MOJO4K 50.000+ Kanäle in 4K." />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/iptv-smarters-pro-deutschland" />
        <meta property="og:title" content="IPTV Smarters Pro Deutschland – Einrichtung & Anleitung 2026 | MOJO4K.DE" />
        <meta property="og:description" content="IPTV Smarters Pro in Deutschland einrichten. Schritt-für-Schritt Anleitung für Fire Stick, Android, iPhone und Smart TV. Mit MOJO4K 50.000+ Kanäle in 4K." />
        <meta property="og:url" content="https://mojo4k.de/iptv-smarters-pro-deutschland" />
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
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+möchte+IPTV+Smarters+Pro+mit+MOJO4K+einrichten`} target="_blank" rel="noopener noreferrer"
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
              <li style={{ color: '#e53935' }}>IPTV Smarters Pro Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>⚡ Smarters Pro Anleitung</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            <span style={{ color: '#e53935' }}>IPTV Smarters Pro</span> einrichten – Komplette Anleitung für Deutschland 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            IPTV Smarters Pro ist der beliebteste IPTV-Player in Deutschland. Er läuft auf allen Geräten – Fire Stick, Android, iPhone, Smart TV – und bietet eine übersichtliche Benutzeroberfläche mit EPG-Guide.
          </p>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '32px' }}>Einrichtung in 4 Schritten</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div key="01" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>01</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>Smarters Pro installieren</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Laden Sie IPTV Smarters Pro kostenlos aus dem App Store Ihres Geräts herunter (Google Play, Amazon, App Store).</p>
                </div>
              </div>
              <div key="02" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>02</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>MOJO4K Abonnement kaufen</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Wählen Sie Ihr MOJO4K-Paket und erhalten Sie Server-URL, Benutzername und Passwort per WhatsApp.</p>
                </div>
              </div>
              <div key="03" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>03</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>Xtream Codes eingeben</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Öffnen Sie Smarters Pro → 'Xtream Codes API' wählen → Server-URL, Benutzername und Passwort eingeben.</p>
                </div>
              </div>
              <div key="04" style={{ display: 'flex', gap: '20px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '52px', height: '52px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '1rem', flexShrink: 0 }}>04</div>
                <div>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '1rem', marginBottom: '6px' }}>Kanäle laden & genießen</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>Warten Sie bis die Kanalliste geladen ist (1–2 Min.) und starten Sie mit dem Streaming von 50.000+ Kanälen.</p>
                </div>
              </div>
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Empfohlene Apps</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '16px' }}>
              <div key="IPTV Smarters Pro" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>IPTV Smarters Pro</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Kostenlos</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Unterstützt Xtream Codes und M3U. Kostenlos, läuft auf allen Plattformen.</p>
              </div>
              <div key="Smarters Player Lite" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>Smarters Player Lite</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Leichtgewicht</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Leichte Version von Smarters Pro. Ideal für ältere Geräte.</p>
              </div>
              <div key="Smarters IPTV (iOS)" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem' }}>Smarters IPTV (iOS)</h3>
                  <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.68rem', fontWeight: 700, padding: '2px 8px', borderRadius: '99px' }}>Für iPhone</span>
                </div>
                <p style={{ color: '#8c8c8c', fontSize: '0.85rem', lineHeight: 1.65 }}>Offizielle iOS-Version für iPhone und iPad. Unterstützt alle Protokolle.</p>
              </div>
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <div key="Ist IPTV Smarters Pro kostenlo" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Ist IPTV Smarters Pro kostenlos?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>Ja, IPTV Smarters Pro ist vollständig kostenlos. Sie laden die App aus dem jeweiligen App Store und geben dann Ihre MOJO4K-Zugangsdaten ein. Es fallen keine zusätzlichen App-Kosten an.</p>
            </div>
            <div key="Auf welchen Geräten läuft IPTV" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Auf welchen Geräten läuft IPTV Smarters Pro?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>IPTV Smarters Pro läuft auf Amazon Fire TV Stick, Android TV, Android-Smartphones, iPhone, iPad, Windows PC, Mac und den meisten Smart TVs über den jeweiligen App Store.</p>
            </div>
            <div key="Was ist der Unterschied zwisch" style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
              <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>Was ist der Unterschied zwischen M3U und Xtream Codes?</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>Xtream Codes API ist die empfohlene Methode für MOJO4K – sie ermöglicht schnelleres Laden, VOD-Bibliotheken und EPG. M3U ist eine einfache Playlist-URL. Beides funktioniert mit Smarters Pro.</p>
            </div>
            </div>
          </section>

          <div style={{ background: 'linear-gradient(135deg, #1a0000, #0a0a0a)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '16px', padding: '40px', textAlign: 'center' }}>
            <h2 style={{ color: '#fff', fontWeight: 900, fontSize: '1.6rem', marginBottom: '12px' }}>Bereit zum Starten?</h2>
            <p style={{ color: '#aaa', marginBottom: '28px', lineHeight: 1.7 }}>Kostenlos testen – kein Vertrag, keine Kreditkarte. Aktivierung in Minuten.</p>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+möchte+IPTV+Smarters+Pro+mit+MOJO4K+einrichten`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 36px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block' }}>
              Kostenlos testen
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
