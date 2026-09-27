# Gera a figura estatica da Aula 13. Pode rodar de qualquer pasta: python scripts/figuras_aula13.py
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

# ---------------- 1. a parabola ------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. A máquina x² desenha uma parábola")
x = np.linspace(-3.2, 3.2, 300)
a.plot(x, x**2, color=AZUL, lw=3)
for v in range(-3, 4):
    a.plot(v, v**2, "o", color=LARANJA, ms=8, mec=TXT)
a.set_xlim(-3.5, 3.5); a.set_ylim(-1, 10.5)

# ---------------- 2. transformacoes ---------------------------------------------------
a = ax[0, 1]
eixos(a, "2. y = a(x − h)² + k: vértice em (h, k)")
x = np.linspace(-5, 5, 300)
a.plot(x, x**2, color=CINZA, lw=2, ls="--", label="x²")
a.plot(x, 0.5 * (x - 2)**2 - 1, color=AZUL, lw=3, label="0,5(x − 2)² − 1")
a.plot(x, -(x + 1)**2 + 3, color=VERM, lw=3, label="−(x + 1)² + 3")
a.plot([2, -1], [-1, 3], "o", color=ROXO, ms=9)
a.set_xlim(-5, 5); a.set_ylim(-4, 6); a.legend(loc="lower right")

# ---------------- 3. zeros --------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. (x − 1)² − 4 = 0  →  x = 3 ou x = −1")
x = np.linspace(-3, 5, 300)
a.plot(x, (x - 1)**2 - 4, color=AZUL, lw=3)
a.plot([-1, 3], [0, 0], "o", color=VERM, ms=10, mec="white", mew=2)
a.set_xlim(-3, 5); a.set_ylim(-5, 8)

# ---------------- 4. vertice como melhor valor --------------------------------------------
a = ax[1, 1]
eixos(a, "4. Área da horta x · (10 − x): topo em x = 5")
x = np.linspace(0, 10, 300)
a.plot(x, x * (10 - x), color=AZUL, lw=3)
a.plot(5, 25, "o", color=ROXO, ms=11)
a.annotate("25 m²", (5, 25), xytext=(6.2, 26.5), fontsize=12, weight="bold", color=ROXO)
a.set_xlim(-0.5, 10.5); a.set_ylim(-2, 29)

fig.suptitle("Aula 13 — Curvas que não são retas", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "13-curvas-que-nao-sao-retas" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
