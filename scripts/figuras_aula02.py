# Gera a figura estatica da Aula 2. Rode de dentro da pasta scripts/:  python3 figuras_aula02.py
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

AZUL, VERM, VERDE, LARANJA, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                          "#d97706", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def papel(a, titulo, lim=7, passo=1):
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim)
    a.set_xticks(range(-lim + 1, lim, passo)); a.set_yticks(range(-lim + 1, lim, passo))
    a.grid(True, alpha=0.35, lw=0.8)
    a.axhline(0, color=TXT, lw=2, zorder=2); a.axvline(0, color=TXT, lw=2, zorder=2)
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    a.tick_params(labelsize=9)
    a.set_aspect("equal")
    for s in a.spines.values():
        s.set_color(CINZA)


# ---------------- 1. as duas reguas + marcar um ponto ---------------------
a = ax[0, 0]
papel(a, "1. Duas réguas: uma deitada e uma em pé")
a.add_patch(FancyArrowPatch((0, 0), (3, 0), arrowstyle="-|>", mutation_scale=20,
                            color=VERDE, lw=3, zorder=4))
a.add_patch(FancyArrowPatch((3, 0), (3, 5), arrowstyle="-|>", mutation_scale=20,
                            color=VERM, lw=3, zorder=4))
a.scatter([3], [5], s=170, color=AZUL, zorder=6, edgecolor="white", lw=2)
a.text(3.35, 5.2, "(3, 5)", fontsize=14, weight="bold", color=AZUL)
a.text(1.5, -1.1, "1º ando 3", fontsize=11, color=VERDE, ha="center", weight="bold")
a.text(3.35, 2.4, "2º subo 5", fontsize=11, color=VERM, weight="bold")
a.text(6.4, -0.75, "deitada", fontsize=10, color=TXT, ha="right", style="italic")
a.text(0.25, 6.3, "em pé", fontsize=10, color=TXT, style="italic")
a.text(-6.5, -6.2, "Sempre nessa ordem:\nprimeiro ando, depois subo.",
       fontsize=10.5, color=TXT)

# ---------------- 2. numeros negativos ------------------------------------
a = ax[0, 1]
papel(a, "2. Antes do zero a régua continua: negativos")
a.add_patch(Rectangle((-7, 0), 7, 7, color=VERM, alpha=0.05, zorder=0))
a.add_patch(Rectangle((-7, -7), 7, 7, color=VERM, alpha=0.09, zorder=0))
a.add_patch(Rectangle((0, -7), 7, 7, color=VERM, alpha=0.05, zorder=0))
pts = [(4, 3, 4.0, 4.4, "(4, 3)\ndireita, cima"),
       (-4, 2, -4.0, 3.4, "(-4, 2)\nesquerda, cima"),
       (-4, -4, -4.0, -5.9, "(-4, -4)\nesquerda, baixo"),
       (4, -3, 4.0, -4.9, "(4, -3)\ndireita, baixo")]
for px, py, tx, ty, rot in pts:
    a.scatter([px], [py], s=150, color=AZUL, zorder=6, edgecolor="white", lw=2)
    a.text(tx, ty, rot, fontsize=9.5, ha="center", color=TXT)
a.text(0.3, 0.3, "0", fontsize=12, weight="bold", color=TXT)

# ---------------- 3. retas: sobe rapido, devagar, desce -------------------
a = ax[1, 0]
papel(a, "3. Toda máquina de multiplicar dá uma linha reta")
xs = np.linspace(-7, 7, 100)
a.plot(xs, 2 * xs, color=VERM, lw=3, label="dobro:  2 · x")
a.plot(xs, xs, color=AZUL, lw=3, label="igual:  1 · x")
a.plot(xs, 0.5 * xs, color=VERDE, lw=3, label="metade:  0,5 · x")
a.plot(xs, -xs, color=LARANJA, lw=3, ls="--", label="negativo:  -1 · x")
a.legend(fontsize=9.5, loc="upper left", framealpha=0.95)
a.text(-6.6, -6.5, "Multiplicar por um número negativo\nvira a linha de cabeça para baixo.",
       fontsize=10, color=LARANJA,
       bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=LARANJA, alpha=0.95))

# ---------------- 4. degraus + somar levanta a linha ----------------------
a = ax[1, 1]
papel(a, "4. O passo da escada e o número que levanta")
a.plot(xs, 2 * xs, color=CINZA, lw=2.5, ls="--", label="2 · x")
a.plot(xs, 2 * xs + 3, color=AZUL, lw=3, label="2 · x + 3")
for i in range(0, 2):
    x1 = i
    a.plot([x1, x1 + 1], [2 * x1 + 3, 2 * x1 + 3], color=VERDE, lw=2.5, zorder=5)
    a.plot([x1 + 1, x1 + 1], [2 * x1 + 3, 2 * x1 + 5], color=VERM, lw=2.5, zorder=5)
a.text(2.35, 5.4, "ando 1\nsubo 2", fontsize=10, color=TXT, weight="bold")
a.add_patch(FancyArrowPatch((-0.55, 0), (-0.55, 3), arrowstyle="<|-|>",
                            mutation_scale=15, color=LARANJA, lw=2.5, zorder=6))
a.text(-6.6, 0.9, "o + 3 levanta\na linha inteira", fontsize=10,
       color=LARANJA, weight="bold",
       bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=LARANJA, alpha=0.95))
a.scatter([0], [3], s=140, color=LARANJA, zorder=7, edgecolor="white", lw=2)
a.legend(fontsize=9.5, loc="lower right", framealpha=0.95)

fig.suptitle("Aula 2 — Desenhar números no papel", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
fig.savefig("../aulas/02-desenhar-numeros-no-papel/figuras.png", dpi=150, facecolor="white")
print("ok")
