import Head from 'next/head'
import Link from 'next/link'
import { useState } from 'react'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

function Navbar() {
  return (
    <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50 }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '64px' }}>
        <Link href="/" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center' }}>
          <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>IPTVV</span>
          <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
        </Link>
        <div style={{ display: 'flex', alignItems: 'center', gap: '32px' }} className="hidden-mobile">
          {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([href, label]) => (
            <Link key={href} href={href} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{label}</Link>
          ))}
        </div>
        <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+den+Service+gerne+testen`} target="_blank" rel="noopener noreferrer"
          style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
          Kostenloser Test
        </a>
      </div>
    </nav>
  )
}

function Hero() {
  return (
    <section style={{ background: 'linear-gradient(135deg, #0a0a0a 0%, #1a0000 60%, #0a0a0a 100%)', paddingTop: '100px', paddingBottom: '80px', position: 'relative', overflow: 'hidden' }}>
      <img
        src="/hero-mobile.webp"
        alt=""
        aria-hidden="true"
        fetchPriority="high"
        decoding="sync"
        style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center', opacity: 0.08, zIndex: 0 }}
      />
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '48px', position: 'relative', zIndex: 1 }}>
        <div style={{ flex: '1 1 400px' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', background: 'rgba(229,57,53,0.12)', border: '1px solid rgba(229,57,53,0.3)', borderRadius: '99px', padding: '6px 16px', marginBottom: '24px' }}>
            <span style={{ width: '8px', height: '8px', background: '#e53935', borderRadius: '50%', display: 'inline-block' }} />
            <span style={{ color: '#e53935', fontSize: '0.83rem', fontWeight: 600 }}>Zufriedene Kunden 4.9 ★★★★★ (1.090)</span>
          </div>
          <h1 style={{ fontSize: 'clamp(1.9rem, 4vw, 3.2rem)', fontWeight: 900, lineHeight: 1.15, color: '#fff', marginBottom: '20px' }}>
            IPTV kaufen bei <span style={{ color: '#e53935' }}>IPTVV Premium</span> – der beste IPTV-Service in Deutschland
          </h1>
          <p style={{ color: '#aaa', fontSize: '1.05rem', lineHeight: 1.75, marginBottom: '36px', maxWidth: '540px' }}>
            Verbessern Sie Ihr Streaming-Erlebnis mit IPTVV Premium. Zuverlässige globale Server, kein Einfrieren, keine Pufferung, kristallklare 4K-Qualität und täglich aktualisierte Inhalte mit Filmen, Serien, Sport und Live-TV.
          </p>
          <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
            <Link href="/preise" style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '14px 32px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none' }}>
              Jetzt starten
            </Link>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+den+Service+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#25D366', color: '#fff', fontWeight: 700, padding: '14px 32px', borderRadius: '8px', fontSize: '1rem', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
              Kostenloser Test
            </a>
          </div>
        </div>
        <div style={{ flex: '1 1 280px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px', maxWidth: '340px' }}>
          {[{ val: '+22.000', label: 'TV-Kanäle' }, { val: '+120.000', label: 'VOD Titel' }, { val: '4K Ultra HD', label: 'Qualität' }, { val: '99,9%', label: 'Verfügbarkeit' }].map(s => (
            <div key={s.label} style={{ background: '#111', border: '1px solid #222', borderRadius: '12px', padding: '22px', textAlign: 'center' }}>
              <div style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>{s.val}</div>
              <div style={{ color: '#8c8c8c', fontSize: '0.8rem', marginTop: '4px' }}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

function Features() {
  const items = [
    { icon: '📺', title: 'BESTE QUALITÄT', desc: 'Sehen Sie sich alle Lieblingsserien, Filme und Kanäle in hoher 4K-Qualität an.' },
    { icon: '📡', title: 'PREMIUM-KANÄLE', desc: 'Mehr als +22.000 TV-Kanäle. Die beste Sendequalität aller Zeiten.' },
    { icon: '🎬', title: 'VOD FERNSEHSERIE', desc: 'Über 120.000 Filme & Serien auf Ihrem Gerät – jederzeit abrufbar.' },
    { icon: '⚡', title: 'SOFORTIGE INSTALLATION', desc: 'Wenige Augenblicke nach Ihrer Bestellung ist der Service einsatzbereit.' },
    { icon: '🎯', title: 'ALLES IN EINEM', desc: 'Netflix, Disney+, Hulu und mehr — alles in einem Dienst gebündelt.' },
    { icon: '🛡️', title: '7/7 LIVE-SUPPORT', desc: 'Rund um die Uhr für Sie da. Kontaktieren Sie uns jederzeit.' },
  ]
  return (
    <section style={{ background: '#0d0d0d', padding: '80px 0' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px' }}>
        <div style={{ textAlign: 'center', marginBottom: '56px' }}>
          <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>Warum IPTVV.DE?</p>
          <h2 style={{ color: '#fff', fontSize: 'clamp(1.7rem, 3vw, 2.4rem)', fontWeight: 900, marginTop: '12px', marginBottom: '16px' }}>
            Warum IPTVV der führende IPTV-Service in Deutschland ist
          </h2>
          <p style={{ color: '#8c8c8c', maxWidth: '580px', margin: '0 auto', lineHeight: 1.75 }}>
            Tauchen Sie ein in 4K-Bildqualität auf jedem Gerät. Mehr als 22.000 Kanäle, 120.000+ VODs und 100% Verfügbarkeit ohne Pufferung oder Einfrieren.
          </p>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '20px', marginBottom: '32px' }}>
          {items.map(item => (
            <div key={item.title} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px', cursor: 'default', transition: 'border-color 0.2s' }}
              onMouseEnter={e => (e.currentTarget.style.borderColor = '#e53935')}
              onMouseLeave={e => (e.currentTarget.style.borderColor = '#1e1e1e')}>
              <div style={{ fontSize: '2.2rem', marginBottom: '14px' }}>{item.icon}</div>
              <h3 style={{ color: '#fff', fontWeight: 800, fontSize: '0.9rem', letterSpacing: '1px', marginBottom: '10px' }}>{item.title}</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>{item.desc}</p>
            </div>
          ))}
        </div>
        <div style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '36px', display: 'flex', flexWrap: 'wrap', gap: '20px', justifyContent: 'center' }}>
          {['+20.000 Kanäle', 'SD-HD-FHD-4K', '+120.000 VOD', 'EPG verfügbar', 'M3U / Enigma2', 'AntiFreeze-Technologie'].map(f => (
            <span key={f} style={{ display: 'inline-flex', alignItems: 'center', gap: '7px', color: '#bbb', fontSize: '0.92rem' }}>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#e53935" strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
              {f}
            </span>
          ))}
        </div>
      </div>
    </section>
  )
}

function HowItWorks() {
  const steps = [
    { n: '01', title: 'Wählen Sie Ihr Paket', desc: 'Wählen Sie das für Sie passende Abonnement aus unseren Preisplänen.' },
    { n: '02', title: 'Zahlung abschließen', desc: 'Kontaktieren Sie uns via WhatsApp und leisten Sie die Zahlung.' },
    { n: '03', title: 'Zugangsdaten erhalten', desc: 'Wir senden Ihnen die Zugangsdaten mit Installationsanleitung.' },
    { n: '04', title: 'Einloggen & Genießen', desc: 'Melden Sie sich an und genießen Sie tausende Sender sofort.' },
  ]
  return (
    <section style={{ background: '#080808', padding: '80px 0' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px' }}>
        <div style={{ textAlign: 'center', marginBottom: '56px' }}>
          <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>Wie es funktioniert</p>
          <h2 style={{ color: '#fff', fontSize: 'clamp(1.7rem, 3vw, 2.4rem)', fontWeight: 900, marginTop: '12px' }}>
            IPTV Kaufen und greifen Sie zu
          </h2>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: '32px' }}>
          {steps.map(s => (
            <div key={s.n} style={{ textAlign: 'center' }}>
              <div style={{ width: '64px', height: '64px', background: 'rgba(229,57,53,0.1)', border: '2px solid #e53935', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 20px', fontSize: '1.2rem', fontWeight: 900, color: '#e53935' }}>{s.n}</div>
              <h3 style={{ color: '#fff', fontWeight: 700, marginBottom: '10px', fontSize: '1rem' }}>{s.title}</h3>
              <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>{s.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

function PricingSection() {
  const plans = [
    { name: '1 Monat', badge: 'Basisplan', price: '15,99', msg: 'ich+m%C3%B6chte+ein+1-Monats-Abonnement+kaufen', popular: false },
    { name: '3 Monate', badge: 'Standardplan', price: '25,99', msg: 'ich+m%C3%B6chte+ein+3-Monats-Abonnement+kaufen', popular: true },
    { name: '6 Monate', badge: 'Premium Plan', price: '39,99', msg: 'ich+m%C3%B6chte+ein+6-Monats-Abonnement+kaufen', popular: false },
    { name: '1 Jahr', badge: 'Goldplan', price: '59,99', msg: 'ich+m%C3%B6chte+ein+1-Jahres-Abonnement+kaufen', popular: false },
  ]
  const features = ['+20.000 Kanäle', '+120.000 VOD', 'SD-HD-FHD-4K', 'EPG', 'M3U / Enigma2', 'Schnelle Aktivierung', '24/7 Support']
  return (
    <section id="preise" style={{ background: '#0d0d0d', padding: '80px 0' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px' }}>
        <div style={{ textAlign: 'center', marginBottom: '56px' }}>
          <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>PREISGESTALTUNG</p>
          <h2 style={{ color: '#fff', fontSize: 'clamp(1.7rem, 3vw, 2.4rem)', fontWeight: 900, marginTop: '12px' }}>
            Unsere Pakete – <span style={{ color: '#e53935' }}>transparent & fair</span>
          </h2>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: '20px' }}>
          {plans.map(p => (
            <div key={p.name} style={{
              background: p.popular ? 'linear-gradient(145deg,#e53935,#b71c1c)' : '#111',
              border: `1px solid ${p.popular ? '#e53935' : '#1e1e1e'}`,
              borderRadius: '12px', padding: '28px', position: 'relative',
              boxShadow: p.popular ? '0 16px 48px rgba(229,57,53,0.25)' : 'none',
              transform: p.popular ? 'scale(1.03)' : 'none',
            }}>
              {p.popular && <div style={{ position: 'absolute', top: '-13px', left: '50%', transform: 'translateX(-50%)', background: '#fff', color: '#e53935', fontWeight: 800, fontSize: '0.73rem', padding: '4px 14px', borderRadius: '99px', whiteSpace: 'nowrap' }}>★ BELIEBT</div>}
              <p style={{ color: p.popular ? 'rgba(255,255,255,0.7)' : '#666', fontSize: '0.78rem', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '6px' }}>{p.badge}</p>
              <h3 style={{ color: '#fff', fontSize: '1.3rem', fontWeight: 900, marginBottom: '4px' }}>{p.name}</h3>
              <p style={{ color: p.popular ? 'rgba(255,255,255,0.6)' : '#555', fontSize: '0.82rem', marginBottom: '14px' }}>1 Gerät</p>
              <div style={{ color: '#fff', fontSize: '2.3rem', fontWeight: 900, marginBottom: '22px' }}>€{p.price}</div>
              <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px', display: 'flex', flexDirection: 'column', gap: '9px' }}>
                {features.map(f => (
                  <li key={f} style={{ display: 'flex', alignItems: 'center', gap: '8px', color: p.popular ? 'rgba(255,255,255,0.88)' : '#999', fontSize: '0.85rem' }}>
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke={p.popular ? '#fff' : '#e53935'} strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
                    {f}
                  </li>
                ))}
              </ul>
              <a href={`${WA}&text=Hallo+IPTVV%2C+${p.msg}`} target="_blank" rel="noopener noreferrer"
                style={{ display: 'block', textAlign: 'center', background: p.popular ? '#fff' : '#e53935', color: p.popular ? '#e53935' : '#fff', fontWeight: 700, padding: '12px', borderRadius: '8px', fontSize: '0.9rem', textDecoration: 'none' }}>
                Jetzt kaufen
              </a>
              <p style={{ textAlign: 'center', color: p.popular ? 'rgba(255,255,255,0.5)' : '#444', fontSize: '0.73rem', marginTop: '10px' }}>1.090 Bewertungen ★★★★★</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

function Stats() {
  return (
    <section style={{ background: '#080808', padding: '80px 0' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px' }}>
        <div style={{ textAlign: 'center', marginBottom: '48px' }}>
          <h2 style={{ color: '#fff', fontSize: 'clamp(1.7rem, 3vw, 2.4rem)', fontWeight: 900 }}>
            besten iptv kaufen in <span style={{ color: '#e53935' }}>Deutschland</span>
          </h2>
          <p style={{ color: '#8c8c8c', marginTop: '16px', maxWidth: '680px', margin: '16px auto 0', lineHeight: 1.75 }}>
            IPTV kaufen bei uns und erhalten Sie Zugang zu 20.000 Kanälen und mehr als 120.000 VOD mit allen Qualitäten in FHD und 4K – Der beste IPTV Anbieter mit 99,9% Verfügbarkeit, <strong style={{ color: '#fff' }}>100% Geld-zurück-Garantie</strong> in 7 Tagen.
          </p>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '20px' }}>
          {[{ val: '100%', label: 'Trusted' }, { val: '7 Tage', label: 'Rückerstattung' }, { val: '99%', label: 'Stabiler Server' }, { val: '120K+', label: 'VOD & Kanäle' }].map(s => (
            <div key={s.label} style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px', textAlign: 'center' }}>
              <div style={{ color: '#e53935', fontSize: '2rem', fontWeight: 900 }}>{s.val}</div>
              <div style={{ color: '#8c8c8c', fontSize: '0.85rem', marginTop: '6px' }}>{s.label}</div>
            </div>
          ))}
        </div>
        <div style={{ textAlign: 'center', marginTop: '48px' }}>
          <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+den+Service+testen`} target="_blank" rel="noopener noreferrer"
            style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '16px 48px', borderRadius: '8px', fontSize: '1.05rem', textDecoration: 'none', display: 'inline-block' }}>
            Zugriff erhalten
          </a>
        </div>
      </div>
    </section>
  )
}

