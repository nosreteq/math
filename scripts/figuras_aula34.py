# Gera a figura estatica da Eletiva 4 (aula 34). Pode rodar de qualquer pasta: python scripts/figuras_aula34.py
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

# ---------------- 1. xicara = rosquinha (buracos) -----------------------------------------------
a = ax[0, 0]
titulo(a, "1. O que a borracha preserva: o número de buracos")
t = np.linspace(0, 2 * np.pi, 200)
for cx, g, rot in [(0, 0, "bola: 0"), (3, 1, "rosquinha: 1"), (6.3, 2, "bitoro: 2")]:
    a.fill(cx + 1.3 * np.cos(t), 0.8 * np.sin(t), color="#c7d2fe", ec="#4338ca", lw=2)
    for k in range(g):
        hx = cx + (k - (g - 1) / 2) * 0.9
        a.fill(hx + 0.28 * np.cos(t), 0.14 * np.sin(t), color="white", ec="#4338ca", lw=2)
    a.text(cx, -1.2, rot, ha="center", fontsize=12, weight="bold")
a.set_xlim(-1.6, 7.9); a.set_ylim(-1.6, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. V - A + F --------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. V − A + F = 2 em todo poliedro sem buracos")
linhas = [("tetraedro", 4, 6, 4), ("cubo", 8, 12, 6), ("octaedro", 6, 12, 8), ("dodecaedro", 20, 30, 12), ("icosaedro", 12, 30, 20), ("pirâmide", 5, 8, 5)]
a.text(0.02, 0.92, "sólido            V     A     F     V − A + F", fontsize=12, weight="bold", family="monospace", transform=a.transAxes)
for k, (n, V, A, F) in enumerate(linhas):
    a.text(0.02, 0.78 - k * 0.12, f"{n:<16}{V:>3}   {A:>3}   {F:>3}        {V - A + F}", fontsize=12, family="monospace", transform=a.transAxes, color=AZUL if k % 2 else TXT)
a.axis("off")

# ---------------- 3. Mobius ---------------------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. A faixa de Möbius: um lado só")
th = np.linspace(0, 2 * np.pi, 160)
for s, cor in [(-0.45, "#93c5fd"), (0.45, "#fdba74")]:
    pass
N = 160
quads = []
for i in range(N):
    for j in range(6):
        u0, u1 = 2 * np.pi * i / N, 2 * np.pi * (i + 1) / N
        s0, s1 = -0.45 + 0.9 * j / 6, -0.45 + 0.9 * (j + 1) / 6
        def P(u, s):
            x = (1.6 + s * np.cos(u / 2)) * np.cos(u); y = (1.6 + s * np.cos(u / 2)) * np.sin(u); z = s * np.sin(u / 2)
            tt = 0.9; return (x, y * np.cos(tt) - z * np.sin(tt), y * np.sin(tt) + z * np.cos(tt))
        pts = [P(u0, s0), P(u1, s0), P(u1, s1), P(u0, s1)]
        quads.append((np.mean([p[2] for p in pts]), pts, i))
for z, pts, i in sorted(quads, key=lambda q: -q[0]):
    xy = [(p[0], p[1]) for p in pts]
    ar = sum(xy[k][0] * xy[(k + 1) % 4][1] - xy[(k + 1) % 4][0] * xy[k][1] for k in range(4))
    a.add_patch(Polygon(xy, closed=True, facecolor="#93c5fd" if ar > 0 else "#fdba74", edgecolor="none"))
a.set_xlim(-2.4, 2.4); a.set_ylim(-1.8, 1.8); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. Jordan --------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Curva de Jordan: cruzamentos ímpares = dentro")
L = [[1, 1], [9, 1], [9, 9], [3, 9], [3, 4], [6, 4], [6, 6], [5, 6], [5, 5], [4, 5], [4, 8], [8, 8], [8, 2], [2, 2], [2, 9.5], [1, 9.5]]
a.add_patch(Polygon(L, closed=True, facecolor="#fef3c7", edgecolor=TXT, lw=2.5))
for (px, py), cor in [((8.5, 5.3), VERDE), ((4.5, 5.5), VERM)]:
    a.plot([px, 10.5], [py, py], color=ROXO, ls="--", lw=1.5)
    a.plot(px, py, "o", color=cor, ms=12, mec=TXT)
a.set_xlim(0, 10.6); a.set_ylim(0, 10.2); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Eletiva 4 — Topologia de borracha: Möbius e V − A + F", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "34-topologia-de-borracha" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
