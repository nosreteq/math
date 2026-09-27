# Matemática do Zero

Um curso de matemática construído do chão para cima, para quem só sabe as quatro operações
(somar, subtrair, multiplicar e dividir) e quer chegar até **trigonometria** e **álgebra linear**
sem passar por nenhuma etapa no escuro.

Cada aula é uma **página HTML interativa e autocontida**: você mexe nos controles, o gráfico
responde na hora, e os exercícios se corrigem sozinhos com explicação do erro. O formato é
inspirado na série *Head First* da O'Reilly — muita ilustração, linguagem de conversa, o Guru
soltando uma frase no meio do caminho e nenhuma fórmula caindo do céu.

---

## Aulas

O curso é dividido em níveis. Dentro de cada nível, cada aula resolve exatamente um obstáculo, sem
usar nada que não tenha sido apresentado numa aula anterior — nem entre níveis.

### Nível 1 — Básico ✅

| # | Aula | Assunto | Estado |
|---|------|---------|--------|
| 01 | [O que é uma função](aulas/01-o-que-e-uma-funcao/) | A máquina de números, a notação `f(x)`, a regra de ouro e o primeiro gráfico | ✅ pronta |
| 02 | [Desenhar números no papel](aulas/02-desenhar-numeros-no-papel/) | As duas réguas, números negativos, o passo da escada e a receita de qualquer reta | ✅ pronta |
| 03 | [Ângulos e o círculo](aulas/03-angulos-e-o-circulo/) | O que é girar, a volta completa, medir giro | ✅ pronta |
| 04 | [Seno e cosseno](aulas/04-seno-e-cosseno/) | A altura e a sombra de um ponto girando | ✅ pronta |
| 05 | [Ondas](aulas/05-ondas/) | Amplitude, frequência e fase | ✅ pronta |
| 06 | [Setas e tabelas de números](aulas/06-setas-e-tabelas-de-numeros/) | Vetores e matrizes | ✅ pronta |

### Nível 2 — Intermediário ✅

| # | Aula | Assunto | Estado |
|---|------|---------|--------|
| 07 | [Equações: a balança](aulas/07-equacoes-a-balanca/) | Isolar o x mantendo a balança equilibrada | ✅ pronta |
| 08 | [Sistemas de equações](aulas/08-sistemas-de-equacoes/) | Resolver = achar onde duas retas se cruzam | ✅ pronta |
| 09 | [Potências, raízes e Pitágoras](aulas/09-potencias-raizes-e-pitagoras/) | O quadrado, o lado dele e o tamanho de qualquer seta | ✅ pronta |
| 10 | [Estatística com vetores](aulas/10-estatistica-com-vetores/) | Média, desvio padrão e correlação como cosseno | ✅ pronta |
| 11 | [Projeção e mínimos quadrados](aulas/11-projecao-e-minimos-quadrados/) | Regressão como geometria de sombra | ✅ pronta |
| 12 | [Decomposição de sinais em ondas](aulas/12-decomposicao-de-sinais-em-ondas/) | Fourier como projeção sobre ondas | ✅ pronta |

O roteiro completo, com o que entra em cada aula, está em **[PLANO.md](PLANO.md)**.

---

## Como usar

**Jeito mais simples:** baixe o repositório e abra `index.html` no navegador. Não precisa de
servidor, nem de internet, nem instalar nada — cada aula é um arquivo único com todo o CSS e
JavaScript embutidos.

```bash
git clone https://github.com/nosreteq/math.git
cd math
# abra index.html no navegador
```

**Publicando no GitHub Pages:** em *Settings → Pages*, escolha a branch `main` e a pasta `/ (root)`.
O curso fica no ar em `https://nosreteq.github.io/math/`.

---

## Estrutura

```
math/
├── index.html                          página inicial com o índice do curso
├── README.md                           este arquivo
├── PLANO.md                            roteiro do curso, por níveis
│
├── aulas/
│   ├── 01-o-que-e-uma-funcao/
│   │   ├── index.html                  a aula interativa
│   │   ├── notas.md                    o texto da aula, para ler ou imprimir
│   │   └── figuras.png                 versão estática das ilustrações
│   │
│   ├── 02-desenhar-numeros-no-papel/       ] Nível 1 — Básico
│   ├── 03-angulos-e-o-circulo/             ]
│   ├── 04-seno-e-cosseno/                  ]
│   ├── 05-ondas/                           ]
│   ├── 06-setas-e-tabelas-de-numeros/      ]
│   ├── 07-equacoes-a-balanca/              ] Nível 2 — Intermediário
│   ├── 08-sistemas-de-equacoes/            ]
│   ├── 09-potencias-raizes-e-pitagoras/    ]
│   ├── 10-estatistica-com-vetores/         ]
│   ├── 11-projecao-e-minimos-quadrados/    ]
│   └── 12-decomposicao-de-sinais-em-ondas/ ]
│       (mesma estrutura: index.html, notas.md, figuras.png)
│
├── assets/
│   └── menu.js                         menu de navegação entre níveis e aulas
│
└── scripts/
    ├── README.md
    └── figuras_aula01.py .. figuras_aula12.py    gera o figuras.png de cada aula (matplotlib)
```

Cada aula tem três formas do mesmo conteúdo:

- **`index.html`** — a aula de verdade, com os laboratórios e os exercícios corrigidos.
- **`notas.md`** — o mesmo conteúdo em texto corrido, bom para revisar no celular ou imprimir.
- **`figuras.png`** — as ilustrações num arquivo só, para colar num caderno ou num slide.

---

## O que tem dentro de uma aula

Cada página segue sempre a mesma anatomia:

- **Laboratórios** 🔧 — controles que mexem no desenho ao vivo. É onde a ideia entra de verdade.
- **O Guru** — uma frase que arruma a cabeça no momento certo.
- **Não existe pergunta idiota** — as dúvidas que sempre aparecem, respondidas antes de você perguntar.
- **Cuidado** ⚠️ — as armadilhas clássicas, marcadas antes de você cair nelas.
- **Pontos importantes** — o resumo da aula em uma tela.
- **Afie o lápis** ✏️ — exercícios com correção na hora: errou, sacode e explica; acertou, ganha selo.

---

## Princípios do curso

1. **Nada de decorar.** Se você entendeu, a fórmula vem sozinha depois. Se decorou sem entender,
   esquece em uma semana.
2. **Nenhum passo pulado.** Todo símbolo novo é apresentado antes de ser usado.
3. **O desenho vem antes da fórmula.** Primeiro você vê a coisa acontecer, depois escreve.
4. **Errar é de graça.** Os exercícios explicam o erro em vez de só marcar em vermelho.
5. **Tudo offline.** Nenhuma aula depende de internet, CDN ou biblioteca externa.

---

## Reconstruindo as figuras

As imagens estáticas são geradas por scripts em Python. Detalhes em
[`scripts/README.md`](scripts/README.md).

```bash
pip install matplotlib numpy
cd scripts
for n in 01 02 03 04 05 06 07 08 09 10 11 12; do python3 figuras_aula$n.py; done
```

---

## Licença

MIT — veja [LICENSE](LICENSE). Use, copie, adapte e ensine alguém.