function Footer() {
  return (
    <footer style={{ background: '#050505', borderTop: '1px solid #111', padding: '60px 0 28px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px' }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: '40px', marginBottom: '40px' }}>
          <div>
            <div style={{ marginBottom: '14px' }}>
              <span style={{ color: '#e53935', fontSize: '1.4rem', fontWeight: 900 }}>IPTVV</span>
              <span style={{ color: '#fff', fontSize: '1.4rem', fontWeight: 900 }}>.DE</span>
            </div>
            <p style={{ color: '#8c8c8c', fontSize: '0.88rem', lineHeight: 1.7 }}>
              Der beste IPTV-Service in Deutschland mit über 22.000 Kanälen und 120.000+ VOD-Titeln in 4K-Qualität.
            </p>
          </div>
          <div>
            <p style={{ color: '#fff', fontWeight: 700, marginBottom: '16px', fontSize: '0.95rem' }}>Schnelllinks</p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {[['/', 'Heim'], ['/preise', 'Preisgestaltung'], ['/faqs', 'FAQs'], ['/datenschutz', 'Datenschutzrichtlinie'], ['/agb', 'Geschäftsbedingungen']].map(([href, label]) => (
                <Link key={href} href={href} style={{ color: '#8c8c8c', fontSize: '0.88rem', textDecoration: 'none' }}>{label}</Link>
              ))}
            </div>
          </div>
          <div>
            <p style={{ color: '#fff', fontWeight: 700, marginBottom: '16px', fontSize: '0.95rem' }}>Support</p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <Link href="/kontakt" style={{ color: '#8c8c8c', fontSize: '0.88rem', textDecoration: 'none' }}>Kontaktiere uns</Link>
              <a href={`https://wa.me/4917600000000`} target="_blank" rel="noopener noreferrer" style={{ color: '#8c8c8c', fontSize: '0.88rem', textDecoration: 'none' }}>WhatsApp Support</a>
              <a href="mailto:info@iptvv.de" style={{ color: '#8c8c8c', fontSize: '0.88rem', textDecoration: 'none' }}>info@iptvv.de</a>
            </div>
          </div>
        </div>
        <div style={{ borderTop: '1px solid #111', paddingTop: '22px', display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
          <p style={{ color: '#333', fontSize: '0.83rem' }}>Alle Rechte vorbehalten © {new Date().getFullYear()} IPTVV.DE</p>
          <p style={{ color: '#2a2a2a', fontSize: '0.78rem' }}>⚠️ Nur für legale Inhalte.</p>
        </div>
      </div>
    </footer>
  )
}

export default function Home() {
  return (
    <>
      <Head>
        <title>IPTV kaufen 2026 – IPTV Anbieter in Deutschland | IPTVV.DE</title>
        <meta name="description" content="IPTV kaufen bei IPTVV Premium – der beste IPTV-Service in Deutschland. +22.000 Kanäle, +120.000 VOD, 4K Ultra HD. Kostenlos testen!" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#0a0a0a" />
        <link rel="preload" as="image" href="/hero-mobile.webp" type="image/webp" fetchPriority="high" />
        <meta property="og:title" content="IPTV kaufen 2026 – IPTV Anbieter in Deutschland | IPTVV.DE" />
        <meta property="og:description" content="+22.000 Kanäle, 4K Qualität, 99,9% Betriebszeit. Jetzt kostenlos testen!" />
        <meta property="og:url" content="https://iptvv.de" />
        <link rel="canonical" href="https://iptvv.de/" />
        <meta name="robots" content="index, follow" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="IPTVV.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta name="twitter:card" content="summary_large_image" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar />
      <main>
        <Hero />
        <Features />
        <HowItWorks />
        <PricingSection />
        <Stats />
      </main>
      <Footer />
    </>
  )
}
