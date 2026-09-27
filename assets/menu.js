/*
 * menu.js — ligação de cada aula com o resto do curso.
 *
 * Precisa de catalogo.js carregado antes. Dois modos:
 *
 *  - Dentro do curso (a aula aberta no quadro da página inicial): não
 *    desenha menu nenhum — o cabeçalho com os níveis já está lá em cima.
 *    Só avisa a página de fora quando um exercício é marcado (para
 *    atualizar o progresso) e faz os links saírem do quadro.
 *
 *  - Aula aberta sozinha (arquivo direto ou link compartilhado): coloca
 *    uma barra fina no topo com o caminho "curso › nível › aula", o link
 *    para abrir a aula dentro do curso e os botões anterior/próxima.
 *
 * Nos dois modos, o fim da aula ganha o botão para a próxima.
 */
(function () {
  "use strict";

  var CAT = window.CATALOGO || [];
  var m = location.pathname.match(/\/aulas\/([^/]+)\//);
  var slug = m ? m[1] : null;
  if (!slug) return;

  var ordem = [];
  CAT.forEach(function (nv) {
    nv.aulas.forEach(function (a) { if (a.slug) ordem.push({ nivel: nv, aula: a }); });
  });
  var i = -1;
  for (var k = 0; k < ordem.length; k++) if (ordem[k].aula.slug === slug) i = k;
  if (i === -1) return;
  var atual = ordem[i], ant = ordem[i - 1], prox = ordem[i + 1];

  var dentro = false;
  try { dentro = window.self !== window.top; } catch (e) { dentro = true; }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  var css = ""
    + ".md0-barra{background:#1b1b1b;color:#e6e0d2;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;border-bottom:3px solid #d97706}"
    + ".md0-barra .in{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:8px 14px;padding:8px 16px;flex-wrap:wrap}"
    + ".md0-barra a{color:#e6e0d2;text-decoration:none}"
    + ".md0-barra a:hover{text-decoration:underline}"
    + ".md0-barra .marca{font-family:'Comic Sans MS','Comic Neue','Chalkboard SE',cursive;font-weight:700;color:#fde68a}"
    + ".md0-barra .sep{color:#6b7280}"
    + ".md0-barra .trilha{flex:1 1 auto;min-width:0}"
    + ".md0-barra .acoes{display:flex;gap:6px;flex-wrap:wrap}"
    + ".md0-barra .acoes a{background:#383838;padding:3px 12px;border-radius:14px;font-weight:600;white-space:nowrap}"
    + ".md0-barra .acoes a.curso{background:#2563eb;color:#fff}"
    + ".md0-fim{max-width:860px;margin:0 auto 60px;padding:0 22px;display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between;font-family:'Segoe UI',system-ui,sans-serif}"
    + ".md0-fim a{flex:1 1 220px;display:block;text-decoration:none;color:#1b1b1b;background:#fffdf7;border:3px solid #1b1b1b;border-radius:12px;padding:12px 16px;box-shadow:4px 4px 0 rgba(27,27,27,.13)}"
    + ".md0-fim a:hover{background:#fff}"
    + ".md0-fim a small{display:block;color:#d97706;font-weight:700;font-size:13px}"
    + ".md0-fim a.prox{text-align:right}"
    + (dentro ? ".md0-auth{display:none!important}" : "");
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // endereço de uma aula: dentro do curso é uma rota; sozinha é o arquivo
  function hrefAula(item) {
    return dentro ? "#" : "../" + item.aula.slug + "/index.html";
  }
  function ligar(a, item) {
    a.href = hrefAula(item);
    if (dentro) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        window.parent.postMessage({ md0: "ir", hash: "#/aula/" + item.aula.slug }, "*");
      });
    }
  }

  // ---------- barra do topo (só na aula aberta sozinha) ----------
  if (!dentro) {
    var barra = document.createElement("nav");
    barra.className = "md0-barra";
    barra.setAttribute("aria-label", "Navegação do curso");
    var base = "../../index.html";
    barra.innerHTML = '<div class="in">'
      + '<span class="trilha"><a class="marca" href="' + base + '#/">✏️ Matemática do Zero</a>'
      + ' <span class="sep">›</span> <a href="' + base + "#/nivel/" + atual.nivel.n + '">' + (atual.nivel.eletiva ? "" : "Nível " + atual.nivel.n + " · ") + esc(atual.nivel.nome) + "</a>"
      + ' <span class="sep">›</span> Aula ' + atual.aula.n + "</span>"
      + '<span class="acoes">'
      + (ant ? '<a href="../' + ant.aula.slug + '/index.html" title="Aula ' + ant.aula.n + " — " + esc(ant.aula.titulo) + '">◀ Aula ' + ant.aula.n + "</a>" : "")
      + '<a class="curso" href="' + base + "#/aula/" + slug + '">Abrir no curso</a>'
      + (prox ? '<a href="../' + prox.aula.slug + '/index.html" title="Aula ' + prox.aula.n + " — " + esc(prox.aula.titulo) + '">Aula ' + prox.aula.n + " ▶</a>" : "")
      + "</span></div>";
    document.body.insertBefore(barra, document.body.firstChild);
  }

  // ---------- fim da aula: anterior / próxima ----------
  var fim = document.createElement("nav");
  fim.className = "md0-fim";
  fim.setAttribute("aria-label", "Aula anterior e próxima");
  [[ant, "◀ Aula anterior", "ant"], [prox, "Próxima aula ▶", "prox"]].forEach(function (p) {
    if (!p[0]) return;
    var a = document.createElement("a");
    a.className = p[2];
    a.innerHTML = "<small>" + p[1] + "</small>Aula " + p[0].aula.n + " — " + esc(p[0].aula.titulo);
    ligar(a, p[0]);
    fim.appendChild(a);
  });
  if (fim.children.length) document.body.appendChild(fim);

  if (!dentro) return;

  // ---------- dentro do curso ----------
  // links para fora da aula (roteiro, README...) saem do quadro
  Array.prototype.forEach.call(document.querySelectorAll("a[href]"), function (a) {
    var h = a.getAttribute("href");
    if (h.charAt(0) !== "#" && !a.target && !a.closest(".md0-fim")) a.target = "_top";
  });

  // avisa a página de fora quando um exercício é marcado
  if (window.Progresso && Progresso.marcar) {
    var marcar = Progresso.marcar;
    Progresso.marcar = function (aulaId, itemId) {
      marcar(aulaId, itemId);
      try { window.parent.postMessage({ md0: "progresso", aula: aulaId }, "*"); } catch (e) { /* sem página de fora */ }
    };
  }
})();
