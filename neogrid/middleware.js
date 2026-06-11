// Edge Middleware — proteção por senha (server-side de verdade).
//
// Fluxo (igual ao metodologia.daltonlab.ai):
//   1. GET sem cookie válido  -> devolve a gate "Acesso restrito".
//   2. POST /auth com a senha  -> compara (constant-time) contra ACCESS_PASSWORD
//      (env var). Se bate, seta cookie HttpOnly assinado (HMAC) e redireciona pra /.
//   3. GET com cookie válido   -> deixa passar (serve o deck estático).
//
// A senha vive só em env var no Vercel (ACCESS_PASSWORD). Nunca no código,
// nunca no bundle do cliente. O cookie é um HMAC assinado com SESSION_SECRET,
// então não dá pra forjar sem o segredo.

export const config = {
  // roda em tudo, menos assets internos do Vercel e favicon
  matcher: ['/((?!_vercel|favicon.ico).*)'],
};

const COOKIE = 'dl_neogrid_auth';

const enc = new TextEncoder();

async function hmac(secret, msg) {
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign'],
  );
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(msg));
  return btoa(String.fromCharCode(...new Uint8Array(sig)))
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function safeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

export default async function middleware(request) {
  const url = new URL(request.url);
  const password = process.env.ACCESS_PASSWORD || '';
  const secret = process.env.SESSION_SECRET || password || 'dl-neogrid-fallback';
  const token = await hmac(secret, 'authorized-v1');

  // 1) Login
  if (url.pathname === '/auth' && request.method === 'POST') {
    let submitted = '';
    try {
      const form = await request.formData();
      submitted = String(form.get('password') || '');
    } catch (_) { /* corpo inválido -> falha */ }

    if (password && safeEqual(submitted, password)) {
      return new Response(null, {
        status: 302,
        headers: {
          'Location': '/',
          'Set-Cookie': `${COOKIE}=${token}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=604800`,
          'Cache-Control': 'no-store',
        },
      });
    }
    return new Response(null, { status: 302, headers: { 'Location': '/?e=1', 'Cache-Control': 'no-store' } });
  }

  // 2) Já autenticado?
  const cookie = request.headers.get('cookie') || '';
  const m = cookie.match(new RegExp('(?:^|;\\s*)' + COOKIE + '=([^;]+)'));
  if (m && safeEqual(m[1], token)) {
    return; // segue pro conteúdo estático
  }

  // 3) Gate
  const err = url.searchParams.get('e') === '1';
  return new Response(gateHtml(err), {
    status: 200,
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow' },
  });
}

function gateHtml(err) {
  const errLine = err
    ? '<div class="error" style="opacity:1">Chave incorreta. Tente de novo.</div>'
    : '<div class="error"></div>';
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Dalton Lab — Acesso restrito</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&family=Fraunces:ital,opsz,wght@0,9..144,300..900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{ --bg:#0a1628; --cyan:#33ADE5; --cyan-bright:#5fc3f0; --cyan-faint:rgba(51,173,229,0.15);
    --text:#e8eef5; --text-3:#8aa5c2; --text-4:#5f7a98; --warn:#ff8080;
    --display:'Bricolage Grotesque',system-ui,sans-serif; --mono:'JetBrains Mono',monospace; --serif:'Fraunces',serif; }
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:100%;min-height:100vh;background:var(--bg);color:var(--text);font-family:var(--display);-webkit-font-smoothing:antialiased}
  body{display:flex;align-items:center;justify-content:center;padding:24px;
    background:radial-gradient(ellipse at 50% 30%,rgba(51,173,229,0.10) 0%,transparent 55%),radial-gradient(ellipse at 20% 80%,rgba(168,85,247,0.05) 0%,transparent 50%),linear-gradient(180deg,#0a1628 0%,#0d1d36 100%)}
  .card{position:relative;width:100%;max-width:430px;background:rgba(13,29,54,0.74);border:1px solid var(--cyan-faint);border-radius:20px;padding:44px 38px 34px;text-align:center;box-shadow:0 30px 90px rgba(0,0,0,0.6),inset 0 1px 0 rgba(255,255,255,0.04);animation:in .7s cubic-bezier(.16,1,.3,1) both}
  .card::before{content:'';position:absolute;top:0;left:32px;right:32px;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:.6}
  @keyframes in{from{opacity:0;transform:translateY(20px) scale(.97);filter:blur(6px)}to{opacity:1;transform:none;filter:blur(0)}}
  .lock{width:56px;height:56px;margin:0 auto 22px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:rgba(51,173,229,0.10);border:1px solid var(--cyan-faint);color:var(--cyan-bright);box-shadow:0 0 30px rgba(51,173,229,0.25)}
  .lock svg{width:26px;height:26px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:var(--cyan);margin-bottom:12px}
  .title{font-size:26px;font-weight:700;letter-spacing:-.02em;color:var(--text);line-height:1.15}
  .title em{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--cyan)}
  .sub{margin-top:12px;font-size:14.5px;color:var(--text-3);line-height:1.5}
  form{margin-top:26px;display:flex;flex-direction:column;gap:12px}
  input{width:100%;padding:15px 16px;background:rgba(7,16,30,0.7);border:1px solid var(--cyan-faint);border-radius:12px;color:var(--text);font-family:var(--display);font-size:16px;letter-spacing:.04em;text-align:center;transition:border-color .2s,box-shadow .2s}
  input::placeholder{color:var(--text-4);letter-spacing:.02em}
  input:focus{outline:none;border-color:var(--cyan);box-shadow:0 0 0 3px rgba(51,173,229,0.18)}
  button{padding:15px 16px;background:var(--cyan);color:#04121f;border:none;border-radius:12px;font-family:var(--display);font-weight:700;font-size:15px;letter-spacing:.02em;cursor:pointer;transition:background .2s,transform .1s}
  button:hover{background:var(--cyan-bright)}
  button:active{transform:scale(.98)}
  .error{font-family:var(--mono);font-size:12px;letter-spacing:.5px;color:var(--warn);min-height:16px;opacity:0}
  .foot{margin-top:24px;font-family:var(--mono);font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-4)}
</style>
</head>
<body>
  <div class="card">
    <div class="lock"><svg viewBox="0 0 24 24"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></div>
    <div class="eyebrow">Dalton Lab</div>
    <h1 class="title">Conteúdo <em>protegido</em></h1>
    <p class="sub">Digite a chave de acesso para visualizar a apresentação.</p>
    <form method="POST" action="/auth" autocomplete="off">
      <input type="password" name="password" placeholder="Chave de acesso" autocomplete="off" spellcheck="false" autofocus aria-label="Chave de acesso">
      <button type="submit">Acessar</button>
      ${errLine}
    </form>
    <div class="foot">Acesso restrito</div>
  </div>
</body>
</html>`;
}
