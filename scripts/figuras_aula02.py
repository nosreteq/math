# Gera a figura estatica da Aula 2. Pode rodar de qualquer pasta: python scripts/figuras_aula02.py
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

# ---------------- 1. pizza -------------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. 3/8: a pizza em 8 fatias, 3 comidas")
for k in range(8):
    a.add_patch(Wedge((0, 0), 1, 90 - 45 * (k + 1), 90 - 45 * k, facecolor=LARANJA if k < 3 else "#fef3c7",
                      edgecolor=TXT, lw=2, alpha=0.85 if k < 3 else 1))
a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. equivalentes ---------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Frações equivalentes: 1/2 = 2/4 = 4/8")
for lin, n in enumerate([2, 4, 8]):
    for k in range(n):
        a.add_patch(Rectangle((k * 8 / n, -lin * 1.4), 8 / n, 1, facecolor=AZUL if k < n / 2 else "#f3f0e8",
                              alpha=0.7 if k < n / 2 else 1, edgecolor=TXT, lw=1.5))
    a.text(-0.4, -lin * 1.4 + 0.5, f"{n // 2}/{n}", ha="right", va="center", fontsize=13, weight="bold", color=TXT)
a.set_xlim(-1.6, 8.3); a.set_ylim(-3.4, 1.4); a.axis("off")

# ---------------- 3. regua dos decimais ---------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Décimos e centésimos: 0,25 = 25/100 = 1/4")
a.plot([0, 1], [0, 0], color=TXT, lw=2)
for k in range(11):
    a.plot([k / 10, k / 10], [-0.05, 0.05], color=TXT, lw=1.5)
    a.text(k / 10, -0.14, f"{k / 10:.1f}".replace(".", ","), ha="center", fontsize=10, color=CINZA)
for v, txt, cor in [(0.25, "0,25 = 1/4", VERDE), (0.5, "0,5 = 1/2", AZUL), (0.75, "0,75 = 3/4", VERM)]:
    a.plot(v, 0, "o", color=cor, ms=11)
    a.text(v, 0.12, txt, ha="center", fontsize=12, weight="bold", color=cor)
a.set_xlim(-0.08, 1.08); a.set_ylim(-0.4, 0.4); a.axis("off")

# ---------------- 4. negativos --------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Negativos: −3 + 5 = 2")
a.plot([-6, 6], [0, 0], color=TXT, lw=2)
for k in range(-6, 7):
    a.plot([k, k], [-0.12, 0.12], color=TXT, lw=1.3)
    a.text(k, -0.45, str(k).replace("-", "−"), ha="center", fontsize=11, color=VERM if k < 0 else (TXT if k == 0 else AZUL))
seta(a, (-3, 0.35), (2, 0.35), VERDE)
a.plot(-3, 0, "o", color=VERM, ms=11); a.plot(2, 0, "o", color=AZUL, ms=11)
a.text(-0.5, 0.65, "+5", ha="center", fontsize=13, weight="bold", color=VERDE)
a.set_xlim(-6.5, 6.5); a.set_ylim(-1.2, 1.4); a.axis("off")

fig.suptitle("Aula 2 — Pedaços e sinais: frações, decimais e negativos", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "02-fracoes-decimais-e-negativos" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
