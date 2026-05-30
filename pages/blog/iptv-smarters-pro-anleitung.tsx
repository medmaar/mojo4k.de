import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const articleSchema = {
  '@context': 'https://schema.org',
  '@type': 'Article',
  headline: 'IPTV Smarters Pro Anleitung 2026 – Einrichtung auf allen Geräten',
  description: 'Komplette Schritt-für-Schritt Anleitung für IPTV Smarters Pro auf Fire Stick, Android, iPhone und Smart TV. Mit Screenshots und Tipps.',
  author: { '@type': 'Organization', name: 'MOJO4K.DE' },
  publisher: { '@type': 'Organization', name: 'MOJO4K.DE', url: 'https://mojo4k.de' },
  datePublished: '2026-01-10',
  dateModified: '2026-05-28',
}

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: [
    { '@type': 'Question', name: 'Was ist IPTV Smarters Pro?', acceptedAnswer: { '@type': 'Answer', text: 'IPTV Smarters Pro ist eine der beliebtesten IPTV-Player-Apps, die auf Android, iOS, Fire TV Stick und Smart TVs läuft. Sie ermöglicht das Abspielen von M3U-Playlisten und Xtream Codes.' } },
    { '@type': 'Question', name: 'Ist IPTV Smarters Pro kostenlos?', acceptedAnswer: { '@type': 'Answer', text: 'Ja, IPTV Smarters Pro ist kostenlos im Google Play Store, Amazon App Store und App Store erhältlich. Sie benötigen lediglich ein IPTV-Abonnement wie MOJO4K.' } },
    { '@type': 'Question', name: 'Wie richte ich IPTV Smarters Pro mit MOJO4K ein?', acceptedAnswer: { '@type': 'Answer', text: 'Laden Sie die App herunter, wählen Sie "Xtream Codes API" und geben Sie Server-URL, Benutzername und Passwort ein, die Sie nach Ihrem MOJO4K-Kauf per WhatsApp erhalten.' } },
  ],
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'Blog', item: 'https://mojo4k.de/blog' },
    { '@type': 'ListItem', position: 3, name: 'IPTV Smarters Pro Anleitung', item: 'https://mojo4k.de/blog/iptv-smarters-pro-anleitung' },
  ],
}

const steps = [
  {
    title: 'App herunterladen',
    content: 'Suchen Sie im Google Play Store, Amazon App Store oder Apple App Store nach "IPTV Smarters Pro" und installieren Sie die App kostenlos auf Ihrem Gerät.',
  },
  {
    title: 'App öffnen und Anmeldemethode wählen',
    content: 'Öffnen Sie die App. Sie sehen drei Anmeldeoptionen: "Xtream Codes API", "M3U URL" und "External Player". Wählen Sie "Xtream Codes API" für die beste Erfahrung mit MOJO4K.',
  },
  {
    title: 'Zugangsdaten eingeben',
    content: 'Geben Sie einen beliebigen Namen ein (z. B. "MOJO4K"), dann Server-URL, Benutzername und Passwort. Diese Daten erhalten Sie nach Ihrer Bestellung per WhatsApp oder E-Mail.',
  },
  {
    title: 'Kanäle laden und genießen',
    content: 'Tippen Sie auf "Hinzufügen". Die App lädt alle Kanäle, VOD-Inhalte und das EPG automatisch. Navigieren Sie zu Live-TV, Filme oder Serien und starten Sie das Streaming.',
  },
]

