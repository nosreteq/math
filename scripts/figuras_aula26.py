# Gera a figura estatica da Aula 26. Pode rodar de qualquer pasta: python scripts/figuras_aula26.py
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

z1, z2 = rng.normal(size=200), rng.normal(size=200)
P = np.column_stack([1.6 * z1, 0.8 * z1 + 0.45 * z2])
P -= P.mean(axis=0)
C = np.cov(P.T)
val, vec = np.linalg.eigh(C)
ordem = np.argsort(val)[::-1]; val, vec = val[ordem], vec[:, ordem]

# ---------------- 1. nuvem e componentes ------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. A nuvem e suas direções principais")
a.plot(P[:, 0], P[:, 1], ".", color=AZUL, alpha=0.6, ms=6)
for k, cor in [(0, VERM), (1, VERDE)]:
    v = vec[:, k] * 2 * np.sqrt(val[k])
    a.plot([-v[0], v[0]], [-v[1], v[1]], color=cor, lw=4)
a.set_aspect("equal"); a.set_xlim(-5, 5); a.set_ylim(-4, 4)

# ---------------- 2. variancia explicada ---------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Variância explicada por componente")
f = val / val.sum()
a.bar(["PC1", "PC2"], f * 100, color=[VERM, VERDE], width=0.5)
for i, x in enumerate(f):
    a.text(i, x * 100 + 2, f"{x * 100:.0f}%", ha="center", fontsize=14, weight="bold")
a.set_ylim(0, 110); a.set_yticks([])
for s in a.spines.values():
    s.set_visible(False)

# ---------------- 3. de 2D para 1D ----------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Comprimir: cada ponto vira sua sombra na PC1")
u = vec[:, 0]
S = (P @ u)[:, None] * u
for p, q in zip(P[::3], S[::3]):
    a.plot([p[0], q[0]], [p[1], q[1]], color="#fca5a5", lw=1)
a.plot(P[:, 0], P[:, 1], ".", color=AZUL, alpha=0.4, ms=5)
a.plot(S[:, 0], S[:, 1], ".", color=VERM, ms=6)
a.set_aspect("equal"); a.set_xlim(-5, 5); a.set_ylim(-4, 4)

# ---------------- 4. imagem comprimida ----------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. Imagem 24 × 24 com 1, 3 e 24 componentes")
N = 24
yy, xx = np.mgrid[0:N, 0:N]
x, y = (xx - 11.5) / 11.5, (yy - 11.5) / 11.5
img = np.where(np.hypot(x, y) < 0.95, 0.85, 0.15)
img[(np.hypot(x + 0.38, y + 0.3) < 0.14) | (np.hypot(x - 0.38, y + 0.3) < 0.14)] = 0.1
img[(y > 0.2) & (y < 0.5) & (np.abs(np.hypot(x, y - 0.05) - 0.45) < 0.09)] = 0.1
U, s, Vt = np.linalg.svd(img)
for i, k in enumerate([1, 3, 24]):
    R = (U[:, :k] * s[:k]) @ Vt[:k]
    a.imshow(np.clip(R, 0, 1), cmap="gray", vmin=0, vmax=1, extent=(i * 26, i * 26 + 24, 0, 24))
    a.text(i * 26 + 12, -3, f"k = {k}", ha="center", fontsize=12, weight="bold")
a.set_xlim(-1, 77); a.set_ylim(-6, 25); a.axis("off")

fig.suptitle("Aula 26 — PCA: as direções principais", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "26-pca" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
