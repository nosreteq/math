/*
 * Auth.js — cadastro, login e sessão do aluno.
 *
 * Guarda o token em localStorage. Enquanto API_BASE (em progresso.js)
 * estiver vazio, o sistema de contas fica inativo e tudo continua
 * funcionando só com localStorage (comportamento anterior).
 */
window.Auth = (function () {
  "use strict";

  var CHAVE_TOKEN = "md0_token";
  var CHAVE_USUARIO = "md0_usuario";

  function apiBase() {
    return (window.Progresso && window.Progresso.apiBase) || "";
  }

  function token() {
    return localStorage.getItem(CHAVE_TOKEN) || "";
  }

  function usuario() {
    try {
      var raw = localStorage.getItem(CHAVE_USUARIO);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  function estaLogado() {
    return !!token();
  }

  function salvarSessao(dados) {
    localStorage.setItem(CHAVE_TOKEN, dados.token);
    localStorage.setItem(CHAVE_USUARIO, JSON.stringify(dados.usuario));
  }

  function logout() {
    localStorage.removeItem(CHAVE_TOKEN);
    localStorage.removeItem(CHAVE_USUARIO);
  }

  function chamar(caminho, opcoes) {
    var base = apiBase();
    if (!base) return Promise.reject(new Error("API não configurada"));
    return fetch(base + caminho, opcoes).then(function (r) {
      return r.json().then(function (corpo) {
        if (!r.ok) throw new Error(corpo.detail || "Erro inesperado");
        return corpo;
      });
    });
  }

  function cadastrar(nome, email, senha) {
    return chamar("/api/auth/cadastro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome: nome, email: email, senha: senha }),
    }).then(function (dados) {
      salvarSessao(dados);
      return dados.usuario;
    });
  }

  function login(email, senha) {
    return chamar("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, senha: senha }),
    }).then(function (dados) {
      salvarSessao(dados);
      return dados.usuario;
    });
  }

  return {
    estaLogado: estaLogado,
    usuario: usuario,
    token: token,
    login: login,
    cadastrar: cadastrar,
    logout: logout,
  };
})();
