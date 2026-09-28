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

## Terceira rodada — análise lúdica (setembro de 2026)

A pergunta agora é outra: **os laboratórios e exercícios são inteligentes e lúdicos em alto nível —
o aluno joga, aposta, se surpreende e quer tentar de novo?**

### Como foi medido

**FATO — playtest automático** (`tests/playtest.js`, reproduzível): em cada um dos 240 laboratórios,
o robô leva cada slider aos dois extremos, clica cada botão duas vezes, mexe cada alça com as setas e
clica no desenho, registrando tudo o que o laboratório responde. Em cada um dos 240 exercícios, clica
todas as alternativas (ou erra e acerta a conta) e guarda a explicação mostrada. Depois, cada aula foi
lida por inteiro a partir desse registro.

**INFERÊNCIA — rubrica lúdica.** Baseada na taxonomia de motivação intrínseca de Malone & Lepper
(1987) — **desafio, curiosidade, controle e fantasia** — mais **rejogabilidade**, e na taxonomia de
Bloom revisada para os exercícios. Nota de 0 a 10 por aula:

| Critério | Pontos | Como conta |
|---|---|---|
| Desafio | 0–2 | laboratórios com meta e vitória (caça, alvo, adivinhe, preveja e confira): 0, 1 ou 2+ |
| Curiosidade | 0–2 | laboratórios que pedem previsão ou entregam uma surpresa: 0, 1 ou 2+ |
| Fantasia/contexto | 0–2 | laboratórios com situação ou história: 0–1 → 0; 2–3 → 1; 4+ → 2 |
| Rejogável | 0–1 | pelo menos um laboratório com sorteio (cada tentativa é nova) |
| Exercícios | 0–3 | +1 se 4+ exigem aplicar ou analisar; +1 se 2+ têm situação real; +1 se o desafio junta duas ideias |

O **controle** (o aluno mexe e o desenho responde) ficou fora da nota porque todas as aulas atingem o
máximo: não diferencia.

### Resultado geral

**FATO** (os números de interatividade vêm do playtest; as contagens de meta, previsão, sorteio,
contexto e nível cognitivo vêm da leitura de cada item com os critérios da rubrica acima):

