# Gera a figura estatica da Aula 14. Pode rodar de qualquer pasta: python scripts/figuras_aula14.py
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

# ---------------- 1. corrida --------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Somar 100 × dobrar: a exponencial passa")
n = np.arange(0, 14)
a.plot(n, 100 + 100 * n, "o-", color=AZUL, lw=2, label="100 + 100n (reta)")
a.plot(n, 2.0**n, "o-", color=VERM, lw=2, label="2ⁿ (exponencial)")
a.legend(loc="upper left"); a.set_xlim(-0.5, 13.5)

# ---------------- 2. escada ---------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. A escada: cada degrau abaixo divide por 2")
k = np.arange(-3, 5)
a.bar(k, 2.0**k, color="#dbeafe", edgecolor=AZUL)
for kk in k:
    rot = f"{2**kk:g}" if kk >= 0 else f"1/{2**-kk}"
    a.text(kk, 2.0**kk + 0.4, rot, ha="center", fontsize=10.5, weight="bold", color=TXT)
x = np.linspace(-3.4, 4.4, 200)
a.plot(x, 2**x, color=VERM, lw=2, ls="--")
a.set_ylim(-0.5, 18)

# ---------------- 3. logaritmo --------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. O logaritmo: o caminho de volta (log₂ x)")
x = np.linspace(0.05, 20, 300)
a.plot(x, np.log2(x), color=ROXO, lw=3)
for v in [1, 2, 4, 8, 16]:
    a.plot(v, np.log2(v), "o", color=LARANJA, ms=8, mec=TXT)
    a.text(v, np.log2(v) + 0.35, f"log₂ {v} = {int(np.log2(v))}", fontsize=9.5, ha="center")
a.set_xlim(-0.5, 20); a.set_ylim(-3, 5.5)

# ---------------- 4. e ----------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. (1 + 1/n)ⁿ se aproxima de e ≈ 2,718")
ns = np.array([1, 2, 4, 12, 52, 365, 8760])
a.plot(range(len(ns)), (1 + 1 / ns)**ns, "o-", color=AZUL, lw=2, ms=8)
a.axhline(np.e, color=ROXO, ls="--", lw=2)
a.set_xticks(range(len(ns))); a.set_xticklabels([str(v) for v in ns])
a.set_xlabel("pedaços do ano"); a.set_ylim(1.9, 2.85)

fig.suptitle("Aula 14 — Crescimento que acelera", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "14-crescimento-que-acelera" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
