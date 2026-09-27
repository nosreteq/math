# Aula 14 — Crescimento que acelera

> Estas são as notas em texto da aula. A versão interativa, com os laboratórios e os exercícios
> que se corrigem sozinhos, está em [`index.html`](index.html).

**Você já sabe:** a reta e o passo da escada (Aula 2), potências e raízes (Aula 9).

![Ilustrações da aula 14](figuras.png)

---

## Somar sempre o mesmo × multiplicar sempre pelo mesmo

Somar um valor fixo por passo: **reta**. Multiplicar por um fator fixo: **exponencial**,
`valor = início · fatorⁿ`. O passo da exponencial cresce junto com o valor — por isso ela sempre
acaba passando qualquer reta. Multiplicar por 1,1 a cada ano é render 10% com juros sobre juros.

---

## A dobra do papel

0,1 mm dobrado n vezes: `0,1 · 2ⁿ` mm. 10 dobras ≈ 10 cm; 23 ≈ 840 m; 42 ≈ 440 mil km — passa
da Lua.

> ⚠️ `2ⁿ` não é `2 · n`: `2 · 10 = 20`, mas `2¹⁰ = 1.024`.

---

## A escada das potências

Cada degrau para baixo divide por 2:

`2³ = 8 → 2² = 4 → 2¹ = 2 → 2⁰ = 1 → 2⁻¹ = ½ → 2⁻² = ¼`

- expoente zero dá 1;
- expoente negativo quer dizer "divida";
- somar expoentes é multiplicar: `2² · 2³ = 2⁵`;
- então `2^0,5 · 2^0,5 = 2`, ou seja, `2^0,5 = √2 ≈ 1,41`.

---

## O logaritmo: a pergunta de volta

"Quantas vezes eu preciso multiplicar?" `log₂ 8 = 3` porque `2³ = 8`; `log₁₀ 1.000 = 3`.
O logaritmo transforma multiplicação em soma: `log(a · b) = log a + log b`. Não existe
logaritmo de zero nem de negativo.

---

## A régua logarítmica

Cada tracinho multiplica pelo mesmo (1, 10, 100, 1.000...). Nela, uma exponencial vira **reta**.

---

## O número e

Juros de 100% ao ano divididos em n pedaços: `(1 + 1/n)ⁿ`. n = 1: 2; n = 2: 2,25; n = 12: 2,61;
n = 365: 2,7146... O total não explode: se aproxima de **e ≈ 2,71828** — o crescimento contínuo.

---

## Pontos importantes

- Reta soma; exponencial multiplica. A exponencial sempre acaba na frente.
- `2⁰ = 1`, `2⁻¹ = ½`, `2^0,5 = √2`.
- Logaritmo = quantas vezes multiplicar.
- Régua logarítmica: exponencial vira reta.
- `(1 + 1/n)ⁿ → e ≈ 2,718`.

---

## Afie o lápis

1. `2⁵`? → **32**
2. `2⁻¹`? → **½**
3. `log₂ 64`? → **6**
4. R$ 1.000 a 10% ao ano, 2 anos, juros compostos? → **R$ 1.210**
5. Bactérias dobrando por hora, a partir de 1: quando passam de 1.000? → **10 horas**
6. A longo prazo, `1.000 · n` ou `2ⁿ`? → **2ⁿ**