- **Interatividade: excelente.** 240 de 240 laboratórios têm controle próprio. No playtest, 232
  mudaram o texto a cada mexida — em geral explicando o caso especial ("o sinal sumiu", "todos os 9
  ganham menos que a média!", "passou do círculo de raio 2 no passo 3"). Dos 8 que não mudaram, 6
  respondem fora do texto (no visor da máquina, na tabela, na animação ou com digitação) e 2 tinham
  mesmo texto fixo (16 "somador de ondas" e 24 "monte uma onda") — corrigidos nesta rodada.
- **Exercícios: corrigem bem, mas pouco situados.** 240 de 240 explicam o erro. 147 (61%) pedem aplicar
  ou analisar. Só **43 (18%) trazem uma situação real**; 30 das 40 aulas têm no máximo um. Em 9 aulas
  o desafio é de um passo só (04, 09, 17, 18, 20, 22, 24, 25, 39).
- **Elementos de jogo: presentes, mas desiguais.** 42 laboratórios (17,5%) têm meta com vitória, 48
  (20%) pedem previsão ou entregam surpresa, 37 (15%) sorteiam, 81 (34%) têm contexto ou fantasia.
  **15 aulas não têm nenhum laboratório com meta** e 23 não têm nenhum sorteio.

**INFERÊNCIA — veredito:** os laboratórios são **inteligentes** (respondem, explicam, apontam o caso
especial) e o controle é de primeira. Mas a **excelência lúdica não é uniforme**: média **4,3 de 10**.
**4 aulas estão em nível de excelência** (01, 05, 06, 14), 9 estão boas e 27 precisam de reforço. O padrão é
claro: a maioria dos laboratórios é um ótimo **brinquedo de explorar**, mas poucos dizem ao aluno
**o que conquistar**; e os exercícios, a partir do Nível 3 e nas eletivas, raramente saem do quadro
para uma situação de verdade.

### Nota por aula

Colunas da nota: desafio · curiosidade · contexto · sorteio · exercícios.

| Aula | Nota | Composição | O que já é lúdico | Lacuna | Proposta |
|---|---|---|---|---|---|
| 01 Múltiplos e primos | **8** (excelente) | 1·2·2·0·3 | engrenagens e ladrilhos com contexto; o texto explica o encaixe e a sobra | MMC e MDC aparecem antes de o aluno procurar; nada sorteado | modo desafio: esconder MMC/MDC até o aluno achar, pares sorteados, 🏆 |
| 02 Frações e negativos | **3** (reforçar) | 0·1·1·0·1 | pizza, termômetro e saldo ("perdoar dívida te deixa mais rico") | nenhum lab com meta; 1 exercício situado | jogo "acerte a fração" (fração-alvo sorteada na pizza); exercícios com receita e dívida |
| 03 Porcentagem | **7** (boa) | 0·2·2·0·3 | desconto × aumento (surpresa); 4 exercícios situados | nenhum lab com meta ou sorteio | aposta antes do desconto × aumento; situações sorteadas em "direta ou inversa?" com placar |
| 04 Potências e raízes | **4** (reforçar) | 1·1·0·1·1 | raiz na mão (preveja e confira) | nenhum contexto real; desafio de 1 passo (∛125) | "ache a aresta" como mais-quente/mais-frio; notação científica com distâncias reais; desafio: dobrar a aresta multiplica o volume por quanto? |
| 05 Estatística | **8** (excelente) | 1·2·1·1·3 | gangorra com meta, salário do chefe (surpresa), histograma sorteado | a gangorra mostra a média antes de o aluno equilibrar | esconder a média até aparecer "equilibrou!" |
| 06 Contagem e chance | **9** (excelente) | 1·2·2·1·3 | a aula mais lúdica: moedas e dados sorteados, 6 exercícios situados | o aluno escolhe o dado viciado (não há mistério) | dado misterioso sorteado: o aluno decide se é viciado |
| 07 Letras e números | **7** (boa) | 2·1·1·1·2 | máquina (fantasia) e ordem das contas (preveja) | "confiável ou quebrada?" não pede veredito; exercícios sem situação | botões de veredito com máquinas sorteadas; exercício do táxi (bandeirada + km) |
| 08 Equações | **7** (boa) | 2·1·2·1·1 | balança com meta e 2 preveja-e-confira | exercícios são equações sem enunciado | 2 problemas de enunciado ("pensei num número…", idades, preços) |
| 09 Plano e reta | **5** (reforçar) | 2·1·1·1·0 | sobe/desce (palpite) e reta misteriosa | desafio é tradução direta; nada situado | desafio do plano de celular (fixo + preço por GB) |
| 10 Sistemas | **5** (reforçar) | 2·2·0·1·0 | 4 labs-jogo: classifique, resolva, ache o cruzamento, acerte o alvo | nenhum contexto, nem nos labs nem nos exercícios | desafio: 2 sucos + 1 lanche custam R$ 20…; alvo com história (duas tarifas de táxi) |
| 11 Ângulos e π | **4** (reforçar) | 0·0·1·0·3 | 3 exercícios situados (relógio, bicicleta, pizza) | 6 labs de exploração, sem meta nem previsão | jogo "estime o ângulo" no transferidor (ângulo sorteado, placar de erro) |
| 12 Áreas e Pitágoras | **6** (boa) | 1·1·1·1·2 | prova dos quatro triângulos (surpresa) e Pitágoras passo a passo | exercícios pouco situados | meta "lata de 350 mL com o mínimo de alumínio"; exercícios com terreno e caixa |
| 13 Curvas | **3** (reforçar) | 1·0·0·0·2 | caça ao vértice com recorde | sem previsão nem sorteio; 1 exercício situado | "acerte a parábola misteriosa" (como a reta misteriosa da Aula 9); trajetória de uma bola |
| 14 Crescimento | **8** (excelente) | 1·2·2·0·3 | dobra do papel até a Lua; corrida soma × multiplicação | nada sorteado | palpite registrado antes: "em quantas dobras chega à Lua?" |
| 15 Trigonometria | **0** (reforçar) | 0·0·0·0·0 | círculo com sombra e altura (visual forte) | 6 labs de exploração sem meta nem previsão; ex2 e ex3 são decoreba (cos 0°, sen 90°) | jogo "acerte a sombra" (valor-alvo sorteado); trocar ex2 e ex3 por pipa e sombra de poste |
| 16 Ondas | **3** (reforçar) | 1·1·0·1·0 | reconheça a onda (alvo) e onda com boia | exercícios sem situação | exercícios com som (oitava = frequência dobrada) |
| 17 Vetores e matrizes | **1** (reforçar) | 1·0·0·0·0 | setas arrastáveis e "chegue na estrela" | o desafio repete a conta do ex4; sem previsão; nada situado | desafio barco + correnteza (soma, múltiplo, tamanho); aposta "o produto escalar será +, − ou 0?" |
| 18 Complexos | **1** (reforçar) | 0·1·0·0·0 | casinha multiplicada; raízes que saem da reta | nenhum lab com meta; desafio de 1 passo | quebra-cabeça "chegue ao alvo com × i, × −1, × 2" no menor número de movimentos |
| 19 Derivada | **4** (reforçar) | 1·2·0·0·1 | caça ao topo; saltos e bicos | exercícios sem situação | desafio da bola lançada: h(t) = −5t² + 20t, quando ela para de subir? |
| 20 Integral | **3** (reforçar) | 1·0·1·1·0 | pilha de moedas; fatias com preveja | ex1 e ex2 repetem a Aula 12; desafio de 1 passo | estimar com 2 fatias; carro acelerando (distância = área do triângulo) |
| 21 Normal | **6** (boa) | 0·1·1·1·3 | 5 exercícios situados; máquina de Galton sorteada | nenhum lab com meta | "aposte na pilha" na máquina de Galton (placar contra o acaso) |
| 22 Correlação | **5** (reforçar) | 2·2·0·1·0 | adivinhe a correlação; pares do dia a dia | desafio é cos 60° (1 passo) | desafio: correlação de (−1, 0, 1) com (−1, 1, 0) (= 0,5) |
| 23 Projeção e MQ | **3** (reforçar) | 2·0·0·1·0 | erro grande ou pequeno (palpite); comparador de erro | sem previsão; nada situado | exercícios com dados reais (horas de estudo × nota) |
| 24 Fourier | **3** (reforçar) | 2·0·0·1·0 | equalizador; notas escondidas; onda misteriosa | desafio trivial (ler o maior coeficiente) | desafio: num sinal de amplitudes 3 e 4, cortar a de 3 apaga quantos % da energia? (36) |
| 25 Determinante e autovalores | **4** (reforçar) | 2·1·0·0·1 | caça às setas que não giram; achatar o plano | desafio é a mesma conta do ex4; nada situado | desafio: para que s a matriz [[2, 1], [4, s]] não tem inversa? (s = 2) |
| 26 PCA | **1** (reforçar) | 0·0·0·0·1 | imagem comprimida | nenhuma meta, previsão ou sorteio | "ache a direção de maior variância" (PC1 escondida até o aluno chegar perto) |
| 27 Otimização | **6** (boa) | 1·2·1·0·2 | vale local e passo que explode (surpresas) | nada sorteado; exercícios sem situação | "desça a montanha no escuro" (partida sorteada, vence quem usar menos passos) |
| 28 EDOs | **4** (reforçar) | 0·1·1·0·2 | predador-presa, mola, remédio | nenhum lab com meta | "siga as setas" como preveja e confira (o aluno calcula o próximo y) |
| 29 Passeio aleatório | **6** (boa) | 0·1·1·1·3 | 5 labs sorteados (moeda, mil caminhantes, caudas gordas) | nenhum lab com meta | "aposte no intervalo": onde o caminhante estará depois de n passos (regra do √n) |
| 30 Pensar como matemático | **7** (boa) | 2·2·1·1·1 | verdadeiro/falso/depende, caça ao contraexemplo, Collatz | exercícios pouco situados | afirmações sorteadas no verdadeiro/falso |
| 31 RSA | **5** (reforçar) | 1·1·1·0·2 | RSA que volta; fatorar é difícil | na cifra de César o aluno cifra e o lab quebra sozinho | "missão espião": chave sorteada e escondida, o aluno descobre pelas barras |
| 32 Grafos | **6** (boa) | 2·0·2·0·2 | Königsberg, casinha e pintar a roda (quebra-cabeças) | Dijkstra e Kruskal só avançam com clique | Dijkstra e Kruskal como preveja e confira (o aluno escolhe o próximo passo) |
| 33 Grupos | **3** (reforçar) | 1·1·0·0·1 | chegar às 6 posições (coleção) | "é grupo ou não é?" revela sem pedir palpite | palpite antes do teste; exercícios com azulejo e cubo mágico |
| 34 Topologia | **3** (reforçar) | 0·2·1·0·0 | alfabeto de borracha; formiga na faixa de Möbius | sem meta; ex3 é decoreba | labirinto de Jordan como "dentro ou fora?" (pontos sorteados, placar) |
| 35 Curvatura | **3** (reforçar) | 0·2·1·0·0 | Groenlândia × África; triângulo de 270° | sem meta; exercícios de aplicar fórmula | "dirija na pista" (acompanhar a curvatura); aposta Groenlândia × Brasil |
| 36 Taylor | **2** (reforçar) | 1·1·0·0·0 | espiral de Euler com alvo | nada situado | desafio de Zenão (metade, metade do resto… = 1) |
| 37 EDPs | **2** (reforçar) | 0·1·1·0·0 | modos normais com notas musicais | sem meta | "afine a corda": nota-alvo sorteada |
| 38 Fractais | **2** (reforçar) | 0·1·0·0·1 | Koch: perímetro infinito, área finita | sem meta nem sorteio | "caça ao c": órbita presa por mais passos; exercício do litoral |
| 39 Cálculo estocástico | **3** (reforçar) | 0·1·1·1·0 | 3 labs sorteados; Monte Carlo × Black–Scholes | desafio é √9 (1 passo) | desafio de 2 passos (σ · √t) |
| 40 Métodos numéricos | **3** (reforçar) | 0·2·0·0·1 | 4 surpresas (Newton se perde, h ótimo, duas fórmulas, passo que explode) | nenhuma meta; a bisseção anda sozinha | bisseção como "mais alto/mais baixo" (o aluno escolhe a metade; placar de passos) |

### Defeitos encontrados e corrigidos nesta rodada (FATO)

- **09 "compare duas retas"** dizia "a reta A sobe mais rápido" com passo −4 (ela desce): o texto
  comparava o tamanho do passo, não o sinal. Agora diz quem sobe, quem desce e quem fica deitada.
- **13 ex6**: uma alternativa citava "exponencial", que só é apresentada na Aula 14 — fere a regra
  "nada é usado antes de ser apresentado". Trocada por "cúbica", vista na própria aula.
- **22 "nuvem de pontos"**: com "o quanto andam juntas" em 0 a correlação podia sair −0,54 e o texto
  chamava de "baixa, sem tendência". Agora o ruído é tornado perpendicular a x (correlação 0 de
  verdade em 0%) e o texto respeita o sinal.
- **16 "somador de ondas"**: o exercício cobra "ondas opostas se cancelam", mas o laboratório não
  tinha atraso. Ganhou o controle de atraso, a pergunta de previsão e texto que calcula a altura da
  soma (reforço 1 + A, cancelamento |1 − A|).
- **24 "monte uma onda"** ganhou texto que escreve a soma; e a própria Aula 24 dizia "a soma de
  ondas da Aula 24" — agora "do começo desta aula".
- **Escrita matemática:** 18 "√(−4² + 4²)" → "√((−4)² + 4²)"; 25 "2 · 1,5 − −2 · 0,5" →
  "− (−2) · 0,5"; 35 "0,8 · −0,6" → "0,8 · (−0,6)"; 17 "(3 · −1)" → "(3 · (−1))".
- **Português:** 17 "Triângulo girada/espelhada/esticada" → masculino; 14 "já passou de a Lua" →
  "da Lua" (e "do Monte Everest"); 21 "nas pilha do meio" → "na pilha do meio"; singular/plural
  em 04, 06, 21, 29, 30 e 31 ("1 bolinhas", "1 jogadas", "1 tentativas"…).

### Proposta para levar as 40 aulas à excelência lúdica (a aprovar)

Em ordem de impacto por esforço:

1. **Modo desafio nos laboratórios de exploração** (as 15 aulas sem meta): esconder a resposta até
   o aluno chegar lá, meta explícita, alvo sorteado e 🏆. Ex.: 01 "ache o primeiro encontro das
   engrenagens", 11 "estime o ângulo", 13 "parábola misteriosa", 15 "acerte a sombra", 26 "ache a
   direção de maior variância", 40 bisseção "mais alto/mais baixo".
2. **Preveja e confira nas simulações que andam sozinhas:** 28 Euler, 32 Dijkstra e Kruskal, 40
   bisseção — o aluno decide o próximo passo e o laboratório confere.
3. **Aposta registrada antes da surpresa** (curiosidade que vale ponto): 03 desconto × aumento, 14
   dobras até a Lua, 21 Galton, 29 caminhante, 33 "é grupo?", 35 Groenlândia.
4. **Exercícios situados:** pelo menos 2 por aula (hoje 30 aulas têm 0 ou 1), começando pelos 9
   desafios de um passo, com as situações da coluna "Proposta".
5. **Camada de jogo do curso:** medalha ao fechar cada nível, recorde de "acertos de primeira" do
   preveja e confira guardado no progresso e mostrado no painel do nível.

**INFERÊNCIA:** os itens 1 a 4 levam cada aula a pelo menos 1 laboratório com meta, 1 com previsão e 2
exercícios situados — pela rubrica, a média subiria de 4,3 para algo entre 7 e 8, com nenhuma aula
abaixo de 6. Continua valendo o limite de sempre: a rubrica mede o desenho da aula, não a
aprendizagem; isso só se mede com alunos (tempo, acerto de primeira e desistência por laboratório).

## O que ainda pode melhorar (2ª rodada, INFERÊNCIA)

- **Sem medida com alunos reais.** A rubrica mede o desenho da aula; tempo gasto, taxa de acerto de
  primeira e desistência por laboratório só aparecem com telemetria (o placar do "preveja e
  confira" calcula o acerto de primeira, mas não o guarda).
- Elementos **clicáveis** dentro de desenhos (barras do equalizador da 24, fórmula clicável da 07)
  têm botões equivalentes ou são complementares, mas não recebem foco eles mesmos.
