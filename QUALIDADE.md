# Análise de qualidade — laboratórios e exercícios das 40 aulas

Revisão feita em setembro de 2026. Pergunta que guiou tudo: **cada aula tem laboratórios simples,
inteligentes e que funcionam, e exercícios objetivos que fazem o aluno pensar — não só decorar?**

## Como foi medido

**FATO (medido por máquina, reproduzível):**

- Auditoria automática no navegador (Chromium/Playwright) de todas as 40 aulas: contagem de
  controles por laboratório (slider, botão, campo, arraste, clique), presença de texto de retorno,
  tipo de cada exercício e número de alternativas, erros de JavaScript.
- "Aluno simulado" nos laboratórios de *preveja e confira*: um robô que **erra tudo** resolve 200
  problemas sorteados em cada um, usando "Mostrar a resposta", e confere que todo problema termina
  com placar e sem `NaN`/`undefined`/`Infinity` no texto.
- Clique em **todas** as alternativas de todos os exercícios: cada alternativa errada precisa
  mostrar a explicação do próprio erro; cada campo precisa aceitar o gabarito.
- Essas três checagens agora fazem parte de `tests/verifica.js` e rodam no CI a cada push.

**INFERÊNCIA (julgamento pedagógico):** a rubrica abaixo e as notas por aula. São critérios de
design instrucional, não medidas de aprendizagem com alunos reais — isso só um teste com turmas
mostraria.

## Rubrica

| # | Critério | Por quê |
|---|---|---|
| L1 | Todo laboratório tem um controle **próprio** (não só reflete outro) | Mexer é o que fixa a ideia |
| L2 | O laboratório **responde** com número ou frase, não só com desenho | O aluno precisa saber o que viu |
| L3 | Há pelo menos um laboratório de **previsão ou descoberta** (o aluno aposta antes) | Errar a aposta é o que ensina |
| E1 | 6 exercícios com correção automática e explicação no erro | Retorno imediato |
| E2 | Múltipla escolha com **4 alternativas**, cada erro plausível e explicado | Com 3, chutar acerta 33% |
| E3 | Pelo menos 3 exercícios de **conta** (campo numérico) | Saber fazer, não só reconhecer |
| E4 | O "desafio" (exercício 5) exige juntar duas ideias | Um desafio que é decoreba não desafia |

## O que a auditoria encontrou (antes)

**FATO:**

- 0 erros de JavaScript nas 40 aulas; todas com 6 laboratórios, 6 exercícios e as peças do livro.
- **5 laboratórios passivos** (L1/L3): o aluno só apertava um botão e assistia à conta pronta —
  07 "a ordem das contas", 08 "a máquina ao contrário", 08 "x dos dois lados", 10 "resolva por
  substituição", 23 "monte a projeção".
- **1 laboratório sem controle próprio** (L1): 24 "o espectro revelado" só espelhava os sliders do
  laboratório anterior.
