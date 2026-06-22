# POC Neogrid — Deck de Apresentação (Diretores)

Deck HTML de **10 slides** da POC do **Agente de Homologação SalesDesk** (Dalton Lab × Neogrid), para apresentação a diretores C-Level.

- **Final:** [`index.html`](index.html) — auto-contido (logo SVG inline, sem dependência externa), estilo cinematográfico navy v2, navegação por teclado, **responsivo (mobile otimizado)**.
- **No ar:** https://deployng26lp5bvjyp.vercel.app (link sem auth, apenas obscuridade pelo URL).
- Sistema de design: skill `dalton-apresentacao-v2`.

## Estrutura (10 slides)

1. O excesso (484/mês) · 2. A capacidade (144) · 3. O transbordo (709 dias) · 4. Timeline da POC (21 dias do acesso ao ar) · 5. O que fizemos (296 reais, 15 min → 1 seg) · 6. Como funciona (cadeia de 6 elos) · 7. Crescer sem contratar (57 a 70 h/mês) · 8. O salto: 15 min → 1 seg · 9. O salto: ~900× + sucesso · 10. Fechamento.

## Como editar

O deck é montado por *splice*: `_template_base.html` (head/CSS/JS) + `_slides.html` (conteúdo). Para reconstruir, injeta-se `_slides.html` entre os marcadores do template e ajusta-se `const total`.

## Versão B (imagens premium)

`_genimg.py` gera imagens via Gemini 3 Pro Image (OpenRouter); `img_s1/5/6.png` são os assets. A **Versão A** (esquemas SVG/CSS, o `index.html`) foi a escolhida.

---

Dalton Lab · 2026
