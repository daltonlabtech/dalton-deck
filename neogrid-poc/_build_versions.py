# -*- coding: utf-8 -*-
import io

tpl = io.open('_template_base.html', encoding='utf-8').read()
base = io.open('_slides.html', encoding='utf-8').read()

# split base slides by markers
marks = ['  <!-- ============ SLIDE 0%d' % n for n in range(1, 8)]
idxs = [base.index(m) for m in marks]
idxs.append(len(base))
sections = [base[idxs[i]:idxs[i+1]] for i in range(7)]  # s[0]=slide1 ... s[6]=slide7

FOOT1 = '<div class="slide-footer"><span class="brand"><strong>Dalton Lab</strong> × Neogrid</span><span>O time faz o melhor possível. O gargalo é o volume.</span></div>'

# ============================================================
# VERSION A — SVG / CSS schematics
# ============================================================
A1 = r'''  <!-- ============ SLIDE 01 (A) — DEFICIT bar ============ -->
  <section class="slide active" data-theme="dark">
    <div class="slide-header reveal"><span class="slide-tag">O gargalo da homologação</span><span class="slide-num"><strong>01</strong> / 07</span></div>
    <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; min-height:0;">
      <div style="max-width:760px;">
        <div class="eyebrow">A conta não fecha</div>
        <h2 class="display-lg" style="margin-top:10px;">Chega muito mais do que o time <em class="highlight">consegue homologar</em>.</h2>
      </div>
      <div style="display:flex; align-items:flex-end; justify-content:center; gap:clamp(34px,5vw,80px); margin-top:clamp(34px,6vh,64px);">
        <div style="text-align:center;">
          <div style="font-family:var(--mono); font-size:13px; letter-spacing:1.5px; text-transform:uppercase; color:var(--text-3); margin-bottom:12px;">Demanda · 484 / mês</div>
          <div style="width:clamp(110px,11vw,150px); height:clamp(230px,34vh,340px); display:flex; flex-direction:column; border-radius:12px; overflow:hidden; border:1px solid var(--cyan-faint);">
            <div style="flex:0 0 70%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; background:repeating-linear-gradient(45deg, rgba(255,128,128,0.28), rgba(255,128,128,0.28) 7px, rgba(255,128,128,0.10) 7px, rgba(255,128,128,0.10) 14px);">
              <span style="font-size:clamp(26px,3vw,44px); font-weight:800; color:#ff9a9a; line-height:1;">+340</span>
              <span style="font-family:var(--mono); font-size:11px; letter-spacing:1px; text-transform:uppercase; color:#ffb3b3;">transbordam</span>
            </div>
            <div style="flex:0 0 30%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2px; background:linear-gradient(180deg, var(--cyan), rgba(51,173,229,0.45));">
              <span style="font-size:clamp(20px,2.2vw,30px); font-weight:800; color:#08263c; line-height:1;">144</span>
              <span style="font-family:var(--mono); font-size:10px; letter-spacing:1px; text-transform:uppercase; color:#08344f;">homologados</span>
            </div>
          </div>
        </div>
        <div style="color:var(--cyan-dim); padding-bottom:clamp(60px,10vh,120px);"><svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/></svg></div>
        <div style="text-align:left; padding-bottom:clamp(40px,7vh,90px);">
          <div style="border:1px solid var(--cyan-faint); border-left:4px solid var(--warn); border-radius:0 14px 14px 0; padding:20px 26px; background:rgba(255,128,128,0.05);">
            <div style="font-size:clamp(54px,7vw,104px); font-weight:800; letter-spacing:-0.03em; color:var(--text); line-height:0.9;">709<span style="font-family:var(--serif); font-style:italic; font-weight:300; font-size:0.34em; color:var(--text-3); padding-left:0.2em;">dias</span></div>
            <div style="font-family:var(--mono); font-size:12px; letter-spacing:1.5px; text-transform:uppercase; color:var(--text-3); margin-top:10px;">parados na fila, em média</div>
          </div>
        </div>
      </div>
      <p class="body" style="margin-top:clamp(28px,5vh,52px); max-width:62ch; font-size:clamp(17px,1.45vw,22px);">Todo mês entram <strong style="color:var(--text);">340 chamados a mais</strong> do que o time dá conta. Eles não somem: viram fila. Cada venda ganha passa por um <em class="highlight">checklist de 39 critérios</em>.</p>
    </div>
    ''' + FOOT1 + '''
  </section>
'''

