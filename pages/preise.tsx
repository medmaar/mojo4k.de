import Head from 'next/head'
import Link from 'next/link'
import { useState } from 'react'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const productSchema = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: 'MOJO4K Premium IPTV Abonnement',
  description: 'Premium IPTV Service in Deutschland mit 50.000+ Kanälen, 120.000+ VOD, 4K Ultra HD, EPG und 24/7 Support.',
  brand: { '@type': 'Brand', name: 'MOJO4K.DE' },
  aggregateRating: {
    '@type': 'AggregateRating',
    ratingValue: '4.9',
    reviewCount: '1090',
    bestRating: '5',
  },
  offers: {
    '@type': 'AggregateOffer',
    lowPrice: '15.99',
    highPrice: '99.99',
    priceCurrency: 'EUR',
    offerCount: '8',
    availability: 'https://schema.org/InStock',
  },
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'Preise', item: 'https://mojo4k.de/preise' },
  ],
}

const plans1 = [
  { name: '1 Monat', badge: 'Basisplan', price: '15,99', msg: '1-Monats-Abonnement+f%C3%BCr+1+Ger%C3%A4t', popular: false },
  { name: '3 Monate', badge: 'Standardplan', price: '25,99', msg: '3-Monats-Abonnement+f%C3%BCr+1+Ger%C3%A4t', popular: true },
  { name: '6 Monate', badge: 'Premium Plan', price: '39,99', msg: '6-Monats-Abonnement+f%C3%BCr+1+Ger%C3%A4t', popular: false },
  { name: '1 Jahr', badge: 'Goldplan', price: '59,99', msg: '1-Jahres-Abonnement+f%C3%BCr+1+Ger%C3%A4t', popular: false },
]
const plans2 = [
  { name: '1 Monat', badge: 'Basisplan (2)', price: '25,99', msg: '1-Monats-Abonnement+f%C3%BCr+2+Ger%C3%A4te', popular: false },
  { name: '3 Monate', badge: 'Standardplan (2)', price: '45,99', msg: '3-Monats-Abonnement+f%C3%BCr+2+Ger%C3%A4te', popular: true },
  { name: '6 Monate', badge: 'Premium Plan (2)', price: '69,99', msg: '6-Monats-Abonnement+f%C3%BCr+2+Ger%C3%A4te', popular: false },
  { name: '1 Jahr', badge: 'Gold Plan (2)', price: '99,99', msg: '1-Jahres-Abonnement+f%C3%BCr+2+Ger%C3%A4te', popular: false },
]
const features = ['+20.000 Kanäle', '+120.000 VOD (Filme & Serien)', 'SD-HD-FHD-4K', 'EPG', 'M3U / Enigma2', 'Schnelle Aktivierung', '24/7 Support']

