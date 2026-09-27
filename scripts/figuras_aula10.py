# Gera a figura estatica da Aula 10. Pode rodar de qualquer pasta: python scripts/figuras_aula10.py
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
rng = np.random.default_rng(7)


def nuvem(a, titulo, forca, cor=AZUL):
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    x = rng.random(30)
    ruido = rng.random(30) - 0.5
    y = x * forca + ruido * (1 - forca) * 1.3
    a.scatter(x, y, s=45, color=cor, alpha=0.75, edgecolor="white", lw=0.8)
    a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values():
        s.set_visible(False)
    a.axhline(min(y) - 0.1, color=TXT, lw=1.5)
    a.axvline(-0.05, color=TXT, lw=1.5)


# ---------------- 1. lista vira vetor -------------------------------------------
a = ax[0, 0]
a.set_title("1. Uma lista de números é um vetor", fontsize=13.5, weight="bold", color=TXT, pad=10)
notas = [6, 8, 7, 9, 5]
a.bar(range(len(notas)), notas, color=ROXO, width=0.5)
a.set_xticks(range(len(notas)))
a.set_xticklabels([str(n) for n in notas], fontsize=11)
a.set_yticks([])
for s in ["top", "right", "left"]:
    a.spines[s].set_visible(False)
a.set_ylim(0, 11)
a.text(2, 10.3, "v = (6, 8, 7, 9, 5)", fontsize=12, weight="bold", color=ROXO, ha="center")

# ---------------- 2. correlacao alta vs baixa ------------------------------------
a = ax[0, 1]
nuvem(a, "2. Correlação alta: quase uma reta", 0.92, AZUL)

a = ax[1, 0]
nuvem(a, "3. Correlação baixa: nuvem espalhada", 0.15, LARANJA)

# ---------------- 4. angulo entre vetores -----------------------------------------
a = ax[1, 1]
a.set_title("4. Correlação = cosseno do ângulo", fontsize=13.5, weight="bold", color=TXT, pad=10)
a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3)
a.set_aspect("equal")
a.axis("off")
a.add_patch(FancyArrowPatch((0, 0), (1, 0), arrowstyle="-|>", mutation_scale=18, color=AZUL, lw=3))
deg = 25
rad = np.radians(deg)
a.add_patch(FancyArrowPatch((0, 0), (np.cos(rad), np.sin(rad)), arrowstyle="-|>",
                            mutation_scale=18, color=VERDE, lw=3))
a.text(1.05, -0.05, "lista A", fontsize=11, color=AZUL, weight="bold")
a.text(np.cos(rad) + 0.05, np.sin(rad), "lista B", fontsize=11, color=VERDE, weight="bold")
a.text(0.3, 0.08, f"{deg}°", fontsize=11, color=TXT)
a.text(0, -1.2, "ângulo pequeno → correlação perto de 1", fontsize=10.5, color=TXT, ha="center")

fig.suptitle("Aula 10 — Estatística com vetores", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "10-estatistica-com-vetores" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
