# Gera a figura estatica da Aula 7. Pode rodar de qualquer pasta: python scripts/figuras_aula07.py
# -*- coding: utf-8 -*-
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

AZUL, VERM, VERDE, LARANJA, ROXO, CINZA, TXT = ("#2563eb", "#dc2626", "#059669",
                                                 "#d97706", "#7c3aed", "#9ca3af", "#111827")

fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.patch.set_facecolor("white")


def balanca(a, titulo, caixas, pesos_esq, pesos_dir, inclina=0.0):
    a.set_xlim(0, 10); a.set_ylim(0, 7); a.axis("off")
    a.set_title(titulo, fontsize=13.5, weight="bold", color=TXT, pad=10)
    a.add_patch(Polygon([[5, 3], [4.4, 0.6], [5.6, 0.6]], closed=True, facecolor="#c9c1ae", edgecolor=TXT, lw=2))
    yl, yr = 3 - inclina, 3 + inclina
    a.plot([1, 9], [yl, yr], color=TXT, lw=5)
    def prato(x0, y0, itens):
        for i, tipo in enumerate(itens):
            col, lin = i % 5, i // 5
            cor = ROXO if tipo == "x" else LARANJA
            a.add_patch(Rectangle((x0 + col * 0.55, y0 + 0.1 + lin * 0.55), 0.48, 0.48, facecolor=cor, edgecolor=TXT, lw=1))
            if tipo == "x":
                a.text(x0 + col * 0.55 + 0.24, y0 + 0.34 + lin * 0.55, "x", color="white", ha="center", va="center", fontsize=9, weight="bold")
    prato(0.8, yl, ["x"] * caixas + ["p"] * pesos_esq)
    prato(6.3, yr, ["p"] * pesos_dir)


balanca(ax[0, 0], "1. 2 · x + 3 = 11: a balança equilibrada", 2, 3, 11)
balanca(ax[0, 1], "2. Tirei 3 dos dois lados: 2 · x = 8", 2, 0, 8)
balanca(ax[1, 0], "3. Mexi num lado só: a balança entorta", 2, 5, 11, inclina=0.8)

a = ax[1, 1]
a.axis("off")
a.set_title("4. A máquina ao contrário", fontsize=13.5, weight="bold", color=TXT, pad=10)
passos = ["saiu 17 da máquina 3 · x + 2", "desfaço o + 2:  17 − 2 = 15", "desfaço o × 3:  15 ÷ 3 = 5", "entrou o 5  ✔"]
for i, p in enumerate(passos):
    a.text(0.03, 0.85 - i * 0.2, p, fontsize=14, transform=a.transAxes,
           color=VERDE if i == 3 else TXT, weight="bold" if i == 3 else "normal")

fig.suptitle("Aula 7 — Equações: a balança", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "07-equacoes-a-balanca" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
