# Gera a figura estatica da Aula 3. Pode rodar de qualquer pasta: python scripts/figuras_aula03.py
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

# ---------------- 1. porcentagem ----------------------------------------------------------------
a = ax[0, 0]
titulo(a, "1. 35% = 35 de cada 100")
for n in range(100):
    lin, col = n // 10, n % 10
    a.add_patch(Rectangle((col, -lin), 0.9, 0.9, facecolor=AZUL if n < 35 else "#f3f0e8", alpha=0.75 if n < 35 else 1,
                          edgecolor="#d6d0c2", lw=1))
a.set_xlim(-0.3, 10.2); a.set_ylim(-9.4, 1.2); a.set_aspect("equal"); a.axis("off")

# ---------------- 2. aumento x desconto ------------------------------------------------------------
a = ax[0, 1]
titulo(a, "2. +10% e depois −10% não volta a 100")
vals = [100, 110, 99]
a.bar([0, 1, 2], vals, color=[CINZA, VERDE, VERM], width=0.6)
for i, v in enumerate(vals):
    a.text(i, v + 2, f"R$ {v}", ha="center", fontsize=13, weight="bold", color=TXT)
a.set_xticks([0, 1, 2], ["preço", "+10%", "−10%"], fontsize=12)
a.set_ylim(0, 125); a.set_yticks([])
for s in a.spines.values():
    s.set_visible(False)

# ---------------- 3. direta -------------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Diretas: dobra uma, dobra a outra")
x = np.arange(0, 7)
a.plot(x, 4 * x, "o-", color=AZUL, lw=3, ms=8)
a.set_xlabel("kg de maçã", fontsize=12); a.set_ylabel("preço (R$)", fontsize=12)
a.set_xlim(-0.3, 6.5); a.set_ylim(-1, 26)

# ---------------- 4. inversa ------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Inversas: dobra uma, a outra cai à metade")
v = np.linspace(20, 120, 200)
a.plot(v, 240 / v, color=VERM, lw=3)
for vv in [30, 60, 120]:
    a.plot(vv, 240 / vv, "o", color=VERM, ms=9)
    a.text(vv + 3, 240 / vv + 0.4, f"{vv} km/h → {240 / vv:g} h", fontsize=11, color=TXT)
a.set_xlabel("velocidade (km/h)", fontsize=12); a.set_ylabel("tempo para 240 km (h)", fontsize=12)
a.set_xlim(0, 130); a.set_ylim(0, 13)

fig.suptitle("Aula 3 — Porcentagem, razão e regra de três", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "03-porcentagem-razao-e-regra-de-tres" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
