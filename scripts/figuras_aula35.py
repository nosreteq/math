# Gera a figura estatica da Eletiva 5 (aula 35). Pode rodar de qualquer pasta: python scripts/figuras_aula35.py
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

# ---------------- 1. circulo osculador --------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. O círculo osculador de y = x²/2 em x = 1")
x = np.linspace(-3, 3, 300)
a.plot(x, x**2 / 2, color=AZUL, lw=3)
x0 = 1.0; d = x0; dd = 1; k = dd / (1 + d * d)**1.5; R = 1 / k
nx, ny = -d / np.sqrt(1 + d * d), 1 / np.sqrt(1 + d * d)
cx, cy = x0 + R * nx, 0.5 + R * ny
t = np.linspace(0, 2 * np.pi, 200)
a.plot(cx + R * np.cos(t), cy + R * np.sin(t), color=ROXO, lw=2)
a.plot(x0, 0.5, "o", color=VERM, ms=9)
a.text(-2.8, 3.6, f"κ = {k:.3f} → R = {R:.2f}".replace(".", ","), fontsize=12, color=ROXO, weight="bold")
a.set_xlim(-3, 3); a.set_ylim(-0.5, 4); a.set_aspect("equal")

# ---------------- 2. bola, sela, cano ----------------------------------------------------------------
for idx, (k1, k2, nome) in enumerate([(0.8, 0.8, "bola: K > 0"), (0.8, -0.8, "sela: K < 0")]):
    a = fig.add_subplot(2, 4, 3 + idx, projection="3d")
    ax[0, 1].axis("off")
    X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 25), np.linspace(-1.5, 1.5, 25))
    a.plot_surface(X, Y, (k1 * X**2 + k2 * Y**2) / 2, cmap="coolwarm", linewidth=0, alpha=0.9)
    a.set_title(nome, fontsize=12, weight="bold"); a.set_axis_off()

# ---------------- 3. triangulo na esfera -----------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. Na esfera: 90° + 90° + 90° = 270°")
t = np.linspace(0, 2 * np.pi, 200)
a.plot(np.cos(t), np.sin(t), color=TXT, lw=2)
a.plot(np.cos(t), 0.3 * np.sin(t), color=CINZA, lw=1.2, ls="--")
tri = [(0, 0.95), (-0.72, -0.2), (0.72, -0.2)]
u = np.linspace(0, 1, 40)
arcs = [np.column_stack([-0.72 * u, 0.95 - 1.15 * u**0.8]), np.column_stack([-0.72 + 1.44 * u, -0.2 - 0.12 * np.sin(np.pi * u)]), np.column_stack([0.72 * (1 - u), -0.2 + 1.15 * u**1.25])]
poly = np.vstack(arcs)
a.add_patch(Polygon(poly, closed=True, facecolor="#fde68a", edgecolor=LARANJA, lw=2.5))
for (x, y) in tri:
    a.plot(x, y, "o", color=VERM, ms=8)
a.set_xlim(-1.2, 1.2); a.set_ylim(-1.2, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 4. Mercator ----------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Mercator: círculos iguais na Terra incham no mapa")
merc = lambda lat: np.log(np.tan(np.pi / 4 + np.radians(lat) / 2))
for lat in range(0, 80, 15):
    a.axhline(merc(lat), color="#bfdbfe", lw=1)
for i, lat in enumerate([0, 30, 50, 65, 75]):
    r = np.radians(8) / np.cos(np.radians(lat))
    a.add_patch(Circle((i * 0.7, merc(lat)), r, facecolor="#fecaca", edgecolor=VERM, lw=1.5))
    a.text(i * 0.7, merc(lat) - r - 0.12, f"{lat}°", ha="center", fontsize=10)
a.set_xlim(-0.5, 3.4); a.set_ylim(-0.4, 2.5); a.set_aspect("equal"); a.axis("off")

fig.suptitle("Eletiva 5 — Curvas e superfícies: curvatura", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "35-curvatura" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
