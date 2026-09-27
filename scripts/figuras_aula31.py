# Gera a figura estatica da Eletiva 1 (aula 31). Pode rodar de qualquer pasta: python scripts/figuras_aula31.py
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

def relogio(a, n, marcas=None, titulo_=""):
    titulo(a, titulo_)
    t = np.linspace(0, 2 * np.pi, 200)
    a.plot(np.cos(t), np.sin(t), color=TXT, lw=2.5)
    for k in range(n):
        ang = np.pi / 2 - 2 * np.pi * k / n
        a.plot(np.cos(ang), np.sin(ang), "o", color=TXT, ms=4)
        a.text(1.18 * np.cos(ang), 1.18 * np.sin(ang), str(k), ha="center", va="center", fontsize=11, weight="bold")
    a.set_xlim(-1.4, 1.4); a.set_ylim(-1.4, 1.4); a.set_aspect("equal"); a.axis("off")


# ---------------- 1. o relogio ------------------------------------------------------------------
a = ax[0, 0]
relogio(a, 12, titulo_="1. 9 + 5 ≡ 2 (mod 12): a conta dá a volta")
for k, cor, L in [(9, CINZA, 0.6), (2, VERM, 0.8)]:
    ang = np.pi / 2 - 2 * np.pi * k / 12
    a.plot([0, L * np.cos(ang)], [0, L * np.sin(ang)], color=cor, lw=5)
s = np.linspace(9, 14, 60)
a.plot(0.9 * np.cos(np.pi / 2 - 2 * np.pi * s / 12), 0.9 * np.sin(np.pi / 2 - 2 * np.pi * s / 12), color=VERDE, lw=3)

# ---------------- 2. tabuada ----------------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. Tabuada do relógio de 10: linhas com um 1 têm inverso")
n = 10
for i in range(n):
    for j in range(n):
        v = i * j % n
        a.add_patch(Rectangle((j, -i), 0.95, 0.95, facecolor=plt.cm.viridis(v / n), edgecolor="#1b1b1b" if v == 1 else "none", lw=2))
        a.text(j + 0.47, -i + 0.47, str(v), ha="center", va="center", fontsize=8, color="white" if v < 5 else TXT)
a.set_xlim(-0.2, 10.2); a.set_ylim(-9.2, 1.1); a.set_aspect("equal"); a.axis("off")

# ---------------- 3. potencias em ciclo -------------------------------------------------------------
a = ax[1, 0]
relogio(a, 7, titulo_="3. Potências de 3 no relógio de 7: 3, 2, 6, 4, 5, 1")
seq = [pow(3, k, 7) for k in range(1, 7)]
pts = [(np.cos(np.pi / 2 - 2 * np.pi * v / 7), np.sin(np.pi / 2 - 2 * np.pi * v / 7)) for v in seq]
for p, q in zip(pts, pts[1:] + pts[:1]):
    a.annotate("", q, p, arrowprops=dict(arrowstyle="-|>", color=ROXO, lw=2))

# ---------------- 4. RSA -----------------------------------------------------------------------------
a = ax[1, 1]
titulo(a, "4. RSA com p = 7, q = 17: n = 119, e = 5, d = 77")
for x, txt, cor in [(0.12, "m = 42", AZUL), (0.5, "c = 77", VERM), (0.88, "m = 42", VERDE)]:
    a.add_patch(Rectangle((x - 0.1, 0.45), 0.2, 0.2, facecolor="white", edgecolor=cor, lw=3))
    a.text(x, 0.55, txt, ha="center", va="center", fontsize=14, weight="bold", color=cor)
for x1, x2, txt in [(0.22, 0.4, "^5 mod 119"), (0.6, 0.78, "^77 mod 119")]:
    a.annotate("", (x2, 0.55), (x1, 0.55), arrowprops=dict(arrowstyle="-|>", color=TXT, lw=2))
    a.text((x1 + x2) / 2, 0.7, txt, ha="center", fontsize=10, weight="bold")
a.text(0.5, 0.25, "público: n = 119, e = 5   ·   secreto: p, q, φ = 96, d = 77", ha="center", fontsize=11, color=ROXO)
a.set_xlim(-0.02, 1.02); a.set_ylim(0, 1); a.axis("off")

fig.suptitle("Eletiva 1 — Aritmética do relógio e criptografia RSA", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "31-aritmetica-do-relogio-e-rsa" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
