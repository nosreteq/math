# Gera a figura estatica da Aula 1. Pode rodar de qualquer pasta: python scripts/figuras_aula01.py
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

# ---------------- 1. multiplos: pulos na reta ------------------------------------------------
a = ax[0, 0]
titulo(a, "1. Múltiplos de 3: pulos de 3 em 3 na reta")
a.plot([0, 24], [0, 0], color=TXT, lw=1.5)
for k in range(25):
    a.plot([k, k], [-0.15, 0.15], color=TXT, lw=1)
    if k % 3 == 0:
        a.text(k, -0.55, str(k), ha="center", fontsize=11, weight="bold", color=AZUL)
for k in range(0, 24, 3):
    t = np.linspace(0, np.pi, 30)
    a.plot(k + 1.5 - 1.5 * np.cos(t), 1.1 * np.sin(t), color=VERDE, lw=2.5)
a.set_xlim(-1, 25); a.set_ylim(-1.5, 2.5); a.axis("off")

# ---------------- 2. crivo --------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Crivo de Eratóstenes: os primos até 60")


def primo(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


for n in range(1, 61):
    lin, col = (n - 1) // 10, (n - 1) % 10
    p = primo(n)
    a.add_patch(Rectangle((col, -lin), 0.92, 0.92, facecolor="#bbf7d0" if p else "#f3f0e8",
                          edgecolor=VERDE if p else "#d6d0c2", lw=1.5))
    a.text(col + 0.46, -lin + 0.46, str(n), ha="center", va="center", fontsize=11,
           weight="bold" if p else "normal", color=TXT if p else CINZA)
a.set_xlim(-0.3, 10.2); a.set_ylim(-5.4, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. arvore de fatores ----------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Árvore de fatores: 60 = 2 · 2 · 3 · 5")
nos = {"60": (0, 0), "2a": (-1.5, -1), "30": (1.5, -1), "2b": (0, -2), "15": (3, -2), "3": (1.8, -3), "5": (4.2, -3)}
rot = {"2a": "2", "2b": "2"}
for p, q in [("60", "2a"), ("60", "30"), ("30", "2b"), ("30", "15"), ("15", "3"), ("15", "5")]:
    a.plot([nos[p][0], nos[q][0]], [nos[p][1], nos[q][1]], color=CINZA, lw=2, zorder=1)
for k, (x, y) in nos.items():
    txt = rot.get(k, k)
    prim = txt in ("2", "3", "5")
    a.add_patch(Circle((x, y), 0.38, facecolor="#bbf7d0" if prim else "#dbeafe", edgecolor=VERDE if prim else AZUL, lw=2, zorder=2))
    a.text(x, y, txt, ha="center", va="center", fontsize=13, weight="bold", color=TXT, zorder=3)
a.set_xlim(-3, 5.5); a.set_ylim(-3.8, 0.8); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. MDC com ladrilhos -----------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. MDC(12, 18) = 6: o maior ladrilho quadrado")
for i in range(3):
    for j in range(2):
        a.add_patch(Rectangle((i * 6, j * 6), 6, 6, facecolor=["#dbeafe", "#fde68a"][(i + j) % 2], edgecolor=AZUL, lw=2))
a.text(9, -1.3, "18", ha="center", fontsize=13, weight="bold", color=TXT)
a.text(-1.3, 6, "12", ha="center", va="center", fontsize=13, weight="bold", color=TXT)
a.set_xlim(-3, 20); a.set_ylim(-3, 14); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Aula 1 — Múltiplos, divisores e primos", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "01-multiplos-divisores-e-primos" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
