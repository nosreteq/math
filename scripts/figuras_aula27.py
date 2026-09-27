# Gera a figura estatica da Aula 27. Pode rodar de qualquer pasta: python scripts/figuras_aula27.py
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

# ---------------- 1. a bolinha desce ---------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. x novo = x − passo · f′(x)")
f = lambda x: 0.5 * (x - 2)**2 + 1
x = np.linspace(-1.5, 6, 200)
a.plot(x, f(x), color=AZUL, lw=3)
xs = [5.5]
for _ in range(6):
    xs.append(xs[-1] - 0.5 * (xs[-1] - 2))
a.plot(xs, [f(v) for v in xs], "o-", color=LARANJA, lw=2, ms=9)
a.set_xlim(-1.5, 6); a.set_ylim(0, 8)

# ---------------- 2. curvas de nivel e gradiente --------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Curvas de nível e a descida pelo gradiente")
X, Y = np.meshgrid(np.linspace(-4.5, 4.5, 200), np.linspace(-4.5, 4.5, 200))
a.contour(X, Y, X**2 + 3 * Y**2, levels=[0.5, 1, 2, 4, 6, 9, 12, 16, 20], cmap="viridis_r", linewidths=1.5)
p = np.array([-3.5, 2.0]); cam = [p]
for _ in range(12):
    p = p - 0.12 * np.array([2 * p[0], 6 * p[1]]); cam.append(p)
cam = np.array(cam)
a.plot(cam[:, 0], cam[:, 1], "o-", color=VERM, lw=2, ms=5)
a.set_aspect("equal"); a.axis("off")

# ---------------- 3. tamanho do passo ---------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Tamanho do passo em f(x) = x²")
x = np.linspace(-4, 4, 200)
a.plot(x, x**2, color=AZUL, lw=3)
for e, cor, rot in [(0.1, VERDE, "passo 0,1: lento"), (0.8, LARANJA, "passo 0,8: zigue-zague"), (1.05, VERM, "passo 1,05: explode")]:
    xs = [3.5]
    for _ in range(8):
        xs.append(xs[-1] * (1 - 2 * e))
    xs = np.array(xs)
    a.plot(xs, xs**2, "o-", color=cor, lw=1.8, ms=5, label=rot)
a.legend(loc="upper center", fontsize=10); a.set_xlim(-4.5, 4.5); a.set_ylim(0, 20)

# ---------------- 4. vale local ---------------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Onde você começa decide onde você para")
f = lambda x: x**4 / 4 - x**2 + 0.3 * x
d = lambda x: x**3 - 2 * x + 0.3
x = np.linspace(-2.4, 2.4, 300)
a.plot(x, f(x), color=AZUL, lw=3)
for x0, cor in [(-0.5, VERDE), (2.0, VERM)]:
    v = x0
    for _ in range(400):
        v -= 0.03 * d(v)
    a.plot(x0, f(x0), "o", color=cor, ms=9); a.plot(v, f(v), "*", color=cor, ms=20)
a.text(-1.48, -2.1, "mínimo global", ha="center", fontsize=11, weight="bold", color=VERDE)
a.text(1.33, -1.25, "mínimo local", ha="center", fontsize=11, weight="bold", color=VERM)
a.set_ylim(-2.4, 3)

fig.suptitle("Aula 27 — Otimização: descer a ladeira", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "27-otimizacao-e-gradiente" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
