# Gera a figura estatica da Aula 20. Pode rodar de qualquer pasta: python scripts/figuras_aula20.py
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

# ---------------- 1. fatias -------------------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Oito fatias debaixo de y = 0,25x² + 1")
f = lambda x: 0.25 * x**2 + 1
w = 0.5
for k in range(8):
    a.add_patch(Rectangle((k * w, 0), w, f(k * w), facecolor=AZUL, alpha=0.22, edgecolor=AZUL))
x = np.linspace(0, 4, 200)
a.plot(x, f(x), color=VERM, lw=3)
a.set_xlim(-0.3, 4.3); a.set_ylim(-0.3, 5.3)

# ---------------- 2. por baixo e por cima ---------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. ∫₀³ x² dx = 9: presa entre as duas somas")
w = 0.5
for k in range(6):
    x0 = k * w
    a.add_patch(Rectangle((x0, 0), w, (x0 + w)**2, fill=False, edgecolor=ROXO, lw=1.5))
    a.add_patch(Rectangle((x0, 0), w, x0**2, facecolor=VERDE, alpha=0.3))
x = np.linspace(0, 3, 200)
a.plot(x, x**2, color=VERM, lw=3)
a.set_xlim(-0.3, 3.3); a.set_ylim(-0.5, 9.6)

# ---------------- 3. velocidade ---------------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Acelerando: distância = triângulo = metade do retângulo")
t = np.linspace(0, 4, 50)
a.fill_between(t[t <= 3], 30 * t[t <= 3], color=LARANJA, alpha=0.35)
a.add_patch(Rectangle((0, 0), 3, 90, fill=False, edgecolor=LARANJA, ls="--", lw=1.5))
a.plot(t, 30 * t, color=AZUL, lw=3)
a.text(1.9, 25, "3 · 90 ÷ 2 = 135 km", fontsize=12, weight="bold", color=TXT)
a.set_xlabel("tempo (h)"); a.set_ylabel("velocidade (km/h)"); a.set_xlim(-0.2, 4.2); a.set_ylim(-5, 125)

# ---------------- 4. acumulado -----------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. O acumulado do cosseno é o seno")
x = np.linspace(0, 2 * np.pi, 300)
a.fill_between(x, np.cos(x), where=np.cos(x) >= 0, color=VERDE, alpha=0.3)
a.fill_between(x, np.cos(x), where=np.cos(x) < 0, color=VERM, alpha=0.25)
a.plot(x, np.cos(x), color=AZUL, lw=2.5, label="curva: cosseno")
a.plot(x, np.sin(x), color=VERDE, lw=3, label="acumulado: seno")
a.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]); a.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
a.legend(loc="lower left"); a.set_ylim(-1.4, 1.4)

fig.suptitle("Aula 20 — A integral", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "20-a-integral" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
