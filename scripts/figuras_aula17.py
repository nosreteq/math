# Gera a figura estatica da Aula 17. Pode rodar de qualquer pasta: python scripts/figuras_aula17.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Arc

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def papel(a, titulo, lim=5):
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim)
    a.axhline(0, color=TXT, lw=1.5); a.axvline(0, color=TXT, lw=1.5)
    a.set_xticks([]); a.set_yticks([])
    a.set_aspect("equal")
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    for s in a.spines.values():
        s.set_visible(False)


# ---------------- 1. soma de vetores -------------------------------------------
a = ax[0, 0]
papel(a, "1. Somar setas: anda uma, depois a outra")
v, w = (3, 1), (1, 2)
a.add_patch(FancyArrowPatch((0, 0), v, arrowstyle="-|>", mutation_scale=18, color=AZUL, lw=3))
a.add_patch(FancyArrowPatch(v, (v[0] + w[0], v[1] + w[1]), arrowstyle="-|>",
                            mutation_scale=18, color=VERDE, lw=3))
a.add_patch(FancyArrowPatch((0, 0), (v[0] + w[0], v[1] + w[1]), arrowstyle="-|>",
                            mutation_scale=18, color=CINZA, lw=2.5, linestyle="--"))
a.text(v[0] / 2, v[1] / 2 - 0.35, "v", fontsize=13, color=AZUL, weight="bold")
a.text(v[0] + w[0] / 2 + 0.2, v[1] + w[1] / 2, "w", fontsize=13, color=VERDE, weight="bold")
a.text(2.7, -0.6, "v + w", fontsize=12, color=CINZA, weight="bold")

# ---------------- 2. multiplicar por numero -------------------------------------
a = ax[0, 1]
papel(a, "2. Multiplicar por um número")
v = (1.5, 1)
a.add_patch(FancyArrowPatch((0, 0), v, arrowstyle="-|>", mutation_scale=16, color=CINZA, lw=2.5))
a.add_patch(FancyArrowPatch((0, 0), (2 * v[0], 2 * v[1]), arrowstyle="-|>", mutation_scale=18, color=VERDE, lw=3))
a.add_patch(FancyArrowPatch((0, 0), (-1.2 * v[0], -1.2 * v[1]), arrowstyle="-|>", mutation_scale=18, color=VERM, lw=3))
a.text(v[0] + 0.15, v[1], "v", fontsize=12, color=CINZA, weight="bold")
a.text(2 * v[0] + 0.15, 2 * v[1], "2v", fontsize=12, color=VERDE, weight="bold")
a.text(-1.2 * v[0] - 0.9, -1.2 * v[1], "-1,2v", fontsize=12, color=VERM, weight="bold")

# ---------------- 3. produto escalar e angulo ------------------------------------
a = ax[1, 0]
papel(a, "3. Produto escalar e o ângulo")
va = (3, 0)
for deg, cor, label in [(40, VERDE, "agudo: + "), (90, TXT, "reto: 0"), (140, VERM, "obtuso: −")]:
    rad = np.radians(deg)
    vb = (2.6 * np.cos(rad), 2.6 * np.sin(rad))
    a.add_patch(FancyArrowPatch((0, 0), vb, arrowstyle="-|>", mutation_scale=14, color=cor, lw=2.2))
a.add_patch(FancyArrowPatch((0, 0), va, arrowstyle="-|>", mutation_scale=16, color=AZUL, lw=3))
a.text(3.1, -0.1, "v", fontsize=12, color=AZUL, weight="bold")
a.text(-4.6, 2, "produto\npositivo = agudo\nzero = reto\nnegativo = obtuso", fontsize=9.5, color=TXT)

# ---------------- 4. matriz de rotacao --------------------------------------------
a = ax[1, 1]
papel(a, "4. Matriz de rotação usa seno e cosseno")
tri = np.array([[0, 2.2], [-1.6, -1], [1.6, -1]])
a.add_patch(Polygon(tri, closed=True, fill=True, facecolor=CINZA, alpha=0.18,
                    edgecolor=CINZA, lw=2, linestyle="--"))
deg = 50
rad = np.radians(deg)
R = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
tri_r = tri @ R.T
a.add_patch(Polygon(tri_r, closed=True, fill=True, facecolor=AZUL, alpha=0.25,
                    edgecolor=AZUL, lw=3))
arc = Arc((0, 0), 1.4, 1.4, angle=90, theta1=0, theta2=deg, color=ROXO, lw=2.5)
a.add_patch(arc)
a.text(0.9, 1.1, f"{deg}°", fontsize=11, color=ROXO, weight="bold")

fig.suptitle("Aula 17 — Vetores e matrizes", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "17-vetores-e-matrizes" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
