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
