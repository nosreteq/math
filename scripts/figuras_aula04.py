# Gera a figura estatica da Aula 4. Pode rodar de qualquer pasta: python scripts/figuras_aula04.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def circulo(a, titulo):
    a.set_xlim(-1.35, 1.35); a.set_ylim(-1.35, 1.35)
    a.set_aspect("equal")
    a.axis("off")
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    c = plt.Circle((0, 0), 1, fill=False, color=CINZA, lw=1.5)
    a.add_patch(c)
    a.plot([-1.25, 1.25], [0, 0], color="#e6e1d4", lw=1)
    a.plot([0, 0], [-1.25, 1.25], color="#e6e1d4", lw=1)


# ---------------- 1. sombra e altura -----------------------------------------
a = ax[0, 0]
circulo(a, "1. A sombra (cosseno) e a altura (seno)")
deg = 40
rad = np.radians(deg)
x, y = np.cos(rad), np.sin(rad)
a.plot([0, x], [0, y], color=AZUL, lw=2.5, ls="--")
a.scatter([x], [y], s=100, color=AZUL, zorder=6, edgecolor="white", lw=1.5)
a.plot([0, x], [0, 0], color=VERDE, lw=4, solid_capstyle="round")
a.plot([x, x], [0, y], color=VERM, lw=4, solid_capstyle="round")
a.text(x / 2, -0.14, "cosseno", fontsize=10.5, color=VERDE, weight="bold", ha="center")
a.text(x + 0.08, y / 2, "seno", fontsize=10.5, color=VERM, weight="bold")

# ---------------- 2. sempre entre -1 e 1 --------------------------------------
a = ax[0, 1]
circulo(a, "2. Preso na borda: sempre entre −1 e 1")
for d, cor in [(20, AZUL), (100, LARANJA), (200, ROXO), (320, VERM)]:
    r = np.radians(d)
    a.scatter([np.cos(r)], [np.sin(r)], s=70, color=cor, zorder=6, edgecolor="white", lw=1.2)
a.text(0, -1.3, "nenhum ponto sai do círculo de raio 1", fontsize=10.5, color=TXT, ha="center")

# ---------------- 3. valores de olho ------------------------------------------
a = ax[1, 0]
circulo(a, "3. Os quatro valores de olho")
for d, txt in [(0, "(1, 0)"), (90, "(0, 1)"), (180, "(−1, 0)"), (270, "(0, −1)")]:
    r = np.radians(d)
    x, y = np.cos(r), np.sin(r)
    a.scatter([x], [y], s=90, color=VERDE if d in (0, 180) else VERM, zorder=6, edgecolor="white", lw=1.5)
    a.text(1.22 * np.cos(r), 1.22 * np.sin(r), f"{d}°\n{txt}", fontsize=9.5, weight="bold",
           color=TXT, ha="center", va="center")

# ---------------- 4. o ponto e as duas coordenadas ----------------------------
a = ax[1, 1]
circulo(a, "4. O ponto = (cosseno, seno)")
deg = 130
rad = np.radians(deg)
x, y = np.cos(rad), np.sin(rad)
a.add_patch(FancyArrowPatch((0, 0), (x, y), arrowstyle="-|>", mutation_scale=18, color=AZUL, lw=3))
a.plot([0, x], [0, 0], color=VERDE, lw=3, ls=":")
a.plot([x, x], [0, y], color=VERM, lw=3, ls=":")
a.text(x, y + 0.12, f"({x:.2f}, {y:.2f})", fontsize=10.5, weight="bold", color=AZUL, ha="center")
a.text(0, -1.3, "mesmo endereço de dois números da Aula 2", fontsize=10, color=TXT,
       ha="center", style="italic")

fig.suptitle("Aula 4 — Seno e cosseno", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "04-seno-e-cosseno" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
