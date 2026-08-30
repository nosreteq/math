/*
 * Progresso.js — salva e restaura o avanço do aluno nas aulas.
 *
 * Guarda sempre uma cópia local (localStorage), e se a API estiver
 * configurada e disponível, também sincroniza com o servidor — assim
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
  // fica só neste navegador (localStorage).
  var API_BASE = "";

  var CHAVE_ALUNO = "md0_aluno_id";
  var PREFIXO_LOCAL = "md0_progresso_";

  function alunoId() {
    var id = localStorage.getItem(CHAVE_ALUNO);
    if (!id) {
      id = "al_" + Date.now().toString(36) + "_" + Math.random().toString(36).slice(2, 10);
      localStorage.setItem(CHAVE_ALUNO, id);
    }
    return id;
  }

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

  function marcar(aulaId, itemId) {
    var itens = lerLocal(aulaId);
    if (itens.indexOf(itemId) === -1) {
      itens.push(itemId);
      salvarLocal(aulaId, itens);
    }

    if (!API_BASE) return;
    fetch(API_BASE + "/api/progresso", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ aluno_id: alunoId(), aula_id: aulaId, item_id: itemId }),
    }).catch(function () {
      /* offline ou API fora do ar: já ficou salvo localmente */
    });
  }

  function carregar(aulaId) {
    var local = lerLocal(aulaId);

    if (!API_BASE) return Promise.resolve(local);

    return fetch(API_BASE + "/api/progresso/" + alunoId() + "?aula_id=" + encodeURIComponent(aulaId))
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

  return { marcar: marcar, carregar: carregar, alunoId: alunoId };
})();
