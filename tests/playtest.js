// Playtest das aulas: para cada laboratório, mexe em cada controle (sliders nos extremos, cada botão
// duas vezes, setas nas alças, cliques no desenho) e registra o que o laboratório responde; para cada
// exercício, clica todas as alternativas (ou erra e acerta a conta) e guarda a explicação mostrada.
// Sai um .md por aula — é a base da análise lúdica em QUALIDADE.md.
//
//   node tests/playtest.js            → todas as aulas
//   node tests/playtest.js 07,16      → só as aulas que começam com 07 e 16
//   OUT=/pasta node tests/playtest.js → onde gravar (padrão: pasta temporária do sistema)
//   CHROMIUM_PATH=/caminho/chromium   → usa um Chromium já instalado
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const OUT = process.env.OUT || path.join(require('os').tmpdir(), 'md0-playtest');
const AULAS = path.join(__dirname, '..', 'aulas');
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const dirs = fs.readdirSync(AULAS).sort().filter(d => !process.argv[2] || process.argv[2].split(',').some(x => d.startsWith(x)));
  const metricas = {};
  for (const d of dirs) {
    const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
    const erros = []; p.on('pageerror', e => erros.push(e.message));
    p.on('dialog', dl => dl.dismiss());
    await p.goto('file://' + path.join(AULAS, d, 'index.html'));
    await p.waitForTimeout(500);
    const r = await p.evaluate(async () => {
      const esp = ms => new Promise(res => setTimeout(res, ms));
      const txt = e => (e ? e.textContent.trim().replace(/\s+/g, ' ') : '');
      const SUCESSO = /🎉|✔|acert|bateu|parab|exat|no alvo|conseguiu|achou|venceu|ganhou|perfeit|isso!|certo!/i;
      const h1 = txt(document.querySelector('h1'));
      const selo = txt(document.querySelector('.aula-num'));
      const pecas = ['cerebro', 'guru', 'idiota', 'cuidado', 'pontos', 'porque', 'lareira', 'ja-sabe'].filter(c => document.querySelector('.' + c));
      const labs = [];
      const ls = [...document.querySelectorAll('div.lab')];
      for (let i = 0; i < ls.length; i++) {
        const l = ls[i];
        const leTexto = () => {
          let t = [...l.querySelectorAll('.rabisco, .pc-caixa')].map(txt).filter(Boolean).join(' ‖ ');
          if (!t) t = [...l.querySelectorAll('[id^=txt], [id^=res], .placar')].map(txt).filter(Boolean).join(' ‖ ');
          return t.slice(0, 260);
        };
        const intro = [...l.querySelectorAll(':scope > p:not(.rabisco)')].map(txt).filter(Boolean).join(' | ');
        const sliders = [...l.querySelectorAll('input[type=range]')];
        const botoes = [...l.querySelectorAll('button')].filter(bt => !bt.closest('.pc-caixa'));
        const campos = [...l.querySelectorAll('input[type=number], input[type=text], select')].filter(c => !c.closest('.pc-caixa'));
        const alcas = [...l.querySelectorAll('svg [tabindex], svg[tabindex]')];
        const clic = [...l.querySelectorAll('svg *')].filter(e => getComputedStyle(e).cursor === 'pointer');
        const vistos = new Set(), eventos = [];
        const registra = (acao) => { const t = leTexto(); if (!vistos.has(t)) { vistos.add(t); eventos.push(acao + ' → ' + t); } };
        registra('início');
        for (const s of sliders) {
          const v0 = s.value, rot = (l.querySelector('label[for="' + s.id + '"]') ? txt(l.querySelector('label[for="' + s.id + '"]')) : s.id);
          for (const v of [s.min, s.max]) { s.value = v; s.dispatchEvent(new Event('input', { bubbles: true })); s.dispatchEvent(new Event('change', { bubbles: true })); await esp(40); registra(rot + '=' + v); }
          s.value = v0; s.dispatchEvent(new Event('input', { bubbles: true })); s.dispatchEvent(new Event('change', { bubbles: true }));
        }
        let aleatorio = false;
        for (const bt of botoes) {
          const rot = txt(bt).slice(0, 40);
          bt.click(); await esp(250); const t1 = leTexto(); registra('[' + rot + ']');
          bt.click(); await esp(250); const t2 = leTexto(); registra('[' + rot + ']×2');
          if (t1 !== t2 && /nov|sort|🎲|outr|jog|mais|embaralh|gera|lanç|rola|próxim/i.test(rot)) aleatorio = true;
        }
        for (const a of alcas.slice(0, 3)) {
          for (let k = 0; k < 3; k++) a.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
          await esp(40); registra('alça→');
        }
        for (const c of clic.slice(0, 3)) { c.dispatchEvent(new MouseEvent('click', { bubbles: true })); c.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true })); await esp(60); registra('clique'); }
        const ctrl = [];
        if (sliders.length) ctrl.push(sliders.length + ' slider(s): ' + sliders.map(s => { const lb = l.querySelector('label[for="' + s.id + '"]'); return (lb ? txt(lb) : s.id) + '[' + s.min + '…' + s.max + ']'; }).join(', '));
        if (botoes.length) ctrl.push('botões: ' + botoes.map(bt => '«' + txt(bt).slice(0, 30) + '»').join(' '));
        if (campos.length) ctrl.push(campos.length + ' campo(s)');
        if (alcas.length) ctrl.push(alcas.length + ' alça(s) arrastável(is)');
        if (clic.length) ctrl.push(clic.length + ' elemento(s) clicável(is) no desenho');
        if (l.querySelector('.pc-caixa')) ctrl.push('preveja-e-confira');
        labs.push({ tit: txt(l.querySelector('.tit')).replace(/^🔧\s*Laborat[óo]rio:\s*/, ''), intro, ctrl, eventos: eventos.slice(0, 9), nTextos: vistos.size, sucesso: [...vistos].some(t => SUCESSO.test(t)), aleatorio: aleatorio || !!l.querySelector('.pc-caixa'), pc: !!l.querySelector('.pc-caixa') });
      }
      const exs = [];
      for (const e of document.querySelectorAll('.ex')) {
        const perg = [...e.querySelectorAll(':scope > p')].filter(pp => !pp.classList.contains('dica') && !pp.querySelector('input,select')).map(txt).join(' ');
        const dica = txt(e.querySelector('.dica'));
        const alts = e.querySelector('.alts');
        const fb = () => txt(e.querySelector('.fb'));
        let tipo, gabarito, detalhes = [];
        if (alts) {
          tipo = 'múltipla escolha';
          const certa = alts.dataset.r;
          for (const a of alts.querySelectorAll('.alt')) {
            a.click(); await esp(10);
            detalhes.push((a.dataset.i === certa ? '(✔) ' : '( ) ') + txt(a) + ' ⇒ ' + fb().slice(0, 170));
          }
          gabarito = txt(alts.querySelector('.alt[data-i="' + certa + '"]'));
        } else {
          const ins = [...e.querySelectorAll('input[data-r]')], sels = [...e.querySelectorAll('select[data-r]')];
          tipo = sels.length ? 'ligar' : (ins.length > 1 ? 'conta (' + ins.length + ' campos)' : 'conta');
          const bt = e.querySelector('button.check');
          ins.forEach(i => i.value = '9999');
          sels.forEach(s => { const op = [...s.options].find(o => o.value !== '' && o.value !== s.dataset.r); if (op) s.value = op.value; });
          bt.click(); await esp(10); detalhes.push('errado ⇒ ' + fb().slice(0, 200));
          ins.forEach(i => i.value = i.dataset.r); sels.forEach(s => s.value = s.dataset.r);
          bt.click(); await esp(10); detalhes.push('certo ⇒ ' + fb().slice(0, 200));
          gabarito = sels.length ? sels.map(s => txt(s.closest('tr').querySelector('td')) + ' → ' + txt(s.querySelector('option[value="' + s.dataset.r + '"]'))).join('; ') : ins.map(i => i.dataset.r).join(' e ');
        }
        exs.push({ id: e.id, tit: txt(e.querySelector('.tit')), perg, tipo, gabarito, dica, detalhes });
      }
      const placar = !!document.getElementById('pn'), confete = typeof window.confete === 'function';
      return { h1, selo, pecas, labs, exs, placar, confete };
    });
    r.erros = erros;
    const L = [];
    L.push('# ' + d + ' — ' + r.h1, '', r.selo + ' · peças: ' + r.pecas.join(', ') + (erros.length ? ' · ERROS JS: ' + erros.join(' / ') : ''), '');
    r.labs.forEach((lb, i) => {
      L.push('## Lab ' + (i + 1) + ': ' + lb.tit + (lb.sucesso ? '  [sucesso detectado]' : '') + (lb.aleatorio ? '  [rejogável]' : ''));
      L.push('- pede: ' + lb.intro);
      L.push('- controles: ' + (lb.ctrl.join('; ') || 'NENHUM'));
      L.push('- respostas (' + lb.nTextos + ' textos distintos):');
      lb.eventos.forEach(ev => L.push('  - ' + ev));
    });
    L.push('');
    r.exs.forEach(ex => {
      L.push('## ' + ex.id + ' (' + ex.tipo + ')' + (ex.tit.match(/desafio/i) ? ' DESAFIO' : '') + ': ' + ex.perg);
      L.push('- gabarito: ' + ex.gabarito + (ex.dica ? ' · ' + ex.dica : ''));
      ex.detalhes.forEach(dt => L.push('  - ' + dt));
    });
    fs.writeFileSync(OUT + '/' + d.slice(0, 2) + '.md', L.join('\n') + '\n');
    metricas[d] = { labs: r.labs.map(lb => ({ tit: lb.tit, ctrl: lb.ctrl, nTextos: lb.nTextos, sucesso: lb.sucesso, aleatorio: lb.aleatorio, pc: lb.pc })), exs: r.exs.map(e => ({ id: e.id, tipo: e.tipo, tit: e.tit })), erros };
    process.stderr.write(d + ' ');
    await p.close();
  }
  fs.writeFileSync(OUT + '/metricas.json', JSON.stringify(metricas, null, 1));
  await b.close();
  console.log('\nplaytest gravado em ' + OUT);
})();
