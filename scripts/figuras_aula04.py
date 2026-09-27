# Gera a figura estatica da Aula 4. Pode rodar de qualquer pasta: python scripts/figuras_aula04.py
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

# ---------------- 3. ao cubo = cubo ----------------------------------------------------------
a = ax[1, 0]
a.set_title("3. 2³ = 8: o volume de um cubo de lado 2", fontsize=13.5, weight="bold", color=TXT, pad=10)
ex, ey, ez = np.array([0.87, -0.5]), np.array([-0.87, -0.5]), np.array([0, 1])


def cubinho(x, y, z):
    o = x * ex + y * ey + z * ez
    topo = [o + ez, o + ez + ex, o + ez + ex + ey, o + ez + ey]
    frente = [o + ex, o + ex + ey, o + ex + ey + ez, o + ex + ez]
    lado = [o + ey, o + ex + ey, o + ex + ey + ez, o + ey + ez]
    for pts, cor in [(topo, "#bfdbfe"), (frente, "#93c5fd"), (lado, "#60a5fa")]:
        a.add_patch(Polygon(pts, closed=True, facecolor=cor, edgecolor=AZUL, lw=1.5))


# pinta de tras para a frente: z crescente, depois x e y crescentes
for z in range(2):
    for x in range(2):
        for y in range(2):
            cubinho(x, y, z)
a.text(0, -2.6, "2 · 2 · 2 = 8 cubinhos", ha="center", fontsize=13, weight="bold", color=AZUL)
a.set_xlim(-3, 3); a.set_ylim(-3, 3); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. x, x² e x³ ---------------------------------------------------------------
a = ax[1, 1]
a.set_title("4. x, x² e x³: antes de 1 encolhem, depois disparam", fontsize=13.5, weight="bold", color=TXT, pad=10)
x = np.linspace(0, 2, 200)
for k, cor, rot in [(1, VERDE, "x"), (2, AZUL, "x²"), (3, VERM, "x³")]:
    a.plot(x, x**k, color=cor, lw=3, label=rot)
a.axvline(1, color=CINZA, ls="--", lw=1.5)
a.set_xlim(0, 2); a.set_ylim(0, 5); a.grid(True, color="#ece7da"); a.legend(loc="upper left", fontsize=12)
for s_ in a.spines.values():
    s_.set_visible(False)

fig.suptitle("Aula 4 — Potências e raízes", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "04-potencias-e-raizes" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
