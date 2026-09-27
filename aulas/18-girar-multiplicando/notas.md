# Aula 18 — Girar multiplicando

> Estas são as notas em texto da aula. A versão interativa, com os laboratórios e os exercícios
> que se corrigem sozinhos, está em [`index.html`](index.html).

**Você já sabe:** o plano (Aula 2), ângulos (Aula 3), seno e cosseno (Aula 4), a matriz de rotação
(Aula 6), a soma de ondas (Aula 12), a parábola que não cruza o zero (Aula 13), o e (Aula 14) e
radianos (Aula 15).

![Ilustrações da aula 18](figuras.png)

---

## Multiplicar por −1 é girar meia volta

Números como setas: multiplicar por −1 gira 180°. "Que número vezes ele mesmo dá −1?" vira "que
giro, feito duas vezes, dá meia volta?" — **90°**. Esse giro se chama **i**: `i² = −1`.

`1 → i → −1 → −i → 1`. As raízes de −1 são i e −i.

---

## O plano complexo

`a + bi` é o ponto `(a, b)`: parte real na régua deitada, parte imaginária na régua em pé.
Tamanho `√(a² + b²)`, e um ângulo. `3 + 4i`: tamanho 5, ângulo ≈ 53,1°.

---

## Multiplicar = girar e esticar

`(a + bi) · (c + di) = (ac − bd) + (ad + bc)i`

No desenho: **tamanhos multiplicam, ângulos somam**. `(1 + i)² = 1 + 2i + i² = 2i`: tamanho
√2 · √2 = 2, ângulo 45° + 45° = 90°. É a matriz de rotação da Aula 6 num número só.

---

## Potências

`wⁿ`: tamanho `rⁿ`, ângulo `n · θ`. Tamanho > 1: espiral para fora; < 1: para dentro; = 1: gira
no círculo.

---

## A fórmula de Euler

Como `(1 + 1/n)ⁿ → e`, girar um pouquinho n vezes dá `(1 + iθ/n)ⁿ → e^(iθ)`, e o resultado é o
ponto do círculo:

`e^(iθ) = cos θ + i · sen θ` (θ em radianos)

Com θ = π: **`e^(iπ) = −1`**.

---

## Ondas como giros

A altura de um ponto girando é uma onda seno. Setas girando uma na ponta da outra, com velocidades
diferentes, desenham a soma de ondas da Aula 12 — é assim que Fourier é escrito: somas de
`e^(iωt)`.

---

## Afie o lápis

1. `i²`? → **−1**
2. Tamanho de `3 + 4i`? → **5**
3. `(1 + i) · (1 − i)`? → **2**
4. Multiplicar por i? → **gira 90° sem mudar o tamanho**
5. `(2i) · (3i)`? → **−6**
6. `e^(iπ)`? → **−1**
