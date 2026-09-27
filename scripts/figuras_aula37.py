# Gera a figura estatica da Eletiva 7 (aula 37). Pode rodar de qualquer pasta: python scripts/figuras_aula37.py
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

# ---------------- 1. barra esfriando ------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Calor: um degrau vira curva lisa e baixa")
N = 81; x = np.linspace(0, 1, N); u = ((x > 0.3) & (x < 0.7)).astype(float); dx = 1 / (N - 1); r = 0.4
a.plot(x, u, color=CINZA, ls="--", lw=2)
for passos, cor in [(80, VERM), (400, LARANJA), (1600, ROXO), (4000, AZUL)]:
    v = u.copy()
    for _ in range(passos):
        v[1:-1] = v[1:-1] + r * (v[:-2] - 2 * v[1:-1] + v[2:])
    a.plot(x, v, color=cor, lw=2.5, label=f"t = {passos * r * dx * dx:.3f}".replace(".", ","))
a.legend(fontsize=10); a.set_ylim(-0.05, 1.1)

# ---------------- 2. instavel ------------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. Mesmo método, r = 0,45 (estável) × r = 0,55 (explode)")
for r, cor in [(0.45, AZUL), (0.55, VERM)]:
    v = np.zeros(21); v[10] = 1
    for _ in range(40):
        v[1:-1] = v[1:-1] + r * (v[:-2] - 2 * v[1:-1] + v[2:])
    a.plot(range(21), np.clip(v, -1.2, 1.2), "o-", color=cor, lw=2)
a.set_ylim(-1.3, 1.3)

# ---------------- 3. corda beliscada -----------------------------------------------------------------
def ext(f, x):
    x = np.mod(x, 2); return np.where(x <= 1, f(x), -f(2 - x))
a = ax[1, 0]
eixos(a, "3. Corda beliscada em 0,3: a forma viaja e volta")
f = lambda x: np.where(x < 0.3, 0.6 * x / 0.3, 0.6 * (1 - x) / 0.7)
x = np.linspace(0, 1, 400)
for t, cor in [(0, CINZA), (0.2, AZUL), (0.5, VERDE), (1.0, VERM)]:
    a.plot(x, 0.5 * (ext(f, x - t) + ext(f, x + t)), color=cor, lw=2.5, ls="--" if t == 0 else "-", label=f"t = {t:g}".replace(".", ","))
a.legend(fontsize=10); a.set_ylim(-0.8, 0.8)

# ---------------- 4. modos normais ----------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Os primeiros modos normais sen(nπx)")
for n, cor in [(1, AZUL), (2, VERDE), (3, LARANJA), (4, ROXO)]:
    a.plot(x, np.sin(n * np.pi * x) - 2.4 * (n - 1), color=cor, lw=3)
    a.text(1.02, -2.4 * (n - 1), f"{110 * n} Hz", va="center", fontsize=11, weight="bold", color=cor)
a.set_xlim(0, 1.2); a.set_ylim(-8.5, 1.3); a.set_yticks([])

fig.suptitle("Eletiva 7 — Calor e ondas: equações diferenciais parciais", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "37-calor-e-ondas-edp" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
