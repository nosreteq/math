# Gera a figura estatica da Aula 3. Pode rodar de qualquer pasta: python scripts/figuras_aula03.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc, Wedge

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


def ponteiro(a, deg, cor=AZUL, r=1.0):
    rad = np.radians(deg)
    x, y = r * np.cos(rad), r * np.sin(rad)
    a.add_patch(FancyArrowPatch((0, 0), (x, y), arrowstyle="-|>", mutation_scale=18,
                                color=cor, lw=3.5, zorder=5))
    a.scatter([0], [0], s=40, color=TXT, zorder=6)


# ---------------- 1. girar nao e andar --------------------------------------
a = ax[0, 0]
circulo(a, "1. Ângulo: quanto virou, não quanto andou")
a.plot([0, 1], [0, 0], color=CINZA, lw=1.5, ls="--")
arc = Arc((0, 0), 0.7, 0.7, angle=0, theta1=0, theta2=50, color=ROXO, lw=3)
a.add_patch(arc)
ponteiro(a, 50, ROXO)
a.text(0.42, 0.16, "50°", fontsize=13, weight="bold", color=ROXO)
a.text(0, -1.3, "o pé não sai do chão —\nsó a direção muda", fontsize=10.5, color=TXT, ha="center")

# ---------------- 2. os quatro marcos ---------------------------------------
a = ax[0, 1]
circulo(a, "2. Os quatro marcos (fatias da pizza)")
cores = [VERDE, AZUL, LARANJA, VERM]
for i, (ini, fim, cor) in enumerate(zip([0, 90, 180, 270], [90, 180, 270, 360], cores)):
    a.add_patch(Wedge((0, 0), 1, ini, fim, facecolor=cor, alpha=0.18, edgecolor=cor, lw=2))
for deg, rot, txt in [(0, 0, "0°"), (90, 90, "90°\nreto"), (180, 180, "180°\nmeia volta"), (270, 270, "270°")]:
    rad = np.radians(deg)
    a.text(1.18 * np.cos(rad), 1.18 * np.sin(rad), txt, fontsize=10.5, weight="bold",
           color=TXT, ha="center", va="center")

# ---------------- 3. sentido de contagem -------------------------------------
a = ax[1, 0]
circulo(a, "3. Começa na direita, conta contra o relógio")
a.plot([0, 1.05], [0, 0], color=TXT, lw=2)
a.text(1.1, -0.05, "0°\ninício", fontsize=9.5, color=TXT, ha="left", va="top")
arc = Arc((0, 0), 1.5, 1.5, angle=0, theta1=0, theta2=150, color=VERDE, lw=3)
a.add_patch(arc)
a.annotate("", xy=(0.75 * np.cos(np.radians(150)), 0.75 * np.sin(np.radians(150))),
           xytext=(0.75 * np.cos(np.radians(140)), 0.75 * np.sin(np.radians(140))),
           arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=3))
ponteiro(a, 150, VERDE)
a.text(-1.05, 0.55, "sentido\nanti-horário\n= positivo", fontsize=10, color=VERDE, weight="bold")
a.text(0, -1.3, "sentido do relógio = ângulo negativo", fontsize=10, color=TXT, ha="center")

# ---------------- 4. onde o ponto para ---------------------------------------
a = ax[1, 1]
circulo(a, "4. Cada ângulo aponta para um único lugar")
for deg, cor in [(30, AZUL), (110, LARANJA), (200, ROXO), (320, VERM)]:
    rad = np.radians(deg)
    x, y = np.cos(rad), np.sin(rad)
    a.scatter([x], [y], s=90, color=cor, zorder=6, edgecolor="white", lw=1.5)
    a.text(1.18 * x, 1.18 * y, f"{deg}°", fontsize=10, weight="bold", color=cor, ha="center", va="center")
a.text(0, -1.3, "esse ponto vira 'seno e cosseno'\nna próxima aula", fontsize=10, color=TXT,
       ha="center", style="italic")

fig.suptitle("Aula 3 — Ângulos e o círculo", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "03-angulos-e-o-circulo" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
