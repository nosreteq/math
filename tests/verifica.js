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

// A página inicial é uma SPA: abas de nível no cabeçalho, painel por nível e a aula num iframe.
async function checaSPA(browser) {
  const nome = 'index.html (SPA)';
  const base = 'file://' + path.join(RAIZ, 'index.html');
  const p = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const erros = [];
  p.on('pageerror', e => erros.push(e.message));
  const visivel = async (sel) => p.locator(sel).isVisible();
  // clicar num link de rota: o hashchange é assíncrono, espera a visão trocar
  const clica = async (sel, hash) => {
    await p.click(sel);
    await p.waitForFunction(h => location.hash === h, hash, { timeout: 3000 }).catch(() => {});
    await p.waitForTimeout(100);
  };

  await p.goto(base);
  if (!(await visivel('#v-inicio'))) falha(nome, 'início não aparece sem rota');
  const abas = await p.locator('#niveis a').count();
  const catalogo = await p.evaluate(() => window.CATALOGO.length);
  if (abas !== catalogo) falha(nome, `${abas} abas de nível no cabeçalho (esperado ${catalogo})`);
  if (await p.locator('.md0-menu-btn').count()) falha(nome, 'ainda existe o botão do menu modal');

  await clica('#niveis a[href="#/nivel/2"]', '#/nivel/2');
  if (p.url().split('#')[1] !== '/nivel/2') falha(nome, `aba do Nível 2 levou a ${p.url()}`);
  if (await visivel('#v-inicio') || !(await visivel('#v-nivel'))) falha(nome, 'aba de nível não trocou o painel');
  const cards2 = await p.locator('#painel-nivel a.card').count();
  if (cards2 !== 6) falha(nome, `painel do Nível 2 com ${cards2} aulas (esperado 6)`);
  if ((await p.locator('#chips a.chip').count()) !== 6) falha(nome, 'faixa de aulas do Nível 2 incompleta');

  await clica('#niveis a[href="#/nivel/3"]', '#/nivel/3');
  if ((await p.locator('#painel-nivel .card.breve').count()) !== 6) falha(nome, 'Nível 3 deveria listar 6 aulas "em breve"');

  // abre uma aula pelo painel: vira iframe abaixo do cabeçalho
  await clica('#niveis a[href="#/nivel/2"]', '#/nivel/2');
  await clica('#painel-nivel a.card >> nth=0', '#/aula/07-equacoes-a-balanca');
  if (!p.url().endsWith('#/aula/07-equacoes-a-balanca')) falha(nome, `card abriu ${p.url()}`);
  const quadro = p.frameLocator('#quadro');
  await quadro.locator('.wrap').waitFor({ timeout: 5000 }).catch(() => falha(nome, 'aula não carregou no iframe'));
  if (await quadro.locator('.md0-barra').count()) falha(nome, 'barra da aula avulsa apareceu dentro do curso');
  const alt = await p.evaluate(() => document.getElementById('quadro').getBoundingClientRect().bottom);
  if (Math.abs(alt - 800) > 2) falha(nome, `iframe não ocupa o resto da tela (termina em ${alt}px)`);
  if (!(await p.locator('#chips a.chip.ativa').count())) falha(nome, 'aula aberta sem destaque na faixa');

  // exercício feito dentro do iframe atualiza o progresso do painel
  const certa = await quadro.locator('#ex1 .alts').getAttribute('data-r').catch(() => null);
  if (certa !== null) await quadro.locator(`#ex1 .alt[data-i="${certa}"]`).click();
  else {
    for (const i of await quadro.locator('#ex1 input[data-r]').all()) await i.fill(await i.getAttribute('data-r'));
    await quadro.locator('#ex1 button.check').click();
  }

  // botão "próxima" do cabeçalho e o do fim da aula
  await clica('#prox', '#/aula/08-sistemas-de-equacoes');
  if (!p.url().endsWith('#/aula/08-sistemas-de-equacoes')) falha(nome, `"Próxima" levou a ${p.url()}`);
  await quadro.locator('.md0-fim a.prox').click();
  await p.waitForFunction(() => location.hash === '#/aula/09-potencias-raizes-e-pitagoras', null, { timeout: 3000 })
    .catch(() => falha(nome, 'botão "Próxima aula" do fim da aula não navegou o curso'));
  await p.goBack({ waitUntil: 'commit' });
  await p.waitForFunction(() => location.hash === '#/aula/08-sistemas-de-equacoes', null, { timeout: 3000 })
    .catch(() => falha(nome, 'voltar do navegador não voltou à aula anterior'));

  await clica('#niveis a[href="#/nivel/2"]', '#/nivel/2');
  const txt = await p.locator('#painel-nivel a.card >> nth=0').innerText();
  if (!txt.includes('1 de 6')) falha(nome, 'progresso feito no iframe não apareceu no card da aula');

  await p.goto(base + '#/rota/que-nao-existe');
  if (!(await visivel('#v-inicio'))) falha(nome, 'rota desconhecida não volta ao início');

  // celular: nenhuma visão rola para o lado
  await p.setViewportSize({ width: 375, height: 800 });
  for (const r of ['#/', '#/nivel/1', '#/nivel/3', '#/aula/06-setas-e-tabelas-de-numeros']) {
    await p.goto(base + r);
    await p.waitForTimeout(300);
    const sobra = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    if (sobra > 0) falha(nome, `transborda ${sobra}px na horizontal no celular em ${r}`);
  }

  for (const e of erros) falha(nome, `erro de JavaScript: ${e}`);
  console.log(`${falhas.some(f => f.startsWith(nome)) ? '✘' : '✔'} ${nome}`);
  await p.close();
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
    if (!(await p.locator('.md0-barra').count())) falha(slug, 'aula aberta sozinha sem a barra de navegação do curso');
    const sobra = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    if (sobra > 0) falha(slug, `transborda ${sobra}px na horizontal no celular (375px)`);

    for (const e of erros) falha(slug, `erro de JavaScript: ${e}`);
    console.log(`${falhas.some(f => f.startsWith(slug)) ? '✘' : '✔'} ${slug}`);
    await p.close();
  }
  await checaSPA(browser);
  await browser.close();
  if (falhas.length) { console.log('\nFalhas:\n- ' + falhas.join('\n- ')); process.exit(1); }
  console.log(`\nTudo certo: ${aulas.length} aulas verificadas.`);
})();
