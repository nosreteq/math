# Gera a figura estatica da Aula 18. Pode rodar de qualquer pasta: python scripts/figuras_aula18.py
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

# ---------------- 1. vezes i ------------------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Multiplicar por i gira 90°: 2 → 2i → −2 → −2i")
for (x, y), cor in zip([(2, 0), (0, 2), (-2, 0), (0, -2)], [ROXO, AZUL, VERM, VERDE]):
    a.annotate("", (x, y), (0, 0), arrowprops=dict(arrowstyle="-|>", color=cor, lw=3))
a.add_patch(Circle((0, 0), 2, fill=False, ls="--", color=CINZA))
a.set_xlim(-3, 3); a.set_ylim(-3, 3); a.set_aspect("equal")

# ---------------- 2. plano complexo ------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. 3 + 4i é o ponto (3, 4): tamanho 5")
a.plot([0, 3], [0, 0], color=VERDE, lw=3, ls="--")
a.plot([3, 3], [0, 4], color=VERM, lw=3, ls="--")
a.annotate("", (3, 4), (0, 0), arrowprops=dict(arrowstyle="-|>", color=ROXO, lw=3))
a.text(1.1, 2.4, "5", fontsize=14, weight="bold", color=ROXO)
a.set_xlim(-1, 5); a.set_ylim(-1, 5); a.set_aspect("equal")

# ---------------- 3. girar e esticar -------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. × w (tamanho 1,5, ângulo 45°): gira e estica")
casa = np.array([0.5, 1.5, 1.5 + 0.8j, 1 + 1.3j, 0.5 + 0.8j])
w = 1.5 * np.exp(1j * np.pi / 4)
for pts, cor in [(casa, CINZA), (casa * w, AZUL)]:
    a.add_patch(Polygon(np.c_[pts.real, pts.imag], closed=True, facecolor=cor, alpha=0.25, edgecolor=cor, lw=2))
a.set_xlim(-2, 3); a.set_ylim(-1, 3.5); a.set_aspect("equal")

# ---------------- 4. euler --------------------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. (1 + iθ/n)ⁿ → e^(iθ) = cos θ + i sen θ")
a.add_patch(Circle((0, 0), 1, fill=False, color=ROXO, lw=2))
t = 2 * np.pi / 3
for n, cor in [(2, CINZA), (8, LARANJA), (64, VERDE)]:
    z = np.cumprod(np.r_[1, np.full(n, 1 + 1j * t / n)])
    a.plot(z.real, z.imag, color=cor, lw=2, marker="o" if n < 10 else None, ms=4, label=f"n = {n}")
a.plot(np.cos(t), np.sin(t), "o", color=ROXO, ms=10)
a.legend(loc="lower left"); a.set_xlim(-1.8, 1.6); a.set_ylim(-1.2, 2.3); a.set_aspect("equal")

fig.suptitle("Aula 18 — Girar multiplicando", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "18-girar-multiplicando" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
