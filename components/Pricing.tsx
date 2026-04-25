const plans = [
  {
    name: 'Starter',
    period: '1 Monat',
    price: '9.99',
    popular: false,
    features: [
      '20.000+ Live-Sender',
      '50.000+ VOD Titel',
      'Full HD Qualität',
      '1 Gerät gleichzeitig',
      'EPG Programmguide',
      'E-Mail Support',
    ],
    cta: 'Starter wählen',
  },
  {
    name: 'Premium',
    period: '3 Monate',
    price: '24.99',
    popular: true,
    badge: 'Beliebteste Wahl',
    features: [
      '20.000+ Live-Sender',
      '50.000+ VOD Titel',
      '4K Ultra HD Qualität',
      '2 Geräte gleichzeitig',
      'EPG + Catch-Up TV',
      'Anti-Freeze Technologie',
      'Priority Support 24/7',
    ],
    cta: 'Premium starten',
  },
  {
    name: 'Jahres-Deal',
    period: '12 Monate',
    price: '69.99',
    popular: false,
    badge: 'Bester Preis',
    features: [
      '20.000+ Live-Sender',
      '50.000+ VOD Titel',
      '4K Ultra HD Qualität',
      '4 Geräte gleichzeitig',
      'EPG + Catch-Up TV',
      'Anti-Freeze Technologie',
      'VIP Support 24/7',
      'Kostenlose Updates',
    ],
    cta: 'Jahresabo sichern',
  },
]

export default function Pricing() {
  return (
    <section id="pricing" className="section-bg py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <span className="text-brand-orange text-sm font-semibold uppercase tracking-wider">Preise & Pakete</span>
          <h2 className="text-4xl md:text-5xl font-black mt-3 mb-4">
            Einfache,{' '}
            <span className="gradient-text">transparente Preise</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Keine versteckten Kosten. Kündige jederzeit. Starte heute mit einem kostenlosen Testzugang.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
          {plans.map((plan) => (
            <div
              key={plan.name}
              className={`relative rounded-2xl p-6 flex flex-col ${
                plan.popular
                  ? 'bg-gradient-to-b from-brand-orange/20 to-brand-orange/5 border-2 border-brand-orange scale-105 shadow-2xl shadow-brand-orange/20'
                  : 'bg-white/5 border border-white/10 card-hover'
              }`}
            >
              {plan.badge && (
                <div className={`absolute -top-4 left-1/2 -translate-x-1/2 text-xs font-bold px-4 py-1.5 rounded-full ${
                  plan.popular ? 'pricing-popular text-white' : 'bg-white/10 text-white border border-white/20'
                }`}>
                  {plan.badge}
                </div>
              )}

              <div className="mb-6">
                <h3 className="text-xl font-bold mb-1">{plan.name}</h3>
                <div className="text-gray-400 text-sm">{plan.period}</div>
              </div>

              <div className="mb-6">
                <span className="text-5xl font-black text-white">€{plan.price}</span>
                <span className="text-gray-400 text-sm ml-2">einmalig</span>
              </div>

              <ul className="space-y-3 mb-8 flex-1">
                {plan.features.map((feat) => (
                  <li key={feat} className="flex items-center gap-2 text-sm text-gray-300">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" strokeWidth="2.5">
                      <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    {feat}
                  </li>
                ))}
              </ul>

              <a
                href="#contact"
                className={`w-full py-3 rounded-xl font-bold text-center transition-all ${
                  plan.popular
                    ? 'pricing-popular text-white hover:opacity-90 glow-orange'
                    : 'bg-white/10 hover:bg-white/20 text-white border border-white/10'
                }`}
              >
                {plan.cta}
              </a>
            </div>
          ))}
        </div>

        {/* Trial note */}
        <p className="text-center text-gray-500 text-sm mt-10">
          ✅ 24-Stunden kostenloser Testaccount verfügbar · Kein Abo · Keine Kreditkarte nötig
        </p>
      </div>
    </section>
  )
}
