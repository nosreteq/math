# Gera a figura estatica da Aula 21. Pode rodar de qualquer pasta: python scripts/figuras_aula21.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def eixos(a, titulo):
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    a.axhline(0, color=TXT, lw=1)
    a.axvline(0, color=TXT, lw=1)
    a.grid(True, color="#ece7da")
    for s in a.spines.values():
        s.set_visible(False)

rng = np.random.default_rng(7)

# ---------------- 1. pascal ----------------------------------------------------------------------------
a = ax[0, 0]
a.set_title("1. Triângulo de Pascal: de quantos jeitos cair em cada casa", fontsize=13.5, weight="bold", color=TXT, pad=10)
from math import comb
for lin in range(9):
    for k in range(lin + 1):
        v = comb(lin, k)
        a.text(k - lin / 2, -lin, str(v), ha="center", va="center", fontsize=11 if v < 100 else 9.5,
               weight="bold", color=AZUL if lin < 8 else VERM)
a.text(0, -9.2, "linha 8: 1 + 8 + 28 + 56 + 70 + 56 + 28 + 8 + 1 = 256 = 2⁸", ha="center", fontsize=11, color=VERM)
a.set_xlim(-5, 5); a.set_ylim(-9.8, 0.8); a.axis("off")

# ---------------- 2. galton -----------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Máquina de Galton (10 fileiras, 2.000 bolinhas)")
pos = (rng.random((2000, 10)) < 0.5).sum(axis=1)
cont = np.bincount(pos, minlength=11)
a.bar(range(11), cont, color=AZUL, alpha=0.75)
x = np.linspace(-0.5, 10.5, 200)
m, s = 5, np.sqrt(10) / 2
a.plot(x, 2000 * np.exp(-((x - m) / s)**2 / 2) / (s * np.sqrt(2 * np.pi)), color=VERM, lw=2.5)

# ---------------- 3. sinos ------------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Média μ posiciona, desvio σ alarga")
x = np.linspace(-6, 6, 400)
for m, s, cor in [(0, 1, ROXO), (2, 0.6, VERDE), (-1.5, 2, LARANJA)]:
    a.plot(x, np.exp(-((x - m) / s)**2 / 2) / (s * np.sqrt(2 * np.pi)), color=cor, lw=3,
           label=f"μ = {m:g}, σ = {s:g}".replace(".", ","))
a.legend(loc="upper left"); a.set_ylim(-0.02, 0.72)

# ---------------- 4. 68-95-99,7 --------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Área = chance: 68% · 95% · 99,7%")
x = np.linspace(-4, 4, 400)
y = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
for k, alfa in [(3, 0.15), (2, 0.25), (1, 0.4)]:
    a.fill_between(x, y, where=np.abs(x) <= k, color=VERDE, alpha=alfa)
a.plot(x, y, color=ROXO, lw=3)
for k, txt in [(1, "68%"), (2, "95%"), (3, "99,7%")]:
    a.text(0, 0.05 + 0.09 * (k - 1), txt, ha="center", fontsize=11, weight="bold", color=TXT)
a.set_ylim(-0.02, 0.45)

fig.suptitle("Aula 21 — A curva normal", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "21-a-curva-normal" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
