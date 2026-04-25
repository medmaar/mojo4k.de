const categories = [
  { name: 'Deutschland', count: '800+', flag: '🇩🇪' },
  { name: 'Sport', count: '500+', flag: '⚽' },
  { name: 'Filme & Serien', count: '3.000+', flag: '🎬' },
  { name: 'Türkei', count: '600+', flag: '🇹🇷' },
  { name: 'UK & USA', count: '1.200+', flag: '🇬🇧' },
  { name: 'Kinder', count: '200+', flag: '🧸' },
  { name: 'News', count: '300+', flag: '📰' },
  { name: 'Musik', count: '150+', flag: '🎵' },
]

const channels = [
  'Das Erste', 'ZDF', 'RTL', 'SAT.1', 'ProSieben', 'VOX', 'kabel eins',
  'DAZN', 'Sky Sport', 'Eurosport', 'Sport1', 'CNN', 'BBC World',
  'Discovery', 'National Geographic', 'Fox', 'Netflix DE', 'Prime Video',
]

export default function Channels() {
  return (
    <section id="channels" className="py-24 bg-black/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <span className="text-brand-orange text-sm font-semibold uppercase tracking-wider">Senderübersicht</span>
          <h2 className="text-4xl md:text-5xl font-black mt-3 mb-4">
            20.000+ Sender{' '}
            <span className="gradient-text">weltweit</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Von deutschen Privatsendern bis zu internationalen Sporkanälen — alles in einem Paket.
          </p>
        </div>

        {/* Category grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-16">
          {categories.map((cat) => (
            <div key={cat.name} className="card-hover bg-white/5 border border-white/10 rounded-xl p-5 text-center">
              <div className="text-4xl mb-3">{cat.flag}</div>
              <div className="font-bold text-white">{cat.name}</div>
              <div className="text-brand-orange font-semibold text-sm mt-1">{cat.count} Sender</div>
            </div>
          ))}
        </div>

        {/* Channel ticker */}
        <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <h3 className="text-center text-gray-400 text-sm uppercase tracking-wider mb-5">Beliebte Sender</h3>
          <div className="flex flex-wrap gap-2 justify-center">
            {channels.map((ch) => (
              <span key={ch} className="bg-white/10 border border-white/10 text-gray-300 text-sm px-3 py-1 rounded-full">
                {ch}
              </span>
            ))}
            <span className="bg-brand-orange/20 border border-brand-orange/30 text-brand-orange text-sm px-3 py-1 rounded-full">
              + 19.982 mehr
            </span>
          </div>
        </div>
      </div>
    </section>
  )
}
