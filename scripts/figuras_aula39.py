# Gera a figura estatica da Eletiva 9 (aula 39). Pode rodar de qualquer pasta: python scripts/figuras_aula39.py
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

# ---------------- 1. variacao quadratica ---------------------------------------------------------
a = ax[0, 0]
eixos(a, "1. Σ(ΔW)² gruda em t (e Σ|ΔW| explode)")
N = 8192; dW = rng.normal(0, np.sqrt(1 / N), N); t = np.arange(1, N + 1) / N
a.plot(t, np.cumsum(dW**2), color=ROXO, lw=2.5, label="Σ(ΔW)²")
a.plot([0, 1], [0, 1], color=TXT, ls="--", lw=1.5, label="y = t")
a.legend(fontsize=10)

# ---------------- 2. lema de Ito --------------------------------------------------------------------
a = ax[0, 1]
eixos(a, "2. W² − 2∫W dW = t (o termo de Itô)")
W = np.concatenate([[0], np.cumsum(dW)]); ito = np.concatenate([[0], np.cumsum(2 * W[:-1] * dW)])
tt = np.arange(N + 1) / N
a.plot(tt, W**2, color=AZUL, lw=2, label="W²")
a.plot(tt, ito, color=LARANJA, lw=2, label="2∫W dW")
a.plot(tt, W**2 - ito, color=VERDE, lw=3, label="diferença")
a.legend(fontsize=10)

# ---------------- 3. browniano geometrico ---------------------------------------------------------------
a = ax[1, 0]
eixos(a, "3. Preços: média e^(μt) × mediana e^((μ − σ²/2)t)")
mu, sg, T, n = 0.08, 0.3, 5, 500
tt = np.linspace(0, T, n + 1)
for _ in range(25):
    Wp = np.concatenate([[0], np.cumsum(rng.normal(0, np.sqrt(T / n), n))])
    a.plot(tt, 100 * np.exp((mu - sg**2 / 2) * tt + sg * Wp), lw=1, alpha=0.7)
a.plot(tt, 100 * np.exp(mu * tt), color=TXT, lw=2.5, ls="--")
a.plot(tt, 100 * np.exp((mu - sg**2 / 2) * tt), color=VERM, lw=2.5, ls=":")
a.set_ylim(0, 350)

# ---------------- 4. opcao ------------------------------------------------------------------------------
a = ax[1, 1]
eixos(a, "4. Opção de compra: pagamento max(S − K, 0), K = 105")
S = np.linspace(30, 220, 400); r, sg, K = 0.05, 0.25, 105
m, v = np.log(100) + (r - sg**2 / 2), sg**2
dens = np.exp(-(np.log(S) - m)**2 / (2 * v)) / (S * np.sqrt(2 * np.pi * v))
a.fill_between(S, 60 * dens / dens.max(), color="#bfdbfe")
a.plot(S, np.maximum(S - K, 0), color=VERM, lw=3)
a.axvline(K, color=TXT, ls=":")
a.set_ylim(-3, 100)

fig.suptitle("Eletiva 9 — Cálculo estocástico: a integral do acaso", fontsize=18, weight="bold", color=TXT)
fig.tight_layout(rect=[0, 0, 1, 0.955])
saida = Path(__file__).resolve().parent.parent / "aulas" / "39-calculo-estocastico" / "figuras.png"
fig.savefig(saida, dpi=150, facecolor="white")
print(f"Salvo em: {saida}")
