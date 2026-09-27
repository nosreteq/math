# Gera a figura estatica da Aula 12. Pode rodar de qualquer pasta: python scripts/figuras_aula12.py
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

# ---------------- 1. triangulo = meio retangulo ---------------------------------------------------
a = ax[0, 0]
titulo(a, "1. Triângulo = metade do retângulo")
a.add_patch(Rectangle((0, 0), 6, 4, facecolor="#f3f0e8", edgecolor=CINZA, lw=2, ls="--"))
a.add_patch(Polygon([[0, 0], [6, 0], [2, 4]], closed=True, facecolor=AZUL, alpha=0.35, edgecolor=AZUL, lw=2.5))
a.plot([2, 2], [0, 4], color=VERM, lw=2, ls=":")
a.text(3, -0.6, "base 6", ha="center", fontsize=12, weight="bold"); a.text(2.2, 2, "altura 4", fontsize=12, weight="bold", color=VERM)
a.text(3, 4.5, "área = 6 · 4 ÷ 2 = 12", ha="center", fontsize=13, weight="bold", color=AZUL)
a.set_xlim(-0.5, 6.5); a.set_ylim(-1.2, 5.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. pitagoras ------------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Pitágoras: 3² + 4² = 5²")
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

# ---------------- 3. prova dos 4 triangulos --------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. A prova: (a + b)² menos 4 triângulos = c²")
aa, bb = 3, 4
L = aa + bb
a.add_patch(Rectangle((0, 0), L, L, facecolor="white", edgecolor=TXT, lw=2))
P = [np.array(p) for p in [(aa, 0), (L, aa), (bb, L), (0, bb)]]
cantos = [np.array(p) for p in [(0, 0), (L, 0), (L, L), (0, L)]]
for k in range(4):
    a.add_patch(Polygon([cantos[k], P[k], P[k - 1]], closed=True, facecolor="#fde68a", edgecolor=TXT, lw=1.5))
a.add_patch(Polygon(P, closed=True, facecolor=ROXO, alpha=0.25, edgecolor=ROXO, lw=2.5))
a.text(L / 2, L / 2, "c²", ha="center", va="center", fontsize=18, weight="bold", color=ROXO)
a.set_xlim(-0.5, L + 0.5); a.set_ylim(-0.5, L + 0.5); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. cilindro ------------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Volume da lata = π · r² · h")
t = np.linspace(0, 2 * np.pi, 200)
r, h, e = 2, 4, 0.6
a.fill_between([-r, r], [0, 0], [h, h], color=AZUL, alpha=0.15)
a.plot(r * np.cos(t), e * np.sin(t), color=AZUL, lw=2, ls="--")
a.fill(r * np.cos(t), h + e * np.sin(t), color=AZUL, alpha=0.3)
a.plot(r * np.cos(t), h + e * np.sin(t), color=AZUL, lw=2.5)
a.plot([-r, -r], [0, h], color=AZUL, lw=2.5); a.plot([r, r], [0, h], color=AZUL, lw=2.5)
a.plot([0, r], [h, h], color=VERM, lw=2.5); a.text(r / 2, h + 0.15, "r", fontsize=13, weight="bold", color=VERM)
a.text(r + 0.3, h / 2, "h", fontsize=13, weight="bold", color=VERDE)
a.set_xlim(-3.5, 3.5); a.set_ylim(-1, 5.3); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Aula 12 — Áreas, volumes e Pitágoras", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "12-areas-volumes-e-pitagoras" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
