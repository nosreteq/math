# Gera a figura estatica da Aula 29. Pode rodar de qualquer pasta: python scripts/figuras_aula29.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Wedge, FancyArrowPatch

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def titulo(a, t):
    a.set_title(t, fontsize=13.5, weight="bold", color=TXT, pad=10)


def eixos(a, t):
    titulo(a, t)
    a.axhline(0, color=TXT, lw=1)
    a.axvline(0, color=TXT, lw=1)
    a.grid(True, color="#ece7da")
    for s in a.spines.values():
        s.set_visible(False)


def seta(a, p, q, cor, lw=3):
    a.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=18, color=cor, lw=lw))


rng = np.random.default_rng(7)

# ---------------- 1. o leque ---------------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Trinta passeios aleatórios e as curvas ±√n, ±2√n")
n = 400
for k in range(30):
    a.plot(np.concatenate([[0], np.cumsum(rng.choice([-1, 1], n))]), lw=1, alpha=0.7)
t = np.arange(n + 1)
for c, ls in [(1, "-"), (2, "--")]:
    a.plot(t, c * np.sqrt(t), color=ROXO, lw=2.5, ls=ls); a.plot(t, -c * np.sqrt(t), color=ROXO, lw=2.5, ls=ls)
a.set_xlim(0, n); a.set_ylim(-55, 55)

# ---------------- 2. mil caminhantes --------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Mil caminhantes, 100 passos: o sino")
fins = rng.choice([-1, 1], (1000, 100)).sum(axis=1)
a.hist(fins, bins=np.arange(-41, 42, 4), color=AZUL, alpha=0.7, edgecolor="white")
x = np.linspace(-40, 40, 300)
a.plot(x, 1000 * 4 / np.sqrt(2 * np.pi * 100) * np.exp(-x**2 / 200), color=VERM, lw=2.5)
a.set_xlim(-42, 42)

# ---------------- 3. browniano ------------------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Passos menores: o movimento browniano")
fino = np.concatenate([[0], np.cumsum(rng.choice([-1, 1], 4096))]) / 64
for N, cor, lw in [(8, LARANJA, 2.5), (64, VERDE, 2), (4096, AZUL, 1)]:
    idx = np.arange(0, 4097, 4096 // N)
    a.plot(idx / 4096, fino[idx], color=cor, lw=lw, label=f"{N} passos")
a.legend(loc="upper left", fontsize=10); a.set_xlim(0, 1)

# ---------------- 4. caudas gordas ---------------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Passos normais (cima) × cauda gorda (baixo)")
N = 1500
norm = rng.normal(size=N)
gord = rng.standard_t(3, size=N) / np.sqrt(3)
for y0, v in [(6, norm), (-6, gord)]:
    a.axhspan(y0 - 4 * 0.5, y0 + 4 * 0.5, color="#f3f0e8")
    grande = np.abs(v) > 4
    a.vlines(np.arange(N), y0, y0 + 0.5 * np.clip(v, -9, 9), color=np.where(grande, VERM, "#60a5fa"), lw=0.8)
a.set_xlim(0, N); a.set_ylim(-11, 11); a.axis("off")

fig.suptitle("Aula 29 — Acaso no tempo: passeio aleatório", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "29-passeio-aleatorio" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
