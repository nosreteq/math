# Gera a figura estatica da Eletiva 10 (aula 40). Pode rodar de qualquer pasta: python scripts/figuras_aula40.py
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

# ---------------- 1. bissecao --------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Bisseção em x² − 2: o intervalo cai à metade")
x = np.linspace(0.8, 2.1, 200)
a.plot(x, x**2 - 2, color=AZUL, lw=3)
lo, hi = 1.0, 2.0
for k in range(7):
    a.plot([lo, hi], [-0.3 - 0.15 * k] * 2, color=VERM, lw=4 - 0.4 * k)
    m = (lo + hi) / 2
    lo, hi = (lo, m) if m * m - 2 > 0 else (m, hi)
a.set_ylim(-1.5, 2.3)

# ---------------- 2. Newton ------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Newton: seguir a tangente até o eixo")
x = np.linspace(0, 3.5, 200)
a.plot(x, x**2 - 2, color=AZUL, lw=3)
xk = 3.0
for _ in range(4):
    y = xk**2 - 2; x2 = xk - y / (2 * xk)
    a.plot([xk, xk], [0, y], color=CINZA, ls=":"); a.plot([xk, x2], [y, 0], color=LARANJA, lw=2)
    a.plot(xk, 0, "o", color=VERM, ms=6); xk = x2
a.set_ylim(-3, 10)

# ---------------- 3. h otimo --------------------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Erro da derivada numérica de sen em 1")
a.grid(True, color="#ece7da")
hs = 10.0**np.arange(-16, 0)
err = np.abs((np.sin(1 + hs) - np.sin(1)) / hs - np.cos(1))
a.loglog(hs, np.maximum(err, 1e-12), "o-", color=ROXO, lw=2)
a.set_xlabel("h", fontsize=12); a.set_ylabel("erro", fontsize=12)
for s_ in a.spines.values():
    s_.set_visible(False)

# ---------------- 4. estabilidade -----------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. y′ = −10y, h = 0,25: explícito × implícito")
h = 0.25; n = 8; t = np.arange(n + 1) * h
a.plot(np.linspace(0, 2, 200), np.exp(-10 * np.linspace(0, 2, 200)), color=CINZA, lw=3)
a.plot(t, (1 - 10 * h)**np.arange(n + 1), "o-", color=VERM, lw=2, label="explícito")
a.plot(t, (1 / (1 + 10 * h))**np.arange(n + 1), "o-", color=VERDE, lw=2, label="implícito")
a.set_ylim(-5, 5); a.legend(fontsize=10)

fig.suptitle("Eletiva 10 — Métodos numéricos: Newton, erro e estabilidade", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "40-metodos-numericos" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
