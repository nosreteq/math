# Deploy da API — VM compartilhada com o nexustrader

Segue o mesmo padrão já usado pelo `nexustrader` na VM Oracle
(`144.22.225.125`, usuário `ubuntu`): push em `main` dispara um
workflow do GitHub Actions que entra por SSH e atualiza o serviço.
Depois do setup inicial (manual, uma vez só), todo deploy seguinte é
só `git push`.

Recursos reservados por este projeto nessa VM (não reutilize em outro
projeto na mesma VM):

| Recurso | Valor |
|---|---|
| Diretório | `/home/ubuntu/math` |
| Serviço systemd | `math-progresso` |
| Porta interna (uvicorn) | `8001` (o nexustrader já usa a `8000`) |
| Domínio da API | `math-api.144-22-225-125.nip.io` (nip.io — sem domínio próprio ainda) |

## Setup inicial (uma vez só, precisa de acesso SSH à VM)

Passos que a Action **não** automatiza — nginx e o primeiro clone
exigem decisão manual, igual está documentado para o nexustrader:

**1. Clonar o projeto na VM:**
```bash
ssh ubuntu@144.22.225.125
git clone https://github.com/nosreteq/math.git /home/ubuntu/math
```

**2. Secret do GitHub Actions**, no repo `nosreteq/math` → Settings →
Secrets and variables → Actions:
- `SSH_PRIVATE_KEY` — pode reaproveitar a mesma chave já usada pelo
  `nexustrader` (mesma VM, mesmo usuário `ubuntu`), ou gerar uma nova
  só para este projeto (mais seguro, dá para revogar sem afetar o
  nexustrader).
- `MATH_VM_HOST` — `144.22.225.125`

**3. nginx + HTTPS** (a Action não mexe em nginx, só no serviço systemd):
```bash
sudo cp deploy/nginx-math-api.conf.example /etc/nginx/sites-available/math-api
sudo ln -s /etc/nginx/sites-available/math-api /etc/nginx/sites-enabled/math-api
sudo nginx -t && sudo systemctl reload nginx

sudo certbot --nginx -d math-api.144-22-225-125.nip.io
```
(Se `certbot` não estiver instalado: `sudo apt install -y certbot python3-certbot-nginx`.)

Confirme de fora da VM:
```bash
curl https://math-api.144-22-225-125.nip.io/api/health
# -> {"status":"ok"}
```

**4. Ligar o front-end na API** — editar `assets/progresso.js` no
repo, trocar `API_BASE = ""` por
`API_BASE = "https://math-api.144-22-225-125.nip.io"`, commitar e
dar push. O GitHub Pages atualiza sozinho; a barra de login
(`assets/auth-ui.js`) passa a aparecer nas páginas automaticamente.

## Deploys seguintes

Só `git push` em `main` tocando algo em `server/`. O workflow
(`.github/workflows/deploy.yml`) então:

1. Para o serviço (evita disputa de RAM na VM free tier durante o deploy).
2. `git fetch` + `git reset --hard origin/main` em `/home/ubuntu/math`.
3. Cria/atualiza o `.venv` e instala `server/requirements.txt`.
4. Garante as chaves no `.env` por upsert — nunca sobrescreve o
   arquivo inteiro, então o `MD0_JWT_SECRET` gerado na primeira vez
   sobrevive aos deploys seguintes (trocar ele desloga todo mundo).
5. Reinstala o unit systemd a partir de `deploy/math-progresso.service`,
   `daemon-reload`, `restart`.
6. Espera ativamente `/api/health` responder (até 60s); se falhar,
   despeja `systemctl status` + `journalctl` no log do Actions antes
   de dar erro.

## Rollback

```bash
ssh ubuntu@144.22.225.125
cd /home/ubuntu/math
git log --oneline -5          # escolher o commit bom
sudo systemctl stop math-progresso
git reset --hard <commit-bom>
cd server && .venv/bin/pip install -r requirements.txt
sudo systemctl start math-progresso
```

## Backup do banco

```bash
sqlite3 /home/ubuntu/math/server/math.db ".backup /home/ubuntu/math/server/backup-$(date +%F).db"
```
