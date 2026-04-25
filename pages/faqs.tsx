import Head from 'next/head'
import Link from 'next/link'
import { useState } from 'react'

const WA = 'https://api.whatsapp.com/send/?phone=4917600000000'

const faqs = [
  { q: 'Wie Kann Ich Den IPTV-Dienst Nutzen?', a: 'Schauen Sie sich unser IPTV-Paket auf all Ihren Geräten an. Nach dem Kauf können Sie es auf Ihrem Fernseher, Android-Box, Mobiltelefon, MAG-Box und Tablets nutzen.' },
  { q: 'Was Ist Nach Der Zahlung Zu Tun?', a: 'Nichts weiter – lassen Sie einfach unserem Team die Zeit, um Ihre Bestellung abzuschließen. Wir werden Ihnen so schnell wie möglich per E-Mail und WhatsApp antworten, nachdem wir Ihre Zahlung überprüft haben.' },
  { q: 'Funktioniert Dieser Service (IPTV) In Meinem Land?', a: 'IPTV funktioniert weltweit, unabhängig davon, wo Sie leben oder sich aufhalten. Solange Sie über eine stabile Internetverbindung verfügen, können Sie Tausende von TV-Kanälen empfangen.' },
  { q: 'Welche Art Von Qualitativ Hochwertigem Service Bieten Wir An?', a: 'Unser Service ist exzellent. Wir überwachen und kontrollieren stets Verzögerungen und Fragmentierung des Dienstes, um Ihnen einen hochwertigen Service zu bieten. Wir halten immer das gewünschte Leistungsniveau aufrecht.' },
  { q: 'Wie Ist Die Qualität Unserer Server?', a: 'Wir sind der bestbewertete Service-Anbieter und bieten eine Technologie ohne Einfrieren (AntiFreeze) mit einer Betriebszeit von 99,9%.' },
  { q: 'Wie Lange Kann Ich Ein Abonnement Haben?', a: 'So lange Sie möchten. Wir bieten Pakete von 1 Monat bis 1 Jahr an. Sie können es jederzeit erneuern, indem Sie nur dann bezahlen, wenn Sie es nutzen.' },
  { q: 'Brauche Ich Eine Satellitenschüssel, Um IPTV Zu Nutzen?', a: 'Nein, Sie verbinden sich über das Internet mit unseren IPTV-Servern. Sie benötigen keine Satellitenschüssel oder Satellitenausrüstung.' },
  { q: 'Welche Internetgeschwindigkeit Benötige Ich?', a: 'Mindestens 16 Mbit/s. Die Verbindung sollte stabil und von guter Qualität sein. Je stabiler die Internetverbindung, desto klarer die Bildqualität.' },
  { q: 'Welche Geräte Werden Unterstützt?', a: 'Wir unterstützen alle Arten von Geräten: MAG, Android-Smartphone, Android-Boxen, Enigma, DreamBox, Vu+, PC, VLC, Kodi/XBMC, Smart TV, Amazon Firestick und viele mehr.' },
  { q: 'Haben Sie Ein Problem?', a: 'Wir sind rund um die Uhr für Sie da. Unser technisches Support-Team steht Ihnen gerne über WhatsApp oder E-Mail zur Verfügung. Zögern Sie nicht, uns zu kontaktieren.' },
]

function FAQItem({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false)
  return (
    <div style={{ border: `1px solid ${open ? '#e53935' : '#1e1e1e'}`, borderRadius: '10px', overflow: 'hidden', transition: 'border-color 0.2s' }}>
      <button onClick={() => setOpen(!open)} style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '18px 22px', background: '#111', border: 'none', cursor: 'pointer', textAlign: 'left', gap: '16px' }}>
        <span style={{ color: '#fff', fontWeight: 600, fontSize: '0.95rem' }}>{q}</span>
        <svg width="18" height="18" fill="none" stroke="#e53935" strokeWidth="2" viewBox="0 0 24 24" style={{ flexShrink: 0, transform: open ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>
          <path d="M6 9l6 6 6-6"/>
        </svg>
      </button>
      {open && <div style={{ padding: '16px 22px 20px', background: '#0d0d0d', color: '#999', fontSize: '0.9rem', lineHeight: 1.75 }}>{a}</div>}
    </div>
  )
}

export default function FAQs() {
  return (
    <>
      <Head>
        <title>FAQs – Häufige Fragen | IPTVV.DE</title>
        <meta name="description" content="Antworten auf häufige Fragen zu unserem IPTV-Service." />
      </Head>
      <div style={{ background: '#0a0a0a', minHeight: '100vh', paddingTop: '64px' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50 }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '64px' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>IPTVV</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <div style={{ display: 'flex', gap: '32px' }}>
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/faqs', 'FAQs'], ['/kontakt', 'Kontakt']].map(([href, label]) => (
                <Link key={href} href={href} style={{ color: '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{label}</Link>
              ))}
            </div>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+m%C3%B6chte+testen`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#e53935', color: '#fff', fontWeight: 700, padding: '8px 20px', borderRadius: '6px', fontSize: '0.9rem', textDecoration: 'none' }}>
              Kostenloser Test
            </a>
          </div>
        </nav>
        <div style={{ maxWidth: '860px', margin: '0 auto', padding: '60px 16px 80px' }}>
          <div style={{ textAlign: 'center', marginBottom: '56px' }}>
            <p style={{ color: '#e53935', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.82rem' }}>FAQ</p>
            <h1 style={{ color: '#fff', fontSize: 'clamp(1.8rem, 3vw, 2.8rem)', fontWeight: 900, marginTop: '12px', marginBottom: '16px' }}>
              Häufig gestellte Fragen
            </h1>
            <p style={{ color: '#777', lineHeight: 1.7 }}>Alles, was Sie über unseren IPTV-Service wissen müssen.</p>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {faqs.map(f => <FAQItem key={f.q} q={f.q} a={f.a} />)}
          </div>
          <div style={{ textAlign: 'center', marginTop: '56px', background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '36px' }}>
            <h3 style={{ color: '#fff', fontWeight: 800, marginBottom: '12px' }}>Noch Fragen? Kontaktieren Sie uns!</h3>
            <p style={{ color: '#777', marginBottom: '24px', fontSize: '0.9rem' }}>Unser Support-Team ist 24/7 für Sie erreichbar.</p>
            <a href={`${WA}&text=Hallo+IPTVV%2C+ich+habe+eine+Frage`} target="_blank" rel="noopener noreferrer"
              style={{ background: '#25D366', color: '#fff', fontWeight: 700, padding: '12px 32px', borderRadius: '8px', textDecoration: 'none', fontSize: '0.95rem', display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
              WhatsApp Support
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
