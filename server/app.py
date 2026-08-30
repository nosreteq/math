"""API de progresso do curso Matemática do Zero.

Guarda, por aluno anônimo, quais exercícios de cada aula já foram
concluídos. Pensada para rodar atrás de um proxy HTTPS (Caddy/nginx)
numa VM, com o front-end estático servido pelo GitHub Pages.
"""
import os
import re
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

DB_PATH = os.environ.get("MD0_DB_PATH", os.path.join(os.path.dirname(__file__), "math.db"))
ALLOWED_ORIGINS = [o.strip() for o in os.environ.get(
    "MD0_ALLOWED_ORIGINS", "https://nosreteq.github.io"
).split(",") if o.strip()]

ID_RE = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")

app = FastAPI(title="Matemática do Zero — Progresso")

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
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS progresso (
                aluno_id TEXT NOT NULL,
                aula_id TEXT NOT NULL,
                item_id TEXT NOT NULL,
                concluido_em TEXT NOT NULL,
                PRIMARY KEY (aluno_id, aula_id, item_id)
            )
        """)


init_db()


def valid_id(v: str) -> str:
    if not ID_RE.match(v):
        raise ValueError("id inválido")
    return v


class MarcarPayload(BaseModel):
    aluno_id: str
    aula_id: str
    item_id: str

    _v1 = field_validator("aluno_id")(valid_id)
    _v2 = field_validator("aula_id")(valid_id)
    _v3 = field_validator("item_id")(valid_id)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/progresso")
def marcar_progresso(payload: MarcarPayload):
    agora = datetime.now(timezone.utc).isoformat()
    with db() as conn:
        conn.execute(
            """INSERT INTO progresso (aluno_id, aula_id, item_id, concluido_em)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(aluno_id, aula_id, item_id) DO NOTHING""",
            (payload.aluno_id, payload.aula_id, payload.item_id, agora),
        )
    return {"status": "ok"}


@app.get("/api/progresso/{aluno_id}")
def ler_progresso(aluno_id: str, aula_id: str | None = None):
    try:
        valid_id(aluno_id)
        if aula_id is not None:
            valid_id(aula_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="id inválido")

    with db() as conn:
        if aula_id:
            rows = conn.execute(
                "SELECT aula_id, item_id, concluido_em FROM progresso WHERE aluno_id=? AND aula_id=?",
                (aluno_id, aula_id),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT aula_id, item_id, concluido_em FROM progresso WHERE aluno_id=?",
                (aluno_id,),
            ).fetchall()

    resultado: dict[str, list[str]] = {}
    for aula, item, _ in rows:
        resultado.setdefault(aula, []).append(item)
    return resultado
