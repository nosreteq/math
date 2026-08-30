# API de progresso — deploy na VM Oracle

Backend pequeno (FastAPI + SQLite) que grava quais exercícios cada aluno
já concluiu, para o site estático em `https://nosreteq.github.io/math/`
poder salvar e restaurar o progresso entre visitas.

## Como funciona

- Cada aluno recebe um ID anônimo gerado pelo navegador (sem login).
- O front-end (`assets/progresso.js`) chama esta API para marcar
  exercícios concluídos e para carregar o progresso salvo.
- Os dados ficam num arquivo SQLite (`math.db`) na própria VM.

## 1. Preparar o projeto na VM

Na mesma VM Oracle onde já roda o `nexustrader`, clone (ou já deve ter)
o repositório `math` e entre na pasta `server/`:

```bash
git clone https://github.com/nosreteq/math.git
cd math/server

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

cp .env.example .env
# edite o .env se quiser mudar o domínio liberado no CORS ou o caminho do banco
```

Teste rápido, ainda em primeiro plano:

```bash
.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8000
# em outro terminal:
curl http://127.0.0.1:8000/api/health
# -> {"status":"ok"}
```

`Ctrl+C` para parar depois de confirmar que respondeu.

## 2. Rodar como serviço (systemd)

Ajuste `math-progresso.service` se o usuário/caminho forem diferentes de
`ubuntu` / `/home/ubuntu/math`, depois:

```bash
sudo cp math-progresso.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now math-progresso
sudo systemctl status math-progresso
```

A API fica escutando só em `127.0.0.1:8000` (não exposta direto na
internet) — quem expõe para fora é o proxy HTTPS do passo 3.

## 3. Expor com HTTPS (proxy reverso)

O site roda em `https://nosreteq.github.io`, então o navegador **bloqueia**
chamadas para um endereço HTTP simples (conteúdo misto). É obrigatório
ter HTTPS na API.

Se a VM não tem um domínio próprio ainda, dá para usar um serviço tipo
`SEU-IP-PUBLICO.nip.io` (resolve automaticamente para o próprio IP) só
para conseguir emitir certificado.

Exemplo com [Caddy](https://caddyserver.com/) (gera e renova o
certificado sozinho):

```bash
sudo apt install -y caddy   # ou seguir instruções oficiais do Caddy
sudo cp Caddyfile.example /etc/caddy/Caddyfile
sudo nano /etc/caddy/Caddyfile   # trocar api.seudominio.com pelo domínio/nip.io real
sudo systemctl restart caddy
```

Se preferir nginx + certbot, o efeito é o mesmo: proxy para
`127.0.0.1:8000` com certificado válido no domínio escolhido.

## 4. Liberar a porta na Oracle Cloud

Na Oracle, além do firewall do próprio SO, existe a **Security List /
Network Security Group** da VCN — sem liberar lá, a porta 443 (e 80,
usada na emissão do certificado) fica bloqueada mesmo com o serviço
rodando local. No console da Oracle Cloud:

- VCN → Security Lists (ou NSG da instância) → Add Ingress Rule
  - Source: `0.0.0.0/0`, porta `443` (HTTPS)
  - Source: `0.0.0.0/0`, porta `80` (HTTP, necessário para o Caddy validar o certificado)

E no SO da VM (Ubuntu costuma vir com `iptables`/`netfilter` via
`iptables-persistent` ou `ufw`):

```bash
sudo ufw allow 80,443/tcp   # se estiver usando ufw
# ou, se for iptables puro:
sudo iptables -I INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
```

## 5. Ligar o front-end na API

Depois que `https://api.seudominio.com/api/health` responder de fora da
VM, edite `assets/progresso.js` no repo (linha `API_BASE`) apontando
para essa URL, commite e dê push — o GitHub Pages atualiza sozinho.

## Backup do banco

`math.db` fica em `server/math.db` (ou no caminho definido em
`MD0_DB_PATH`). É só um arquivo — para backup, copie-o
(`sqlite3 math.db ".backup backup.db"` evita copiar um arquivo em uso).
