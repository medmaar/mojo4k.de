import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="de">
      <Head>
        {/* Critical above-fold CSS inlined — no render blocking */}
        <style dangerouslySetInnerHTML={{ __html: `
          *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
          html{scroll-behavior:smooth}
          body{background:#0a0a0a;color:#fff;font-family:system-ui,-apple-system,sans-serif}
          nav{background:#0a0a0a;border-bottom:1px solid #1a1a1a;position:fixed;top:0;left:0;right:0;z-index:50;height:64px;display:flex;align-items:center}
          a{transition:opacity 0.2s}a:hover{opacity:.85}
          @media(max-width:768px){.hidden-mobile{display:none!important}}
        `}} />
        {/* Google Fonts — deferred via JS to avoid render-blocking */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link rel="dns-prefetch" href="https://fonts.googleapis.com" />
        <script dangerouslySetInnerHTML={{ __html: `
          (function(){
            var l=document.createElement('link');
            l.rel='stylesheet';
            l.href='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=optional';
            document.head.appendChild(l);
          })();
        `}} />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
