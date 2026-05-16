import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Was ist eine IPTV M3U Playlist?', acceptedAnswer: { '@type': 'Answer', text: 'Eine M3U Playlist ist eine Textdatei mit URLs zu IPTV-Streams. Sie enthält alle Kanäle Ihres IPTV-Anbieters und kann in Apps wie TiviMate, Smarters Pro oder VLC eingefügt werden. IPTVV stellt nach dem Kauf eine persönliche M3U-URL zur Verfügung.' } },
    { '@type': 'Question', name: 'Wo bekomme ich eine IPTV M3U Playlist für Deutschland?', acceptedAnswer: { '@type': 'Answer', text: 'Mit einem IPTVV-Abonnement erhalten Sie eine persönliche M3U-URL mit 50.000+ deutschen und internationalen Kanälen. Die URL wird nach dem Kauf sofort per WhatsApp zugeschickt.' } },
    { '@type': 'Question', name: 'In welche Apps kann ich die M3U URL eingeben?', acceptedAnswer: { '@type': 'Answer', text: 'Die M3U-URL funktioniert mit TiviMate, IPTV Smarters Pro, GSE Smart IPTV, VLC, Kodi (PVR IPTV Simple Client), Smart IPTV (Samsung/LG) und SS IPTV. Fast jeder IPTV-Player unterstützt M3U.' } },
    { '@type': 'Question', name: 'Was ist der Unterschied zwischen M3U und Xtream Codes?', acceptedAnswer: { '@type': 'Answer', text: 'M3U ist eine einfache Playlist-URL – universell, funktioniert überall. Xtream Codes ist ein API-Protokoll, das zusätzlich VOD-Bibliotheken, EPG und schnelleres Laden ermöglicht. IPTVV unterstützt beide Methoden.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://iptvv.de' },
    { '@type': 'ListItem', position: 2, name: 'IPTV M3U Playlist Deutschland', item: 'https://iptvv.de/iptv-m3u-playlist-deutschland' },
  ],
}

const compatibleApps = [
  { name: 'TiviMate', devices: 'Fire Stick, Android TV', note: 'Bestes EPG-Design' },
  { name: 'IPTV Smarters Pro', devices: 'Alle Plattformen', note: 'Kostenlos' },
  { name: 'GSE Smart IPTV', devices: 'iOS, Android', note: 'Sehr flexibel' },
  { name: 'VLC Media Player', devices: 'Windows, Mac, Linux', note: 'Gratis, überall' },
  { name: 'SS IPTV', devices: 'Samsung, LG webOS', note: 'Für Smart TVs' },
  { name: 'Kodi + PVR Plugin', devices: 'Windows, Mac, Android', note: 'Open Source' },
  { name: 'Smart IPTV', devices: 'Samsung, LG', note: 'Im TV App Store' },
  { name: 'Enigma2 (E2m3u2bouquet)', devices: 'VU+, GigaBlue, Dreambox', note: 'Für Receiver' },
]

