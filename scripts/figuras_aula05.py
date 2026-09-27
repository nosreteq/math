# Gera a figura estatica da Aula 5. Pode rodar de qualquer pasta: python scripts/figuras_aula05.py
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

# ---------------- 1. gangorra -----------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. A média é o ponto de equilíbrio da gangorra")
dados = [2, 3, 3, 5, 9]
m = np.mean(dados)
a.plot([0, 10], [0, 0], color=TXT, lw=4)
for v in sorted(set(dados)):
    for k in range(dados.count(v)):
        a.add_patch(Circle((v, 0.45 + 0.8 * k), 0.35, facecolor=AZUL, edgecolor=TXT, lw=1.5))
a.add_patch(Polygon([[m, -0.05], [m - 0.5, -1], [m + 0.5, -1]], closed=True, facecolor=VERM))
a.text(m, -1.6, f"média = {m:g}".replace(".", ","), ha="center", fontsize=13, weight="bold", color=VERM)
for k in range(11):
    a.text(k, -0.35, str(k), ha="center", fontsize=9, color=CINZA)
a.set_xlim(-0.5, 10.5); a.set_ylim(-2.2, 2.6); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. media x mediana -----------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. O salário do chefe puxa a média")
sal = [2, 2.5, 3, 3, 3.5, 4, 40]
a.bar(range(7), sal, color=[AZUL] * 6 + [VERM], width=0.7)
media, med = np.mean(sal), np.median(sal)
a.axhline(media, color=LARANJA, lw=2.5, ls="--"); a.axhline(med, color=VERDE, lw=2.5, ls="--")
a.text(0, media + 1, f"média ≈ {media:.1f} mil".replace(".", ","), fontsize=12, weight="bold", color=LARANJA)
a.text(0, med + 1, f"mediana = {med:g} mil".replace(".", ","), fontsize=12, weight="bold", color=VERDE)
a.set_xticks([]); a.set_ylim(0, 43)
for s in a.spines.values():
    s.set_visible(False)

# ---------------- 3. histograma -----------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Histograma: a moda é a barra mais alta")
alturas = rng.normal(165, 8, 300)
cont, bordas, barras = a.hist(alturas, bins=np.arange(140, 192, 4), color=AZUL, alpha=0.75, edgecolor="white")
i = int(np.argmax(cont)); barras[i].set_facecolor(VERM)
a.set_xlabel("altura (cm)", fontsize=12); a.set_xlim(138, 192)

# ---------------- 4. desvio ---------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Mesma média, desvios diferentes")
for lin, (d, cor) in enumerate([([4, 5, 5, 5, 6], VERDE), ([1, 3, 5, 7, 9], VERM)]):
    y = -lin * 1.5
    a.plot([0, 10], [y, y], color=CINZA, lw=1.5)
    for v in d:
        a.plot(v, y, "o", color=cor, ms=12)
    a.plot([5, 5], [y - 0.35, y + 0.35], color=TXT, lw=2)
    a.text(10.3, y, f"desvio ≈ {np.std(d):.1f}".replace(".", ","), va="center", fontsize=12, weight="bold", color=cor)
a.set_xlim(-0.5, 13.5); a.set_ylim(-2.3, 0.8); a.axis("off")

fig.suptitle("Aula 5 — Dados: média, mediana, moda e desvio", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "05-dados-media-mediana-moda-e-desvio" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
