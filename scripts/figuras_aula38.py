# Gera a figura estatica da Eletiva 8 (aula 38). Pode rodar de qualquer pasta: python scripts/figuras_aula38.py
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

def koch(p, q, n):
    if n == 0: return [p, q]
    p, q = np.array(p, float), np.array(q, float); d = (q - p) / 3
    c, s = np.cos(-np.pi / 3), np.sin(-np.pi / 3)
    p1, p3 = p + d, p + 2 * d; p2 = p1 + np.array([d[0] * c - d[1] * s, d[0] * s + d[1] * c])
    out = []
    for i, (u, v) in enumerate([(p, p1), (p1, p2), (p2, p3), (p3, q)]):
        k = koch(u, v, n - 1); out += k if i == 0 else k[1:]
    return out


# ---------------- 1. floco de Koch -------------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. Floco de Koch: perímetro infinito, área 8/5")
V = [np.array([np.cos(np.pi / 2 + 2 * np.pi * k / 3), np.sin(np.pi / 2 + 2 * np.pi * k / 3)]) for k in range(3)]
pts = []
for k in range(3):
    seg = koch(V[k], V[(k + 1) % 3], 5); pts += seg if k == 0 else seg[1:]
pts = np.array(pts)
a.fill(pts[:, 0], pts[:, 1], color="#dbeafe", ec=AZUL, lw=0.8)
a.set_aspect("equal"); a.axis("off")

# ---------------- 2. jogo do caos -----------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Jogo do caos: 30.000 pulos ao ponto médio")
C = np.array([[0.5, 0.87], [0, 0], [1, 0]]); p = np.array([0.3, 0.3]); P = []; cs = []
esc = rng.integers(0, 3, 30000)
for i in esc:
    p = (p + C[i]) / 2; P.append(p); cs.append(i)
P = np.array(P)
a.scatter(P[:, 0], P[:, 1], s=0.3, c=np.array([VERM, AZUL, VERDE])[cs])
a.set_aspect("equal"); a.axis("off")

# ---------------- 3. dimensoes -----------------------------------------------------------------------------
a = ax[1, 0]
titulo(a, "3. D = log N / log(1/r)")
formas = [("segmento", 3, 3), ("quadrado", 9, 3), ("Cantor", 2, 3), ("Koch", 4, 3), ("Sierpinski", 3, 2), ("tapete", 8, 3)]
Ds = [np.log(n) / np.log(i) for _, n, i in formas]
a.barh([f[0] for f in formas], Ds, color=[CINZA, CINZA, AZUL, AZUL, AZUL, AZUL])
for k, d in enumerate(Ds):
    a.text(d + 0.03, k, f"{d:.3f}".replace(".", ","), va="center", fontsize=11)
a.set_xlim(0, 2.3); a.invert_yaxis()
for s in a.spines.values():
    s.set_visible(False)

# ---------------- 4. Mandelbrot ---------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. O conjunto de Mandelbrot")
X, Y = np.meshgrid(np.linspace(-2.25, 0.75, 450), np.linspace(-1.25, 1.25, 375))
Cc = X + 1j * Y; Z = np.zeros_like(Cc); it = np.zeros(Cc.shape)
for k in range(60):
    viva = np.abs(Z) <= 2
    Z[viva] = Z[viva]**2 + Cc[viva]; it[viva] += 1
a.imshow(np.where(it >= 60, 0, it), extent=(-2.25, 0.75, -1.25, 1.25), cmap="magma", origin="lower")
a.axis("off")

fig.suptitle("Eletiva 8 — Fractais e dimensão", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "38-fractais-e-dimensao" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
