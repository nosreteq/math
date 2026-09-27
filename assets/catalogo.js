/*
 * catalogo.js — fonte única dos níveis e aulas do curso.
 * Lido pela SPA (index.html) e pela barra das aulas abertas avulsas (menu.js).
 * Aula sem "slug" ainda não existe: aparece como "em breve".
 * CATALOGO_ANTIGOS mapeia os endereços da numeração anterior (18 aulas) para os novos.
 */
window.CATALOGO = [
  {
    n: 1, nome: "Fundamentos", etapa: "Ensino Fundamental I e II", estado: "completo",
    resumo: "Conta com qualquer tipo de número — primos, frações, negativos, porcentagem, potências — e o resumo de uma lista de dados.",
    aulas: [
      { n: 1, slug: "01-multiplos-divisores-e-primos", titulo: "Múltiplos, divisores e primos", desc: "Quem cabe dentro de quem: pulos na reta, o crivo dos primos, engrenagens (MMC) e ladrilhos (MDC)." },
      { n: 2, slug: "02-fracoes-decimais-e-negativos", titulo: "Pedaços e sinais: frações, decimais e negativos", desc: "Pizza, régua e termômetro: todo tipo de número morando na mesma reta." },
      { n: 3, slug: "03-porcentagem-razao-e-regra-de-tres", titulo: "Porcentagem, razão e regra de três", desc: "Desconto, receita de bolo e mapa são a mesma conta: comparar por divisão." },
      { n: 4, slug: "04-potencias-e-raizes", titulo: "Potências e raízes", desc: "Ao quadrado é um quadrado, ao cubo é um cubo, e a raiz é o lado deles. Mais: números gigantes com potências de 10." },
      { n: 5, slug: "05-dados-media-mediana-moda-e-desvio", titulo: "Dados: média, mediana, moda e desvio", desc: "Resumir uma lista em poucos números — e descobrir o que cada resumo esconde." },
      { n: 6, slug: "06-contagem-e-chance", titulo: "Contagem e chance", desc: "Árvores de possibilidades, filas e moedas: o acaso tem régua." }
    ]
  },
  {
    n: 2, nome: "Álgebra e Geometria", etapa: "Ensino Fundamental II", estado: "completo",
    resumo: "Letras no lugar de números, equações, o plano cartesiano e as medidas de figuras no plano e no espaço.",
    aulas: [
      { n: 7, slug: "07-letras-no-lugar-de-numeros", titulo: "Letras no lugar de números: a função", desc: "A máquina de números, aquele f(x) que assustou você na escola, a regra de ouro e o primeiro gráfico." },
      { n: 8, slug: "08-equacoes-e-inequacoes", titulo: "Equações e inequações: a balança", desc: "Descobrir o número escondido sem chute — e o que muda quando a balança pende." },
      { n: 9, slug: "09-o-plano-e-a-reta", titulo: "O plano e a reta", desc: "As duas réguas, o endereço de um ponto e a receita que descreve qualquer linha reta." },
      { n: 10, slug: "10-sistemas-de-equacoes", titulo: "Sistemas de equações", desc: "Resolver duas equações ao mesmo tempo é só achar onde duas retas se cruzam." },
      { n: 11, slug: "11-angulos-circulo-e-pi", titulo: "Ângulos, círculo e π", desc: "O que é girar, por que a volta tem 360° e de onde sai o π." },
      { n: 12, slug: "12-areas-volumes-e-pitagoras", titulo: "Áreas, volumes e Pitágoras", desc: "Toda figura é um retângulo arrumado — e três quadrados guardam o segredo do triângulo retângulo." }
    ]
  },
  {
    n: 3, nome: "Ensino Médio", etapa: "Ensino Médio", estado: "completo",
    resumo: "O comportamento das funções clássicas, trigonometria, vetores e matrizes e os números que giram.",
    aulas: [
      { n: 13, slug: "13-curvas-que-nao-sao-retas", titulo: "Curvas que não são retas", desc: "Parábolas e polinômios: a máquina de sempre com um quadrado dentro." },
      { n: 14, slug: "14-crescimento-que-acelera", titulo: "Crescimento que acelera", desc: "PA e PG, juros simples e compostos, exponenciais e logaritmos." },
      { n: 15, slug: "15-trigonometria", titulo: "Trigonometria: seno, cosseno, tangente e radianos", desc: "A altura, a sombra e a inclinação de um ponto girando — medidas em graus e em radianos." },
      { n: 16, slug: "16-ondas", titulo: "Ondas", desc: "Desenrolando o círculo: o giro vira onda. Altura, largura e atraso." },
      { n: 17, slug: "17-vetores-e-matrizes", titulo: "Vetores e matrizes", desc: "Vetor é uma seta. Matriz é uma tabela que move setas. Álgebra linear desmistificada." },
      { n: 18, slug: "18-girar-multiplicando", titulo: "Girar multiplicando: números complexos", desc: "A raiz de −1 é só um jeito de escrever \"gire 90°\"." }
    ]
  },
  {
    n: 4, nome: "Superior I", etapa: "Faculdade: cálculo e dados", estado: "completo",
    resumo: "Limites, derivadas e integrais, a curva normal e a extração de padrões em dados.",
    aulas: [
      { n: 19, slug: "19-limites-e-a-derivada", titulo: "Limites e a derivada", desc: "A lupa que endireita a curva: a inclinação em cada ponto." },
      { n: 20, slug: "20-a-integral", titulo: "A integral", desc: "Somar fatias cada vez mais finas — e o caminho de volta da derivada." },
      { n: 21, slug: "21-a-curva-normal", titulo: "A curva normal", desc: "Pascal, Galton e o sino: milhares de acasos desenham sempre a mesma curva." },
      { n: 22, slug: "22-correlacao", titulo: "Correlação: estatística com vetores", desc: "Correlação é só o cosseno do ângulo entre duas listas de números." },
      { n: 23, slug: "23-projecao-e-minimos-quadrados", titulo: "Projeção e mínimos quadrados", desc: "A reta que melhor se ajusta aos pontos é geometria de sombra." },
      { n: 24, slug: "24-fourier", titulo: "Decomposição de sinais: Fourier", desc: "Todo som complicado é várias ondas simples somadas — ou setas girando." }
    ]
  },
  {
    n: 5, nome: "Superior II", etapa: "Faculdade: aplicada e computacional", estado: "completo",
    resumo: "Transformações, dados em muitas dimensões, otimização, sistemas que mudam no tempo, o acaso no tempo e a demonstração.",
    aulas: [
      { n: 25, slug: "25-determinante-inversa-e-autovalores", titulo: "Matrizes que transformam", desc: "Determinante é área, inversa desfaz, autovetor é a seta que só estica." },
      { n: 26, slug: "26-pca", titulo: "PCA: as direções principais", desc: "A direção mais comprida de uma nuvem de pontos — e como resumir muitos dados em poucos." },
      { n: 27, slug: "27-otimizacao-e-gradiente", titulo: "Otimização: descer a ladeira", desc: "Curvas de nível, a seta do gradiente e o tamanho do passo." },
      { n: 28, slug: "28-equacoes-diferenciais", titulo: "Equações diferenciais e o método de Euler", desc: "Quando a regra fala da inclinação: campos de setinhas, molas e populações." },
      { n: 29, slug: "29-passeio-aleatorio", titulo: "Acaso no tempo: passeio aleatório", desc: "Uma moeda que anda: o √n do espalhamento e o movimento browniano." },
      { n: 30, slug: "30-pensar-como-matematico", titulo: "Pensar como matemático", desc: "Contraexemplo, demonstração, indução e os problemas que ninguém resolveu." }
    ]
  }
];

/* endereços da numeração anterior (18 aulas) → aula nova correspondente */
window.CATALOGO_ANTIGOS = {
  "01-o-que-e-uma-funcao": "07-letras-no-lugar-de-numeros",
  "02-desenhar-numeros-no-papel": "09-o-plano-e-a-reta",
  "03-angulos-e-o-circulo": "11-angulos-circulo-e-pi",
  "04-seno-e-cosseno": "15-trigonometria",
  "05-ondas": "16-ondas",
  "06-setas-e-tabelas-de-numeros": "17-vetores-e-matrizes",
  "07-equacoes-a-balanca": "08-equacoes-e-inequacoes",
  "08-sistemas-de-equacoes": "10-sistemas-de-equacoes",
  "09-potencias-raizes-e-pitagoras": "04-potencias-e-raizes",
  "10-estatistica-com-vetores": "22-correlacao",
  "11-projecao-e-minimos-quadrados": "23-projecao-e-minimos-quadrados",
  "12-decomposicao-de-sinais-em-ondas": "24-fourier",
  "15-a-inclinacao-em-cada-ponto": "19-limites-e-a-derivada",
  "16-somando-fatias": "20-a-integral",
  "17-acaso-com-regua": "21-a-curva-normal"
};