A5 = r'''  <!-- ============ SLIDE 05 (A) — growth area ============ -->
  <section class="slide" data-theme="dark">
    <div class="slide-header reveal"><span class="slide-tag">O que isso destrava</span><span class="slide-num"><strong>05</strong> / 07</span></div>
    <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0;">
      <div class="s6-head" style="margin-bottom:clamp(20px,3.5vh,36px);">
        <h2 class="s6-title">Fazer mais com o time que <em>já existe</em>.</h2>
        <p class="s6-body" style="font-size:clamp(16px,1.3vw,21px);">A meta que vocês definiram no diagnóstico: crescer em volume sem crescer o quadro.</p>
      </div>
      <div style="display:grid; grid-template-columns:1.3fr 0.9fr; gap:clamp(30px,4vw,64px); align-items:center;">
        <div>
          <svg viewBox="0 0 560 280" style="width:100%; height:auto; overflow:visible;">
            <defs>
              <linearGradient id="agentFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="rgba(51,173,229,0.45)"/><stop offset="1" stop-color="rgba(51,173,229,0.06)"/></linearGradient>
            </defs>
            <line x1="40" y1="240" x2="540" y2="240" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
            <line x1="40" y1="40" x2="40" y2="240" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
            <!-- human flat band -->
            <path d="M40 240 L40 205 L540 205 L540 240 Z" fill="rgba(255,255,255,0.10)"/>
            <!-- agent area filling up to demand -->
            <path d="M40 205 L40 200 C 180 192, 320 150, 540 70 L540 205 Z" fill="url(#agentFill)"/>
            <!-- demand line -->
            <path d="M40 200 C 180 192, 320 150, 540 70" fill="none" stroke="var(--cyan)" stroke-width="2.5"/>
            <circle cx="540" cy="70" r="4.5" fill="#eaf6ff"/>
            <text x="362" y="120" fill="var(--cyan-bright)" font-family="var(--mono)" font-size="13" letter-spacing="1">demanda</text>
            <text x="300" y="180" fill="var(--text-2)" font-family="var(--mono)" font-size="13" letter-spacing="1">agente preenche</text>
            <text x="120" y="228" fill="var(--text-3)" font-family="var(--mono)" font-size="12" letter-spacing="1">equipe (sem contratar)</text>
          </svg>
        </div>
        <div>
          <div style="display:flex; align-items:center; gap:clamp(14px,2vw,26px);">
            <div style="text-align:center;">
              <div style="font-size:clamp(40px,5vw,72px); font-weight:800; letter-spacing:-0.03em; line-height:0.9; color:var(--text-2);">~57<span style="font-family:var(--serif); font-style:italic; font-weight:300; font-size:0.3em; color:var(--text-3); padding-left:0.18em;">h/mês</span></div>
              <div style="font-family:var(--mono); font-size:11px; letter-spacing:1px; text-transform:uppercase; color:var(--text-3); margin-top:10px;">POC hoje · leitura</div>
            </div>
            <div style="color:var(--cyan);"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/></svg></div>
            <div style="text-align:center;">
              <div class="stat-number" style="font-size:clamp(48px,6vw,86px); line-height:0.9;">~69<span class="frac" style="padding-left:0.18em;">h/mês</span></div>
              <div style="font-family:var(--mono); font-size:11px; letter-spacing:1px; text-transform:uppercase; color:var(--cyan); margin-top:10px;">implementação completa</div>
            </div>
          </div>
          <p class="body" style="margin-top:clamp(20px,3vh,32px); font-size:clamp(14px,1.2vw,18px);">A analista vira <strong style="color:var(--text);">gestora de exceção</strong>: confirma, em vez de investigar. O déficit de <strong style="color:var(--text);">+340/mês para de crescer</strong>.</p>
        </div>
      </div>
    </div>
    <div class="slide-footer"><span class="brand"><strong>Dalton Lab</strong> × Neogrid</span><span>Horas devolvidas · projeção sobre o volume real, a validar</span></div>
  </section>
'''

