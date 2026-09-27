# Gera a figura estatica da Eletiva 3 (aula 33). Pode rodar de qualquer pasta: python scripts/figuras_aula33.py
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

def tri(a, cx, cy, R, rot, lab):
    P = [(cx + R * np.cos(np.pi / 2 + 2 * np.pi * k / 3), cy + R * np.sin(np.pi / 2 + 2 * np.pi * k / 3)) for k in range(3)]
    a.add_patch(Polygon(P, closed=True, facecolor="#fef3c7", edgecolor=TXT, lw=2))
    cores = ["#fca5a5", "#93c5fd", "#86efac"]
    for (x, y), r in zip(P, rot):
        a.add_patch(Circle((x, y), R * 0.18, facecolor=cores[r - 1], edgecolor=TXT, lw=1.5))
        a.text(x, y, str(r), ha="center", va="center", fontsize=10, weight="bold")
    a.text(cx, cy - R * 0.95, lab, ha="center", fontsize=11, weight="bold", color=ROXO)


# ---------------- 1. as 6 simetrias -------------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. As 6 simetrias do triângulo")
arr = [((1, 2, 3), "e"), ((3, 1, 2), "r"), ((2, 3, 1), "r²"), ((1, 3, 2), "s₀"), ((3, 2, 1), "s₁"), ((2, 1, 3), "s₂")]
for k, (rot, lab) in enumerate(arr):
    tri(a, (k % 3) * 2.4, -(k // 3) * 2.6, 0.9, rot, lab)
a.set_xlim(-1.2, 6); a.set_ylim(-4, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. tabela de Cayley -------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Tabela de Cayley de D₃ (linha ∘ coluna)")
D3 = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
N = ["e", "r", "r²", "s₀", "s₁", "s₂"]
comp = lambda x, y: tuple(x[y[i]] for i in range(3))
for i in range(6):
    a.text(i + 1.5, 0.5, N[i], ha="center", va="center", fontsize=12, weight="bold")
    a.text(0.5, -i - 0.5, N[i], ha="center", va="center", fontsize=12, weight="bold")
    for j in range(6):
        v = D3.index(comp(D3[i], D3[j]))
        a.add_patch(Rectangle((j + 1.05, -i - 0.95), 0.9, 0.9, facecolor="#dbeafe" if v < 3 else "#fce7f3"))
        a.text(j + 1.5, -i - 0.5, N[v], ha="center", va="center", fontsize=11)
a.set_xlim(0, 7.2); a.set_ylim(-6.2, 1.1); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. gerador ciclico ----------------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Girar 3/8 de volta gera as 8 rotações (mdc(3, 8) = 1)")
P = [(np.cos(np.pi / 2 - 2 * np.pi * k / 8), np.sin(np.pi / 2 - 2 * np.pi * k / 8)) for k in range(8)]
a.add_patch(Polygon(P, closed=True, fill=False, edgecolor=CINZA, lw=1.5))
ordem = [(3 * k) % 8 for k in range(9)]
a.plot([P[k][0] for k in ordem], [P[k][1] for k in ordem], color=ROXO, lw=2.5)
for k, (x, y) in enumerate(P):
    a.add_patch(Circle((x, y), 0.1, facecolor="#c4b5fd", edgecolor=TXT))
    a.text(1.2 * x, 1.2 * y, str(k), ha="center", va="center", fontsize=11, weight="bold")
a.set_xlim(-1.4, 1.4); a.set_ylim(-1.4, 1.4); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. rosacea D5 -----------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Rosácea com simetria D₅ (5 giros + 5 espelhos)")
band = np.array([[0, 0.18], [0, 0.95], [0.32, 0.82], [0.1, 0.7], [0.1, 0.18]])
for k in range(5):
    t = 2 * np.pi * k / 5
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    for sx, cor in [(1, "#93c5fd"), (-1, "#f9a8d4")]:
        pts = (band * [sx, 1]) @ R.T
        a.add_patch(Polygon(pts, closed=True, facecolor=LARANJA if (k == 0 and sx == 1) else cor, edgecolor=TXT, lw=1))
a.set_xlim(-1.1, 1.1); a.set_ylim(-1.1, 1.1); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Eletiva 3 — Simetrias: o que é um grupo", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "33-simetrias-e-grupos" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