function PlanGrid({ plans, devices }: { plans: typeof plans1, devices: string }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: '20px' }}>
      {plans.map(p => (
        <div key={p.name} style={{
          background: p.popular ? 'linear-gradient(145deg,#e53935,#b71c1c)' : '#111',
          border: `1px solid ${p.popular ? '#e53935' : '#1e1e1e'}`,
          borderRadius: '12px', padding: '28px', position: 'relative',
          boxShadow: p.popular ? '0 16px 48px rgba(229,57,53,0.25)' : 'none',
          transform: p.popular ? 'scale(1.03)' : 'none',
        }}>
          {p.popular && <div style={{ position: 'absolute', top: '-13px', left: '50%', transform: 'translateX(-50%)', background: '#fff', color: '#e53935', fontWeight: 800, fontSize: '0.73rem', padding: '4px 14px', borderRadius: '99px' }}>★ BELIEBT</div>}
          <p style={{ color: p.popular ? 'rgba(255,255,255,0.7)' : '#666', fontSize: '0.78rem', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '6px' }}>{p.badge}</p>
          <h3 style={{ color: '#fff', fontSize: '1.3rem', fontWeight: 900, marginBottom: '4px' }}>{p.name}</h3>
          <p style={{ color: p.popular ? 'rgba(255,255,255,0.6)' : '#555', fontSize: '0.82rem', marginBottom: '14px' }}>{devices}</p>
          <div style={{ color: '#fff', fontSize: '2.3rem', fontWeight: 900, marginBottom: '22px' }}>€{p.price}</div>
          <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px', display: 'flex', flexDirection: 'column', gap: '9px' }}>
            {features.map(f => (
              <li key={f} style={{ display: 'flex', alignItems: 'center', gap: '8px', color: p.popular ? 'rgba(255,255,255,0.88)' : '#999', fontSize: '0.85rem' }}>
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={p.popular ? '#fff' : '#e53935'} strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
                {f}
              </li>
            ))}
          </ul>
          <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+ein+${p.msg}+kaufen`} target="_blank" rel="noopener noreferrer"
            style={{ display: 'block', textAlign: 'center', background: p.popular ? '#fff' : '#e53935', color: p.popular ? '#e53935' : '#fff', fontWeight: 700, padding: '12px', borderRadius: '8px', fontSize: '0.9rem', textDecoration: 'none' }}>
            Jetzt kaufen
          </a>
          <p style={{ textAlign: 'center', color: p.popular ? 'rgba(255,255,255,0.5)' : '#444', fontSize: '0.73rem', marginTop: '10px' }}>1.090 Bewertungen ★★★★★</p>
        </div>
      ))}
    </div>
  )
}

export default function Preise() {
  const [tab, setTab] = useState<'1' | '2'>('1')
  return (
    <>
      <Head>
        <title>IPTV Preise 2026 – Ab €9/Monat | MOJO4K.DE</title>
        <meta name="description" content="IPTV Preise bei MOJO4K.DE – ab €9/Monat. 1 bis 2 Geräte, alle Pakete inkl. 50.000+ Kanäle, 120.000+ VOD in 4K. Jetzt kostenlos testen!" />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/preise/" />
        <meta property="og:title" content="IPTV Preise 2026 – Ab €9/Monat | MOJO4K.DE" />
        <meta property="og:description" content="IPTV Preise bei MOJO4K.DE – ab €9/Monat. 50.000+ Kanäle, 120.000+ VOD in 4K. Jetzt kostenlos testen!" />
        <meta property="og:url" content="https://mojo4k.de/preise/" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="IPTV Preise MOJO4K.DE" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="IPTV Preise 2026 – Ab €9/Monat | MOJO4K.DE" />
        <meta name="twitter:description" content="IPTV Preise bei MOJO4K.DE – ab €9/Monat. 50.000+ Kanäle, 120.000+ VOD in 4K." />
        <meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta name="author" content="MOJO4K.DE" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon.svg" />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(productSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      </Head>
      <div style={{ background: '#0a0a0a', minHeight: '100vh', paddingTop: '64px' }}>
        {/* Navbar */}
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

        <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '60px 16px 80px' }}>
          <div style={{ textAlign: 'center', marginBottom: '48px' }}>
            <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>PREISGESTALTUNG</p>
            <h1 style={{ color: '#fff', fontSize: 'clamp(1.8rem, 3vw, 2.8rem)', fontWeight: 900, marginTop: '12px', marginBottom: '16px' }}>
              Sie können unsere Dienste auf allen Geräten nutzen
            </h1>
            {/* Tab switcher */}
            <div style={{ display: 'inline-flex', background: '#111', border: '1px solid #222', borderRadius: '10px', padding: '4px', marginTop: '16px' }}>
              <button onClick={() => setTab('1')} style={{ padding: '10px 28px', borderRadius: '8px', fontWeight: 700, fontSize: '0.9rem', border: 'none', cursor: 'pointer', background: tab === '1' ? '#e53935' : 'transparent', color: tab === '1' ? '#fff' : '#888', transition: 'all 0.2s' }}>
                1 Gerät
              </button>
              <button onClick={() => setTab('2')} style={{ padding: '10px 28px', borderRadius: '8px', fontWeight: 700, fontSize: '0.9rem', border: 'none', cursor: 'pointer', background: tab === '2' ? '#e53935' : 'transparent', color: tab === '2' ? '#fff' : '#888', transition: 'all 0.2s' }}>
                2 Geräte
              </button>
            </div>
          </div>
          {tab === '1' ? <PlanGrid plans={plans1} devices="1 Gerät" /> : <PlanGrid plans={plans2} devices="2 Geräte" />}
          <p style={{ textAlign: 'center', color: '#444', fontSize: '0.83rem', marginTop: '32px' }}>
            ✅ 24h kostenloser Testaccount verfügbar – kein Abo, keine Kreditkarte nötig
          </p>
        </div>
      </div>
    </>
  )
}
