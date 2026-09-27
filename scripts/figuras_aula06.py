# Gera a figura estatica da Aula 6. Pode rodar de qualquer pasta: python scripts/figuras_aula06.py
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

# ---------------- 1. arvore de possibilidades -----------------------------------------------------
a = ax[0, 0]
titulo(a, "1. 3 camisas × 2 calças = 6 roupas")
cam = [("azul", AZUL), ("verde", VERDE), ("vermelha", VERM)]
for i, (n, c) in enumerate(cam):
    yc = 2 - 2 * i
    a.plot([0, 2], [0, yc], color=CINZA, lw=2)
    a.add_patch(Circle((2, yc), 0.3, color=c))
    for j, (cal, yy) in enumerate([("jeans", 0.5), ("preta", -0.5)]):
        a.plot([2.3, 4.5], [yc, yc + yy], color=CINZA, lw=1.5)
        a.text(4.7, yc + yy, f"{n} + {cal}", va="center", fontsize=11, color=TXT)
a.plot(0, 0, "o", color=TXT, ms=10)
a.set_xlim(-0.5, 8); a.set_ylim(-3, 3); a.axis("off")

# ---------------- 2. duas moedas ---------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Duas moedas: 4 resultados igualmente prováveis")
res = ["KK", "KC", "CK", "CC"]
for i, r in enumerate(res):
    for j, ch in enumerate(r):
        a.add_patch(Circle((i * 2.2 + j * 0.9, 0), 0.4, facecolor="#fde68a" if ch == "K" else "#e5e7eb", edgecolor=TXT, lw=1.5))
        a.text(i * 2.2 + j * 0.9, 0, ch, ha="center", va="center", fontsize=13, weight="bold")
    a.text(i * 2.2 + 0.45, -0.9, "1/4", ha="center", fontsize=12, color=AZUL, weight="bold")
a.text(3.75, -1.8, "K = cara, C = coroa · uma cara e uma coroa: 2/4 = 1/2", ha="center", fontsize=11, color=TXT)
a.set_xlim(-0.8, 8.2); a.set_ylim(-2.3, 1); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. soma de dois dados --------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Soma de dois dados: o 7 aparece de 6 jeitos em 36")
somas = np.arange(2, 13)
jeitos = 6 - np.abs(somas - 7)
a.bar(somas, jeitos, color=[VERM if s == 7 else AZUL for s in somas], alpha=0.8)
a.set_xticks(somas); a.set_ylabel("jeitos (de 36)", fontsize=12)

# ---------------- 4. frequencia gruda na chance ---------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. A fração de caras gruda em ½")
jog = rng.random(2000) < 0.5
a.plot(np.arange(1, 2001), np.cumsum(jog) / np.arange(1, 2001), color=AZUL, lw=2)
a.axhline(0.5, color=ROXO, ls="--", lw=2)
a.set_xscale("log"); a.set_xlabel("lançamentos", fontsize=12); a.set_ylim(0, 1)

fig.suptitle("Aula 6 — Contagem e chance", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "06-contagem-e-chance" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
