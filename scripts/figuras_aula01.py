# Gera a figura estatica da Aula 1. Rode de dentro da pasta scripts/:  python3 figuras_aula01.py
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AZUL, VERM, VERDE, CINZA, TXT = "#2563eb", "#dc2626", "#059669", "#9ca3af", "#111827"

fig, ax = plt.subplots(2, 2, figsize=(13, 9.5))
fig.patch.set_facecolor("white")

# ---------------- 1. A maquina -------------------------------------------
a = ax[0, 0]
a.set_xlim(0, 10); a.set_ylim(0, 6); a.axis("off")
a.set_title("1. A função é uma máquina", fontsize=14, weight="bold", color=TXT, pad=12)

box = FancyBboxPatch((3.5, 2.1), 3.0, 1.9, boxstyle="round,pad=0.15",
                     facecolor="#dbeafe", edgecolor=AZUL, lw=2.5)
a.add_patch(box)
a.text(5.0, 3.05, "DOBRAR", fontsize=17, weight="bold", ha="center", va="center", color=AZUL)

a.add_patch(FancyArrowPatch((1.3, 3.05), (3.35, 3.05), arrowstyle="-|>",
                            mutation_scale=26, color=TXT, lw=2.5))
a.add_patch(FancyArrowPatch((6.65, 3.05), (8.7, 3.05), arrowstyle="-|>",
                            mutation_scale=26, color=TXT, lw=2.5))
a.text(0.9, 3.05, "3", fontsize=28, weight="bold", ha="center", va="center", color=VERDE)
a.text(9.1, 3.05, "6", fontsize=28, weight="bold", ha="center", va="center", color=VERM)
a.text(2.3, 3.6, "entra", fontsize=11, ha="center", color=TXT)
a.text(7.7, 3.6, "sai", fontsize=11, ha="center", color=TXT)

a.text(5.0, 1.1, "Põe um número, sai outro.\nO mesmo número que entra sempre dá a mesma resposta.",
       fontsize=11.5, ha="center", va="center", color=TXT)

# ---------------- 2. A tabela --------------------------------------------
a = ax[0, 1]
a.set_xlim(0, 10); a.set_ylim(0, 6); a.axis("off")
a.set_title("2. Anotamos tudo numa tabela", fontsize=14, weight="bold", color=TXT, pad=12)

entradas = [1, 2, 3, 4]
x0, y0, dy = 3.0, 4.6, 0.72
a.text(x0 + 0.6, y0 + 0.55, "entra", fontsize=12.5, weight="bold", ha="center", color=VERDE)
a.text(x0 + 3.4, y0 + 0.55, "sai", fontsize=12.5, weight="bold", ha="center", color=VERM)
a.plot([x0 - 0.4, x0 + 4.4], [y0 + 0.22, y0 + 0.22], color=TXT, lw=2)
a.plot([x0 + 2.0, x0 + 2.0], [y0 + 0.45, y0 - dy * 3.6], color=CINZA, lw=1.5)

for i, e in enumerate(entradas):
    y = y0 - i * dy
    a.text(x0 + 0.6, y, f"{e}", fontsize=15, ha="center", va="center", color=VERDE)
    a.text(x0 + 2.0, y, "→", fontsize=12, ha="center", va="center", color=CINZA)
    a.text(x0 + 3.4, y, f"{2*e}", fontsize=15, ha="center", va="center", color=VERM)

a.text(5.0, 1.0, "Cada linha é uma pergunta e a resposta dela.",
       fontsize=11.5, ha="center", va="center", color=TXT)

# ---------------- 3. Pontos no papel quadriculado -------------------------
def papel(a, titulo):
    a.set_xlim(-0.6, 5.4); a.set_ylim(-0.9, 9.6)
    a.set_xticks(range(0, 6)); a.set_yticks(range(0, 10, 2))
    a.grid(True, alpha=0.35, lw=0.8)
    a.axhline(0, color=TXT, lw=1.8); a.axvline(0, color=TXT, lw=1.8)
    a.set_title(titulo, fontsize=14, weight="bold", color=TXT, pad=12)
    a.set_xlabel("o número que entra", fontsize=10.5, color=VERDE)
    a.set_ylabel("o número que sai", fontsize=10.5, color=VERM)
    a.tick_params(labelsize=10)
    for s in a.spines.values():
        s.set_color(CINZA)

a = ax[1, 0]
papel(a, "3. Cada linha da tabela vira um ponto")
for e in entradas:
    a.plot([e, e], [0, 2 * e], color=VERDE, ls=":", lw=1.4, alpha=0.8)
    a.plot([0, e], [2 * e, 2 * e], color=VERM, ls=":", lw=1.4, alpha=0.8)
    a.scatter([e], [2 * e], s=130, color=AZUL, zorder=5, edgecolor="white", lw=1.5)
a.annotate("ando 3 para a direita,\nsubo 6 para cima", xy=(3, 6), xytext=(0.35, 8.1),
           fontsize=10.5, color=TXT,
           arrowprops=dict(arrowstyle="->", color=TXT, lw=1.5))

a = ax[1, 1]
papel(a, "4. Ligando os pontos: o desenho da máquina")
xs = np.linspace(0, 5, 100)
a.plot(xs, 2 * xs, color=AZUL, lw=3, zorder=3)
a.scatter(entradas, [2 * e for e in entradas], s=130, color=AZUL,
          zorder=5, edgecolor="white", lw=1.5)
a.text(2.55, 1.1, "Esse desenho mostra\ntodas as respostas\nde uma vez só.",
       fontsize=11, color=TXT)

fig.suptitle("Aula 1 — O que é uma função", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
fig.savefig("../aulas/01-o-que-e-uma-funcao/figuras.png", dpi=150, facecolor="white")
print("ok")
