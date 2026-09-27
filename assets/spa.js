/*
 * spa.js — a página inicial como aplicação de uma página só.
 *
 * Rotas (no #, para funcionar direto do arquivo, sem servidor):
 *   #/              início do curso
 *   #/nivel/N       painel com as aulas do nível N
 *   #/aula/<slug>   a aula aberta num quadro (iframe) abaixo do cabeçalho
 *
 * A aula continua sendo um arquivo HTML autocontido: o iframe mantém o CSS
 * e o JavaScript de cada uma isolados e tudo segue funcionando offline.
 */
(function () {
  "use strict";

  var CAT = window.CATALOGO || [];
  var TOTAL_EX = 6;
  var $ = function (id) { return document.getElementById(id); };

  // lista linear de aulas prontas, na ordem do curso (para anterior/próxima)
  var ordem = [];
  CAT.forEach(function (nv) {
    nv.aulas.forEach(function (a) { if (a.slug) ordem.push({ nivel: nv, aula: a }); });
  });

  function acharAula(slug) {
    for (var i = 0; i < ordem.length; i++) if (ordem[i].aula.slug === slug) return i;
    return -1;
  }
  function acharNivel(n) {
    for (var i = 0; i < CAT.length; i++) if (CAT[i].n === n) return CAT[i];
    return null;
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function feitos(slug) {
    try {
      var itens = JSON.parse(localStorage.getItem("md0_progresso_" + slug) || "[]");
      return Math.min(TOTAL_EX, itens.filter(function (id) { return /^ex\d+$/.test(id); }).length);
    } catch (e) { return 0; }
  }
  function prontas(nv) { return nv.aulas.filter(function (a) { return a.slug; }); }

  // ---------- cabeçalho ----------
  function renderNiveis(ativo) {
    $("niveis").innerHTML = CAT.map(function (nv) {
      var breve = !prontas(nv).length;
      return '<a href="#/nivel/' + nv.n + '"' + (breve ? ' class="breve"' : "")
        + (ativo === nv.n ? ' aria-current="page"' : "") + '><span class="nn">Nível </span>' + nv.n + " · " + esc(nv.nome)
        + (breve ? '<span class="mini">em breve</span>' : "") + "</a>";
    }).join("");
  }

  function renderChips(nv, slugAtivo) {
    $("chips").innerHTML = nv.aulas.map(function (a) {
      if (!a.slug) {
        return '<span class="chip breve" title="' + esc(a.titulo) + ' — em breve"><b>' + a.n + "</b>" + esc(a.titulo) + "</span>";
      }
      var cls = "chip" + (a.slug === slugAtivo ? " ativa" : "") + (feitos(a.slug) === TOTAL_EX ? " feita" : "");
      return '<a class="' + cls + '" href="#/aula/' + a.slug + '"' + (a.slug === slugAtivo ? ' aria-current="page"' : "")
        + '><b>' + a.n + "</b>" + esc(a.titulo) + "</a>";
    }).join("");
    var ativa = $("chips").querySelector(".ativa");
    if (ativa) $("chips").scrollLeft = ativa.offsetLeft - 16;
  }

  // ---------- visões ----------
  function mostrar(id) {
    ["v-inicio", "v-nivel", "v-aula"].forEach(function (v) { $(v).hidden = v !== id; });
    document.body.classList.toggle("modo-aula", id === "v-aula");
    if (id !== "v-aula") {
      var q = $("quadro");
      if (q.getAttribute("src")) {
        var vazio = document.createElement("iframe");
        vazio.id = "quadro";
        vazio.title = "Aula";
        q.parentNode.replaceChild(vazio, q);
      }
    }
  }

  function cardAula(a) {
    if (!a.slug) {
      return '<div class="card breve"><span class="estado">🔜</span><span class="num">AULA ' + a.n + "</span>"
        + "<h3>" + esc(a.titulo) + "</h3><p>" + esc(a.desc) + '</p><p class="labs">em preparo</p></div>';
    }
    var f = feitos(a.slug);
    var estado = f === TOTAL_EX ? "✅" : f ? "✏️" : "";
    return '<a class="card" href="#/aula/' + a.slug + '">'
      + (estado ? '<span class="estado">' + estado + "</span>" : "")
      + '<span class="num">AULA ' + a.n + "</span><h3>" + esc(a.titulo) + "</h3><p>" + esc(a.desc) + "</p>"
      + '<p class="labs">🔧 6 laboratórios · ✏️ ' + f + " de " + TOTAL_EX + " exercícios feitos</p>"
      + '<div class="barra"><i style="width:' + (f / TOTAL_EX * 100) + '%"></i></div></a>';
  }

  function renderInicio() {
    var niveisProntos = CAT.filter(function (nv) { return prontas(nv).length; }).length;
    $("tag-contagem").textContent = niveisProntos + " níveis · " + ordem.length + " aulas";
    $("escolha").innerHTML = CAT.map(function (nv) {
      var pr = prontas(nv);
      if (!pr.length) {
        return '<a class="card breve" href="#/nivel/' + nv.n + '" style="cursor:pointer"><span class="estado">🔜</span>'
          + '<span class="num">NÍVEL ' + nv.n + "</span><h3>" + esc(nv.nome) + "</h3><p>" + esc(nv.resumo) + '</p><p class="labs">em breve</p></a>';
      }
      var f = 0;
      pr.forEach(function (a) { f += feitos(a.slug); });
      var tot = pr.length * TOTAL_EX;
      return '<a class="card" href="#/nivel/' + nv.n + '"><span class="num">NÍVEL ' + nv.n + "</span><h3>" + esc(nv.nome) + "</h3>"
        + "<p>" + esc(nv.resumo) + '</p><p class="labs">📘 ' + pr.length + " aulas · ✏️ " + f + " de " + tot + " exercícios</p>"
        + '<div class="barra"><i style="width:' + (f / tot * 100) + '%"></i></div></a>';
    }).join("");
  }

  function renderNivel(nv) {
    var pr = prontas(nv);
    var f = 0;
    pr.forEach(function (a) { f += feitos(a.slug); });
    var tot = pr.length * TOTAL_EX;
    var h = '<p class="rotulo">NÍVEL ' + nv.n + " DE " + CAT.length + "</p>"
      + "<h1>" + esc(nv.nome) + ' <span class="badge' + (pr.length ? "" : " breve") + '">' + esc(nv.estado) + "</span></h1>"
      + '<p class="resumo">' + esc(nv.resumo) + "</p>";
    if (pr.length) {
      h += '<p class="geral">✏️ ' + f + " de " + tot + " exercícios feitos neste nível</p>"
        + '<div class="barra"><i style="width:' + (f / tot * 100) + '%"></i></div>';
    } else {
      h += '<p class="aviso-breve">As aulas deste nível ainda estão sendo preparadas. O que vai entrar em cada uma está no '
        + '<a href="PLANO.md">roteiro completo do curso</a>.</p>';
    }
    h += '<div class="grade">' + nv.aulas.map(cardAula).join("") + "</div>";
    $("painel-nivel").innerHTML = h;
  }

  function ajustarQuadro() {
    if (!document.body.classList.contains("modo-aula")) return;
    var alt = window.innerHeight - $("topo").getBoundingClientRect().height;
    $("quadro").style.height = Math.max(240, alt) + "px";
  }

  function passo(el, i) {
    if (i >= 0 && i < ordem.length) {
      el.classList.remove("off");
      el.href = "#/aula/" + ordem[i].aula.slug;
      el.title = "Aula " + ordem[i].aula.n + " — " + ordem[i].aula.titulo;
      el.removeAttribute("aria-disabled");
    } else {
      el.classList.add("off");
      el.href = "#/";
      el.title = "";
      el.setAttribute("aria-disabled", "true");
    }
  }

  // ---------- roteador ----------
  function rota() {
    var h = location.hash.replace(/^#\/?/, "");
    var m;
    // endereço da numeração antiga (18 aulas): troca pelo novo sem empilhar histórico
    var antigos = window.CATALOGO_ANTIGOS || {};
    if ((m = h.match(/^aula\/([\w-]+)$/)) && acharAula(m[1]) === -1 && antigos[m[1]]) {
      history.replaceState(null, "", "#/aula/" + antigos[m[1]]);
      h = "aula/" + antigos[m[1]];
    }
    if ((m = h.match(/^aula\/([\w-]+)$/)) && acharAula(m[1]) !== -1) {
      var i = acharAula(m[1]);
      var item = ordem[i];
      renderNiveis(item.nivel.n);
      renderChips(item.nivel, item.aula.slug);
      $("l2").hidden = false;
      $("passo").hidden = false;
      passo($("ant"), i - 1);
      passo($("prox"), i + 1);
      mostrar("v-aula");
      var src = "aulas/" + item.aula.slug + "/index.html";
      var q = $("quadro");
      if (q.getAttribute("src") !== src) {
        // iframe novo a cada aula: trocar o src empilharia uma entrada extra no
        // histórico e o "voltar" do navegador mexeria só no quadro
        var novo = document.createElement("iframe");
        novo.id = "quadro";
        novo.setAttribute("src", src);
        q.parentNode.replaceChild(novo, q);
        q = novo;
      }
      q.title = "Aula " + item.aula.n + " — " + item.aula.titulo;
      document.title = "Aula " + item.aula.n + " — " + item.aula.titulo + " · Matemática do Zero";
      window.scrollTo(0, 0);
      ajustarQuadro();
      return;
    }
    if ((m = h.match(/^nivel\/(\d+)$/)) && acharNivel(+m[1])) {
      var nv = acharNivel(+m[1]);
      renderNiveis(nv.n);
      renderChips(nv, null);
      $("l2").hidden = false;
      $("passo").hidden = true;
      renderNivel(nv);
      mostrar("v-nivel");
      document.title = "Nível " + nv.n + " — " + nv.nome + " · Matemática do Zero";
      window.scrollTo(0, 0);
      return;
    }
    if (h && location.hash !== "#/") {
      // rota desconhecida: volta ao início sem empilhar histórico
      history.replaceState(null, "", "#/");
    }
    renderNiveis(null);
    $("l2").hidden = true;
    renderInicio();
    mostrar("v-inicio");
    document.title = "Matemática do Zero — o curso";
  }

  // progresso marcado dentro da aula (menu.js avisa) ou em outra aba
  function atualizarProgresso() {
    var h = location.hash;
    var m = h.match(/^#\/aula\/([\w-]+)$/);
    if (m) {
      var i = acharAula(m[1]);
      if (i !== -1) renderChips(ordem[i].nivel, m[1]);
    } else {
      rota();
    }
  }
  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!d || typeof d !== "object" || d.md0 == null) return;
    if (d.md0 === "progresso") atualizarProgresso();
    if (d.md0 === "ir" && typeof d.hash === "string" && /^#\/[\w\/-]*$/.test(d.hash)) location.hash = d.hash;
  });
  window.addEventListener("storage", function (e) {
    if (e.key && e.key.indexOf("md0_progresso_") === 0) atualizarProgresso();
  });

  window.addEventListener("hashchange", rota);
  window.addEventListener("resize", ajustarQuadro);
  rota();
})();
