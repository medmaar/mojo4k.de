import Head from 'next/head'
import Link from 'next/link'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

export default function Kontakt() {
  return (
    <>
      <Head>
        <title>Kontakt – 24/7 Support via WhatsApp | MOJO4K.DE</title>
        <meta name="description" content="Kontaktieren Sie MOJO4K.DE – 24/7 Support via WhatsApp oder E-Mail. Schnelle Hilfe bei allen IPTV-Fragen." />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/kontakt/" />
        <meta property="og:title" content="Kontakt – 24/7 Support via WhatsApp | MOJO4K.DE" />
        <meta property="og:description" content="Kontaktieren Sie MOJO4K.DE – 24/7 Support via WhatsApp oder E-Mail. Schnelle Hilfe bei allen IPTV-Fragen." />
        <meta property="og:url" content="https://mojo4k.de/kontakt/" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="MOJO4K.DE Kontakt und Support" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kontakt – 24/7 Support via WhatsApp | MOJO4K.DE" />
        <meta name="twitter:description" content="Kontaktieren Sie MOJO4K.DE – 24/7 Support via WhatsApp oder E-Mail." />
        <meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta name="author" content="MOJO4K.DE" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon.svg" />
      </Head>
      <div style={{ background: '#0a0a0a', minHeight: '100vh', paddingTop: '64px' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50 }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '64px' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>MOJO4K</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <div style={{ display: 'flex', gap: '32px' }}>
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([href, label]) => (
                <Link key={href} href={href} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{label}</Link>
              ))}
            </div>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
              Kostenloser Test
            </a>
          </div>
        </nav>
        <div style={{ maxWidth: '760px', margin: '0 auto', padding: '60px 16px 80px', textAlign: 'center' }}>
          <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>Kontakt</p>
          <h1 style={{ color: '#fff', fontSize: 'clamp(1.8rem, 3vw, 2.8rem)', fontWeight: 900, marginTop: '12px', marginBottom: '16px' }}>
            Kontaktiere uns
          </h1>
          <p style={{ color: '#8c8c8c', lineHeight: 1.75, marginBottom: '48px' }}>
            Unser Support-Team ist 7 Tage die Woche für Sie erreichbar. Schreiben Sie uns einfach über einen der folgenden Kanäle.
          </p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: '20px', marginBottom: '48px' }}>
            {[
              { icon: '💬', label: 'WhatsApp', val: 'Klicken zum Schreiben', href: `${WA}&text=Hallo+MOJO4K%2C+ich+habe+eine+Frage`, color: '#25D366' },
              { icon: '✉️', label: 'E-Mail', val: 'info[at]mojo4k.de', href: '#email', color: '#e53935' },
            ].map(c => (
              <a key={c.label} href={c.href} target="_blank" rel="noopener noreferrer"
                style={{ background: '#111', border: `1px solid #1e1e1e`, borderRadius: '12px', padding: '32px', textDecoration: 'none', display: 'block', transition: 'border-color 0.2s' }}
                onMouseEnter={e => (e.currentTarget.style.borderColor = c.color)}
                onMouseLeave={e => (e.currentTarget.style.borderColor = '#1e1e1e')}>
                <div style={{ fontSize: '2.5rem', marginBottom: '14px' }}>{c.icon}</div>
                <div style={{ color: '#fff', fontWeight: 700, fontSize: '1.05rem', marginBottom: '6px' }}>{c.label}</div>
                <div style={{ color: '#666', fontSize: '0.88rem' }}>{c.val}</div>
              </a>
            ))}
          </div>
          <div style={{ background: 'linear-gradient(135deg, rgba(229,57,53,0.15), rgba(229,57,53,0.05))', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '12px', padding: '36px' }}>
            <h3 style={{ color: '#fff', fontWeight: 800, marginBottom: '12px', fontSize: '1.2rem' }}>Kostenlos testen</h3>
            <p style={{ color: '#888', marginBottom: '24px', fontSize: '0.92rem', lineHeight: 1.7 }}>
              Noch unentschlossen? Holen Sie sich Ihren kostenlosen 24-Stunden-Testaccount und überzeugen Sie sich selbst!
            </p>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+den+Service+kostenlos+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 36px', borderRadius: '8px', textDecoration: 'none', fontSize: '1rem', display: 'inline-block' }}>
              Jetzt kostenlos testen
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
