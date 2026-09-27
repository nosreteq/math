# Gera a figura estatica da Eletiva 6 (aula 36). Pode rodar de qualquer pasta: python scripts/figuras_aula36.py
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

from math import factorial
# ---------------- 1. e^x ---------------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. eˣ e os polinômios de Taylor de grau 1, 2, 3 e 5")
x = np.linspace(-3, 2.5, 300)
a.plot(x, np.exp(x), color=AZUL, lw=4, label="eˣ")
for n, cor in [(1, VERDE), (2, LARANJA), (3, ROXO), (5, VERM)]:
    a.plot(x, sum(x**k / factorial(k) for k in range(n + 1)), color=cor, lw=2, ls="--", label=f"grau {n}")
a.set_ylim(-2, 10); a.legend(loc="upper left", fontsize=10)

# ---------------- 2. seno ---------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. sen x e os polinômios de grau 1, 3, 7 e 15")
x = np.linspace(-10, 10, 600)
a.plot(x, np.sin(x), color=AZUL, lw=4)
for n, cor in [(1, VERDE), (3, LARANJA), (7, ROXO), (15, VERM)]:
    a.plot(x, sum((-1)**((k - 1) // 2) * x**k / factorial(k) for k in range(1, n + 1, 2)), color=cor, lw=2, ls="--")
a.set_ylim(-2.5, 2.5)

# ---------------- 3. soma 1/k! -----------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. 1 + 1 + 1/2 + 1/6 + ... chega em e depressa")
k = np.arange(0, 12)
termos = np.array([1 / factorial(i) for i in k])
a.bar(k, termos, color="#93c5fd")
a.plot(k, np.cumsum(termos), "o-", color=ROXO, lw=2.5)
a.axhline(np.e, color=VERM, ls="--")
a.set_ylim(0, 3)

# ---------------- 4. espiral de Euler ------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Os termos de e^(ix) para x = 2 espiralam")
t = np.linspace(0, 2 * np.pi, 200)
a.plot(np.cos(t), np.sin(t), color=CINZA, lw=1.5)
z, xv = 0 + 0j, 2.0
cores = [AZUL, VERDE, LARANJA, ROXO]
for n in range(14):
    termo = (1j * xv)**n / factorial(n)
    a.annotate("", ((z + termo).real, (z + termo).imag), (z.real, z.imag), arrowprops=dict(arrowstyle="-|>", color=cores[n % 4], lw=2))
    z += termo
a.plot(np.cos(xv), np.sin(xv), "o", color=VERM, ms=10)
a.set_xlim(-2.4, 1.6); a.set_ylim(-1.6, 2.4); a.set_aspect("equal"); a.grid(True, color="#ece7da")
for s in a.spines.values():
    s.set_visible(False)

fig.suptitle("Eletiva 6 — Séries de Taylor: trocar uma curva por potências", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "36-series-de-taylor" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
