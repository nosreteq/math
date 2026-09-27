# Gera a figura estatica da Aula 12. Pode rodar de qualquer pasta: python scripts/figuras_aula12.py
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
xs = np.linspace(0, 720, 400)


def onda(a, titulo, ylim=2.2):
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    a.axhline(0, color=TXT, lw=1.5)
    a.set_ylim(-ylim, ylim); a.set_xlim(0, 720)
    a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values():
        s.set_visible(False)


# ---------------- 1. montar a onda complicada -----------------------------------
a = ax[0, 0]
onda(a, "1. Somando notas simples")
y1 = np.sin(np.radians(xs))
y2 = 0.6 * np.sin(np.radians(2 * xs))
y3 = 0.3 * np.sin(np.radians(3 * xs))
a.plot(xs, y1, color=VERDE, lw=1.5, ls="--", alpha=.8, label="freq. 1")
a.plot(xs, y2, color=AZUL, lw=1.5, ls="--", alpha=.8, label="freq. 2")
a.plot(xs, y3, color=LARANJA, lw=1.5, ls="--", alpha=.8, label="freq. 3")
a.plot(xs, y1 + y2 + y3, color=ROXO, lw=3, label="soma")
a.legend(fontsize=8.5, loc="upper right", framealpha=0.95)

# ---------------- 2. espectro ------------------------------------------------------
a = ax[0, 1]
a.set_title("2. O espectro: quanto tem de cada frequência", fontsize=13.5, weight="bold", color=TXT, pad=10)
freqs = [1, 2, 3]
amps = [1.0, 0.6, 0.3]
cores = [VERDE, AZUL, LARANJA]
a.bar(freqs, amps, color=cores, width=0.5, edgecolor=TXT, linewidth=1.5)
a.set_xticks(freqs); a.set_xticklabels(["freq. 1", "freq. 2", "freq. 3"], fontsize=10)
a.set_yticks([])
a.set_ylim(0, 1.3)
for s in ["top", "right", "left"]:
    a.spines[s].set_visible(False)

# ---------------- 3. acorde de piano -------------------------------------------------
a = ax[1, 0]
a.axis("off")
a.set_title("3. Um acorde: três notas, uma soma", fontsize=13.5, weight="bold", color=TXT, pad=10)
for i, (cor, y0) in enumerate(zip([VERDE, AZUL, LARANJA], [0.75, 0.55, 0.35])):
    xs2 = np.linspace(0.15, 0.85, 200)
    ys2 = y0 + 0.06 * np.sin(2 * np.pi * (i + 1) * (xs2 - 0.15) / 0.2)
    a.plot(xs2, ys2, color=cor, lw=2.5, transform=a.transAxes)
a.text(0.5, 0.1, "três ondas separadas,\ntocando ao mesmo tempo,\nsoam como uma coisa só",
       fontsize=12, ha="center", color=TXT, transform=a.transAxes)

# ---------------- 4. decompor de volta --------------------------------------------------
a = ax[1, 1]
onda(a, "4. Decompor: achar as notas escondidas")
y_alvo = 0.7 * np.sin(np.radians(xs)) + 0.5 * np.sin(np.radians(2 * xs))
a.plot(xs, y_alvo, color=CINZA, lw=3, ls="--", label="onda misteriosa")
a.plot(xs, y_alvo, color=ROXO, lw=2, alpha=0.01)
a.text(360, 1.8, "freq. 1 = 0,7\nfreq. 2 = 0,5", fontsize=11, color=TXT, ha="center",
       bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=CINZA))
a.legend(fontsize=8.5, loc="lower right", framealpha=0.95)

fig.suptitle("Aula 12 — Decomposição de sinais em ondas", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "12-decomposicao-de-sinais-em-ondas" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
