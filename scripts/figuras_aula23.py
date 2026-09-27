# Gera a figura estatica da Aula 23. Pode rodar de qualquer pasta: python scripts/figuras_aula23.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def papel(a, titulo, lim=6):
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim)
    a.axhline(0, color=TXT, lw=1.5); a.axvline(0, color=TXT, lw=1.5)
    a.set_xticks([]); a.set_yticks([])
    a.set_aspect("equal")
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    for s in a.spines.values():
        s.set_visible(False)


# ---------------- 1. projecao = sombra -----------------------------------------
a = ax[0, 0]
papel(a, "1. Projeção: a sombra de v sobre w")
a.add_patch(FancyArrowPatch((0, 0), (4.5, 0), arrowstyle="-|>", mutation_scale=16, color=LARANJA, lw=3))
deg = 35
rad = np.radians(deg)
vx, vy = 4 * np.cos(rad), 4 * np.sin(rad)
a.add_patch(FancyArrowPatch((0, 0), (vx, vy), arrowstyle="-|>", mutation_scale=16, color=AZUL, lw=3))
proj = 4 * np.cos(rad)
a.add_patch(FancyArrowPatch((0, 0), (proj, 0), arrowstyle="-|>", mutation_scale=16, color=VERDE, lw=4))
a.plot([vx, proj], [vy, 0], color=CINZA, lw=1.5, ls="--")
a.text(4.6, -0.1, "w", fontsize=12, color=LARANJA, weight="bold")
a.text(vx + 0.1, vy + 0.15, "v", fontsize=12, color=AZUL, weight="bold")
a.text(proj / 2, -0.5, "sombra", fontsize=10.5, color=VERDE, weight="bold", ha="center")

# ---------------- 2. erro entre ponto e reta -------------------------------------
a = ax[0, 1]
papel(a, "2. Erro: distância do ponto até a reta")
xs = np.linspace(-5, 5, 20)
a.plot(xs, 0.6 * xs, color=ROXO, lw=2.5)
pontos = [(-3, -1), (-1, 0.5), (1.5, 0.3), (3.5, 2.8)]
for px, py in pontos:
    yreta = 0.6 * px
    a.plot([px, px], [py, yreta], color=VERM, lw=2, ls=":")
    a.scatter([px], [py], s=70, color=AZUL, zorder=6, edgecolor="white", lw=1.2)
a.text(-5.5, 5.2, "linhas vermelhas = erros", fontsize=9.5, color=VERM)

# ---------------- 3. minimos quadrados -----------------------------------------------
a = ax[1, 0]
papel(a, "3. A reta que minimiza a soma dos erros²")
rng = np.random.default_rng(3)
xs2 = np.linspace(-4, 4, 10)
ys2 = 0.5 * xs2 + rng.normal(0, 0.8, size=10)
a.scatter(xs2, ys2, s=60, color=AZUL, zorder=6, edgecolor="white", lw=1.2)
coef = np.polyfit(xs2, ys2, 1)
a.plot(xs2, coef[0] * xs2 + coef[1], color=ROXO, lw=3, label="melhor ajuste")
a.plot(xs2, 0.5 * xs2 - 2, color=CINZA, lw=2, ls="--", label="outra reta qualquer")
a.legend(fontsize=8.5, loc="upper left", framealpha=0.95)

# ---------------- 4. mesma receita da aula 2 --------------------------------------------
a = ax[1, 1]
a.axis("off")
a.set_title("4. A receita continua igual", fontsize=13.5, weight="bold", color=TXT, pad=10)
a.text(0.5, 0.65, "f(x) = passo · x + altura de partida", fontsize=15, weight="bold",
       color=TXT, ha="center", transform=a.transAxes)
a.text(0.5, 0.4, "só muda COMO passo e altura\nsão escolhidos: para minimizar\na soma dos erros ao quadrado",
       fontsize=12, ha="center", color=CINZA, transform=a.transAxes)

fig.suptitle("Aula 23 — Projeção e mínimos quadrados", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "23-projecao-e-minimos-quadrados" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
