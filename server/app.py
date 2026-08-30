"""API do curso Matemática do Zero: contas de aluno + progresso.

Cada aluno cria uma conta (nome, e-mail, senha) e o progresso nos
exercícios de cada aula fica gravado no SQLite, associado ao usuário.
Pensada para rodar atrás de um proxy HTTPS (Caddy/nginx) numa VM, com
o front-end estático servido pelo GitHub Pages.
"""
import hashlib
import hmac
import os
import re
import secrets
import sqlite3
import time
from contextlib import contextmanager
from datetime import datetime, timezone

import jwt
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

DB_PATH = os.environ.get("MD0_DB_PATH", os.path.join(os.path.dirname(__file__), "math.db"))
ALLOWED_ORIGINS = [o.strip() for o in os.environ.get(
    "MD0_ALLOWED_ORIGINS", "https://nosreteq.github.io"
).split(",") if o.strip()]
JWT_SECRET = os.environ.get("MD0_JWT_SECRET")
JWT_ALG = "HS256"
JWT_TTL_SEGUNDOS = 60 * 60 * 24 * 30  # 30 dias

if not JWT_SECRET:
    raise RuntimeError(
        "Defina MD0_JWT_SECRET no .env antes de subir o serviço "
        "(ex: python3 -c \"import secrets; print(secrets.token_hex(32))\")"
    )

ID_RE = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

app = FastAPI(title="Matemática do Zero — Contas e Progresso")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                senha_salt TEXT NOT NULL,
                criado_em TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS progresso (
                usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                aula_id TEXT NOT NULL,
                item_id TEXT NOT NULL,
                concluido_em TEXT NOT NULL,
                PRIMARY KEY (usuario_id, aula_id, item_id)
            )
        """)


init_db()


# ---------------- senha ----------------

def hash_senha(senha: str, salt: bytes | None = None) -> tuple[str, str]:
    salt = salt or secrets.token_bytes(16)
    h = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, 200_000)
    return h.hex(), salt.hex()


def senha_confere(senha: str, hash_hex: str, salt_hex: str) -> bool:
    h, _ = hash_senha(senha, bytes.fromhex(salt_hex))
    return hmac.compare_digest(h, hash_hex)


# ---------------- token ----------------

def emitir_token(usuario_id: int) -> str:
    agora = int(time.time())
    payload = {"sub": str(usuario_id), "iat": agora, "exp": agora + JWT_TTL_SEGUNDOS}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)


def usuario_atual(authorization: str | None = Header(default=None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Faça login para continuar")
    token = authorization.removeprefix("Bearer ").strip()
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        usuario_id = int(payload["sub"])
    except (jwt.PyJWTError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")

    with db() as conn:
        row = conn.execute(
            "SELECT id, nome, email FROM usuarios WHERE id=?", (usuario_id,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return {"id": row[0], "nome": row[1], "email": row[2]}


# ---------------- validação ----------------

def valid_id(v: str) -> str:
    if not ID_RE.match(v):
        raise ValueError("id inválido")
    return v


class CadastroPayload(BaseModel):
    nome: str
    email: str
    senha: str

    @field_validator("nome")
    @classmethod
    def v_nome(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 120):
            raise ValueError("nome inválido")
        return v

    @field_validator("email")
    @classmethod
    def v_email(cls, v: str) -> str:
        v = v.strip().lower()
        if not EMAIL_RE.match(v) or len(v) > 200:
            raise ValueError("e-mail inválido")
        return v

    @field_validator("senha")
    @classmethod
    def v_senha(cls, v: str) -> str:
        if not (6 <= len(v) <= 200):
            raise ValueError("a senha precisa ter pelo menos 6 caracteres")
        return v


class LoginPayload(BaseModel):
    email: str
    senha: str


class MarcarPayload(BaseModel):
    aula_id: str
    item_id: str

    _v1 = field_validator("aula_id")(valid_id)
    _v2 = field_validator("item_id")(valid_id)


# ---------------- rotas ----------------

@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/auth/cadastro", status_code=201)
def cadastro(payload: CadastroPayload):
    senha_hash, senha_salt = hash_senha(payload.senha)
    agora = datetime.now(timezone.utc).isoformat()
    try:
        with db() as conn:
            cur = conn.execute(
                "INSERT INTO usuarios (nome, email, senha_hash, senha_salt, criado_em) VALUES (?, ?, ?, ?, ?)",
                (payload.nome, payload.email, senha_hash, senha_salt, agora),
            )
            usuario_id = cur.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Já existe uma conta com esse e-mail")

    token = emitir_token(usuario_id)
    return {"token": token, "usuario": {"id": usuario_id, "nome": payload.nome, "email": payload.email}}


@app.post("/api/auth/login")
def login(payload: LoginPayload):
    email = payload.email.strip().lower()
    with db() as conn:
        row = conn.execute(
            "SELECT id, nome, email, senha_hash, senha_salt FROM usuarios WHERE email=?", (email,)
        ).fetchone()

    if not row or not senha_confere(payload.senha, row[3], row[4]):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

    token = emitir_token(row[0])
    return {"token": token, "usuario": {"id": row[0], "nome": row[1], "email": row[2]}}


@app.get("/api/auth/me")
def me(usuario: dict = Depends(usuario_atual)):
    return usuario


@app.post("/api/progresso")
def marcar_progresso(payload: MarcarPayload, usuario: dict = Depends(usuario_atual)):
    agora = datetime.now(timezone.utc).isoformat()
    with db() as conn:
        conn.execute(
            """INSERT INTO progresso (usuario_id, aula_id, item_id, concluido_em)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(usuario_id, aula_id, item_id) DO NOTHING""",
            (usuario["id"], payload.aula_id, payload.item_id, agora),
        )
    return {"status": "ok"}


@app.get("/api/progresso")
def ler_progresso(aula_id: str | None = None, usuario: dict = Depends(usuario_atual)):
    if aula_id is not None:
        try:
            valid_id(aula_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="aula_id inválido")

    with db() as conn:
        if aula_id:
            rows = conn.execute(
                "SELECT aula_id, item_id FROM progresso WHERE usuario_id=? AND aula_id=?",
                (usuario["id"], aula_id),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT aula_id, item_id FROM progresso WHERE usuario_id=?",
                (usuario["id"],),
            ).fetchall()

    resultado: dict[str, list[str]] = {}
    for aula, item in rows:
        resultado.setdefault(aula, []).append(item)
    return resultado


@app.get("/api/progresso/resumo")
def resumo_progresso(usuario: dict = Depends(usuario_atual)):
    """Quantos itens concluídos por aula — para um painel 'meu progresso'."""
    with db() as conn:
        rows = conn.execute(
            "SELECT aula_id, COUNT(*) FROM progresso WHERE usuario_id=? GROUP BY aula_id",
            (usuario["id"],),
        ).fetchall()
    return {aula: n for aula, n in rows}
