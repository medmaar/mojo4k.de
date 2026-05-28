import Head from 'next/head'
import Link from 'next/link'
import { useState } from 'react'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqs = [
  { q: 'Was ist IPTV und wie funktioniert es?', a: 'IPTV (Internet Protocol Television) überträgt TV-Inhalte über das Internet statt über Kabel oder Satellit. Sie erhalten Zugang zu über 50.000 Live-Kanälen und 120.000+ Filmen und Serien in HD und 4K – auf jedem Gerät mit Internetverbindung.' },
  { q: 'Wie Kann Ich Den IPTV-Dienst Nutzen?', a: 'Schauen Sie sich unser IPTV-Paket auf all Ihren Geräten an. Nach dem Kauf können Sie es auf Ihrem Fernseher, Android-Box, Mobiltelefon, MAG-Box und Tablets nutzen.' },
  { q: 'Welche Geräte werden von MOJO4K.DE unterstützt?', a: 'MOJO4K.DE funktioniert auf Amazon Fire TV Stick, Android TV Box, Samsung Smart TV, LG Smart TV, iPhone, iPad, Android-Smartphones, PC, Mac, MAG-Box, Enigma2 und allen IPTV-Playern wie Smarters Pro, TiviMate und GSE IPTV.' },
  { q: 'Kann ich MOJO4K.DE kostenlos testen?', a: 'Ja! Wir bieten einen kostenlosen Testplan an. Kontaktieren Sie uns einfach über WhatsApp, und wir aktivieren Ihren Test sofort – ohne Kreditkarte und ohne Vertrag.' },
  { q: 'Was Ist Nach Der Zahlung Zu Tun?', a: 'Nichts weiter – lassen Sie einfach unserem Team die Zeit, um Ihre Bestellung abzuschließen. Wir werden Ihnen so schnell wie möglich per E-Mail und WhatsApp antworten, nachdem wir Ihre Zahlung überprüft haben.' },
  { q: 'Wie schnell wird mein Abonnement aktiviert?', a: 'Die Aktivierung erfolgt innerhalb weniger Minuten nach Zahlungseingang. Sie erhalten Ihre Zugangsdaten per E-Mail und WhatsApp und können sofort mit dem Streaming beginnen.' },
  { q: 'Funktioniert Dieser Service (IPTV) In Meinem Land?', a: 'IPTV funktioniert weltweit, unabhängig davon, wo Sie leben oder sich aufhalten. Solange Sie über eine stabile Internetverbindung verfügen, können Sie Tausende von TV-Kanälen empfangen.' },
  { q: 'Ist IPTV legal in Deutschland?', a: 'Die IPTV-Technologie selbst ist legal und wird von großen Anbietern wie Telekom MagentaTV und Vodafone TV verwendet. Entscheidend ist die Quelle des Inhalts. Nutzer sind für die Einhaltung der Gesetze in ihrem Land verantwortlich.' },
  { q: 'Welche Internetgeschwindigkeit benötige ich?', a: 'Für HD-Streaming empfehlen wir mindestens 16 Mbit/s, für 4K Ultra HD mindestens 25 Mbit/s. Eine stabile Verbindung ist wichtiger als die reine Geschwindigkeit.' },
  { q: 'Wie Lange Kann Ich Ein Abonnement Haben?', a: 'So lange Sie möchten. Wir bieten Pakete von 1 Monat bis 1 Jahr an. Sie können es jederzeit erneuern, indem Sie nur dann bezahlen, wenn Sie es nutzen. Keine Verträge, keine versteckten Kosten.' },
  { q: 'Brauche Ich Eine Satellitenschüssel, Um IPTV Zu Nutzen?', a: 'Nein. Sie verbinden sich über das Internet mit unseren IPTV-Servern. Sie benötigen keine Satellitenschüssel oder Satellitenausrüstung – nur eine stabile Internetverbindung.' },
  { q: 'Wie ist die Qualität der Server?', a: 'Wir sind der bestbewertete Service-Anbieter und bieten eine Technologie ohne Einfrieren (AntiFreeze) mit einer Betriebszeit von 99,9%. Unsere Server werden rund um die Uhr überwacht.' },
]

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: faqs.map(f => ({
    '@type': 'Question',
    name: f.q,
    acceptedAnswer: { '@type': 'Answer', text: f.a },
  })),
}

const breadcrumbSchema = {
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Startseite', item: 'https://mojo4k.de' },
    { '@type': 'ListItem', position: 2, name: 'FAQ', item: 'https://mojo4k.de/faqs' },
  ],
}

