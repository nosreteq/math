# Aula 13 — Curvas que não são retas

> Estas são as notas em texto da aula. A versão interativa, com os laboratórios e os exercícios
> que se corrigem sozinhos, está em [`index.html`](index.html).

**Você já sabe:** máquinas e gráficos (Aula 1), a receita da reta (Aula 2), esticar e deslocar
(Aula 5), a balança (Aula 7) e o quadrado que nunca é negativo (Aula 9).

![Ilustrações da aula 13](figuras.png)

---

## A máquina que dobra

`f(x) = x²`: `f(1) = 1`, `f(2) = 4`, `f(3) = 9`, e `f(−2) = 4` também. Marcando os pontos aparece
uma curva em U, simétrica: a **parábola**.

---

## As mesmas transformações de sempre

`y = a · (x − h)² + k`

- **a** estica (negativo: de cabeça para baixo); com `a = 0` sobra uma reta deitada;
- **h** desloca para o lado (o "atraso" da Aula 5);
- **k** levanta ou abaixa (o "somar na saída" das Aulas 1 e 2).

O ponto da dobra, o **vértice**, fica em `(h, k)`.

> ⚠️ `x²` não é `2x`: com x = 3, `3² = 9` e `2 · 3 = 6`.

---

## Onde a parábola cruza o zero

Resolver `y = 0` é uma equação do 2º grau — e a balança resolve:

```
(x − 1)² − 4 = 0
(x − 1)² = 4
x − 1 = 2   ou   x − 1 = −2
x = 3       ou   x = −1
```

**Abrir os parênteses** é área de retângulo (Aula 9): cada pedaço de um lado vezes cada pedaço
do outro. `(x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6`; com sinais,
`(x − 1)(x − 1) = x² − x − x + 1 = x² − 2x + 1` (menos vezes menos dá mais).

A raiz tem **dois lados**, porque `(−2)² = 4` também. Se sobrar "quadrado = negativo", a parábola
não cruza o zero. `x² − 2x − 3` é o mesmo que `(x − 1)² − 4`: a fórmula de Bhaskara é só essa
arrumação feita uma vez para todos os casos.

---

## O vértice como "melhor valor"

20 m de cerca, lados `x` e `10 − x`: área `x · (10 − x) = 10x − x²`. Zera em 0 e 10; o topo fica no meio,
`x = 5`, área 25 m². O vértice está sempre na média dos dois zeros.

---

## Polinômios

`y = d + c·x + b·x² + a·x³`. A maior potência é o **grau**. Grau 1: reta. Grau 2: uma dobra.
Grau 3: até duas. Cada grau a mais permite uma dobra a mais.

---

## Reta ou curva? O teste das diferenças

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `2x + 1` | 1 | 3 | 5 | 7 | 9 |
| diferenças | | 2 | 2 | 2 | 2 |
| `x²` | 0 | 1 | 4 | 9 | 16 |
| diferenças | | 1 | 3 | 5 | 7 |
| dif. das dif. | | | 2 | 2 | 2 |

Reta: diferenças iguais. Parábola: diferenças das diferenças iguais.

---

## Pontos importantes

- `x²` na máquina faz o gráfico dobrar: a parábola.
- `y = a(x − h)² + k`: vértice em `(h, k)`.
- Cruzar o zero = balança; a raiz tem dois lados.
- O vértice é o melhor valor e fica no meio dos zeros.
- Polinômio = soma de potências; grau n permite até n − 1 dobras.

---

## Afie o lápis

1. `f(x) = x² − 1`. Quanto vale `f(3)`? → **8**
2. Vértice de `y = (x − 2)² + 1`? → **(2, 1)**
3. Maior solução de `(x − 1)² = 9`? → **4** (a outra é −2)
4. `y = x² + 5` cruza o eixo? → **Não**: é sempre pelo menos 5.
5. Maior área com 12 m de cerca? → **9 m²** (quadrado 3 × 3)
6. Tabela 1, 2, 5, 10: que desenho? → **Parábola** (dif. 1, 3, 5; dif. das dif. 2, 2)
