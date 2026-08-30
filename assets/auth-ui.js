/*
 * auth-ui.js — barra flutuante de login/cadastro/logout.
 *
 * Basta incluir <script src=".../auth.js">, <script src=".../progresso.js">
 * e este arquivo em qualquer página. Se a API não estiver configurada
 * (Progresso.apiBase vazio), a barra nem aparece — o site continua
 * funcionando normalmente com progresso só local.
 */
(function () {
  "use strict";

  if (!window.Progresso || !Progresso.apiBase) return;

  var css = ""
    + ".md0-auth{position:fixed;top:14px;right:14px;z-index:9999;font-family:'Segoe UI',system-ui,sans-serif;font-size:14px}"
    + ".md0-auth-chip{background:#1b1b1b;color:#f6f2e9;padding:8px 16px;border-radius:20px;cursor:pointer;box-shadow:2px 3px 6px rgba(0,0,0,.2);border:none;font-size:14px}"
    + ".md0-auth-user{background:#fffdf7;color:#1b1b1b;border:2px solid #1b1b1b;padding:6px 14px;border-radius:20px;box-shadow:2px 3px 6px rgba(0,0,0,.15);display:flex;align-items:center;gap:10px}"
    + ".md0-auth-user button{background:none;border:none;color:#dc2626;font-weight:700;cursor:pointer;font-size:13px;padding:0}"
    + ".md0-auth-overlay{position:fixed;inset:0;background:rgba(27,27,27,.55);z-index:10000;display:flex;align-items:center;justify-content:center;padding:16px}"
    + ".md0-auth-modal{background:#fffdf7;border-radius:12px;padding:26px 26px 22px;max-width:340px;width:100%;box-shadow:0 12px 30px rgba(0,0,0,.3)}"
    + ".md0-auth-modal h3{margin:0 0 14px;font-size:19px}"
    + ".md0-auth-tabs{display:flex;gap:6px;margin-bottom:16px}"
    + ".md0-auth-tabs button{flex:1;padding:8px;border-radius:8px;border:2px solid #1b1b1b;background:#fff;cursor:pointer;font-weight:600}"
    + ".md0-auth-tabs button.on{background:#1b1b1b;color:#fff}"
    + ".md0-auth-modal input{width:100%;padding:9px 10px;margin-bottom:10px;border:2px solid #c9c1ae;border-radius:8px;font-size:14px;box-sizing:border-box}"
    + ".md0-auth-modal .msg{color:#dc2626;font-size:13px;margin:0 0 10px;min-height:1em}"
    + ".md0-auth-modal .ok{color:#059669}"
    + ".md0-auth-acoes{display:flex;gap:8px;align-items:center;justify-content:space-between}"
    + ".md0-auth-acoes button.enviar{background:#2563eb;color:#fff;border:none;padding:9px 18px;border-radius:8px;font-weight:700;cursor:pointer}"
    + ".md0-auth-acoes button.fechar{background:none;border:none;color:#6b7280;cursor:pointer;font-size:13px}";
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var raiz = document.createElement("div");
  raiz.className = "md0-auth";
  document.body.appendChild(raiz);

  function renderBarra() {
    raiz.innerHTML = "";
    if (Auth.estaLogado()) {
      var u = Auth.usuario() || {};
      var box = document.createElement("div");
      box.className = "md0-auth-user";
      box.innerHTML = "<span>👤 " + escapeHtml(u.nome || u.email || "aluno") + "</span>";
      var sair = document.createElement("button");
      sair.textContent = "Sair";
      sair.addEventListener("click", function () {
        Auth.logout();
        location.reload();
      });
      box.appendChild(sair);
      raiz.appendChild(box);
    } else {
      var btn = document.createElement("button");
      btn.className = "md0-auth-chip";
      btn.textContent = "Entrar / Criar conta";
      btn.addEventListener("click", abrirModal);
      raiz.appendChild(btn);
    }
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function abrirModal() {
    var overlay = document.createElement("div");
    overlay.className = "md0-auth-overlay";
    overlay.innerHTML =
      '<div class="md0-auth-modal">' +
      '  <div class="md0-auth-tabs">' +
      '    <button type="button" data-t="login" class="on">Entrar</button>' +
      '    <button type="button" data-t="cadastro">Criar conta</button>' +
      "  </div>" +
      '  <h3 data-titulo>Entrar</h3>' +
      '  <form>' +
      '    <input type="text" name="nome" placeholder="Seu nome" style="display:none">' +
      '    <input type="email" name="email" placeholder="E-mail" required>' +
      '    <input type="password" name="senha" placeholder="Senha" required>' +
      '    <p class="msg" data-msg></p>' +
      '    <div class="md0-auth-acoes">' +
      '      <button type="button" class="fechar" data-fechar>Cancelar</button>' +
      '      <button type="submit" class="enviar">Entrar</button>' +
      "    </div>" +
      "  </form>" +
      "</div>";
    document.body.appendChild(overlay);

    var modo = "login";
    var form = overlay.querySelector("form");
    var campoNome = overlay.querySelector("input[name=nome]");
    var msg = overlay.querySelector("[data-msg]");
    var titulo = overlay.querySelector("[data-titulo]");
    var enviar = overlay.querySelector(".enviar");

    overlay.querySelectorAll(".md0-auth-tabs button").forEach(function (tab) {
      tab.addEventListener("click", function () {
        modo = tab.dataset.t;
        overlay.querySelectorAll(".md0-auth-tabs button").forEach(function (b) { b.classList.remove("on"); });
        tab.classList.add("on");
        var cadastro = modo === "cadastro";
        campoNome.style.display = cadastro ? "block" : "none";
        campoNome.required = cadastro;
        titulo.textContent = cadastro ? "Criar conta" : "Entrar";
        enviar.textContent = cadastro ? "Criar conta" : "Entrar";
        msg.textContent = "";
      });
    });

    overlay.querySelector("[data-fechar]").addEventListener("click", function () {
      overlay.remove();
    });
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) overlay.remove();
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      msg.className = "msg";
      msg.textContent = "";
      var email = form.email.value.trim();
      var senha = form.senha.value;
      var acao = modo === "cadastro"
        ? Auth.cadastrar(form.nome.value.trim(), email, senha)
        : Auth.login(email, senha);

      enviar.disabled = true;
      acao.then(function () {
        msg.className = "msg ok";
        msg.textContent = "Pronto! Atualizando...";
        setTimeout(function () { location.reload(); }, 500);
      }).catch(function (err) {
        enviar.disabled = false;
        msg.textContent = err.message || "Não foi possível concluir.";
      });
    });
  }

  renderBarra();
})();