function FAQItem({ q, a, index }: { q: string; a: string; index: number }) {
  const [open, setOpen] = useState(false)
  return (
    <div style={{ border: `1px solid ${open ? '#e53935' : '#1e1e1e'}`, borderRadius: '10px', overflow: 'hidden', transition: 'border-color 0.2s' }}>
      <button onClick={() => setOpen(!open)}
        style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '18px 22px', background: '#111', border: 'none', cursor: 'pointer', textAlign: 'left', gap: '16px' }}
        aria-expanded={open}>
        <span style={{ color: '#fff', fontWeight: 600, fontSize: '0.95rem' }}>{q}</span>
        <svg width="18" height="18" fill="none" stroke="#e53935" strokeWidth="2" viewBox="0 0 24 24"
          style={{ flexShrink: 0, transform: open ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }} aria-hidden="true">
          <path d="M6 9l6 6 6-6" />
        </svg>
      </button>
      {open && (
        <div style={{ padding: '16px 22px 20px', background: '#0d0d0d', color: '#999', fontSize: '0.9rem', lineHeight: 1.75 }}>
          {a}
        </div>
      )}
    </div>
  )
}

export default function FAQs() {
  return (
    <>
      <Head>
        <title>IPTV FAQ – Häufige Fragen zu IPTV Deutschland | MOJO4K.DE</title>
        <meta name="description" content="Antworten auf alle Fragen zu IPTV in Deutschland: kompatible Geräte, Smarters Pro, Bundesliga, Aktivierung, Internetgeschwindigkeit und mehr. MOJO4K.DE erklärt alles." />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://mojo4k.de/faqs/" />
        <meta property="og:title" content="IPTV FAQ – Häufige Fragen zu IPTV Deutschland | MOJO4K.DE" />
        <meta property="og:description" content="Alle Antworten zu IPTV in Deutschland: Geräte, Smarters Pro, Aktivierung und mehr." />
        <meta property="og:url" content="https://mojo4k.de/faqs/" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="MOJO4K.DE" />
        <meta property="og:locale" content="de_DE" />
        <meta property="og:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="IPTV FAQ Deutschland – MOJO4K" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="IPTV FAQ – Häufige Fragen zu IPTV Deutschland | MOJO4K.DE" />
        <meta name="twitter:description" content="Alle Antworten zu IPTV in Deutschland: Geräte, Smarters Pro, Aktivierung und mehr." />
        <meta name="twitter:image" content="https://mojo4k.de/iptv-kaufen.jpg" />
        <meta name="author" content="MOJO4K.DE" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon.svg" />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      </Head>
      <div style={{ background: '#0a0a0a', minHeight: '100vh', paddingTop: '64px' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50 }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '64px' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>MOJO4K</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <div style={{ display: 'flex', gap: '32px' }} className="hidden-mobile">
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([href, label]) => (
                <Link key={href} href={href} style={{ color: href === '/faqs' ? '#fff' : '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{label}</Link>
              ))}
            </div>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+m%C3%B6chte+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
              Kostenloser Test
            </a>
          </div>
        </nav>

        <div style={{ maxWidth: '860px', margin: '0 auto', padding: '60px 16px 80px' }}>
          {/* Breadcrumb */}
          <nav aria-label="Breadcrumb" style={{ marginBottom: '40px' }}>
            <ol style={{ listStyle: 'none', display: 'flex', gap: '8px', fontSize: '0.82rem', color: '#555' }}>
              <li><Link href="/" style={{ color: '#555', textDecoration: 'none' }}>Startseite</Link></li>
              <li style={{ color: '#333' }}>›</li>
              <li style={{ color: '#e53935' }}>FAQ</li>
            </ol>
          </nav>

          <div style={{ textAlign: 'center', marginBottom: '56px' }}>
            <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>FAQ</p>
            <h1 style={{ color: '#fff', fontSize: 'clamp(1.8rem, 3vw, 2.8rem)', fontWeight: 900, marginTop: '12px', marginBottom: '16px' }}>
              Häufig gestellte Fragen zu IPTV
            </h1>
            <p style={{ color: '#8c8c8c', lineHeight: 1.7, maxWidth: '560px', margin: '0 auto' }}>
              Alles, was Sie über unseren IPTV-Service in Deutschland wissen müssen – von der Einrichtung bis zur Gerätekompatibilität.
            </p>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {faqs.map((f, i) => <FAQItem key={f.q} q={f.q} a={f.a} index={i} />)}
          </div>

          <div style={{ textAlign: 'center', marginTop: '56px', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '36px' }}>
            <h2 style={{ color: '#fff', fontWeight: 800, marginBottom: '12px', fontSize: '1.3rem' }}>Noch Fragen? Kontaktieren Sie uns!</h2>
            <p style={{ color: '#8c8c8c', marginBottom: '24px', fontSize: '0.9rem' }}>Unser Support-Team ist 24/7 für Sie erreichbar – auf Deutsch.</p>
            <a href={`${WA}&text=Hallo+MOJO4K%2C+ich+habe+eine+Frage`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#25D366', color: '#fff', fontWeight: 700, padding: '12px 32px', borderRadius: '8px', textDecoration: 'none', fontSize: '0.95rem', display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="white" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
              WhatsApp Support
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
