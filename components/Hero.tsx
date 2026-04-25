export default function Hero() {
  return (
    <section className="hero-bg min-h-screen flex items-center pt-16 relative overflow-hidden">
      {/* Background grid */}
      <div className="absolute inset-0 opacity-5" style={{
        backgroundImage: `linear-gradient(rgba(255,107,0,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,107,0,0.5) 1px, transparent 1px)`,
        backgroundSize: '60px 60px'
      }}/>

      {/* Floating orbs */}
      <div className="absolute top-1/4 right-1/4 w-72 h-72 bg-brand-orange/10 rounded-full blur-3xl pointer-events-none"/>
      <div className="absolute bottom-1/4 left-1/3 w-48 h-48 bg-brand-gold/10 rounded-full blur-3xl pointer-events-none"/>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 relative z-10">
        <div className="text-center max-w-4xl mx-auto">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 bg-brand-orange/10 border border-brand-orange/30 rounded-full px-4 py-1.5 mb-8">
            <span className="w-2 h-2 bg-brand-orange rounded-full animate-pulse"/>
            <span className="text-brand-orange text-sm font-medium">Über 20.000 Sender verfügbar</span>
          </div>

          {/* Headline */}
          <h1 className="text-5xl md:text-7xl font-black mb-6 leading-tight">
            Das beste{' '}
            <span className="gradient-text">IPTV-Erlebnis</span>
            <br />
            in Deutschland
          </h1>

          <p className="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
            Streame über <strong className="text-white">20.000+ Live-Sender</strong>, Filme und Serien in 4K-Qualität. 
            Keine Unterbrechungen, kein Puffern — nur pures Entertainment.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-16">
            <a href="#pricing" className="inline-flex items-center justify-center gap-2 bg-brand-orange hover:bg-brand-orange-dark text-white font-bold px-8 py-4 rounded-xl text-lg transition-all glow-orange">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8 5v14l11-7z"/>
              </svg>
              Kostenlos testen
            </a>
            <a href="#features" className="inline-flex items-center justify-center gap-2 bg-white/5 hover:bg-white/10 border border-white/10 text-white font-semibold px-8 py-4 rounded-xl text-lg transition-all">
              Mehr erfahren
              <svg width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                <path d="M9 18l6-6-6-6"/>
              </svg>
            </a>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-3xl mx-auto">
            {[
              { num: '20.000+', label: 'Live-Sender' },
              { num: '50.000+', label: 'VOD Titel' },
              { num: '4K Ultra', label: 'HD Qualität' },
              { num: '99.9%', label: 'Betriebszeit' },
            ].map((stat) => (
              <div key={stat.label} className="bg-white/5 border border-white/10 rounded-xl p-4">
                <div className="text-2xl font-black gradient-text">{stat.num}</div>
                <div className="text-gray-400 text-sm">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
