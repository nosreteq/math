# Gera a figura estatica da Eletiva 2 (aula 32). Pode rodar de qualquer pasta: python scripts/figuras_aula32.py
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

# ---------------- 1. Konigsberg -------------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. Königsberg: 4 margens de grau ímpar → impossível")
V = {"N": (0, 1.2), "S": (0, -1.2), "I": (-0.8, 0), "L": (1.2, 0)}
def arco(p, q, curva):
    p, q = np.array(p), np.array(q); m = (p + q) / 2; d = q - p; n = np.array([-d[1], d[0]]) / np.hypot(*d)
    c = m + curva * n; t = np.linspace(0, 1, 40)[:, None]
    pts = (1 - t)**2 * p + 2 * (1 - t) * t * c + t**2 * q
    a.plot(pts[:, 0], pts[:, 1], color=LARANJA, lw=3)
for p, q, c in [("N", "I", 0.25), ("N", "I", -0.25), ("S", "I", 0.25), ("S", "I", -0.25), ("N", "L", 0), ("S", "L", 0), ("I", "L", 0)]:
    arco(V[p], V[q], c)
grau = {"N": 3, "S": 3, "I": 5, "L": 3}
for k, (x, y) in V.items():
    a.add_patch(Circle((x, y), 0.2, facecolor="#fecaca", edgecolor=TXT, lw=2, zorder=3))
    a.text(x, y, grau[k], ha="center", va="center", fontsize=13, weight="bold", zorder=4)
a.set_xlim(-1.4, 1.7); a.set_ylim(-1.6, 1.6); a.set_aspect("equal"); a.axis("off")

# ---------------- 2/3. mapa com pesos -------------------------------------------------------------
NOMES = "ABCDEFGH"
P = [(40, 140), (130, 50), (140, 232), (240, 140), (250, 40), (260, 248), (365, 88), (425, 205)]
E = [(0, 1, 4), (0, 2, 3), (1, 2, 5), (1, 3, 6), (1, 4, 5), (2, 3, 4), (2, 5, 6), (3, 4, 3), (3, 5, 5), (3, 6, 6), (4, 6, 4), (5, 7, 7), (6, 7, 3), (3, 7, 9)]
def mapa(a, destaque, cor, t):
    titulo(a, t)
    for i, j, w in E:
        on = (i, j) in destaque or (j, i) in destaque
        a.plot([P[i][0], P[j][0]], [-P[i][1], -P[j][1]], color=cor if on else "#d6d0c2", lw=5 if on else 2)
        a.text((P[i][0] + P[j][0]) / 2, -(P[i][1] + P[j][1]) / 2, str(w), fontsize=9, ha="center", va="center",
               bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec="#d6d0c2"))
    for k, (x, y) in enumerate(P):
        a.add_patch(Circle((x, -y), 14, facecolor="white", edgecolor=TXT, lw=2, zorder=3))
        a.text(x, -y, NOMES[k], ha="center", va="center", fontsize=11, weight="bold", zorder=4)
    a.set_xlim(10, 460); a.set_ylim(-275, -15); a.set_aspect("equal"); a.axis("off")
mapa(ax[0, 1], [(0, 2), (2, 5), (5, 7)], VERM, "2. Dijkstra: A → C → F → H, custo 16")
mapa(ax[1, 0], [(0, 2), (3, 4), (6, 7), (0, 1), (2, 3), (4, 6), (3, 5)], VERDE, "3. Kruskal: a rede mais barata (custo 26)")

# ---------------- 4. roda colorida ---------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. A roda de 5 raios precisa de 4 cores")
cores = ["#fde68a", "#93c5fd", "#fca5a5", "#86efac", "#93c5fd", "#86efac"]
pts = [(0, 0)] + [(np.cos(np.pi / 2 + 2 * np.pi * k / 5), np.sin(np.pi / 2 + 2 * np.pi * k / 5)) for k in range(5)]
cores = ["#fde68a", "#93c5fd", "#fca5a5", "#93c5fd", "#fca5a5", "#86efac"]
for k in range(5):
    a.plot([0, pts[k + 1][0]], [0, pts[k + 1][1]], color=CINZA, lw=2)
    a.plot([pts[k + 1][0], pts[(k + 1) % 5 + 1][0]], [pts[k + 1][1], pts[(k + 1) % 5 + 1][1]], color=CINZA, lw=2)
for (x, y), c in zip(pts, cores):
    a.add_patch(Circle((x, y), 0.15, facecolor=c, edgecolor=TXT, lw=2, zorder=3))
a.set_xlim(-1.4, 1.4); a.set_ylim(-1.3, 1.3); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Eletiva 2 — Grafos: caminhos, redes e rotas", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "32-grafos" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