A6 = r'''  <!-- ============ SLIDE 06 (A) — ratio bars ============ -->
  <section class="slide" data-theme="dark">
    <div class="slide-header reveal"><span class="slide-tag">O salto</span><span class="slide-num"><strong>06</strong> / 07</span></div>
    <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0;">
      <div class="s6-head" style="margin-bottom:clamp(26px,4.5vh,48px);">
        <h2 class="s6-title">O que levava <em>~15 minutos</em> agora leva ~1 segundo.</h2>
      </div>
      <div style="display:flex; flex-direction:column; gap:clamp(20px,3.5vh,40px); max-width:1000px;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;"><span style="font-family:var(--mono); font-size:13px; letter-spacing:1.5px; text-transform:uppercase; color:var(--text-3);">Antes · conferência manual</span><span style="font-weight:700; font-size:clamp(20px,2vw,30px); color:var(--text);">~15 min</span></div>
          <div style="height:clamp(26px,3.5vh,40px); width:100%; border-radius:8px; background:linear-gradient(90deg, rgba(255,128,128,0.5), rgba(255,128,128,0.18)); border:1px solid rgba(255,128,128,0.3);"></div>
        </div>
        <div>
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;"><span style="font-family:var(--mono); font-size:13px; letter-spacing:1.5px; text-transform:uppercase; color:var(--cyan);">Agora · com o agente</span><span style="font-weight:700; font-size:clamp(20px,2vw,30px); color:var(--cyan);">~1 seg</span></div>
          <div style="height:clamp(26px,3.5vh,40px); width:6px; min-width:6px; border-radius:8px; background:linear-gradient(180deg, var(--cyan), rgba(51,173,229,0.6)); box-shadow:0 0 16px rgba(51,173,229,0.7);"></div>
        </div>
      </div>
      <div style="display:flex; align-items:baseline; gap:18px; margin-top:clamp(24px,4vh,44px);">
        <span style="font-size:clamp(56px,8vw,130px); font-weight:800; letter-spacing:-0.03em; line-height:0.9; background:linear-gradient(180deg, var(--cyan), rgba(51,173,229,0.4)); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent;">~900×</span>
        <span style="font-size:clamp(20px,2vw,30px); color:var(--text-2); font-weight:500;">mais rápido</span>
      </div>
      <div style="margin-top:clamp(24px,4vh,42px); border-left:4px solid var(--cyan); background:linear-gradient(90deg, rgba(51,173,229,0.12), rgba(51,173,229,0)); border-radius:0 12px 12px 0; padding:20px 28px; max-width:920px;">
        <div style="font-weight:700; font-size:clamp(18px,1.8vw,26px); color:var(--text);">POC realizada com sucesso. Próximo passo: a implementação completa.</div>
        <p class="body" style="margin-top:10px; font-size:clamp(15px,1.3vw,19px);">Em produção, com permissão de escrita, o agente deixa de só apontar e passa a resolver. A cobertura cresce mês a mês, com curadoria mensal e otimizações sob medida.</p>
      </div>
    </div>
    <div class="slide-footer"><span class="brand"><strong>Dalton Lab</strong> × Neogrid</span><span>POC · Agente de Homologação SalesDesk</span></div>
  </section>
'''

# ============================================================
# VERSION B — Gemini premium images as background
# ============================================================
def scrim(img, active=False):
    act = ' active' if active else ''
    return img, act

