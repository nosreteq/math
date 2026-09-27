# Gera a figura estatica da Aula 30. Pode rodar de qualquer pasta: python scripts/figuras_aula30.py
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

# ---------------- 1. n^2 + n + 41 ------------------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. n² + n + 41: primo até n = 39; em 40, não")


def primo(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


for n in range(50):
    lin, col = n // 10, n % 10
    p = primo(n * n + n + 41)
    a.add_patch(Rectangle((col, -lin), 0.9, 0.9, facecolor="#bbf7d0" if p else "#fecaca", edgecolor=VERDE if p else VERM, lw=1.5))
    a.text(col + 0.45, -lin + 0.45, str(n), ha="center", va="center", fontsize=11, weight="bold")
a.set_xlim(-0.2, 10.1); a.set_ylim(-4.3, 1.1); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. gauss ----------------------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Duas escadas formam um retângulo 6 × 7")
n = 6
for lin in range(n):
    for col in range(n + 1):
        az = col <= lin
        a.add_patch(Rectangle((col, -lin), 0.92, 0.92, facecolor="#93c5fd" if az else "#fdba74", edgecolor=AZUL if az else LARANJA, lw=1))
a.text(3.5, -6.6, "1 + 2 + ... + n = n · (n + 1) ÷ 2", ha="center", fontsize=13, weight="bold", color=TXT)
a.set_xlim(-0.5, 7.5); a.set_ylim(-7.2, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. soma dos impares -------------------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Indução: 1 + 3 + 5 + ... + (2n − 1) = n²")
cores = ["#93c5fd", "#fdba74", "#86efac", "#f9a8d4", "#c4b5fd", "#fde68a"]
for i in range(6):
    for j in range(6):
        a.add_patch(Rectangle((j, -i), 0.92, 0.92, facecolor=cores[max(i, j)], edgecolor="#6b7280", lw=1))
for k in range(6):
    a.text(k + 0.46, 1.3, str(2 * k + 1), ha="center", fontsize=12, weight="bold")
a.set_xlim(-0.5, 6.5); a.set_ylim(-5.5, 2); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. collatz -------------------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Collatz a partir de 27: 111 passos, pico em 9.232")
s = [27]
while s[-1] != 1:
    v = s[-1]; s.append(v // 2 if v % 2 == 0 else 3 * v + 1)
a.plot(s, color=ROXO, lw=2)
a.set_xlim(0, len(s)); a.set_ylim(0, 10000)

fig.suptitle("Aula 30 — Pensar como matemático", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "30-pensar-como-matematico" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
