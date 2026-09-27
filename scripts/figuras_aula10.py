# Gera a figura estatica da Aula 10. Pode rodar de qualquer pasta: python scripts/figuras_aula10.py
# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def papel(a, titulo, lim=7):
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim)
    a.axhline(0, color=TXT, lw=1.8); a.axvline(0, color=TXT, lw=1.8)
    a.set_xticks([]); a.set_yticks([])
    a.set_aspect("equal")
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    for s in a.spines.values():
        s.set_visible(False)


xs = np.linspace(-7, 7, 50)

# ---------------- 1. cruzamento ------------------------------------------------
a = ax[0, 0]
papel(a, "1. O cruzamento: onde as duas concordam")
a.plot(xs, 2 * xs + 1, color=AZUL, lw=3, label="f(x) = 2x + 1")
a.plot(xs, -xs + 7, color=LARANJA, lw=3, label="g(x) = −x + 7")
a.scatter([2], [5], s=140, color=ROXO, zorder=6, edgecolor="white", lw=2)
a.text(2.3, 5.3, "(2, 5)", fontsize=12, weight="bold", color=ROXO)
a.legend(fontsize=9.5, loc="upper left", framealpha=0.95)

# ---------------- 2. tres casos --------------------------------------------------
a = ax[0, 1]
papel(a, "2. Uma, nenhuma ou infinitas soluções")
a.plot(xs, xs + 1, color=AZUL, lw=2.5)
a.plot(xs, -0.5 * xs - 1, color=LARANJA, lw=2.5)
a.scatter([-1.33], [-0.33], s=90, color=ROXO, zorder=6, edgecolor="white", lw=1.5)
a.text(-6.6, 5.6, "uma solução", fontsize=10, weight="bold", color=TXT)
a.text(-6.6, -6, "(paralelas: use o laboratório\npara ver retas com o mesmo\npasso nunca se cruzando)",
       fontsize=8.8, color=CINZA)

# ---------------- 3. substituicao -------------------------------------------------
a = ax[1, 0]
a.axis("off")
a.set_title("3. Resolver por substituição", fontsize=13.5, weight="bold", color=TXT, pad=10)
passos = [
    "f(x) = 2x + 1      g(x) = −x + 7",
    "f(x) = g(x):  2x + 1 = −x + 7",
    "3x = 6",
    "x = 2",
    "f(2) = 2·2 + 1 = 5",
    "cruzamento: (2, 5)",
]
for i, p in enumerate(passos):
    a.text(0.02, 0.92 - i * 0.16, p, fontsize=13, color=AZUL if i == len(passos) - 1 else TXT,
           weight="bold" if i == len(passos) - 1 else "normal", transform=a.transAxes)

# ---------------- 4. leia o cruzamento -----------------------------------------------
a = ax[1, 1]
papel(a, "4. Leia o cruzamento no desenho")
a.plot(xs, xs + 2, color=AZUL, lw=3)
a.plot(xs, -xs + 4, color=LARANJA, lw=3)
a.scatter([1], [3], s=140, color=ROXO, zorder=6, edgecolor="white", lw=2)
a.text(1.3, 3.3, "(1, 3)", fontsize=12, weight="bold", color=ROXO)

fig.suptitle("Aula 10 — Sistemas de equações", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "10-sistemas-de-equacoes" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