B1 = r'''  <!-- ============ SLIDE 01 (B) — image ============ -->
  <section class="slide active" data-theme="dark" style="padding:0; overflow:hidden;">
    <img src="img_s1.png" alt="" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;">
    <div style="position:absolute; inset:0; z-index:1; background:linear-gradient(90deg, rgba(10,22,40,0.97) 0%, rgba(10,22,40,0.88) 36%, rgba(10,22,40,0.30) 66%, rgba(10,22,40,0) 100%);"></div>
    <div style="position:relative; z-index:2; padding:6vh 7vw; height:100%; display:flex; flex-direction:column;">
      <div class="slide-header reveal"><span class="slide-tag">O gargalo da homologação</span><span class="slide-num"><strong>01</strong> / 07</span></div>
      <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0; max-width:56%;">
        <div class="stat-number" style="font-size:clamp(120px,17vw,260px); line-height:0.82;">709<span class="frac" style="padding-left:0.42em;">dias</span></div>
        <div class="stat-label" style="max-width:20ch; margin-top:10px; font-size:clamp(22px,2.4vw,38px);">parados, em média, por chamado na fila de homologação.</div>
        <p class="body" style="margin-top:3.5vh; max-width:48ch; font-size:clamp(17px,1.45vw,22px);">Toda venda ganha passa por um <em class="highlight">checklist de 39 critérios</em>, conferidos um a um, antes de virar contrato.</p>
        <div style="display:flex; gap:clamp(30px,4vw,60px); margin-top:clamp(30px,4.5vh,52px);">
          <div><div class="metric-num" style="font-size:clamp(34px,3.6vw,56px);">484</div><div class="metric-label" style="margin-top:8px;">chamados / mês</div></div>
          <div><div class="metric-num" style="font-size:clamp(34px,3.6vw,56px);">144</div><div class="metric-label" style="margin-top:8px;">capacidade</div></div>
          <div><div class="metric-num" style="font-size:clamp(34px,3.6vw,56px);"><span>+</span>340</div><div class="metric-label" style="margin-top:8px;">a fila cresce / mês</div></div>
        </div>
      </div>
      ''' + FOOT1 + '''
    </div>
  </section>
'''

B5 = r'''  <!-- ============ SLIDE 05 (B) — image ============ -->
  <section class="slide" data-theme="dark" style="padding:0; overflow:hidden;">
    <img src="img_s5.png" alt="" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;">
    <div style="position:absolute; inset:0; z-index:1; background:linear-gradient(90deg, rgba(10,22,40,0.97) 0%, rgba(10,22,40,0.88) 36%, rgba(10,22,40,0.30) 66%, rgba(10,22,40,0) 100%);"></div>
    <div style="position:relative; z-index:2; padding:6vh 7vw; height:100%; display:flex; flex-direction:column;">
      <div class="slide-header reveal"><span class="slide-tag">O que isso destrava</span><span class="slide-num"><strong>05</strong> / 07</span></div>
      <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0; max-width:60%;">
        <h2 class="display-lg" style="max-width:18ch;">Fazer mais com o time que <em class="highlight">já existe</em>.</h2>
        <p class="body" style="margin-top:14px; max-width:46ch; font-size:clamp(17px,1.45vw,22px);">A meta que vocês definiram no diagnóstico: crescer em volume sem crescer o quadro.</p>
        <div style="display:flex; align-items:center; gap:clamp(22px,3vw,52px); margin:clamp(30px,5vh,56px) 0;">
          <div>
            <div style="font-size:clamp(52px,6.5vw,110px); font-weight:800; letter-spacing:-0.03em; line-height:0.9; color:var(--text-2);">~57<span style="font-family:var(--serif); font-style:italic; font-weight:300; font-size:0.3em; color:var(--text-3); padding-left:0.18em;">h/mês</span></div>
            <div style="font-family:var(--mono); font-size:12px; letter-spacing:1.5px; text-transform:uppercase; color:var(--text-3); margin-top:12px;">POC hoje · leitura</div>
          </div>
          <div style="color:var(--cyan);"><svg width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/></svg></div>
          <div>
            <div class="stat-number" style="font-size:clamp(52px,6.5vw,110px); line-height:0.9;">~69<span class="frac" style="padding-left:0.18em;">h/mês</span></div>
            <div style="font-family:var(--mono); font-size:12px; letter-spacing:1.5px; text-transform:uppercase; color:var(--cyan); margin-top:12px;">implementação completa</div>
          </div>
        </div>
        <p class="body" style="max-width:52ch; font-size:clamp(15px,1.25vw,19px);">A analista vira <strong style="color:var(--text);">gestora de exceção</strong>: confirma, em vez de investigar. O déficit de <strong style="color:var(--text);">+340 chamados/mês para de crescer</strong>.</p>
      </div>
      <div class="slide-footer"><span class="brand"><strong>Dalton Lab</strong> × Neogrid</span><span>Horas devolvidas · projeção sobre o volume real, a validar</span></div>
    </div>
  </section>
'''

