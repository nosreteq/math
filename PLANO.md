# Plano do curso

> **Estado:** ✅ fases 1 a 8 concluídas — as **30 aulas** da trilha e as **10 eletivas** estão
> publicadas, com as peças novas da metodologia. Próxima etapa: a fase 9, **testes unitários em todas
> as aulas** ([veja o plano](#fase-9--testes-unitários-em-todas-as-aulas)). A coluna **Estado** das
> tabelas registra de onde cada aula veio na [migração](#migração-das-18-aulas-publicadas).

## Objetivo

Ensinar **toda a matemática da escola até a faculdade** — do "sei somar, subtrair, multiplicar e
dividir" até cálculo, álgebra linear, probabilidade, equações diferenciais e o jeito de pensar de
quem pesquisa matemática — **sem pular nenhum degrau e sem decorar nada**.

O curso segue a **ordem da escola** (Ensino Fundamental → Ensino Médio → Faculdade), porque é a
ordem em que os conceitos de fato dependem uns dos outros, e porque o aluno se reconhece nela. Os
**nomes dos níveis** vêm da trilha de referência — **Básico, Intermediário, Avançado, Especialista e
Pesquisador** —, e a etapa da escola aparece ao lado de cada um como referência. O
que muda é o **jeito de ensinar**: em vez de lista de fórmulas, cada ideia chega por um desenho que
se mexe, uma história e um exercício que explica o erro — a metodologia da série *Head First*, da
O'Reilly.

Três regras valem para as 30 aulas:

1. **Nada é usado antes de ser apresentado** — nem entre níveis. Cada aula abre com "Você já sabe"
   listando de onde vem cada peça.
2. **O desenho vem antes da fórmula.** Primeiro o aluno vê a coisa acontecer num laboratório,
   depois escreve.
3. **Reencontros, não assuntos soltos.** Cada ideia nova é apresentada como uma ideia antiga vista
   de outro jeito (a PA é a reta de passo em passo, a correlação é um cosseno, o número complexo é
   um giro).

---

## Visão geral

| Nível | Etapa da escola | Aulas | Ao terminar, o aluno consegue... |
|---|---|---|---|
| **1 — Básico** | Fundamental I e II | 1–6 | fazer conta com qualquer tipo de número (inteiro, negativo, fração, decimal, porcentagem, potência) e resumir uma lista de dados |
| **2 — Intermediário** | Fundamental II | 7–12 | trocar número por letra, resolver equações e sistemas, desenhar retas e medir figuras no plano e no espaço |
| **3 — Avançado** | Ensino Médio | 13–18 | entender o comportamento das funções clássicas (quadrática, exponencial, trigonométricas), usar vetores e matrizes e girar com números complexos |
| **4 — Especialista** | Faculdade: cálculo e dados | 19–24 | derivar, integrar, medir incerteza com a curva normal e extrair padrões de dados (correlação, regressão, Fourier) |
| **5 — Pesquisador** | Faculdade: matemática aplicada e computacional | 25–30 | modelar sistemas que mudam no tempo, otimizar, trabalhar com acaso ao longo do tempo e demonstrar um resultado |
| **Eletivas** | Aprofundamento | 31–40 | seguir para áreas específicas: criptografia, grafos, grupos, topologia, curvatura, séries, EDPs, fractais, cálculo estocástico e métodos numéricos |

Nas tabelas abaixo, o **Estado** registra de onde veio cada aula (todas já publicadas):

- ✅ **mantida** — já existia; mudou só de número e de referências.
- ♻️ **adaptada** — já existia; foi dividida, ampliada ou juntada com outra.
- 🆕 **nova** — escrita do zero na reestruturação.

---

## Metodologia: a anatomia de toda aula

Inspirada na série *Head First*: o cérebro presta atenção no que é visual, conversado, surpreendente
e feito com as próprias mãos. Toda aula, em todos os níveis, tem:

| Peça | Para quê | Obrigatório |
|---|---|---|
| **Cabeçalho** com "AULA N de 30 · NÍVEL X" e o quadro **Você já sabe** | Mostra de onde vem cada peça usada na aula | sim |
| **Gancho** — um problema ou uma história do mundo real | Dar um motivo antes da teoria | sim |
| **6 laboratórios** 🔧 | Sliders, botões e arrastar: a ideia entra pelas mãos | sim, exatamente 6 |
| **O Guru** 🧘 | Uma frase que arruma a cabeça no momento certo | sim, ao menos 1 |
| **Não existe pergunta idiota** 💬 | As dúvidas que todo mundo tem, respondidas antes | sim, ao menos 1 |
| **Cuidado** ⚠️ | A armadilha clássica, marcada antes da queda | sim, ao menos 1 |
| **Pontos importantes** 📌 | O resumo da aula em uma tela | sim |
| **Afie o lápis** ✏️ | 6 exercícios; errou → explica o porquê; acertou → selo; um deles é o desafio 🏆 | sim, exatamente 6 |
| **Placar** e progresso salvo | Motivação e retomada | sim |
| **notas.md** e **figuras.png** | O mesmo conteúdo para ler, imprimir ou colar num caderno | sim |

Peças que entraram na reestruturação:

| Peça | Para quê | Onde |
|---|---|---|
| **🧠 Poder do cérebro** | Uma pergunta aberta *antes* da explicação: o aluno pensa primeiro | todas as 30 aulas |
| **Por que é verdade?** | Uma mini-demonstração visual (sem formalismo) de um fato da aula | nas aulas com uma demonstração-chave: 8, 11, 12, 14, 27, 28, 29 e 30 |
| **Conversa ao pé da lareira** | Diálogo entre dois conceitos que se confundem | uma por nível (lista abaixo) |
| **Quem faz o quê?** | Exercício de ligar colunas (novo tipo de exercício no motor das aulas) | todas as aulas a partir do Nível 2, e as 1, 2, 3 e 5 |

**Conversas ao pé da lareira** (uma por nível): Média × Mediana (N1) · Equação × Função (N2) ·
Seno × Cosseno (N3) · Derivada × Integral (N4) · Determinístico × Aleatório (N5).

**Critério de qualidade** de cada aula, antes de publicar:

1. `tests/verifica.js` verde: 6 laboratórios, 6 exercícios, controles nos extremos sem `NaN`,
   erro nunca pontua e gabarito sempre é aceito, nenhum erro de JavaScript, nada rolando para o
   lado a 375 px, links válidos.
2. Toda conta citada no texto e nas notas foi conferida numericamente.
3. Nenhuma peça é usada antes de ser apresentada (conferir contra a tabela de pré-requisitos).
4. Nenhum laboratório dá "acertou" sozinho ao carregar a página.

---

## Nível 1 — Básico

*Ensino Fundamental I e II · trilha: frações e decimais, múltiplos e divisores, potências e raízes,
proporcionalidade.*

O aluno sai daqui fazendo conta com **qualquer tipo de número** e resumindo uma lista de dados. É o
chão de todo o resto: porcentagem, frações e negativos aparecem em todas as aulas seguintes.

| # | Aula | Estado | Vem de |
|---|---|---|---|
| 1 | Múltiplos, divisores e primos | 🆕 | — |
| 2 | Pedaços e sinais: frações, decimais e negativos | 🆕 | — |
| 3 | Porcentagem, razão e regra de três | 🆕 | — |
| 4 | Potências e raízes | ♻️ | atual Aula 9 (seções 1, 2 e 6) |
| 5 | Dados: média, mediana, moda e desvio | ♻️ | atual Aula 10 (seção 1) + novo |
| 6 | Contagem e chance | ♻️ | atual Aula 17 (seções 1–3) + novo |

### Aula 1 — Múltiplos, divisores e primos 🆕

**O obstáculo:** somar frações, simplificar e dividir coisas em partes iguais dependem de saber
"quem cabe dentro de quem" — e isso nunca é mostrado, só decorado.

- Múltiplos: pular de 3 em 3 na reta; divisores: quem divide sem sobrar
- Números primos: os que só se dividem por 1 e por eles mesmos; o crivo de Eratóstenes
- Todo número é um produto de primos (a "receita" do número)
- MMC: quando duas engrenagens voltam à posição inicial juntas
- MDC: o maior ladrilho quadrado que cobre um retângulo sem cortar

**Laboratórios:** pulos na reta · caixas de bombons · o crivo de Eratóstenes · a árvore de fatores ·
engrenagens (MMC) · ladrilhos (MDC)

### Aula 2 — Pedaços e sinais: frações, decimais e negativos 🆕

**O obstáculo:** meio, terço, 0,25, −3 °C — todos são "números", mas cada um parece ter suas
próprias regras.

- Fração como pedaço: pizza e barra de chocolate; frações equivalentes
- Somar frações: deixar os pedaços do mesmo tamanho (reencontro com o MMC da Aula 1)
- Decimais: a fração de 10, 100, 1000 — a vírgula na régua
- A reta numerada inteira: negativos à esquerda do zero (termômetro, saldo no banco)
- Somar e multiplicar com sinais: andar para trás; menos vezes menos dá mais

**Laboratórios:** a pizza fatiada · frações equivalentes · soma de pedaços · a régua dos decimais ·
o termômetro · o saldo que entra e sai

### Aula 3 — Porcentagem, razão e regra de três 🆕

**O obstáculo:** desconto, juros, receita de bolo e mapa são a mesma conta, mas parecem quatro
assuntos.

- Razão: comparar por divisão (2 xícaras de farinha para 1 de açúcar)
- Proporção: duas razões iguais; a receita que dobra
- Porcentagem: "por cem" — a fração de denominador 100
- Aumentos e descontos em sequência (e por que 10% de aumento seguido de 10% de desconto não volta
  ao preço original)
- Regra de três simples e composta; grandezas diretas e inversas

**Laboratórios:** a receita que dobra · a barra de porcentagem · desconto × aumento · a escala do
mapa · regra de três ao vivo · direta ou inversa?

### Aula 4 — Potências e raízes ♻️

**O obstáculo:** "ao quadrado" e "raiz" parecem símbolos soltos; são um quadrado de verdade e o
lado dele.

- Ao quadrado é, literalmente, um quadrado; ao cubo é um cubo (volume)
- A raiz quadrada como caminho de volta; a raiz cúbica
- Nem toda raiz é inteira (√2 ≈ 1,41)
- Quadrado nunca é negativo (reencontro com os sinais da Aula 2)
- Notação científica: potências de 10 para números enormes e minúsculos

**Laboratórios:** o quadrado cresce · ache o lado · o cubo cresce · ache a aresta · quadrado nunca é
negativo · a régua das potências de 10

### Aula 5 — Dados: média, mediana, moda e desvio ♻️

**O obstáculo:** uma lista de números não diz nada até ser resumida — e cada resumo esconde algo.

- Média como ponto de equilíbrio (a gangorra)
- Mediana: o do meio; moda: o que mais aparece; quando cada uma engana (salários)
- Gráficos de barras e histogramas
- Desvio: o quanto a lista se espalha (usa quadrado e raiz da Aula 4)
- **Conversa ao pé da lareira:** Média × Mediana

**Laboratórios:** a gangorra da média · o do meio · o salário do chefe · monte o histograma ·
centralize a lista · espalhado ou apertado?

### Aula 6 — Contagem e chance ♻️

**O obstáculo:** o acaso parece não ter regra, e contar possibilidades parece exigir fórmulas
decoradas.

- Contar com árvores de possibilidades (princípio multiplicativo)
- Permutações e arranjos: de quantos jeitos dá para ordenar ou escolher em ordem; o fatorial
- Probabilidade como fração dos casos (reencontro com as Aulas 2 e 3)
- Repetir muitas vezes: a frequência se aproxima da probabilidade
- A moeda não tem memória (falácia do apostador)

**Laboratórios:** a árvore de roupas · ordenar a fila · duas moedas, quatro casos · a moeda repetida
· o dado viciado? · a média que gruda

---

## Nível 2 — Intermediário

*Ensino Fundamental II · trilha: expressões algébricas, equações e inequações, sistemas lineares,
geometria plana.*

O aluno troca número por letra, resolve equações e sistemas, desenha retas e mede figuras. Aqui
começam as peças **Por que é verdade?** e **Quem faz o quê?**.

| # | Aula | Estado | Vem de |
|---|---|---|---|
| 7 | Letras no lugar de números: a função | ♻️ | atual Aula 1 + expressões algébricas |
| 8 | Equações e inequações: a balança | ♻️ | atual Aula 7 + inequações + abrir parênteses (da atual 13) |
| 9 | O plano e a reta | ✅ | atual Aula 2 |
| 10 | Sistemas de equações | ✅ | atual Aula 8 |
| 11 | Ângulos, círculo e π | ♻️ | atual Aula 3 + perímetro, área do círculo e π (da atual 15) |
| 12 | Áreas, volumes e Pitágoras | ♻️ | atual Aula 9 (seção 3) + áreas de figuras + volumes |

### Aula 7 — Letras no lugar de números: a função ♻️

**O obstáculo:** o `x` e o `f(x)` assustam mais do que a ideia por trás deles.

- A máquina: entra um número, sai outro; o `x` é um espaço esperando ser preenchido
- Expressões algébricas: `3x + 2` como receita; juntar termos parecidos
- Máquinas de dois passos e a ordem das contas
- A regra de ouro: mesma entrada → sempre a mesma saída
- Cada teste vira um ponto; todos juntos formam o gráfico
- **Conversa ao pé da lareira:** Equação × Função

**Laboratórios:** mexa na máquina · a fórmula clicável · troque o x por um número · a ordem das
contas · confiável ou quebrada? · veja o gráfico nascer

### Aula 8 — Equações e inequações: a balança ♻️

**O obstáculo:** descobrir o número escondido parece chute.

- A balança: o que fizer de um lado, faça do outro
- Isolar o x passo a passo; conferir é de graça
- Abrir parênteses: cada pedaço vezes cada pedaço, pela área do retângulo
- Inequações: a balança que pende para um lado; o sinal que vira quando se multiplica por negativo
- **Por que é verdade?** Por que multiplicar por −1 vira o sinal da desigualdade (reta numerada)

**Laboratórios:** a balança em equilíbrio · a máquina ao contrário · x dos dois lados, passo a passo
· abra os parênteses · a balança que pende · o sinal que vira

### Aula 9 — O plano e a reta ✅

Atual Aula 2, sem mudança de conteúdo: as duas réguas, o endereço de um ponto, os quatro
quadrantes, o passo da escada e a receita `y = ax + b`. Na migração ganha um reencontro: **a
sequência de passo fixo (PA) é a reta vista de degrau em degrau**, preparando a Aula 14.

### Aula 10 — Sistemas de equações ✅

Atual Aula 8, sem mudança de conteúdo: resolver = achar onde duas retas se cruzam; um, nenhum ou
infinitos cruzamentos; substituição.

### Aula 11 — Ângulos, círculo e π ♻️

**O obstáculo:** grau, volta e π parecem convenções arbitrárias.

- O que é girar; a volta de 360°; sentido anti-horário e ângulos negativos (reencontro com a reta
  numerada)
- Onde o ponto para depois de girar
- **O comprimento da volta:** enrolar uma linha no círculo → `2π · raio`, com π ≈ 3,14
- **A área do círculo:** fatiar em gomos e rearrumar num quase-retângulo → `π · raio²`
- **Por que é verdade?** A área do círculo pelos gomos

**Laboratórios:** o ponteiro que gira · o relógio de ângulos · ângulos negativos e voltas extras · o
transferidor interativo · desenrole o círculo · os gomos viram retângulo

### Aula 12 — Áreas, volumes e Pitágoras ♻️

**O obstáculo:** cada figura parece ter sua fórmula decorada; são todas "retângulo arrumado".

- Área do retângulo, do triângulo (metade do retângulo), do paralelogramo e do trapézio
- Pitágoras: três quadrados num triângulo retângulo
- **Por que é verdade?** Pitágoras rearrumando quatro triângulos
- Volume: área da base × altura (prisma, cilindro); cubo e esfera
- Perímetro × área: a mesma cerca, áreas diferentes

**Laboratórios:** o triângulo é meio retângulo · o paralelogramo que vira retângulo · Pitágoras com
quadrados · a prova dos quatro triângulos · empilhe a base · a lata de refrigerante

---

## Nível 3 — Avançado

*Ensino Médio · trilha: sequências (PA e PG), matemática financeira, funções, trigonometria,
exponenciais e logaritmos, polinômios e complexos, geometria analítica, matemática discreta.*

O aluno passa a estudar o **comportamento** das funções clássicas e ganha as ferramentas de
geometria que o cálculo vai precisar.

| # | Aula | Estado | Vem de |
|---|---|---|---|
| 13 | Curvas que não são retas: a parábola | ♻️ | atual Aula 13 (abrir parênteses vai para a 8) |
| 14 | Crescimento que acelera: PA, PG, juros, exponenciais e logaritmos | ♻️ | atual Aula 14 + PA/PG + juros simples |
| 15 | Trigonometria: seno, cosseno, tangente e radianos | ♻️ | atual Aula 4 + tangente + radianos (da atual 15) |
| 16 | Ondas | ✅ | atual Aula 5 |
| 17 | Vetores e matrizes | ♻️ | atual Aula 6 + tamanho da seta (da atual 9) + distância e circunferência |
| 18 | Números complexos | ♻️ | atual Aula 18 (as ondas como giros vão para a 24) |

### Aula 13 — Curvas que não são retas: a parábola ♻️

Atual Aula 13. Na migração, as transformações `a(x − h)² + k` passam a ser apresentadas **aqui pela
primeira vez** (reencontrando a reta da Aula 9 e a máquina da Aula 7); a Aula 16 (ondas) é que
passa a reencontrá-las. Zeros pela balança com a raiz de dois lados, Bhaskara como "arrumar e passar
para o outro lado", o vértice como melhor valor, polinômios e o teste das diferenças.

**Laboratórios:** a máquina que dobra · três sliders da parábola · ache onde ela cruza o zero · caça
ao vértice · somador de potências · reta ou curva?

### Aula 14 — Crescimento que acelera ♻️

**O obstáculo:** crescer somando e crescer multiplicando parecem parecidos no começo.

- PA: somar sempre o mesmo — a reta da Aula 9 de degrau em degrau; a soma de Gauss
- PG: multiplicar sempre pelo mesmo — a dobra do papel
- Juros simples (PA) × juros compostos (PG) (reencontro com a porcentagem da Aula 3)
- A escada das potências: expoente zero, negativo e fracionário; o chapeuzinho `^`
- O logaritmo: "quantas vezes multipliquei?"; a régua logarítmica
- O número e: `(1 + 1/n)ⁿ`

**Laboratórios:** corrida soma × multiplicação · a dobra do papel · a escada das potências · quantas
dobras? (o logaritmo) · a régua logarítmica · de onde vem o e

### Aula 15 — Trigonometria: seno, cosseno, tangente e radianos ♻️

**O obstáculo:** seno e cosseno parecem fórmulas decoradas de triângulo.

- A altura e a sombra de um ponto girando (reencontro com a Aula 11)
- No triângulo retângulo: cateto oposto, adjacente e hipotenusa (reencontro com a Aula 12)
- Tangente: a altura dividida pela sombra — a inclinação da reta (reencontro com a Aula 9)
- `cos² + sen² = 1` (Pitágoras no círculo)
- Radianos: o ângulo medido pelo arco (reencontro com o π da Aula 11)
- **Conversa ao pé da lareira:** Seno × Cosseno

**Laboratórios:** o círculo com a sombra e a altura ao vivo · a tabela que se preenche sozinha ·
simetria do círculo · o triângulo retângulo · o círculo de raio 1 · radianos, o ângulo medido pelo
arco

### Aula 16 — Ondas ✅

Atual Aula 5: desenrolar o círculo, amplitude, frequência e fase, somar ondas. Na migração, o
reencontro das transformações aponta para a parábola (Aula 13) e os ângulos podem aparecer também
em radianos (Aula 15).

### Aula 17 — Vetores e matrizes ♻️

**O obstáculo:** "álgebra linear" soa abstrato; é só seta e tabela que move seta.

- Vetor é uma seta; somar setas; esticar uma seta
- O tamanho de uma seta: `√(x² + y²)` (reencontro com Pitágoras da Aula 12)
- Distância entre dois pontos e a equação da circunferência (geometria analítica)
- Produto escalar: o quanto duas setas apontam juntas (reencontro com o cosseno da Aula 15)
- Matriz é uma tabela que transforma setas: esticar, espelhar, girar
- Sistema de equações como uma matriz (reencontro com a Aula 10)

**Laboratórios:** somador de setas arrastável · o tamanho da seta e a distância · multiplicar por um
número · produto escalar ao vivo · gire a figura com uma matriz · o sistema como matriz

### Aula 18 — Números complexos ♻️

Atual Aula 18: `i` como giro de 90°, o plano complexo, multiplicar = girar e esticar, potências e
a fórmula de Euler por `(1 + iθ/n)ⁿ`. Na migração, a seção "ondas como giros" (que depende de
Fourier) vai para a Aula 24; no lugar entra **resolver equações do 2º grau sem solução real**
(pendência da Aula 13) — o laboratório "as raízes que faltavam".

**Laboratórios:** multiplique por i · o plano complexo · girar e esticar · potências de um número
complexo · o ponto de Euler · as raízes que faltavam

---

## Nível 4 — Especialista: Cálculo e Dados

*Faculdade · trilha: limites e continuidade, cálculo diferencial, cálculo integral; estatística e
análise de sinais.*

A matemática do movimento, da variação contínua e da extração de padrões em dados.

| # | Aula | Estado | Vem de |
|---|---|---|---|
| 19 | Limites e a derivada | ♻️ | atual Aula 15 (radianos vão para a 15) + limites e continuidade |
| 20 | A integral | ♻️ | atual Aula 16 + volumes por fatias |
| 21 | A curva normal | ♻️ | atual Aula 17 (seções 4–6) + combinações e o triângulo de Pascal |
| 22 | Correlação: estatística com vetores | ♻️ | atual Aula 10 (seções 2–4) |
| 23 | Projeção e mínimos quadrados | ✅ | atual Aula 11 |
| 24 | Decomposição de sinais: Fourier | ♻️ | atual Aula 12 + ondas como giros (da atual 18) |

### Aula 19 — Limites e a derivada ♻️

- Chegar cada vez mais perto: o limite (a lupa e os dois pontos que se aproximam)
- Continuidade: curva sem saltos; onde a derivada não existe (bicos)
- A reta tangente e a inclinação em cada ponto
- A derivada como máquina: `x² → 2x`, `x³ → 3x²`, `eˣ → eˣ`, `sen → cos` (em radianos, Aula 15)
- Topos e fundos: candidatos em `f′(x) = 0`, conferidos pela troca de sinal
- **Conversa ao pé da lareira:** Derivada × Integral (fecha na Aula 20)

**Laboratórios:** a lupa que endireita a curva · a reta que encosta · dois pontos se aproximando · o
gráfico da inclinação · saltos e bicos · caça ao topo

### Aula 20 — A integral ♻️

Atual Aula 16: fatias, somas por baixo e por cima, velocidade → distância, o acumulado e o Teorema
Fundamental. Ganha **volumes por fatias** (o sólido de revolução como pilha de moedas, reencontro com
o volume da Aula 12).

**Laboratórios:** fatie a curva · fatias mais finas · velocidade vira distância · o acumulado ao
vivo · derivar o acumulado · a pilha de moedas

### Aula 21 — A curva normal ♻️

- Combinações e o triângulo de Pascal (reencontro com a contagem da Aula 6)
- A máquina de Galton: somar muitos acasos pequenos dá o sino
- A fórmula do sino: `e`, π e o expoente negativo (Aulas 11, 14)
- Área = chance (integral, Aula 20); a regra 68–95–99,7
- Onde a normal **não** vale: caudas gordas

**Laboratórios:** o triângulo de Pascal · a máquina de Galton · o sino ajustável · área = chance ·
padronizar (z) · caudas gordas × sino

### Aula 22 — Correlação: estatística com vetores ♻️

Atual Aula 10 sem a seção de média e desvio (que foi para a Aula 5): a lista como vetor, o ângulo
entre duas listas, a correlação como cosseno, a escala que não muda a correlação, correlação não é
causa.

### Aula 23 — Projeção e mínimos quadrados ✅

Atual Aula 11: projetar é jogar sombra, a reta que melhor se ajusta, por que o quadrado dos erros.

### Aula 24 — Decomposição de sinais: Fourier ♻️

Atual Aula 12 (espectro, projeção sobre cada onda, voltas completas) mais **as ondas como giros**
vindas da atual Aula 18: a soma de setas girando `e^(iωt)` é a forma de verdade da série de Fourier.

---

## Nível 5 — Pesquisador: Matemática Aplicada e Computacional

*Faculdade · trilha: equações diferenciais, probabilidade avançada e processos estocásticos,
análise numérica, otimização; e o que a trilha não tem — lógica e demonstração.*

Todas as aulas são novas. Cada uma junta ferramentas de vários níveis para modelar algo que muda,
que é incerto ou que precisa ser calculado por um computador — e a última mostra como um matemático
tem certeza de que algo é verdade.

| # | Aula | Estado | Reencontra |
|---|---|---|---|
| 25 | Matrizes que transformam: determinante, inversa e autovalores | 🆕 | 10, 17, 18 |
| 26 | PCA: as direções principais dos dados | 🆕 | 22, 23, 25 |
| 27 | Otimização: descer a ladeira pelo gradiente | 🆕 | 19, 23 |
| 28 | Equações diferenciais e o método de Euler | 🆕 | 14, 16, 19, 20 |
| 29 | Acaso no tempo: passeio aleatório e movimento browniano | 🆕 | 6, 21, 28 |
| 30 | Pensar como matemático: lógica, demonstração e conjecturas | 🆕 | todas |

### Aula 25 — Matrizes que transformam: determinante, inversa e autovalores 🆕

**O obstáculo:** determinante e autovalor são ensinados como contas; são área e direção.

- O determinante é o quanto a matriz estica a **área** (e o sinal diz se ela espelha)
- Determinante zero: a matriz achata o plano numa reta — o sistema sem solução única (Aula 10)
- A inversa: a transformação que desfaz a outra
- Autovetores: as setas que a matriz só estica, sem girar; o autovalor é o quanto
- A rotação não tem autovetor real — seus autovalores são complexos (Aula 18)

**Laboratórios:** o quadrado que vira paralelogramo · achatar o plano · desfazer a transformação ·
caça às setas que não giram · autovalores ao vivo · a rotação e os complexos

### Aula 26 — PCA: as direções principais dos dados 🆕

**O obstáculo:** dados com muitas colunas parecem impossíveis de visualizar.

- A nuvem de pontos e sua "direção mais comprida" (reencontro com a correlação da Aula 22)
- Projetar a nuvem numa reta perdendo o mínimo (Aula 23)
- A matriz de covariância e seus autovetores (Aula 25)
- Quanto da variação cada direção explica
- Aplicação: comprimir imagens e resumir muitas variáveis em poucas

**Laboratórios:** a nuvem e sua direção · gire a reta de projeção · a variância explicada · os
autovetores da covariância · de 2 dimensões para 1 · a imagem comprimida

### Aula 27 — Otimização: descer a ladeira pelo gradiente 🆕

**O obstáculo:** achar o melhor valor quando há muitas variáveis parece impossível de fazer à mão.

- A derivada diz para onde a curva desce (Aula 19)
- Com duas variáveis: o relevo, as curvas de nível e o gradiente (a seta de subida mais íngreme)
- Descer a ladeira passo a passo; o tamanho do passo (pequeno demais × grande demais)
- Mínimos locais: o vale que não é o mais fundo
- Reencontro com os mínimos quadrados (Aula 23): a mesma reta, achada descendo

**Laboratórios:** a bolinha na curva · o mapa de curvas de nível · a seta do gradiente · o tamanho
do passo · presos num vale local · ajuste a reta descendo

### Aula 28 — Equações diferenciais e o método de Euler 🆕

**O obstáculo:** equações em que a incógnita é uma função inteira parecem outro planeta.

- Quando a regra fala da inclinação: `y′ = k · y` (juros contínuos e decaimento — reencontro com o e)
- O campo de direções: setinhas que mostram para onde ir em cada ponto
- O método de Euler: andar pequenos passos na direção da seta (reencontro com a integral)
- A mola: `y″ = −y` devolve seno e cosseno (reencontro com as ondas)
- Erro numérico: passos grandes enganam

**Laboratórios:** o campo de setinhas · siga as setas · crescimento e decaimento · a mola que oscila
· passo grande × passo pequeno · o predador e a presa

### Aula 29 — Acaso no tempo: passeio aleatório e movimento browniano 🆕

**O obstáculo:** "cálculo estocástico" soa inalcançável; começa com uma moeda.

- O passeio aleatório: cada passo é uma moeda (reencontro com a Aula 6)
- Depois de n passos, o espalhamento cresce como `√n` (reencontro com a normal da Aula 21)
- Passos cada vez menores e mais rápidos: o movimento browniano
- Tendência + ruído: `dy = tendência · dt + ruído` (reencontro com Euler da Aula 28)
- Aplicações e limites: difusão, preços, e por que o modelo subestima eventos extremos

**Laboratórios:** a moeda que anda · mil caminhantes · o leque de caminhos · do passeio ao browniano
· tendência + ruído · caudas gordas de novo

### Aula 30 — Pensar como matemático: lógica, demonstração e conjecturas 🆕

**O obstáculo:** ver um fato dar certo em mil exemplos não prova nada — e ninguém ensina o que prova.

- Afirmações, "e", "ou", "se... então"; contraexemplo derruba uma regra (reencontro com o patamar de
  `x³` na Aula 19)
- Demonstração direta: a soma de Gauss (Aula 14)
- Por absurdo: √2 não é fração (Aulas 2 e 4); os primos nunca acabam (Aula 1)
- Por indução: o dominó que derruba todos
- Conjecturas: problemas simples que ninguém resolveu (Collatz, primos gêmeos) — o que é pesquisa

**Laboratórios:** verdadeiro, falso ou depende? · caça ao contraexemplo · a soma de Gauss · o dominó
da indução · tente escrever √2 como fração · a sequência de Collatz

---

## Eletivas

Módulos independentes, numerados de 31 a 40, para depois do Nível 5 — ou antes, assim que os
pré-requisitos de cada um estiverem feitos. Mesma anatomia de aula (6 laboratórios, 6 exercícios com
desafio e Quem faz o quê?, Poder do cérebro, Por que é verdade?, Guru, Cuidado, Não existe pergunta
idiota). No curso, aparecem numa aba própria, "Eletivas"; o cabeçalho de cada uma diz "ELETIVA N de 10".

| Eletiva | Aula | Pré-requisitos | Área da trilha |
|---|---|---|---|
| 1. Aritmética do relógio e criptografia RSA | 31 | 1, 4, 14, 30 | Teoria dos números |
| 2. Grafos: caminhos, redes e rotas | 32 | 6, 17, 27, 30 | Otimização combinatória e grafos |
| 3. Simetrias: o que é um grupo | 33 | 6, 15, 17, 18 | Álgebra abstrata |
| 4. Topologia de borracha: Möbius e V − A + F | 34 | 6, 12, 17 | Topologia |
| 5. Curvas e superfícies: curvatura | 35 | 11, 15, 17, 19, 20 | Geometria diferencial |
| 6. Séries de Taylor: trocar uma curva por potências | 36 | 13, 14, 15, 18, 19 | Análise |
| 7. Calor e ondas: equações diferenciais parciais | 37 | 16, 19, 24, 28 | EDP |
| 8. Fractais e dimensão | 38 | 12, 14, 17, 18, 23 | Geometria (fractais) |
| 9. Cálculo estocástico: a integral do acaso | 39 | 20, 21, 28, 29 | Probabilidade avançada |
| 10. Métodos numéricos: Newton, erro e estabilidade | 40 | 13, 19, 27, 28 | Análise numérica |

### Eletiva 1 (Aula 31) — Aritmética do relógio e criptografia RSA ✅

**O obstáculo:** como trocar mensagens secretas com quem você nunca combinou senha nenhuma.

- Aritmética modular: somar e multiplicar ficando com o resto
- Inverso no relógio existe quando mdc(a, n) = 1 (reencontro com a Aula 1)
- Potências andam em ciclos; pequeno teorema de Fermat, com demonstração
- Cifra de César e a quebra por frequência de letras
- RSA completo: n = p · q, φ, e, d; trancar e abrir
- Por que é seguro: multiplicar é fácil, fatorar é difícil

**Laboratórios:** o relógio de n horas · a tabuada do relógio · o passeio das potências · cifre e
quebre a cifra de César · monte o seu RSA · multiplicar × fatorar

### Eletiva 2 (Aula 32) — Grafos: caminhos, redes e rotas ✅

**O obstáculo:** mapas, redes e rotas parecem problemas sem forma matemática.

- Vértices, arestas e grau; soma dos graus = 2 × arestas
- Pontes de Königsberg e a regra de Euler dos vértices ímpares (com demonstração)
- Matriz de adjacência: Aᵏ conta caminhos (reencontro com a Aula 17)
- Caminho mais curto (Dijkstra) e árvore geradora mínima (Kruskal)
- Coloração e o teorema das quatro cores

**Laboratórios:** as pontes de Königsberg · a casinha sem tirar o lápis · potências da matriz contam
caminhos · Dijkstra passo a passo · Kruskal liga as cidades · pinte a roda

### Eletiva 3 (Aula 33) — Simetrias: o que é um grupo ✅

**O obstáculo:** álgebra abstrata parece uma coleção de definições sem desenho.

- As 6 simetrias do triângulo (contagem com demonstração)
- Composição e a tabela de Cayley; a ordem importa
- As quatro regras de grupo e contraexemplos
- Grupos cíclicos e geradores (mdc de novo); raízes da unidade (reencontro com a Aula 18)
- Rosáceas: grupos cíclico Cₙ e diedral Dₙ

**Laboratórios:** gire e espelhe o triângulo · a tabela de Cayley do triângulo · é grupo ou não é? ·
quem gera o grupo? · as raízes da unidade · monte uma rosácea

### Eletiva 4 (Aula 34) — Topologia de borracha: Möbius e V − A + F ✅

**O obstáculo:** topologia soa abstrata demais; começa com massinha.

- Igualdade topológica: esticar sem rasgar nem colar
- Fórmula de Euler V − A + F = 2 nos poliedros
- O toro como quadrado colado; χ = 0
- Faixa de Möbius: um lado só
- Curva de Jordan e a regra da paridade; 3 casas e 3 serviços (demonstração)
- Característica de Euler χ = 2 − 2g

**Laboratórios:** o alfabeto de borracha · conte V, A e F · V − A + F no toro · a formiga na faixa ·
o labirinto de Jordan · o gênero e a característica

### Eletiva 5 (Aula 35) — Curvas e superfícies: curvatura ✅

**O obstáculo:** geometria diferencial parece exigir anos de cálculo; começa com um volante.

- Círculo osculador e κ = 1/R
- Curvatura com sinal ao longo de uma pista
- Teorema da rotação das tangentes: 360°
- Curvaturas principais e curvatura de Gauss
- Triângulos esféricos e o excesso angular
- Por que todo mapa-múndi distorce (demonstração); a projeção de Mercator

**Laboratórios:** o círculo que beija a curva · o volante na pista · quanto a direção girou? · monte
a superfície · o triângulo polo–equador · o círculo que incha no mapa

### Eletiva 6 (Aula 36) — Séries de Taylor: trocar uma curva por potências ✅

**O obstáculo:** não se sabe como uma calculadora acha seno ou eˣ.

- Polinômio de Taylor e o k! (com demonstração)
- Séries de eˣ, sen x e do número e
- Série geométrica e raio de convergência
- Mudança de centro (ln x)
- e^(ix) = cos x + i sen x pelas séries

**Laboratórios:** imitando eˣ · polinômios que ondulam · somando 1/k! · converge ou explode? · o
logaritmo em volta de a · a espiral de Euler

### Eletiva 7 (Aula 37) — Calor e ondas: equações diferenciais parciais ✅

**O obstáculo:** equações com derivadas em várias variáveis parecem inalcançáveis.

- Equação do calor como "média dos vizinhos" (com demonstração)
- Estabilidade: r ≤ 1/2
- Solução de Fourier: cada seno decai no seu ritmo
- Equação da onda, d'Alembert e reflexões
- Modos normais e a série harmônica

**Laboratórios:** a barra que esfria · estável ou instável? · cada seno encolhe no seu ritmo ·
belisque a corda · o pulso que se divide · os modos normais

### Eletiva 8 (Aula 38) — Fractais e dimensão ✅

**O obstáculo:** formas "irregulares" como litorais parecem fora do alcance da geometria.

- Floco de Koch: perímetro infinito, área finita (com demonstração)
- Jogo do caos e o triângulo de Sierpinski
- Dimensão de autossemelhança D = log N / log(1/r)
- Contagem de caixas e a reta log-log (reencontro com a Aula 23)
- Conjunto de Mandelbrot e órbitas de z² + c

**Laboratórios:** o floco de neve de Koch · o jogo do caos · calcule a dimensão · contagem de caixas
na curva de Koch · o conjunto de Mandelbrot · siga a órbita de c

### Eletiva 9 (Aula 39) — Cálculo estocástico: a integral do acaso ✅

**O obstáculo:** o browniano não tem derivada; como fazer cálculo com ele?

- Integral de Itô: avaliar no começo do passo
- Variação quadrática: (dW)² = dt (com demonstração)
- Lema de Itô: d(W²) = 2W dW + dt
- Movimento browniano geométrico: média × mediana
- Monte Carlo e o preço de uma opção (Black–Scholes), com os limites do modelo

**Laboratórios:** soma pela esquerda × soma pela direita · somando os quadrados dos passos ·
conferindo o lema de Itô · preços simulados · 4.000 futuros de um ano · Monte Carlo × Black–Scholes

### Eletiva 10 (Aula 40) — Métodos numéricos: Newton, erro e estabilidade ✅

**O obstáculo:** o computador não "resolve" equações: chuta, corrige e erra.

- Bisseção e método de Newton; convergência quadrática (com demonstração)
- Onde Newton falha: ciclos e tangentes deitadas
- Arredondamento de ponto flutuante e o h ótimo da derivada numérica
- Cancelamento catastrófico e fórmulas estáveis
- Euler explícito × implícito: estabilidade

**Laboratórios:** a bisseção acha √2 · siga a tangente · onde Newton se perde · o h ótimo da
derivada · duas fórmulas para a mesma raiz · o passo que explode

---

## Cobertura da trilha de referência

Cada tópico da [trilha](trilha_de_aprendizado_em_matemativa.md) e onde ele é ensinado aqui.

| Nível da trilha | Tópico | Aulas |
|---|---|---|
| 1 | Frações e decimais | 2 |
| 1 | Múltiplos e divisores (MMC, MDC) | 1 |
| 1 | Potenciação e radiciação (quadrada, cúbica) | 4 |
| 1 | Razão, proporção, porcentagem, regra de três simples e composta | 3 |
| 2 | Expressões algébricas | 7, 8 |
| 2 | Equações de 1º e 2º grau (Bhaskara) e inequações | 8, 13 |
| 2 | Sistemas lineares | 10, 17 |
| 2 | Geometria plana: ângulos, perímetros, áreas, círculo, Pitágoras | 11, 12 |
| 2 | Estatística básica: média, mediana, moda, desvio | 5 |
| 3 | PA e PG | 14 (e 9) |
| 3 | Juros simples e compostos | 3, 14 |
| 3 | Funções: retas e parábolas | 7, 9, 13 |
| 3 | Trigonometria: seno, cosseno, tangente, triângulo retângulo, ciclo | 11, 15 |
| 3 | Exponenciais e logaritmos | 14 |
| 3 | Polinômios de grau maior que 2 e números complexos | 13, 18 |
| 3 | Geometria espacial (volumes) e analítica | 12, 17, 20 |
| 3 | Combinatória (arranjos, permutações) e probabilidade | 6, 21 |
| 4 | Limites e continuidade | 19 |
| 4 | Derivadas | 19 |
| 4 | Integrais (áreas e volumes) | 20 |
| 4 | Álgebra linear: matrizes, transformações, sistemas | 17, 25 |
| 5 | Equações diferenciais ordinárias e parciais | 28; eletiva de EDP |
| 5 | Álgebra abstrata e teoria dos números | 1, 30; eletivas de grupos e de criptografia |
| 5 | Cálculo estocástico e probabilidade avançada | 21, 29; eletiva de cálculo estocástico |
| 5 | Análise numérica | 28; eletiva de métodos numéricos |
| 5 | Geometria diferencial e topologia | eletivas de curvatura e de topologia |
| 5 | Otimização combinatória e grafos | 27; eletiva de grafos |
| — | *Fora da trilha:* lógica e demonstração | 30 |
| — | *Fora da trilha:* estatística de dados (correlação, regressão, PCA, Fourier) | 22, 23, 24, 26 |

---

## Pré-requisitos: onde cada peça é apresentada

Tabela de controle da regra "nada é usado antes de ser apresentado". Toda aula nova ou adaptada é
conferida contra ela.

| Peça | Apresentada na aula | Usada depois em |
|---|---|---|
| Múltiplos, primos, MMC | 1 | 2, 30 |
| Frações, decimais | 2 | todas |
| Números negativos e regra de sinais | 2 | 4, 5, 8, 9 |
| Porcentagem, razão, regra de três | 3 | 5, 6, 14, 21 |
| Potências, raízes, notação científica | 4 | 5, 12, 14 |
| Média e desvio padrão | 5 | 13, 21, 22 |
| Contagem, fatorial, probabilidade | 6 | 21, 29 |
| Variável, expressão algébrica, função | 7 | todas |
| Balança, abrir parênteses, inequações | 8 | 10, 13, 18 |
| Plano cartesiano, reta, passo da escada | 9 | 10, 13, 14, 15, 19 |
| Ângulo, π, comprimento e área do círculo | 11 | 15, 21 |
| Área do triângulo, Pitágoras, volume | 12 | 15, 17, 20 |
| Parábola, transformações `a(x − h)² + k` | 13 | 16, 18, 19 |
| PA, PG, expoente negativo/fracionário, log, e | 14 | 19, 21, 28, 30 |
| Seno, cosseno, tangente, radianos | 15 | 16, 17, 19, 22 |
| Vetor, produto escalar, matriz | 17 | 22, 23, 25 |
| Número complexo, Euler | 18 | 24, 25 |
| Limite, derivada | 19 | 20, 27, 28 |
| Integral | 20 | 21, 28 |

---

## Migração das 18 aulas publicadas

| Atual | Nova | Estado | O que muda |
|---|---|---|---|
| 1 O que é uma função | 7 | ♻️ | expressões algébricas; Equação × Função |
| 2 Desenhar números no papel | 9 | ✅ | reencontro com PA |
| 3 Ângulos e o círculo | 11 | ♻️ | ganha π, perímetro e área do círculo |
| 4 Seno e cosseno | 15 | ♻️ | ganha tangente, triângulo retângulo e radianos |
| 5 Ondas | 16 | ✅ | reencontro das transformações passa a apontar para a 13 |
| 6 Setas e tabelas de números | 17 | ♻️ | ganha tamanho da seta, distância, circunferência e sistema como matriz |
| 7 Equações: a balança | 8 | ♻️ | ganha abrir parênteses e inequações |
| 8 Sistemas de equações | 10 | ✅ | só referências |
| 9 Potências, raízes e Pitágoras | 4 + 12 + 17 | ♻️ | dividida: potências/raízes (4), Pitágoras (12), tamanho da seta (17) |
| 10 Estatística com vetores | 5 + 22 | ♻️ | dividida: média e desvio (5), correlação (22) |
| 11 Projeção e mínimos quadrados | 23 | ✅ | só referências |
| 12 Decomposição de sinais | 24 | ♻️ | ganha as ondas como giros |
| 13 Curvas que não são retas | 13 | ♻️ | apresenta as transformações; abrir parênteses vai para a 8 |
| 14 Crescimento que acelera | 14 | ♻️ | ganha PA, PG e juros simples |
| 15 A inclinação em cada ponto | 19 | ♻️ | perde radianos (→ 15), ganha continuidade |
| 16 Somando fatias | 20 | ♻️ | ganha volumes por fatias |
| 17 Acaso com régua | 6 + 21 | ♻️ | dividida: contagem e chance (6), curva normal (21) |
| 18 Girar multiplicando | 18 | ♻️ | ondas como giros → 24; ganha as raízes que faltavam |

**Detalhes técnicos da migração:**

- **Pastas e endereços:** cada aula ganha a pasta com o número novo (`aulas/07-letras-no-lugar-de-numeros/`
  etc.). A SPA passa a aceitar os endereços antigos (`#/aula/<slug antigo>`) e redireciona para os
  novos, para não quebrar links compartilhados.
- **Progresso salvo:** o `progresso.js` ganha um mapa slug antigo → slug novo e converte, uma vez,
  o `localStorage` do aluno. Em aulas divididas, os exercícios que continuam iguais mantêm o selo;
  os novos começam em branco.
- **Numeração:** "AULA N de 30 · NÍVEL X" em todas; `catalogo.js` com os 5 níveis.
- **Testes:** `tests/verifica.js` passa a conferir também que toda aula tem Guru, Não existe pergunta
  idiota, Cuidado e Pontos importantes.

**Fases** (testes verdes antes de cada merge):

1. ✅ **Plano** — este documento.
2. ✅ **Reorganização** — renumerar, migrar pastas e progresso, dividir 9, 10 e 17, mover π, radianos,
   parênteses e Fourier, reescrever "Você já sabe" e reencontros. Ao fim, as 18 aulas atuais estão
   no lugar novo e o curso continua completo.
3. ✅ **Nível 1** — Aulas 1, 2 e 3 (novas) e a ampliação das 4, 5 e 6.
4. ✅ **Nível 2** — ampliações das 7, 8, 11 e 12.
5. ✅ **Níveis 3 e 4** — ampliações (tangente, PA/PG, continuidade, Pascal, volumes...).
6. ✅ **Nível 5** — Aulas 25 a 30.
7. ✅ **Peças novas** — Poder do cérebro, Por que é verdade?, Conversa ao pé da lareira e o exercício
   Quem faz o quê? (onde cada uma entra: tabela da metodologia).
8. ✅ **Eletivas** — as 10, numeradas de 31 a 40, com aba própria no curso.
9. ⏳ **Testes unitários em todas as aulas** — próxima etapa; plano detalhado logo abaixo.

---

## Revisão de qualidade dos laboratórios e exercícios ✅

Auditoria das 40 aulas com rubrica (laboratório com controle próprio, retorno, previsão; exercícios
com 4 alternativas explicadas, contas e desafio de verdade). Resultado, método e o que mudou em
[`QUALIDADE.md`](QUALIDADE.md): 5 laboratórios passivos viraram "preveja e confira", o espectro da
Aula 24 virou equalizador, a onda ao vivo da Aula 16 ganhou boia e segundo controle, todas as
múltiplas escolhas passaram a 4 alternativas e 15 exercícios de memória viraram conta. O
`tests/verifica.js` passou a exigir 4 alternativas com explicação em cada erro e a rodar um aluno
simulado nos laboratórios "preveja e confira".

Segunda rodada: mínimo de 3 contas em todas as aulas (17, 23, 24), teclado em todas as alças
arrastáveis (helper `arrasta()` + 09, 17, 23; checado pelo `verifica.js`) e blocos "Agora é você"
de preveja e confira dentro dos laboratórios das aulas 04 (raiz na mão), 12 (Pitágoras) e 20
(somar as fatias).

## Fase 9 — testes unitários em todas as aulas

**Por quê.** O `tests/verifica.js` é um teste de ponta a ponta: abre cada aula num navegador e confere
que nada quebra (texto `NaN`, erro de JavaScript, gabarito aceito, resposta errada recusada, links,
celular). Ele **não** confere se a matemática mostrada está certa. Um laboratório pode exibir um
número errado, uma fórmula pode ter o sinal trocado, e a suíte continua verde. Exemplo real, pego na
revisão visual da Eletiva 9: uma variável da aula (`NS`) sobrescreveu o namespace SVG do código comum
e **todos** os gráficos ficaram invisíveis, com os testes passando. (Esse caso específico já virou
uma checagem no `verifica.js`; a fase 9 cobre a classe inteira de erros "roda, mas calcula errado".)

**Como (sem quebrar "cada aula é um arquivo que funciona offline").**

1. **Separar a matemática do desenho.** As funções puras hoje repetidas dentro das aulas passam a
   morar em módulos compartilhados em `assets/matematica/`, carregados por `<script src>` (funcionam
   em `file://`) e exportados também para o Node (padrão UMD, sem build):
   - `numeros.js`: `mdc`, `ehPrimo`, `fatores`, `potmod`, `inverso`, frações, arredondamento;
   - `algebra.js`: raízes do 2º grau (forma estável), sistemas 2×2, determinante, inversa, autovalores 2×2 e Jacobi;
   - `calculo.js`: derivada numérica, somas de Riemann, Euler (explícito e implícito), Runge–Kutta, Newton, bisseção, séries de Taylor;
   - `estatistica.js`: média, mediana, desvio, covariância, correlação, regressão, Φ (normal acumulada), geradores pseudoaleatórios com semente;
   - `grafos.js`: Dijkstra, Kruskal, potências da matriz de adjacência;
   - `formato.js`: `num` e `milhar` (vírgula decimal, sinal "−", milhar com ponto).
   O código de desenho (SVG) continua dentro de cada aula.
2. **Testes com `node --test`** (nativo do Node, sem dependências), um arquivo por módulo em
   `tests/unit/`, mais um `tests/unit/aulas.test.js` que percorre as 40 aulas.
3. **O que cada teste cobre:**
   - **valores conhecidos** — `potmod(3, 4, 5) = 1`; Dijkstra A → H = 16 e Kruskal = 26 no mapa da
     Eletiva 2; κ de um círculo = 1/R; `(1 + h)^n` de Euler; Φ(1,96) ≈ 0,975; Black–Scholes contra
     valores de referência publicados; Σ 1/k! → e;
   - **propriedades** — `mdc(a, b)` divide a e b; `a · inverso(a) ≡ 1`; Runge–Kutta com erro caindo
     ~16× ao dividir o passo por 2; bisseção sempre dentro do intervalo; Newton com convergência
     quadrática perto da raiz; `Aᵏ` contando caminhos;
   - **exercícios** — para cada aula: todo `.ex` tem gabarito (`data-r`) e explicação (`explica`/`expAlt`)
     para cada alternativa; e, onde o enunciado é uma conta, o gabarito é **recalculado** pelo módulo
     (ex.: 2 · 7 = 14 na soma dos graus; d = 7 no RSA do exercício 5 da Eletiva 1);
   - **formatação** — casos de borda de `num`/`milhar` (−0, arredondamento de ,5, números enormes);
   - **figuras** — os 40 scripts de `scripts/` rodam sem erro e sem avisos (`pytest` simples).
4. **CI:** um segundo job no workflow, "Testes unitários", rodando em menos de 30 s, com relatório de
   cobertura (`node --test --experimental-test-coverage`). Meta: toda função que produz um número
   mostrado ao aluno tem pelo menos um teste; cobertura ≥ 90% em `assets/matematica/`.
5. **Ordem:** eletivas e Nível 5 primeiro (mais contas numéricas, maior risco), depois Níveis 4, 3,
   2 e 1.
6. **Regra daqui em diante:** aula nova ou alterada só entra com os testes dos seus cálculos.

**Pronto quando:** as 40 aulas usam os módulos compartilhados, os dois jobs de CI estão verdes e a
meta de cobertura foi atingida.

---

## De onde veio esta estrutura

- **Ordem da escola** (Fundamental → Médio → Faculdade), por ser a ordem real de dependência entre
  os conceitos.
- **Trilha de referência** de cinco níveis (Básico → Pesquisador), guardada em
  [`trilha_de_aprendizado_em_matemativa.md`](trilha_de_aprendizado_em_matemativa.md). Adotamos os
  tópicos dela e fizemos quatro ajustes:
  1. Vetores e matrizes vêm no Ensino Médio (Aula 17), não depois do cálculo — álgebra linear não
     depende de cálculo, e o cálculo e a estatística ficam mais claros com vetores.
  2. Limites entram dentro da derivada (Aula 19), com a lupa, e não como bloco isolado.
  3. O Nível 5 mantém o nome "Pesquisador" da trilha, mas o conteúdo é o de disciplinas de
     graduação aplicadas e computacionais. Temas que exigem anos de base (topologia, geometria
     diferencial, EDP rigorosa) viraram eletivas em versão visual.
  4. Entrou **lógica e demonstração** (Aula 30), que a trilha não tem e que é o que separa usar
     matemática de fazer matemática.
- **Auditorias anteriores** deste curso: frações, porcentagem e decimais já eram usados sem terem
  sido ensinados — agora são as Aulas 2 e 3.
