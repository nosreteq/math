// Verificação automática de todas as aulas. Rode da raiz do projeto:
//   npm install --no-save playwright && npx playwright install chromium
//   node tests/verifica.js
// Para usar um Chromium já instalado: CHROMIUM_PATH=/caminho/chromium node tests/verifica.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const RAIZ = path.resolve(__dirname, '..');
const falhas = [];
const falha = (aula, msg) => falhas.push(`${aula}: ${msg}`);

function checaLinks() {
  const arquivos = ['index.html'];
  for (const d of fs.readdirSync(path.join(RAIZ, 'aulas'))) arquivos.push(`aulas/${d}/index.html`, `aulas/${d}/notas.md`);
  for (const f of arquivos) {
    const txt = fs.readFileSync(path.join(RAIZ, f), 'utf8');
    const hrefs = [...txt.matchAll(/href="([^"#]+)"/g), ...txt.matchAll(/\]\((\.\.[^)]+)\)/g)].map(m => m[1]);
    for (const h of hrefs) {
      if (/^https?:/.test(h)) continue;
      if (!fs.existsSync(path.resolve(RAIZ, path.dirname(f), h))) falha(f, `link quebrado → ${h}`);
    }
  }
}

(async () => {
  checaLinks();
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const aulas = fs.readdirSync(path.join(RAIZ, 'aulas')).sort();
  for (const slug of aulas) {
    const url = 'file://' + path.join(RAIZ, 'aulas', slug, 'index.html');
    const p = await browser.newPage();
    const erros = [];
    p.on('pageerror', e => erros.push(e.message));
    await p.goto(url);

    const textoQuebrado = async (onde) => {
      const t = await p.evaluate(() => document.querySelector('.wrap').innerText);
      for (const bad of ['NaN', 'undefined', 'Infinity', ' + -', '[object']) if (t.includes(bad)) falha(slug, `"${bad}" no texto (${onde})`);
    };
    await textoQuebrado('carga');

    const labs = await p.locator('div.lab').count();
    if (labs !== 6) falha(slug, `${labs} laboratórios (esperado 6)`);

    for (const r of await p.locator('.lab input[type=range]').all()) {
      for (const attr of ['min', 'max', 'value']) {
        const v = await r.getAttribute(attr);
        await r.evaluate((el, v) => { el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); }, v);
      }
    }
    for (const b of await p.locator('.lab button').all()) { try { await b.click({ timeout: 1500 }); } catch (e) {} }
    await p.waitForTimeout(3000);
    await textoQuebrado('após mexer nos labs');

    // exercícios: primeiro errado (não pode pontuar), depois certo (tem que pontuar)
    const ids = await p.locator('.ex').evaluateAll(els => els.map(e => e.id));
    if (ids.length !== 6) falha(slug, `${ids.length} exercícios (esperado 6)`);
    for (const id of ids) {
      if (await p.locator(`#${id} .alts`).count()) {
        const certa = await p.locator(`#${id} .alts`).getAttribute('data-r');
        const errada = certa === '0' ? '1' : '0';
        await p.click(`#${id} .alt[data-i="${errada}"]`);
        if (!(await p.textContent(`#${id} .fb`)).trim().startsWith('✘')) falha(slug, `${id}: alternativa errada sem feedback de erro`);
        await p.click(`#${id} .alt[data-i="${certa}"]`);
      } else {
        const ins = await p.locator(`#${id} input[data-r]`).all();
        for (const i of ins) await i.fill('9999');
        await p.click(`#${id} button.check`);
        if (!(await p.textContent(`#${id} .fb`)).trim().startsWith('✘')) falha(slug, `${id}: resposta errada sem feedback de erro`);
        for (const i of ins) await i.fill(await i.getAttribute('data-r'));
        await p.click(`#${id} button.check`);
      }
      if (!(await p.textContent(`#${id} .fb`)).trim().startsWith('✔')) falha(slug, `${id}: gabarito não aceito`);
    }
    const placar = await p.textContent('#pn');
    if (placar !== String(ids.length)) falha(slug, `placar ${placar}/${ids.length}`);

    await p.setViewportSize({ width: 375, height: 800 });
    await p.reload();
    const sobra = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    if (sobra > 0) falha(slug, `transborda ${sobra}px na horizontal no celular (375px)`);

    for (const e of erros) falha(slug, `erro de JavaScript: ${e}`);
    console.log(`${falhas.some(f => f.startsWith(slug)) ? '✘' : '✔'} ${slug}`);
    await p.close();
  }
  await browser.close();
  if (falhas.length) { console.log('\nFalhas:\n- ' + falhas.join('\n- ')); process.exit(1); }
  console.log(`\nTudo certo: ${aulas.length} aulas verificadas.`);
})();
