# Gera a figura estatica da Aula 9. Pode rodar de qualquer pasta: python scripts/figuras_aula09.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")

# ---------------- 1. ao quadrado = quadrado ---------------------------------------
a = ax[0, 0]
a.set_title("1. 5² = 25: a área de um quadrado de lado 5", fontsize=13.5, weight="bold", color=TXT, pad=10)
for i in range(5):
    for j in range(5):
        a.add_patch(Rectangle((j, i), 0.92, 0.92, facecolor="#dbeafe", edgecolor=AZUL, lw=1.2))
a.set_xlim(-0.5, 5.5); a.set_ylim(-0.5, 5.5); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. raiz --------------------------------------------------------------
a = ax[0, 1]
a.set_title("2. Raiz: o lado de um quadrado de área dada", fontsize=13.5, weight="bold", color=TXT, pad=10)
for area, x0, cor in [(4, 0, VERDE), (9, 2.6, AZUL), (2, 6.4, ROXO)]:
    l = np.sqrt(area)
    a.add_patch(Rectangle((x0, 0), l, l, facecolor=cor, alpha=0.2, edgecolor=cor, lw=2))
    lbl = f"√{area} = {int(l)}" if l == int(l) else f"√{area} ≈ {l:.2f}".replace(".", ",")
    a.text(x0 + l / 2, -0.5, lbl, ha="center", fontsize=11, color=cor, weight="bold")
a.set_xlim(-0.5, 8.5); a.set_ylim(-1, 4); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. pitagoras ------------------------------------------------------------
a = ax[1, 0]
a.set_title("3. Pitágoras: 3² + 4² = 5²", fontsize=13.5, weight="bold", color=TXT, pad=10)
O, A, B = np.array([0, 0]), np.array([4, 0]), np.array([0, 3])
n = np.array([3, 4])
for pts, cor, txt in [([O, A, A + [0, -4], O + [0, -4]], VERDE, "16"),
                      ([O, B, B + [-3, 0], O + [-3, 0]], VERM, "9"),
                      ([B, A, A + n, B + n], ROXO, "25")]:
    a.add_patch(Polygon(pts, closed=True, facecolor=cor, alpha=0.2, edgecolor=cor, lw=2))
    c = np.mean(pts, axis=0)
    a.text(c[0], c[1], txt, ha="center", va="center", fontsize=14, weight="bold", color=cor)
a.add_patch(Polygon([O, A, B], closed=True, facecolor="#fde68a", edgecolor=TXT, lw=2))
a.set_xlim(-4, 8); a.set_ylim(-5, 8); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. cos² + sen² = 1 -------------------------------------------------------
a = ax[1, 1]
a.set_title("4. No círculo de raio 1: cos² + sen² = 1", fontsize=13.5, weight="bold", color=TXT, pad=10)
t = np.linspace(0, 2 * np.pi, 200)
a.plot(np.cos(t), np.sin(t), color=CINZA, lw=1.5)
ang = np.radians(35)
c, s = np.cos(ang), np.sin(ang)
a.plot([0, c], [0, 0], color=VERDE, lw=4)
a.plot([c, c], [0, s], color=VERM, lw=4)
a.plot([0, c], [0, s], color=ROXO, lw=3)
a.text(c / 2, -0.12, "cosseno", ha="center", color=VERDE, weight="bold")
a.text(c + 0.05, s / 2, "seno", color=VERM, weight="bold")
a.text(c / 2 - 0.15, s / 2 + 0.08, "1", color=ROXO, weight="bold", fontsize=13)
a.set_xlim(-1.2, 1.2); a.set_ylim(-1.2, 1.2); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Aula 9 — Potências, raízes e Pitágoras", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "09-potencias-raizes-e-pitagoras" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