export default function IPTVm3u() {
  return (
    <>
      <Head>
        <title>IPTV M3U Playlist Deutschland 2026 – URL für alle Apps | IPTVV.DE</title>
        <meta name="description" content="IPTV M3U Playlist für Deutschland 2026. Persönliche M3U-URL mit 50.000+ Kanälen für TiviMate, Smarters Pro, VLC, Kodi & Smart TV. Jetzt kostenlos testen bei IPTVV.DE!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://iptvv.de/iptv-m3u-playlist-deutschland" />
        <meta property="og:title" content="IPTV M3U Playlist Deutschland 2026 – URL für alle Apps | IPTVV.DE" />
        <meta property="og:description" content="IPTV M3U Playlist für Deutschland 2026. Persönliche M3U-URL mit 50.000+ Kanälen für TiviMate, Smarters Pro, VLC & Smart TV. Kostenlos testen!" />
        <meta property="og:url" content="https://iptvv.de/iptv-m3u-playlist-deutschland" />
        <meta property="og:type" content="article" />
        <meta property="og:site_name" content="IPTVV.DE" />
        <meta property="og:locale" content="de_DE" />
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
            <div style={{ display: 'flex', gap: '32px' }} className="hidden-mobile">
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([h, l]) => (
                <Link key={h} href={h} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{l}</Link>
              ))}
            </div>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+eine+M3U+Playlist+f%C3%BCr+Deutschland`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
              M3U URL anfordern
            </a>
          </div>
        </nav>

        <div style={{ maxWidth: '900px', margin: '0 auto', padding: '100px 16px 80px' }}>
          <nav aria-label="Breadcrumb" style={{ marginBottom: '32px' }}>
            <ol style={{ listStyle: 'none', display: 'flex', gap: '8px', fontSize: '0.82rem', color: '#555' }}>
              <li><Link href="/" style={{ color: '#555', textDecoration: 'none' }}>Startseite</Link></li>
              <li>›</li>
              <li style={{ color: '#e53935' }}>IPTV M3U Playlist Deutschland</li>
            </ol>
          </nav>

          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '5px 14px', marginBottom: '20px' }}>
            <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 600 }}>📋 M3U Playlist Guide</span>
          </div>

          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.8rem)', fontWeight: 900, lineHeight: 1.15, marginBottom: '20px' }}>
            IPTV <span style={{ color: '#e53935' }}>M3U Playlist</span> Deutschland – Persönliche URL für alle IPTV-Apps 2026
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
            Mit einem IPTVV-Abonnement erhalten Sie eine persönliche M3U-URL mit 50.000+ deutschen und internationalen Kanälen. Einfach in TiviMate, Smarters Pro, VLC oder Ihren Smart TV eingeben – fertig.
          </p>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '20px' }}>Was ist eine M3U Playlist?</h2>
            <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px', marginBottom: '20px' }}>
              <p style={{ color: '#aaa', lineHeight: 1.8, marginBottom: '16px', fontSize: '0.95rem' }}>
                Eine M3U-Datei (oder M3U-URL) ist eine Playlist, die Ihrem IPTV-Player sagt, wo er die Videostreams findet. Jede Zeile enthält einen Kanal mit Name und Stream-URL. So sieht das Format aus:
              </p>
              <div style={{ background: '#0a0a0a', border: '1px solid #222', borderRadius: '8px', padding: '16px', fontFamily: 'monospace', fontSize: '0.82rem', color: '#4caf50' }}>
                <div>#EXTM3U</div>
                <div>#EXTINF:-1 tvg-name="ARD" group-title="Deutschland",ARD Das Erste</div>
                <div style={{ color: '#666' }}>http://server.iptvv.de:8080/ARD/stream.ts</div>
                <div style={{ marginTop: '8px' }}>#EXTINF:-1 tvg-name="ZDF" group-title="Deutschland",ZDF</div>
                <div style={{ color: '#666' }}>http://server.iptvv.de:8080/ZDF/stream.ts</div>
              </div>
              <p style={{ color: '#555', fontSize: '0.8rem', marginTop: '10px' }}>Hinweis: Dies ist ein Beispiel. Ihre persönliche M3U-URL enthält alle 50.000+ Kanäle.</p>
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '28px' }}>So bekommen Sie Ihre persönliche M3U-URL</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {[
                { n: '01', t: 'Abonnement kaufen', d: 'Wählen Sie ein IPTVV-Paket ab €15,99/Monat. Zahlung und Aktivierung via WhatsApp.' },
                { n: '02', t: 'M3U-URL erhalten', d: 'Innerhalb von Minuten erhalten Sie Ihre persönliche M3U-URL per WhatsApp. Format: http://server/get.php?username=XXX&password=YYY&type=m3u' },
                { n: '03', t: 'In Ihre App eingeben', d: 'Kopieren Sie die URL in TiviMate, Smarters Pro, VLC oder eine andere kompatible App. Kanäle laden automatisch.' },
              ].map(s => (
                <div key={s.n} style={{ display: 'flex', gap: '16px', alignItems: 'flex-start', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '20px' }}>
                  <div style={{ width: '44px', height: '44px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: '#e53935', fontSize: '0.9rem', flexShrink: 0 }}>{s.n}</div>
                  <div>
                    <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '5px' }}>{s.t}</h3>
                    <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{s.d}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Kompatible Apps & Geräte</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '12px' }}>
              {compatibleApps.map(a => (
                <div key={a.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '16px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <div style={{ color: '#fff', fontWeight: 700, fontSize: '0.9rem' }}>{a.name}</div>
                    <div style={{ color: '#555', fontSize: '0.78rem', marginTop: '2px' }}>{a.devices}</div>
                  </div>
                  <span style={{ background: 'rgba(229,57,53,0.12)', color: '#e53935', fontSize: '0.7rem', fontWeight: 600, padding: '2px 8px', borderRadius: '99px', flexShrink: 0 }}>{a.note}</span>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '20px' }}>M3U vs. Xtream Codes – Was ist besser?</h2>
            <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', overflow: 'hidden' }}>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', background: '#0d0d0d', padding: '13px 22px', borderBottom: '1px solid #1a1a1a' }}>
                <span style={{ color: '#555', fontSize: '0.8rem', fontWeight: 700 }}>Feature</span>
                <span style={{ color: '#e53935', fontSize: '0.8rem', fontWeight: 700 }}>M3U URL</span>
                <span style={{ color: '#888', fontSize: '0.8rem', fontWeight: 700 }}>Xtream Codes</span>
              </div>
              {[
                ['Kompatibilität', '✅ Überall (VLC, Kodi)', 'Apps mit Xtream-Support'],
                ['VOD (Filme & Serien)', '⚠️ Eingeschränkt', '✅ Vollständige Bibliothek'],
                ['EPG-Geschwindigkeit', 'Mittel', '✅ Schneller'],
                ['Empfehlung für...', 'Smart TV, VLC, Kodi', 'TiviMate, Smarters Pro'],
                ['IPTVV Support', '✅ Ja', '✅ Ja'],
              ].map(([feat, m3u, xtream], i) => (
                <div key={feat} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', padding: '13px 22px', borderBottom: i < 4 ? '1px solid #1a1a1a' : 'none' }}>
                  <span style={{ color: '#666', fontSize: '0.85rem' }}>{feat}</span>
                  <span style={{ color: '#ccc', fontSize: '0.85rem' }}>{m3u}</span>
                  <span style={{ color: '#8c8c8c', fontSize: '0.85rem' }}>{xtream}</span>
                </div>
              ))}
            </div>
          </section>

          <section style={{ marginBottom: '56px' }}>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 900, marginBottom: '24px' }}>Häufige Fragen zur M3U Playlist</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {faqSchema.mainEntity.map((f: any) => (
                <div key={f.name} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '20px' }}>
                  <h3 style={{ color: '#fff', fontWeight: 700, fontSize: '0.95rem', marginBottom: '8px' }}>{f.name}</h3>
                  <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{f.acceptedAnswer.text}</p>
                </div>
              ))}
            </div>
          </section>

          <div style={{ background: 'linear-gradient(135deg, #1a0000, #0a0a0a)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '16px', padding: '40px', textAlign: 'center' }}>
            <h2 style={{ color: '#fff', fontWeight: 900, fontSize: '1.6rem', marginBottom: '12px' }}>M3U Playlist anfordern</h2>
            <p style={{ color: '#aaa', marginBottom: '28px', lineHeight: 1.7 }}>Kaufen Sie ein IPTVV-Abonnement und erhalten Sie Ihre persönliche M3U-URL in Minuten.</p>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+eine+M3U+Playlist+f%C3%BCr+Deutschland+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 36px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-block' }}>
              Kostenlos testen – M3U URL erhalten
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
