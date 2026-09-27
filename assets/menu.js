/*
 * menu.js — menu de navegação entre níveis e aulas.
 *
 * Basta incluir <script src=".../assets/menu.js"> em qualquer página
 * (home ou aula) para ganhar um botão fixo "☰ Aulas" que abre um painel
 * com todos os níveis e aulas do curso, destacando a aula atual e
 * marcando as que ainda não existem como "em preparo".
 */
(function () {
  "use strict";

  var NIVEIS = [
    {
      nome: "Nível 1 — Básico",
      aulas: [
        { n: 1, slug: "01-o-que-e-uma-funcao", titulo: "O que é uma função" },
        { n: 2, slug: "02-desenhar-numeros-no-papel", titulo: "Desenhar números no papel" },
        { n: 3, slug: "03-angulos-e-o-circulo", titulo: "Ângulos e o círculo" },
        { n: 4, slug: "04-seno-e-cosseno", titulo: "Seno e cosseno" },
        { n: 5, slug: "05-ondas", titulo: "Ondas" },
        { n: 6, slug: "06-setas-e-tabelas-de-numeros", titulo: "Setas e tabelas de números" }
      ]
    },
    {
      nome: "Nível 2 — Intermediário",
      aulas: [
        { n: 7, slug: "07-sistemas-de-equacoes", titulo: "Sistemas de equações" },
        { n: 8, slug: "08-decomposicao-de-sinais-em-ondas", titulo: "Decomposição de sinais em ondas" },
        { n: 9, slug: "09-estatistica-com-vetores", titulo: "Estatística com vetores" },
        { n: 10, slug: "10-projecao-e-minimos-quadrados", titulo: "Projeção e mínimos quadrados" }
      ]
    }
  ];

  var emAula = location.pathname.indexOf("/aulas/") !== -1;
  var prefixoAulas = emAula ? "../../aulas/" : "aulas/";
  var hrefHome = emAula ? "../../index.html" : "index.html";
  var hrefPlano = emAula ? "../../PLANO.md" : "PLANO.md";

  var css = ""
    + ".md0-menu{position:fixed;top:14px;left:14px;z-index:9999;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px}"
    + ".md0-menu-btn{background:#1b1b1b;color:#f6f2e9;padding:8px 16px;border-radius:20px;cursor:pointer;box-shadow:2px 3px 6px rgba(0,0,0,.2);border:none;font-size:14px;font-weight:700}"
    + ".md0-menu-overlay{position:fixed;inset:0;background:rgba(27,27,27,.55);z-index:10000;display:flex;align-items:flex-start;justify-content:center;padding:70px 16px 16px}"
    + ".md0-menu-panel{background:#fffdf7;border-radius:12px;padding:20px 22px 16px;max-width:380px;width:100%;max-height:80vh;overflow-y:auto;box-shadow:0 12px 30px rgba(0,0,0,.3)}"
    + ".md0-menu-panel h4{margin:18px 0 8px;font-size:13px;letter-spacing:.4px;color:#6b7280;text-transform:uppercase;display:flex;align-items:center;gap:6px}"
    + ".md0-menu-panel h4:first-of-type{margin-top:2px}"
    + ".md0-menu-fechar{background:none;border:none;color:#6b7280;cursor:pointer;font-size:20px;float:right;line-height:1;padding:0}"
    + ".md0-menu-home{display:block;padding:9px 12px;border-radius:8px;text-decoration:none;color:#1b1b1b;font-weight:700;background:#fde68a;margin-bottom:4px}"
    + ".md0-menu-item{display:block;padding:9px 12px;border-radius:8px;text-decoration:none;color:#1b1b1b;font-size:14.5px;margin:2px 0}"
    + ".md0-menu-item:hover{background:#eae4d6}"
    + ".md0-menu-item.ativa{background:#dbeafe;font-weight:700;color:#1e3a8a}"
    + ".md0-menu-item.bloqueada{color:#9ca3af;cursor:default;display:flex;justify-content:space-between;gap:8px}"
    + ".md0-menu-item.bloqueada:hover{background:none}"
    + ".md0-menu-tag{font-size:11px;background:#e5e7eb;color:#6b7280;padding:2px 8px;border-radius:10px;white-space:nowrap}"
    + "@media(max-width:620px){.md0-menu{top:auto;bottom:14px;left:14px}.md0-menu-btn{box-shadow:0 4px 12px rgba(0,0,0,.35)}}"
    + ".md0-menu-plano{display:block;margin-top:16px;padding-top:14px;border-top:2px solid #e6e0d2;color:#2563eb;font-weight:700;text-decoration:none;font-size:14px}";
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var raiz = document.createElement("div");
  raiz.className = "md0-menu";
  document.body.appendChild(raiz);

  var btn = document.createElement("button");
  btn.className = "md0-menu-btn";
  btn.textContent = "☰ Aulas";
  btn.setAttribute("aria-haspopup", "true");
  btn.addEventListener("click", abrirMenu);
  raiz.appendChild(btn);

  function slugAtual() {
    if (!emAula) return null;
    var m = location.pathname.match(/\/aulas\/([^/]+)\//);
    return m ? m[1] : null;
  }

  function abrirMenu() {
    var atual = slugAtual();
    var overlay = document.createElement("div");
    overlay.className = "md0-menu-overlay";

    var painel = document.createElement("div");
    painel.className = "md0-menu-panel";

    var fechar = document.createElement("button");
    fechar.className = "md0-menu-fechar";
    fechar.setAttribute("aria-label", "Fechar menu");
    fechar.innerHTML = "&times;";
    fechar.addEventListener("click", function () { overlay.remove(); });
    painel.appendChild(fechar);

    var home = document.createElement("a");
    home.className = "md0-menu-home";
    home.href = hrefHome;
    home.textContent = "🏠 Início do curso";
    painel.appendChild(home);

    NIVEIS.forEach(function (nivel) {
      var h4 = document.createElement("h4");
      h4.textContent = nivel.nome;
      painel.appendChild(h4);

      nivel.aulas.forEach(function (aula) {
        if (aula.slug) {
          var a = document.createElement("a");
          a.className = "md0-menu-item" + (aula.slug === atual ? " ativa" : "");
          a.href = prefixoAulas + aula.slug + "/index.html";
          a.textContent = "Aula " + aula.n + " — " + aula.titulo;
          painel.appendChild(a);
        } else {
          var span = document.createElement("span");
          span.className = "md0-menu-item bloqueada";
          span.innerHTML = "<span>Aula " + aula.n + " — " + aula.titulo + "</span><span class=\"md0-menu-tag\">em preparo</span>";
          painel.appendChild(span);
        }
      });
    });

    var plano = document.createElement("a");
    plano.className = "md0-menu-plano";
    plano.href = hrefPlano;
    plano.textContent = "📋 Ver o roteiro completo do curso";
    painel.appendChild(plano);

    overlay.appendChild(painel);
    document.body.appendChild(overlay);

    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) overlay.remove();
    });
    document.addEventListener("keydown", function fechaEsc(e) {
      if (e.key === "Escape") { overlay.remove(); document.removeEventListener("keydown", fechaEsc); }
    });
  }
})();
