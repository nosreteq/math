# Gera a figura estatica da Aula 25. Pode rodar de qualquer pasta: python scripts/figuras_aula25.py
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

def papel(a, t, lim=3.5):
    titulo(a, t)
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim); a.set_aspect("equal")
    a.axhline(0, color=TXT, lw=1); a.axvline(0, color=TXT, lw=1)
    a.grid(True, color="#ece7da"); a.set_xticks(range(-3, 4)); a.set_yticks(range(-3, 4))
    for s in a.spines.values():
        s.set_visible(False)


Q = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
# ---------------- 1. determinante = area ------------------------------------------------------------
a = ax[0, 0]
papel(a, "1. det = 3: toda área fica 3 vezes maior")
M = np.array([[2, 1], [0, 1.5]])
a.add_patch(Polygon(Q, closed=True, facecolor=CINZA, alpha=0.3, edgecolor=CINZA, lw=2))
a.add_patch(Polygon(Q @ M.T, closed=True, facecolor=AZUL, alpha=0.3, edgecolor=AZUL, lw=2.5))
seta(a, (0, 0), M[:, 0], VERM); seta(a, (0, 0), M[:, 1], VERDE)

# ---------------- 2. det zero ------------------------------------------------------------------------
a = ax[0, 1]
papel(a, "2. Determinante 0: o plano é achatado numa reta")
M = np.array([[1, 2], [0.5, 1]])
for x in np.arange(-3, 3.1, 0.5):
    for y in np.arange(-3, 3.1, 0.5):
        p = M @ [x, y]
        a.plot(x, y, ".", color=CINZA, ms=3)
        if abs(p[0]) < 3.5 and abs(p[1]) < 3.5:
            a.plot(p[0], p[1], "o", color=VERM, ms=4, alpha=0.5)
a.text(-3.3, 2.9, "tudo cai na reta y = x/2:\nnão dá para desfazer (sem inversa)", fontsize=10.5, color=TXT)

# ---------------- 3. autovetores -----------------------------------------------------------------------
a = ax[1, 0]
papel(a, "3. [[2, 1], [1, 2]]: o círculo vira elipse")
t = np.linspace(0, 2 * np.pi, 200)
C = np.vstack([np.cos(t), np.sin(t)])
E = np.array([[2, 1], [1, 2]]) @ C
a.plot(C[0], C[1], color=CINZA, lw=2, ls="--")
a.plot(E[0], E[1], color=ROXO, lw=2.5)
s = 1 / np.sqrt(2)
seta(a, (0, 0), (3 * s, 3 * s), VERM); seta(a, (0, 0), (-s, s), VERDE)
a.text(2.3, 1.7, "autovalor 3", fontsize=11, weight="bold", color=VERM)
a.text(-2.4, 0.9, "autovalor 1", fontsize=11, weight="bold", color=VERDE)

# ---------------- 4. rotacao: sem autovetor real ------------------------------------------------------------
a = ax[1, 1]
papel(a, "4. Rotação de 90°: nenhum autovetor real")
R = np.array([[0, -1], [1, 0]])
for ang in np.radians([0, 40, 80, 120, 160]):
    v = 2 * np.array([np.cos(ang), np.sin(ang)])
    seta(a, (0, 0), v, CINZA, lw=2)
    seta(a, (0, 0), R @ v, AZUL, lw=2)
a.text(-3.3, -3.1, "autovalores complexos: ± i (o giro da Aula 18)", fontsize=11, color=TXT)

fig.suptitle("Aula 25 — Matrizes que transformam", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "25-determinante-inversa-e-autovalores" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
