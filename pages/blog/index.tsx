import Head from 'next/head'
import Link from 'next/link'

const posts = [
  {
    slug: 'iptv-bundesliga-2026',
    title: 'IPTV Bundesliga 2026 – Alle Spiele live streamen in Deutschland',
    excerpt: 'Wie Sie Bundesliga, Champions League und DFB-Pokal live via IPTV auf jedem Gerät schauen können. Die beste Anleitung für Deutschland.',
    date: '2026-01-15',
    tag: 'Sport',
  },
  {
    slug: 'iptv-smarters-pro-anleitung',
    title: 'IPTV Smarters Pro Anleitung 2026 – Einrichtung auf allen Geräten',
    excerpt: 'Komplette Schritt-für-Schritt Anleitung für IPTV Smarters Pro auf Fire Stick, Android, iPhone und Smart TV. Mit Screenshots und Tipps.',
    date: '2026-01-10',
    tag: 'Anleitung',
  },
  {
    slug: 'iptv-stick-test-deutschland',
    title: 'Bester IPTV Stick Deutschland 2026 – Test & Vergleich',
    excerpt: 'Amazon Fire TV Stick 4K, Chromecast und Android Stick im Vergleich. Welcher IPTV Stick eignet sich am besten für Deutschland?',
    date: '2026-01-05',
    tag: 'Test',
  },
]

export default function Blog() {
  return (
    <>
      <Head>
        <title>IPTV Blog Deutschland – Anleitungen, Tests & Tipps | IPTVV.DE</title>
        <meta name="description" content="IPTV Blog für Deutschland: Anleitungen für Fire Stick, Smarters Pro, Bundesliga live, Android Box und mehr. Aktuelle Tipps von IPTVV.DE." />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://iptvv.de/blog" />
        <meta property="og:title" content="IPTV Blog Deutschland – Anleitungen & Tipps | IPTVV.DE" />
        <meta property="og:url" content="https://iptvv.de/blog" />
        <meta property="og:type" content="website" />
      </Head>
      <div style={{ background: '#0a0a0a', minHeight: '100vh', color: '#fff' }}>
        <nav style={{ background: '#0a0a0a', borderBottom: '1px solid #1a1a1a', position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, height: '64px', display: 'flex', alignItems: 'center' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Link href="/" style={{ textDecoration: 'none' }}>
              <span style={{ color: '#e53935', fontSize: '1.5rem', fontWeight: 900 }}>IPTVV</span>
              <span style={{ color: '#fff', fontSize: '1.5rem', fontWeight: 900 }}>.DE</span>
            </Link>
            <div style={{ display: 'flex', gap: '28px' }} className="hidden-mobile">
              {[['/', 'Heim'], ['/preise', 'Preise'], ['/blog', 'Blog'], ['/faqs', 'FAQs']].map(([h, l]) => (
                <Link key={h} href={h} style={{ color: h === '/blog' ? '#fff' : '#ccc', textDecoration: 'none', fontSize: '0.95rem' }}>{l}</Link>
              ))}
            </div>
          </div>
        </nav>
        <div style={{ maxWidth: '900px', margin: '0 auto', padding: '100px 16px 80px' }}>
          <h1 style={{ fontSize: 'clamp(1.8rem, 4vw, 2.6rem)', fontWeight: 900, marginBottom: '12px' }}>IPTV Blog Deutschland</h1>
          <p style={{ color: '#8c8c8c', marginBottom: '48px', lineHeight: 1.7 }}>Anleitungen, Tests und Tipps für IPTV in Deutschland.</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            {posts.map(p => (
              <Link key={p.slug} href={`/blog/${p.slug}`} style={{ textDecoration: 'none' }}>
                <article style={{ background: '#111', border: '1px solid #1e1e1e', borderRadius: '12px', padding: '28px', transition: 'border-color 0.2s' }}
                  onMouseEnter={e => (e.currentTarget.style.borderColor = '#e53935')}
                  onMouseLeave={e => (e.currentTarget.style.borderColor = '#1e1e1e')}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
                    <span style={{ background: 'rgba(229,57,53,0.15)', color: '#e53935', fontSize: '0.72rem', fontWeight: 700, padding: '3px 10px', borderRadius: '99px' }}>{p.tag}</span>
                    <span style={{ color: '#444', fontSize: '0.8rem' }}>{p.date}</span>
                  </div>
                  <h2 style={{ color: '#fff', fontWeight: 800, fontSize: '1.1rem', marginBottom: '10px', lineHeight: 1.4 }}>{p.title}</h2>
                  <p style={{ color: '#8c8c8c', fontSize: '0.9rem', lineHeight: 1.7 }}>{p.excerpt}</p>
                  <p style={{ color: '#e53935', fontSize: '0.85rem', fontWeight: 600, marginTop: '14px' }}>Weiterlesen →</p>
                </article>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </>
  )
}
