# Gera a figura estatica da Aula 28. Pode rodar de qualquer pasta: python scripts/figuras_aula28.py
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

def rk(f, y0, t0, t1, n=400):
    h = (t1 - t0) / n; t, y = t0, np.array(y0, float); out = [y.copy()]
    for _ in range(n):
        k1 = f(t, y); k2 = f(t + h / 2, y + h * k1 / 2); k3 = f(t + h / 2, y + h * k2 / 2); k4 = f(t + h, y + h * k3)
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; t += h; out.append(y.copy())
    return np.linspace(t0, t1, n + 1), np.array(out)


# ---------------- 1. campo de direcoes ------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Campo de direções de y′ = t − y e três soluções")
T, Y = np.meshgrid(np.arange(0.25, 5, 0.5), np.arange(-1.75, 4, 0.5))
M = T - Y; L = np.hypot(1, M)
a.quiver(T, Y, 1 / L, M / L, color=CINZA, angles="xy", pivot="mid", scale=22, width=0.004, headwidth=2)
for y0, cor in [(3.5, VERM), (1, AZUL), (-1.5, VERDE)]:
    t, y = rk(lambda t, y: t - y, [y0], 0, 5)
    a.plot(t, y[:, 0], color=cor, lw=3)
a.set_xlim(0, 5); a.set_ylim(-2, 4)

# ---------------- 2. euler ---------------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Euler em y′ = y: passo menor, erro menor")
t = np.linspace(0, 2, 200)
a.plot(t, np.exp(t), color=AZUL, lw=3, label="exata: eᵗ")
for h, cor in [(0.5, VERM), (0.1, LARANJA)]:
    n = int(round(2 / h)); ts = np.arange(n + 1) * h
    a.plot(ts, (1 + h)**np.arange(n + 1), "o-", color=cor, lw=2, ms=5, label=f"Euler, h = {h:g}".replace(".", ","))
a.legend(loc="upper left", fontsize=11); a.set_xlim(0, 2.1); a.set_ylim(0, 8)

# ---------------- 3. mola -----------------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. A mola: y″ = −y − c · y′")
for c, cor in [(0, CINZA), (0.2, ROXO), (2.2, VERDE)]:
    t, Y = rk(lambda t, y: np.array([y[1], -y[0] - c * y[1]]), [1, 0], 0, 20, 1000)
    a.plot(t, Y[:, 0], color=cor, lw=2.5 if c else 2, ls="--" if c == 0 else "-", label=f"atrito {c:g}".replace(".", ","))
a.legend(loc="upper right", fontsize=10); a.set_ylim(-1.3, 1.3)

# ---------------- 4. predador e presa ------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Coelhos × raposas: ciclos")
for c0, cor in [(4, VERDE), (6, AZUL), (8, ROXO)]:
    t, Y = rk(lambda t, y: np.array([y[0] - 0.5 * y[0] * y[1], -0.75 * y[1] + 0.25 * y[0] * y[1]]), [c0, 2], 0, 20, 2000)
    a.plot(Y[:, 0], Y[:, 1], color=cor, lw=2.5)
a.plot(3, 2, "o", color=TXT, ms=8)
a.set_xlabel("coelhos", fontsize=12); a.set_ylabel("raposas", fontsize=12); a.set_xlim(0, 12); a.set_ylim(0, 7)

fig.suptitle("Aula 28 — Equações diferenciais e o método de Euler", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "28-equacoes-diferenciais" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
