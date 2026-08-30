# API de contas e progresso

Backend pequeno (FastAPI + SQLite) com contas de aluno (cadastro/login)
e o progresso nos exercícios de cada aula gravado por usuário, para o
site estático em `https://nosreteq.github.io/math/` poder salvar e
restaurar o progresso entre visitas e dispositivos.

Para o passo a passo de **deploy na VM** (Oracle Cloud, compartilhada
com o `nexustrader`), veja **[`deploy/README.md`](../deploy/README.md)**
— o deploy é automatizado via GitHub Actions a partir daqui.

## Como funciona

- Cada aluno cria a própria conta (nome, e-mail, senha) — sem aprovação
  manual. Senha guardada com hash (PBKDF2-SHA256, salgado), nunca em
  texto puro. Login devolve um token (JWT) válido por 30 dias.
- O front-end (`assets/auth.js` + `assets/auth-ui.js`) mostra uma barra
  de "Entrar / Criar conta" no canto da página; `assets/progresso.js`
  usa o token para marcar exercícios concluídos e carregar o progresso
  salvo, sempre associado à conta logada.
- Sem login, o progresso continua funcionando só no navegador
  (`localStorage`), como antes — a conta é só para acompanhar entre
  dispositivos.
- Os dados ficam num arquivo SQLite (`math.db`) na própria VM.
- **Não há recuperação de senha por e-mail nesta v1** (a VM não tem
  SMTP configurado). Se um aluno esquecer a senha, quem administra o
  servidor reseta manualmente no banco (veja "Resetar senha" abaixo).

## Rodar localmente (dev)

```bash
cd server
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

cp .env.example .env
python3 -c "import secrets; print(secrets.token_hex(32))"   # cole em MD0_JWT_SECRET no .env

.venv/bin/uvicorn app:app --reload --port 8001
curl http://127.0.0.1:8001/api/health
```

## Testar cadastro e login

```bash
curl -X POST http://127.0.0.1:8001/api/auth/cadastro \
  -H "Content-Type: application/json" \
  -d '{"nome":"Teste","email":"teste@exemplo.com","senha":"123456"}'
# -> {"token": "...", "usuario": {...}}

curl http://127.0.0.1:8001/api/auth/me \
  -H "Authorization: Bearer TOKEN_RECEBIDO_ACIMA"
```

## Resetar senha de um aluno manualmente

Sem recuperação por e-mail, o jeito de trocar a senha de alguém é
gerar um novo hash e atualizar direto no banco:

```bash
sqlite3 /home/ubuntu/math/server/math.db "SELECT id, nome, email FROM usuarios;"

python3 - <<'EOF'
import hashlib, secrets
salt = secrets.token_bytes(16)
h = hashlib.pbkdf2_hmac("sha256", "novaSenha123".encode(), salt, 200_000)
print("hash:", h.hex())
print("salt:", salt.hex())
EOF

sqlite3 /home/ubuntu/math/server/math.db \
  "UPDATE usuarios SET senha_hash='HASH_AQUI', senha_salt='SALT_AQUI' WHERE email='aluno@exemplo.com';"
```

## Backup do banco

`math.db` fica em `server/math.db` (ou no caminho definido em
`MD0_DB_PATH`). É só um arquivo — para backup, copie-o
(`sqlite3 math.db ".backup backup.db"` evita copiar um arquivo em uso).
