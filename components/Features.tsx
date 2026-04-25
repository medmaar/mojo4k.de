const features = [
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/>
      </svg>
    ),
    title: '4K Ultra HD',
    desc: 'Genieße gestochen scharfe Bilder in 4K-Auflösung auf allen deinen Geräten.',
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V6h16v12zM6 10h2v2H6zm0 4h8v2H6zm10 0h2v2h-2zm-6-4h8v2h-8z"/>
      </svg>
    ),
    title: '20.000+ Sender',
    desc: 'Über 20.000 Live-Sender aus Deutschland, Europa und weltweit.',
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z"/>
      </svg>
    ),
    title: 'Catch-Up TV',
    desc: 'Verpasse nie wieder deine Lieblingssendungen — bis zu 7 Tage zurückschauen.',
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M21 3H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h5v2H6v2h12v-2h-2v-2h5c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 14H3V5h18v12z"/>
      </svg>
    ),
    title: 'Alle Geräte',
    desc: 'Smart TV, Android, iOS, PC, MAG, Firestick — überall verfügbar.',
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M19.35 10.04A7.49 7.49 0 0 0 12 4C9.11 4 6.6 5.64 5.35 8.04A5.994 5.994 0 0 0 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/>
      </svg>
    ),
    title: 'Anti-Freeze',
    desc: 'Unsere Server garantieren flüssiges Streaming ohne Puffern oder Unterbrechungen.',
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/>
      </svg>
    ),
    title: '24/7 Support',
    desc: 'Unser deutschsprachiger Support-Team hilft dir rund um die Uhr.',
  },
]

export default function Features() {
  return (
    <section id="features" className="section-bg py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <span className="text-brand-orange text-sm font-semibold uppercase tracking-wider">Warum IPTVV.DE?</span>
          <h2 className="text-4xl md:text-5xl font-black mt-3 mb-4">
            Alle Features,{' '}
            <span className="gradient-text">die du brauchst</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Erstklassiger IPTV-Service mit modernster Infrastruktur für das beste Streaming-Erlebnis.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((f) => (
            <div key={f.title} className="card-hover bg-white/5 border border-white/10 rounded-2xl p-6 group">
              <div className="w-14 h-14 bg-brand-orange/10 border border-brand-orange/20 rounded-xl flex items-center justify-center text-brand-orange mb-5 group-hover:bg-brand-orange group-hover:text-white transition-all">
                {f.icon}
              </div>
              <h3 className="text-xl font-bold mb-2">{f.title}</h3>
              <p className="text-gray-400 leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
