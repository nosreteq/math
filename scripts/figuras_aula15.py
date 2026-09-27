# Gera a figura estatica da Aula 15. Pode rodar de qualquer pasta: python scripts/figuras_aula15.py
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

# ---------------- 1. tangente -------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. A reta que encosta em x = 1 sobe 2 por passo")
x = np.linspace(-2.5, 2.5, 300)
a.plot(x, x**2, color=AZUL, lw=3)
a.plot(x, 1 + 2 * (x - 1), color=VERM, lw=2.5)
a.plot(1, 1, "o", color=LARANJA, ms=10, mec=TXT)
a.set_xlim(-2.5, 2.5); a.set_ylim(-2, 6)

# ---------------- 2. secantes ---------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Dois pontos se aproximando: o passo vai para 2")
x = np.linspace(-0.5, 3.2, 300)
a.plot(x, x**2, color=AZUL, lw=3)
for h, cor in [(2, CINZA), (1, LARANJA), (0.3, ROXO)]:
    m = ((1 + h)**2 - 1) / h
    a.plot(x, 1 + m * (x - 1), color=cor, lw=1.8, label=f"h = {h:g}: passo {m:g}".replace(".", ","))
a.plot(1, 1, "o", color=TXT, ms=8)
a.legend(loc="upper left"); a.set_xlim(-0.5, 3.2); a.set_ylim(-1, 10)

# ---------------- 3. derivada -----------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Em radianos, a inclinação do seno é o cosseno")
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
a.plot(x, np.sin(x), color=AZUL, lw=3, label="seno")
a.plot(x, np.cos(x), color=VERM, lw=2.5, ls="--", label="inclinação = cosseno")
a.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]); a.set_xticklabels(["−2π", "−π", "0", "π", "2π"])
a.legend(loc="lower left"); a.set_ylim(-1.6, 1.6)

# ---------------- 4. topo e fundo -------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. x³ − 3x: inclinação zero no morro e no vale")
x = np.linspace(-2.3, 2.3, 300)
a.plot(x, x**3 - 3 * x, color=AZUL, lw=3)
for x0 in (-1, 1):
    y0 = x0**3 - 3 * x0
    a.plot([x0 - 0.7, x0 + 0.7], [y0, y0], color=VERM, lw=2.5)
    a.plot(x0, y0, "o", color=LARANJA, ms=10, mec=TXT)
a.set_xlim(-2.5, 2.5); a.set_ylim(-3.5, 3.5)

fig.suptitle("Aula 15 — A inclinação em cada ponto", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "15-a-inclinacao-em-cada-ponto" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
