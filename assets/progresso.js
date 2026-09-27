/*
 * Progresso.js — salva e restaura o avanço do aluno nas aulas.
 *
 * Sem login: guarda só neste navegador (localStorage).
 * Logado (ver auth.js): sincroniza com a API, contado por conta —
 * o progresso passa a acompanhar o aluno em qualquer dispositivo.
 *
 * Uso em cada aula:
 *   Progresso.marcar("01-o-que-e-uma-funcao", "ex1");
 *   Progresso.carregar("01-o-que-e-uma-funcao").then(function(feitos){ ... });
 */
window.Progresso = (function () {
  "use strict";

  // Preencha com a URL pública da API depois do deploy na VM, ex:
  // "https://api.seudominio.com". Enquanto estiver vazio, o progresso
  // fica só neste navegador (localStorage) e o login fica desativado.
  var API_BASE = "";

  var PREFIXO_LOCAL = "md0_progresso_";

  // Reestruturação em 30 aulas: o progresso das aulas que mudaram de número
  // (com os mesmos exercícios) é copiado uma vez para o endereço novo. As
  // aulas antigas 9, 10 e 17 foram divididas e ganharam exercícios novos,
  // então não entram aqui.
  var MIGRACAO_30 = {
    "01-o-que-e-uma-funcao": "07-letras-no-lugar-de-numeros",
    "02-desenhar-numeros-no-papel": "09-o-plano-e-a-reta",
    "03-angulos-e-o-circulo": "11-angulos-circulo-e-pi",
    "04-seno-e-cosseno": "15-trigonometria",
    "05-ondas": "16-ondas",
    "06-setas-e-tabelas-de-numeros": "17-vetores-e-matrizes",
    "07-equacoes-a-balanca": "08-equacoes-e-inequacoes",
    "08-sistemas-de-equacoes": "10-sistemas-de-equacoes",
    "11-projecao-e-minimos-quadrados": "23-projecao-e-minimos-quadrados",
    "12-decomposicao-de-sinais-em-ondas": "24-fourier",
    "15-a-inclinacao-em-cada-ponto": "19-limites-e-a-derivada",
    "16-somando-fatias": "20-a-integral"
  };
  (function migrar() {
    try {
      if (localStorage.getItem("md0_migracao_30")) return;
      Object.keys(MIGRACAO_30).forEach(function (antigo) {
        var v = localStorage.getItem(PREFIXO_LOCAL + antigo);
        var novo = PREFIXO_LOCAL + MIGRACAO_30[antigo];
        if (v && !localStorage.getItem(novo)) localStorage.setItem(novo, v);
      });
      localStorage.setItem("md0_migracao_30", "1");
    } catch (e) { /* sem localStorage: nada a migrar */ }
  })();

  function lerLocal(aulaId) {
    try {
      var raw = localStorage.getItem(PREFIXO_LOCAL + aulaId);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function salvarLocal(aulaId, itens) {
    localStorage.setItem(PREFIXO_LOCAL + aulaId, JSON.stringify(itens));
  }

  function logado() {
    return !!(window.Auth && Auth.estaLogado());
  }

  function cabecalhos() {
    return { "Content-Type": "application/json", "Authorization": "Bearer " + Auth.token() };
  }

  function marcar(aulaId, itemId) {
    var itens = lerLocal(aulaId);
    if (itens.indexOf(itemId) === -1) {
      itens.push(itemId);
      salvarLocal(aulaId, itens);
    }

    if (!API_BASE || !logado()) return;
    fetch(API_BASE + "/api/progresso", {
      method: "POST",
      headers: cabecalhos(),
      body: JSON.stringify({ aula_id: aulaId, item_id: itemId }),
    }).catch(function () {
      /* offline ou API fora do ar: já ficou salvo localmente */
    });
  }

  function carregar(aulaId) {
    var local = lerLocal(aulaId);

    if (!API_BASE || !logado()) return Promise.resolve(local);

    return fetch(API_BASE + "/api/progresso?aula_id=" + encodeURIComponent(aulaId), {
      headers: cabecalhos(),
    })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (dados) {
        var remoto = dados[aulaId] || [];
        var unidos = local.slice();
        remoto.forEach(function (id) {
          if (unidos.indexOf(id) === -1) unidos.push(id);
        });
        salvarLocal(aulaId, unidos);
        return unidos;
      })
      .catch(function () { return local; });
  }

  return { marcar: marcar, carregar: carregar, apiBase: API_BASE };
})();