export default function IptvSmartersProAnleitung() {
  return (
    <>
      <Head>
        <title>IPTV Smarters Pro Anleitung 2026 – Einrichtung | MOJO4K.DE</title>
        <meta name="description" content="IPTV Smarters Pro einrichten 2026: Anleitung für Fire Stick, Android & iPhone. Xtream Codes & M3U erklärt. Mit MOJO4K kostenlos testen!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/blog/iptv-smarters-pro-anleitung/" />
        <meta property="og:title" content="IPTV Smarters Pro Anleitung 2026 – Einrichtung auf allen Geräten | MOJO4K.DE" />
        <meta property="og:description" content="Schritt-für-Schritt Anleitung für IPTV Smarters Pro. Fire Stick, Android, iPhone & Smart TV. Mit MOJO4K kostenlos testen!" />
        <meta property="og:url" content="https://mojo4k.de/blog/iptv-smarters-pro-anleitung/" />
        <meta property="og:type" content="article" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="IPTV Smarters Pro Anleitung – MOJO4K" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="IPTV Smarters Pro Anleitung 2026 – Einrichtung | MOJO4K.DE" />
        <meta name="twitter:description" content="Schritt-für-Schritt Anleitung für IPTV Smarters Pro auf allen Geräten. Mit MOJO4K kostenlos testen!" />
        <meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      </Head>

      <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, height: '64px', display: 'flex', alignItems: 'center' }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
          <Link href="/" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center' }}>
            <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>MOJO4K</span>
            <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
          </Link>
          <div style={{ display: 'flex', gap: '28px' }} className="hidden-mobile">
            {[['/', 'Heim'], ['/preise/', 'Preise'], ['/blog/', 'Blog'], ['/faqs/', 'FAQs']].map(([href, label]) => (
              <Link key={href} href={href} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{label}</Link>
            ))}
          </div>
        </div>
      </nav>

      <main style={{ maxWidth: '860px', margin: '0 auto', padding: '100px 16px 80px' }}>
        <nav aria-label="Breadcrumb" style={{ marginBottom: '24px', fontSize: '0.85rem', color: '#666' }}>
          <Link href="/" style={{ color: '#666', textDecoration: 'none' }}>Startseite</Link>
          <span style={{ margin: '0 8px' }}>›</span>
          <Link href="/blog/" style={{ color: '#666', textDecoration: 'none' }}>Blog</Link>
          <span style={{ margin: '0 8px' }}>›</span>
          <span style={{ color: '#aaa' }}>IPTV Smarters Pro Anleitung</span>
        </nav>

        <div style={{ display: 'flex', gap: '10px', alignItems: 'center', marginBottom: '16px' }}>
          <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.72rem', fontWeight: 700, padding: '3px 10px', borderRadius: '99px' }}>Anleitung</span>
          <span style={{ color: '#444', fontSize: '0.8rem' }}>2026-01-10</span>
        </div>

        <h1 style={{ fontSize: 'clamp(1.7rem, 3.5vw, 2.4rem)', fontWeight: 900, lineHeight: 1.2, marginBottom: '16px' }}>
          IPTV Smarters Pro Anleitung 2026 – Einrichtung auf allen Geräten
        </h1>
        <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '40px', maxWidth: '680px' }}>
          Komplette Schritt-für-Schritt Anleitung für IPTV Smarters Pro auf Fire Stick, Android, iPhone und Smart TV. Mit Screenshots und Tipps für das beste Streaming-Erlebnis mit MOJO4K.
        </p>

        <section style={{ marginBottom: '48px' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '24px' }}>Einrichtung in 4 Schritten</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {steps.map((step, i) => (
              <div key={i} style={{ display: 'flex', gap: '20px', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '24px' }}>
                <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'rgba(229,57,53,0.15)', border: '1px solid rgba(229,57,53,0.3)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, color: '#e53935', fontWeight: 900, fontSize: '1rem' }}>{i + 1}</div>
                <div>
                  <h3 style={{ fontWeight: 700, marginBottom: '8px', fontSize: '1rem' }}>{step.title}</h3>
                  <p style={{ color: '#aaa', lineHeight: 1.7, fontSize: '0.95rem' }}>{step.content}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section style={{ marginBottom: '48px' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '20px' }}>Häufig gestellte Fragen</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {[
              { q: 'Was ist IPTV Smarters Pro?', a: 'IPTV Smarters Pro ist eine der beliebtesten IPTV-Player-Apps, die auf Android, iOS, Fire TV Stick und Smart TVs läuft. Sie ermöglicht das Abspielen von M3U-Playlisten und Xtream Codes.' },
              { q: 'Ist IPTV Smarters Pro kostenlos?', a: 'Ja, die App ist kostenlos. Sie benötigen lediglich ein IPTV-Abonnement wie MOJO4K, um Inhalte zu streamen.' },
              { q: 'Wie richte ich IPTV Smarters Pro mit MOJO4K ein?', a: 'Laden Sie die App herunter, wählen Sie "Xtream Codes API" und geben Sie die Zugangsdaten ein, die Sie nach Ihrer MOJO4K-Bestellung per WhatsApp erhalten.' },
            ].map((faq, i) => (
              <details key={i} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '10px', padding: '18px 22px' }}>
                <summary style={{ fontWeight: 700, cursor: 'pointer', fontSize: '0.95rem', listStyle: 'none' }}>{faq.q}</summary>
                <p style={{ color: '#aaa', marginTop: '12px', lineHeight: 1.7, fontSize: '0.9rem' }}>{faq.a}</p>
              </details>
            ))}
          </div>
        </section>

        <div style={{ background: 'linear-gradient(135deg, #1a0000, #0a0a0a)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '16px', padding: '32px', textAlign: 'center' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 900, marginBottom: '12px' }}>MOJO4K kostenlos testen</h2>
          <p style={{ color: '#aaa', marginBottom: '24px' }}>Kein Abonnement nötig – 24h gratis, ohne Kreditkarte.</p>
          <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+möchte+IPTV+Smarters+Pro+testen`} target="_blank" rel="noopener noreferrer"
            style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: '#25D366', color: '#fff', fontWeight: 700, padding: '14px 32px', borderRadius: '8px', textDecoration: 'none', fontSize: '1rem' }}>
            Jetzt kostenlos testen
          </a>
        </div>

        <div style={{ marginTop: '48px', paddingTop: '32px', borderTop: '1px solid #1e1e1e' }}>
          <Link href="/blog/" style={{ color: '#e53935', textDecoration: 'none', fontWeight: 600, fontSize: '0.9rem' }}>← Zurück zum Blog</Link>
        </div>
      </main>
    </>
  )
}