- **1 laboratório pobre** (L2): 16 "onda ao vivo" tinha um slider de velocidade e nenhum texto.
- **22 exercícios com 3 alternativas** (E2), concentrados nas aulas 08–24.
- **Aula 16 sem nenhuma conta** (E3): os 6 exercícios eram de reconhecer.
- **Desafios fracos** (E4) em 11, 15, 16, 22, 23 e 24, e perguntas só de memória em
  11 ex2/ex3, 17 ex2, 22 ex2, 23 ex6 e 24 ex3 ("quantos graus tem uma volta?", "qual o erro de um
  ponto sobre a reta?").

## O que mudou

### Laboratórios

- **Novo componente "preveja e confira"** (`assets/pecas.css` + script na aula). Sorteia um
  problema, pede **cada passo** ao aluno, confere na hora, dá dica no erro, oferece "Mostrar a
  resposta" depois de 2 tentativas e termina com "Você acertou X de N passos de primeira". Botão
  🎲 para novos números — o aluno treina quantas vezes quiser. Substituiu os 5 laboratórios passivos:
  - **07** a ordem das contas — `a · x + b` ou `a · (x + b)`: o aluno faz na ordem certa e, no fim,
    vê quanto daria na ordem errada.
  - **08** a máquina ao contrário — desfaz o `+ b`, depois o `× a`.
  - **08** x dos dois lados — `a·x + b = c·x + d`: junta os x, junta os números, divide.
  - **10** resolva o sistema, passo a passo — iguala as retas, acha x, acha y e confere na outra.
  - **23** monte a projeção — produto escalar, tamanho de w (triplas 3-4-5), sombra; o desenho
    aparece no fim.
- **24 o equalizador** (substitui "o espectro revelado"): clicar numa barra do espectro liga ou
  desliga aquela frequência; a onda filtrada aparece sobre a original e o texto diz quantos % da
  "energia" (soma dos quadrados) foram cortados — com a ligação ao MP3.
- **16 onda ao vivo**: ganhou o controle "ondas na tela", uma **boia** que só sobe e desce
  (a pergunta de previsão é "a boia vai junto com a onda?") e texto com período e frequência
  calculados ao vivo.

### Exercícios

- **Todos os 69 exercícios de múltipla escolha agora têm 4 alternativas**, e cada alternativa errada
  explica o erro específico (ex.: 14 ex6 "1.000·n vence quando n é par" → "a partir de n = 14,
  2¹⁴ = 16.384 > 14.000"). A posição da resposta certa foi variada (antes quase sempre a 2ª).
- **15 exercícios reescritos para exigir conta:**

| Aula | Ex. | Antes | Agora | Resposta |
|---|---|---|---|---|
| 11 | 2 | graus de uma volta | ponteiro de 12h00 a 12h45 | 270° |
| 11 | 3 | graus do ângulo reto | roda de 70 cm de diâmetro, uma volta | 219,8 cm |
| 11 | 5 | ¾ de volta | área de 1 fatia de pizza (r = 20, 8 fatias) | 157 cm² |
| 15 | 5 | cos 180° | rampa de 5 m, cosseno 0,8: avanço horizontal | 4 m |
| 16 | 2 | "qual controle deixa mais alta?" | altura máxima de `3 · seno(2x)` | 3 |
| 16 | 3 | "qual controle aperta?" | ondas de `seno(4x)` em 0°–360° | 4 |
| 16 | 5 | ondas sincronizadas se reforçam? | amplitudes 2 e 3 sincronizadas | 5 |
| 17 | 2 | 1ª coordenada de uma soma | tamanho de (6, 8) | 10 |
| 22 | 2 | média de (4, 6, 8, 10, 12) | o 6 depois de centralizar | −2 |
| 22 | 5 | correlação a 0° | correlação a 60° | 0,5 |
| 23 | 1 | "qual laboratório da Aula 15?" | sombra de uma seta de 10 a 60° (4 alternativas) | 5 |
| 23 | 5 | f(4) com passo 2 | soma dos erros² da reta y = x | 2 |
| 23 | 6 | erro de um ponto sobre a reta | erro de (3, 9) para f(x) = 2x | 3 |
| 24 | 3 | quantas ondas nas freq. 1 e 3 | alturas das barras de `3·seno(x) + seno(3x)` | 3 e 1 |
| 24 | 5 | qual barra é mais alta | altura da barra mais alta de `2·seno(x) + 0,5·seno(2x)` | 2 |

**FATO:** antes 73 múltipla escolha (22 com 3 alternativas) + 167 campos; agora **69 múltipla
escolha, todas com 4 alternativas, + 171 campos/ligar**. Aula 16 passou de 0 para 3 contas.

## Situação por aula (depois)

Critérios da rubrica: ✅ atende. Todas as aulas têm 6 laboratórios e 6 exercícios, 0 erros de
JavaScript, e passam em L1, L2, E1 e E2 (FATO, medido). As colunas L3 e E4 são julgamento
(INFERÊNCIA); a coluna de contas é contagem (FATO).

| Aula | Laboratórios (resumo) | Previsão/descoberta (L3) | Contas (E3) | Desafio (E4) |
|---|---|---|---|---|
| 01 Múltiplos e primos | crivo, árvore de fatores, engrenagens (MMC), ladrilhos (MDC) | ✅ engrenagens: quando realinham? | 3 | ✅ |
| 02 Frações e negativos | pizza, equivalentes, régua decimal, termômetro, saldo | ✅ | 4 | ✅ |
| 03 Porcentagem | receita que dobra, desconto × aumento, direta ou inversa? | ✅ desconto × aumento | 4 | ✅ |
| 04 Potências e raízes | quadrado/cubo crescem, ache o lado **+ raiz na mão (preveja)**, potências de 10 | ✅ **novo** | 5 | ✅ |
| 05 Estatística | gangorra da média, salário do chefe, histograma | ✅ salário do chefe | 3 | ✅ |
| 06 Contagem e chance | árvore de roupas, moedas, dado viciado?, média que gruda | ✅ dado viciado? | 4 | ✅ |
| 07 Letras e números | máquina, fórmula clicável, **ordem das contas (preveja)** | ✅ **novo** | 3 | ✅ |
| 08 Equações | balança, **máquina ao contrário e x dos dois lados (preveja)** | ✅ **novo** | 4 | ✅ |
| 09 Plano e reta | encontre/leia o ponto (**mouse ou teclado**), elevador, fábrica de retas | ✅ | 3 | ✅ |
| 10 Sistemas | cruzamento, paralelas, **resolva passo a passo (preveja)**, alvo | ✅ **novo** | 4 | ✅ |
| 11 Ângulos e π | ponteiro, transferidor, desenrole o círculo, gomos | ✅ | 4 (**+2**) | ✅ **refeito** |
| 12 Áreas e Pitágoras | triângulos, Pitágoras **+ passo a passo (preveja)**, prova dos quatro triângulos, lata | ✅ **novo** | 4 | ✅ |
| 13 Curvas | três sliders da parábola, caça ao vértice, reta ou curva? | ✅ | 3 | ✅ |
| 14 Crescimento | corrida soma × multiplicação, dobras, régua log, o e | ✅ corrida | 4 | ✅ |
| 15 Trigonometria | sombra e altura, simetria, triângulo, radianos | ✅ | 4 | ✅ **refeito** |
| 16 Ondas | três sliders, somador, reconheça, **onda ao vivo com boia** | ✅ **novo** | 3 (**+3**) | ✅ **refeito** |
| 17 Vetores e matrizes | setas arrastáveis (**mouse ou teclado**), produto escalar, gire com matriz | ✅ | 3 (**+1**) | ✅ |
| 18 Complexos | multiplique por i, girar e esticar, Euler, raízes | ✅ | 4 | ✅ |
| 19 Derivada | lupa, reta que encosta, saltos e bicos, caça ao topo | ✅ | 4 | ✅ |
| 20 Integral | fatias **+ some as fatias (preveja)**, velocidade → distância, derivar o acumulado | ✅ **novo** | 4 | ✅ |
| 21 Normal | Galton, sino ajustável, padronizar, caudas gordas | ✅ | 4 | ✅ |
| 22 Correlação | nuvem ao vivo, **adivinhe a correlação**, o que ela não vê | ✅ adivinhe | 3 (**+1**) | ✅ **refeito** |
| 23 Projeção e MQ | **monte a projeção (preveja)**, regressão ao vivo (**mouse ou teclado**), comparador | ✅ **novo** | 3 (**+3**) | ✅ **refeito** |
| 24 Fourier | monte a onda, **equalizador**, decomponha a misteriosa | ✅ **novo** | 3 (**+2**) | ✅ **refeito** |
| 25 Determinante e autovalores | achatar o plano, caça às setas que não giram | ✅ | 4 | ✅ |
| 26 PCA | gire a reta de projeção, variância explicada, imagem comprimida | ✅ | 3 | ✅ |
| 27 Otimização | bolinha na curva, tamanho do passo, vale local | ✅ passo | 3 | ✅ |
| 28 EDOs | campo de setas, siga as setas, passo grande × pequeno, predador–presa | ✅ | 3 | ✅ |
| 29 Passeio aleatório | mil caminhantes, leque, tendência + ruído | ✅ | 3 | ✅ |
| 30 Pensar como matemático | verdadeiro/falso/depende, contraexemplo, Collatz | ✅ | 3 | ✅ |
| 31 RSA | relógio de n horas, quebre César, monte seu RSA | ✅ | 3 | ✅ |
| 32 Grafos | Königsberg, casinha, Dijkstra e Kruskal passo a passo | ✅ | 3 | ✅ |
| 33 Grupos | gire e espelhe, Cayley, é grupo ou não é? | ✅ | 3 | ✅ |
| 34 Topologia | alfabeto de borracha, V − A + F, formiga na faixa | ✅ | 3 | ✅ |
| 35 Curvatura | círculo que beija, volante, triângulo polo–equador | ✅ | 3 | ✅ |
| 36 Taylor | imitando eˣ, converge ou explode?, espiral de Euler | ✅ | 3 | ✅ |
| 37 EDPs | barra que esfria, estável ou instável?, belisque a corda | ✅ | 3 | ✅ |
| 38 Fractais | Koch, jogo do caos, contagem de caixas, Mandelbrot | ✅ | 3 | ✅ |
| 39 Cálculo estocástico | esquerda × direita, lema de Itô, Monte Carlo × Black–Scholes | ✅ | 3 | ✅ |
| 40 Métodos numéricos | bisseção, Newton se perde, h ótimo, passo que explode | ✅ | 3 | ✅ |

"Contas" conta os campos numéricos; o exercício "quem faz o quê?" (ligar) está fora dessa contagem.

## Segunda rodada — pendências aplicadas

- **Mínimo de 3 contas em todas as aulas.** 17 ex4 (produto escalar de (3, 4) e (4, −3) → 0),
  23 ex1 (sombra de uma seta de 10 a 60° → 5, agora em campo numérico) e 24 ex6 (projeção de
  (2, 0, −2, 0) sobre (1, 0, −1, 0) → 2) viraram contas. **FATO:** 66 múltipla escolha + 174
  campos/ligar; nenhuma aula com menos de 3 campos numéricos.
- **Teclado em todos os arrastes.** O helper `arrasta()` (usado por 35 aulas) ganhou `teclaAlca`:
  a alça recebe foco e as setas a movem (Shift = passo maior), aumentando o passo até ela sair do
  lugar — funciona também nos laboratórios que encaixam numa grade. Casos à parte: 09 "leia o ponto"
  (setas andam uma casa), 17 somador de setas (pontas de v e w) e 23 regressão (cada ponto).
  Foco visível em laranja. **FATO:** 13 alças focáveis em 6 aulas, todas respondem às setas; o
  `tests/verifica.js` agora falha se alguma alça focável não responder ao teclado.
- **"Agora é você" nas aulas 04, 12 e 20** — em vez de trocar laboratórios bons, o bloco
  *preveja e confira* entrou **dentro** do laboratório, depois da parte visual:
  - **04 ache o lado** → raiz de um quadrado perfeito (121 a 841) sem calculadora: a dezena pelo
    tamanho, a unidade pelo último algarismo, teste do candidato.
  - **12 Pitágoras com quadrados** → hipotenusa pelos catetos ou altura da escada no muro
    (Pitágoras ao contrário), com triplas inteiras e o triângulo desenhado no fim.
  - **20 fatias mais finas** → alturas das fatias pela esquerda ou pela direita, soma, área exata
    e o erro em %, ligando ao slider de mais fatias.
  - Aluno simulado: 200 problemas em cada, 0 falhas.

## O que ainda pode melhorar (INFERÊNCIA)

- **Sem medida com alunos reais.** A rubrica mede o desenho da aula; tempo gasto, taxa de acerto de
  primeira e desistência por laboratório só aparecem com telemetria (o placar do "preveja e
  confira" calcula o acerto de primeira, mas não o guarda).
- Elementos **clicáveis** dentro de desenhos (barras do equalizador da 24, fórmula clicável da 07)
  têm botões equivalentes ou são complementares, mas não recebem foco eles mesmos.
