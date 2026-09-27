# Gera a figura estatica da Aula 5. Pode rodar de qualquer pasta: python scripts/figuras_aula05.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")
xs = np.linspace(0, 720, 400)


def onda(a, titulo, ylim=1.6):
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    a.axhline(0, color=TXT, lw=1.5)
    a.set_ylim(-ylim, ylim)
    a.set_xlim(0, 720)
    a.set_xticks([0, 180, 360, 540, 720])
    a.set_yticks([])
    for s in a.spines.values():
        s.set_visible(False)
    a.tick_params(labelsize=9)


# ---------------- 1. desenrolando o circulo -----------------------------------
a = ax[0, 0]
a.set_title("1. Desenrolando o círculo em onda", fontsize=13.5, weight="bold", color=TXT, pad=10)
a.axis("off")
circ = plt.Circle((-1.4, 0), 1, fill=False, color=CINZA, lw=1.5, transform=a.transData)
a.add_patch(circ)
degs = np.linspace(0, 360, 200)
ys = np.sin(np.radians(degs))
xs_line = -0.4 + degs / 360 * 2.6
a.plot(xs_line, ys, color=VERM, lw=2.5)
a.axhline(0, xmin=0.13, xmax=0.98, color=CINZA, lw=1)
deg0 = 60
x0, y0 = np.cos(np.radians(deg0)) - 1.4, np.sin(np.radians(deg0))
a.scatter([x0], [y0], s=70, color=AZUL, zorder=6, edgecolor="white", lw=1.3)
a.plot([-1.4, x0], [0, y0], color=AZUL, lw=1.5, ls="--")
xw = -0.4 + deg0 / 360 * 2.6
a.scatter([xw], [y0], s=70, color=VERM, zorder=6, edgecolor="white", lw=1.3)
a.plot([x0, xw], [y0, y0], color=CINZA, lw=1, ls=":")
a.set_xlim(-2.6, 2.4); a.set_ylim(-1.4, 1.4)

# ---------------- 2. tres controles ---------------------------------------------
a = ax[0, 1]
onda(a, "2. Amplitude, frequência e fase")
a.plot(xs, np.sin(np.radians(xs)), color=CINZA, lw=1.5, ls="--", label="seno(x)")
a.plot(xs, 1.4 * np.sin(np.radians(xs)), color=VERDE, lw=2.5, label="amplitude maior")
a.plot(xs, np.sin(np.radians(2 * xs)), color=AZUL, lw=2.5, label="frequência maior")
a.plot(xs, np.sin(np.radians(xs - 90)), color=ROXO, lw=2.5, label="fase deslocada")
a.legend(fontsize=8.5, loc="upper right", framealpha=0.95)

# ---------------- 3. reencontro aula 1 -------------------------------------------
a = ax[1, 0]
onda(a, "3. As mesmas transformações da Aula 1")
a.plot(xs, np.sin(np.radians(xs)), color=CINZA, lw=2, ls="--")
a.plot(xs, 1.3 * np.sin(np.radians(xs)), color=VERDE, lw=2.5)
a.annotate("multiplica a saída\n(amplitude)", xy=(90, 1.3), xytext=(150, 1.5),
           fontsize=9, color=VERDE, weight="bold",
           arrowprops=dict(arrowstyle="->", color=VERDE))
a.annotate("multiplica a entrada\n(frequência)", xy=(360, 0), xytext=(430, -1.0),
           fontsize=9, color=AZUL, weight="bold",
           arrowprops=dict(arrowstyle="->", color=AZUL))
a.annotate("soma na entrada\n(fase)", xy=(540, -1), xytext=(560, 1.1),
           fontsize=9, color=ROXO, weight="bold",
           arrowprops=dict(arrowstyle="->", color=ROXO))

# ---------------- 4. somar duas ondas --------------------------------------------
a = ax[1, 1]
onda(a, "4. Somar duas ondas", ylim=2.1)
y1 = np.sin(np.radians(xs))
y2 = 0.6 * np.sin(np.radians(2 * xs))
a.plot(xs, y1, color=VERDE, lw=2, ls="--", label="onda 1")
a.plot(xs, y2, color=AZUL, lw=2, ls="--", label="onda 2")
a.plot(xs, y1 + y2, color=ROXO, lw=3, label="soma")
a.legend(fontsize=8.5, loc="upper right", framealpha=0.95)

fig.suptitle("Aula 5 — Ondas", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "05-ondas" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