B6 = r'''  <!-- ============ SLIDE 06 (B) — image ============ -->
  <section class="slide" data-theme="dark" style="padding:0; overflow:hidden;">
    <img src="img_s6.png" alt="" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;">
    <div style="position:absolute; inset:0; z-index:1; background:linear-gradient(90deg, rgba(10,22,40,0.97) 0%, rgba(10,22,40,0.88) 38%, rgba(10,22,40,0.32) 68%, rgba(10,22,40,0) 100%);"></div>
    <div style="position:relative; z-index:2; padding:6vh 7vw; height:100%; display:flex; flex-direction:column;">
      <div class="slide-header reveal"><span class="slide-tag">O salto</span><span class="slide-num"><strong>06</strong> / 07</span></div>
      <div class="reveal" style="flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0; max-width:62%;">
        <div class="stat-number" style="font-size:clamp(110px,16vw,250px); line-height:0.84;">~900<span class="frac" style="padding-left:0.3em;">×</span></div>
        <div class="stat-label" style="max-width:22ch; margin-top:10px; font-size:clamp(22px,2.4vw,38px);">mais rápido. O que levava ~15 minutos agora leva ~1 segundo.</div>
        <div style="margin-top:clamp(28px,4.5vh,50px); border-left:4px solid var(--cyan); background:linear-gradient(90deg, rgba(51,173,229,0.14), rgba(51,173,229,0)); border-radius:0 12px 12px 0; padding:20px 28px; max-width:58ch;">
          <div style="font-weight:700; font-size:clamp(18px,1.8vw,26px); color:var(--text);">POC realizada com sucesso. Próximo passo: a implementação completa.</div>
          <p class="body" style="margin-top:10px; font-size:clamp(15px,1.3vw,19px);">Em produção, com permissão de escrita, o agente deixa de só apontar e passa a resolver. A cobertura cresce mês a mês, com curadoria mensal e otimizações sob medida.</p>
        </div>
      </div>
      <div class="slide-footer"><span class="brand"><strong>Dalton Lab</strong> × Neogrid</span><span>POC · Agente de Homologação SalesDesk</span></div>
    </div>
  </section>
'''

def assemble(s1, s5, s6):
    return s1 + sections[1] + sections[2] + sections[3] + s5 + s6 + sections[6]

def splice(slides_html, outfile):
    i = tpl.index('  <!-- ============ SLIDE 01'); j = tpl.index('</div>\n\n<div class="nav">')
    out = tpl[:i] + slides_html + '\n\n' + tpl[j:]
    out = out.replace('const total = 19;', 'const total = 7;')
    out = out.replace('<title>Dalton Lab — Como sua empresa se torna uma Organização Agêntica</title>',
                      '<title>POC Agente de Homologação SalesDesk — Dalton Lab para Neogrid</title>')
    io.open(outfile, 'w', encoding='utf-8').write(out)
    print('wrote', outfile, '| sections', out.count('<section class="slide'))

splice(assemble(A1, A5, A6), 'index-a.html')
splice(assemble(B1, B5, B6), 'index-b.html')
