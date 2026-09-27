# Aula 9 — Estatística com vetores

> Estas são as notas em texto da aula. A versão interativa, com os laboratórios e os exercícios
> que se corrigem sozinhos, está em [`index.html`](index.html).

**No nível 1:** vetor é uma seta (Aula 6), e o produto escalar conta uma história sobre o ângulo
entre duas setas.

![Ilustrações da aula 9](figuras.png)

---

## Uma lista de números é um vetor

Uma lista de números pareados — por exemplo, a nota de 5 provas — pode ser vista como um vetor de
5 coordenadas. Não dá mais para desenhar a seta no papel, mas a ideia continua a mesma.

---

## Duas listas, dois vetores, um ângulo

Se eu tenho duas listas relacionadas, cada lista vira um vetor. O **ângulo entre esses dois
vetores** conta o quanto elas "andam juntas".

> Vetores apontando quase para o mesmo lado → as listas sobem e descem juntas. Vetores apontando
> para lados opostos → quando uma sobe, a outra desce.

---

## Reencontro com o produto escalar

A correlação usa a mesma conta da Aula 6: primeiro cada lista é **centralizada** (subtrai-se a
média dela mesma), depois calcula-se o produto escalar entre elas, dividido pelos tamanhos das
duas setas.

```
correlação = cosseno do ângulo entre os vetores (depois de centralizar)
```

Por isso a correlação sempre vive entre **−1 e 1** — ela é, literalmente, um cosseno (Aula 4).

---

## Lendo o valor da correlação

- **perto de 1:** forte e positiva — quando uma sobe, a outra sobe junto.
- **perto de 0:** praticamente nenhuma relação linear.
- **perto de −1:** forte e negativa — quando uma sobe, a outra desce.

Correlação alta **não** prova que uma coisa causa a outra — só mostra que andam juntas.

---

## Pontos importantes

- Uma lista de números pareados vira um **vetor**.
- Duas listas relacionadas → dois vetores; o **ângulo** entre eles conta a história.
- **Correlação = cosseno do ângulo** entre os vetores centralizados.
- Vive sempre entre **−1 e 1** — porque é literalmente um cosseno.
- Perto de 1: andam juntas. Perto de 0: sem relação linear. Perto de −1: andam opostas.
- Correlação não é prova de causa — só mede o "andam juntas".

---

## Exercícios

**1.** A correlação entre duas listas é, na essência, o quê?

**2.** Por que a correlação nunca passa de 1?

**3.** Duas listas têm correlação −1. Que ângulo isso representa entre os vetores?

**4.** Duas variáveis têm correlação alta. Isso prova que uma causa a outra?

**5.** O ângulo entre dois vetores de dados é 0°. Qual é a correlação?

**6.** Uma nuvem de pontos parece completamente espalhada. A correlação está perto de quê?

<details>
<summary>Respostas</summary>

1. **O cosseno do ângulo** entre os dois vetores (depois de centralizar).
2. Porque ela **é um cosseno**, e cosseno nunca passa de 1.
3. **180°**.
4. **Não** — só mostra que andam juntas, não o motivo.
5. **1**.
6. Perto de **0**.

</details>

---

**Aula anterior:** [Decomposição de sinais em ondas](../08-decomposicao-de-sinais-em-ondas/)
**Próxima aula:** projeção e mínimos quadrados — a regressão como geometria de sombra.
