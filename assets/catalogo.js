/*
 * catalogo.js — fonte única dos níveis e aulas do curso.
 * Lido pela SPA (index.html) e pela barra das aulas abertas avulsas (menu.js).
 * Aula sem "slug" ainda não existe: aparece como "em breve".
 */
window.CATALOGO = [
  {
    n: 1, nome: "Básico", estado: "completo",
    resumo: "Das quatro operações até trigonometria e álgebra linear. Seis aulas, sem pular nenhum degrau.",
    aulas: [
      { n: 1, slug: "01-o-que-e-uma-funcao", titulo: "O que é uma função", desc: "A máquina de números, aquele f(x) que assustou você na escola, a regra de ouro e o seu primeiro gráfico." },
      { n: 2, slug: "02-desenhar-numeros-no-papel", titulo: "Desenhar números no papel", desc: "As duas réguas, o endereço de um ponto, os números negativos e a receita que descreve qualquer linha reta do mundo." },
      { n: 3, slug: "03-angulos-e-o-circulo", titulo: "Ângulos e o círculo", desc: "O que é girar, por que a volta inteira tem 360, e onde o ponto para depois de girar tanto." },
      { n: 4, slug: "04-seno-e-cosseno", titulo: "Seno e cosseno", desc: "As duas palavras mais assustadoras da matemática viram só isto: a altura e a sombra de um ponto girando." },
      { n: 5, slug: "05-ondas", titulo: "Ondas", desc: "Desenrolando o círculo: o giro vira onda. Altura, largura e o quanto ela está atrasada." },
      { n: 6, slug: "06-setas-e-tabelas-de-numeros", titulo: "Setas e tabelas de números", desc: "Vetor é uma seta. Matriz é uma tabela que move setas. Pronto, álgebra linear desmistificada." }
    ]
  },
  {
    n: 2, nome: "Intermediário", estado: "completo",
    resumo: "Equações, sistemas, potências e Pitágoras, estatística, regressão e decomposição de ondas — reencontrando o Nível 1 o tempo todo.",
    aulas: [
      { n: 7, slug: "07-equacoes-a-balanca", titulo: "Equações: a balança", desc: "Descobrir o número escondido sem chute: o que fizer de um lado, faça do outro." },
      { n: 8, slug: "08-sistemas-de-equacoes", titulo: "Sistemas de equações", desc: "Resolver duas equações ao mesmo tempo é só achar onde duas retas se cruzam." },
      { n: 9, slug: "09-potencias-raizes-e-pitagoras", titulo: "Potências, raízes e Pitágoras", desc: "Ao quadrado é um quadrado de verdade, a raiz é o lado dele, e o triângulo retângulo mede qualquer seta." },
      { n: 10, slug: "10-estatistica-com-vetores", titulo: "Estatística com vetores", desc: "Média, desvio padrão e correlação — que é só o cosseno do ângulo entre dois vetores." },
      { n: 11, slug: "11-projecao-e-minimos-quadrados", titulo: "Projeção e mínimos quadrados", desc: "A reta que melhor se ajusta aos pontos não precisa de cálculo avançado — é geometria de sombra." },
      { n: 12, slug: "12-decomposicao-de-sinais-em-ondas", titulo: "Decomposição de sinais em ondas", desc: "Todo som complicado é várias ondas simples somadas — e a projeção desmonta a soma de volta." }
    ]
  },
  {
    n: 3, nome: "Avançado", estado: "completo",
    resumo: "Curvas que dobram, crescimento que acelera, a inclinação em cada ponto, a área acumulada, o acaso com régua e um número que gira quando multiplica.",
    aulas: [
      { n: 13, slug: "13-curvas-que-nao-sao-retas", titulo: "Curvas que não são retas", desc: "Parábolas e polinômios: a máquina da Aula 1 com um quadrado dentro." },
      { n: 14, slug: "14-crescimento-que-acelera", titulo: "Crescimento que acelera", desc: "Exponenciais e logaritmos: somar sempre o mesmo contra multiplicar sempre pelo mesmo." },
      { n: 15, slug: "15-a-inclinacao-em-cada-ponto", titulo: "A inclinação em cada ponto", desc: "A derivada — e os radianos, a medida de ângulo que faz tudo encaixar." },
      { n: 16, slug: "16-somando-fatias", titulo: "Somando fatias", desc: "A integral: a área debaixo de uma curva, cortada em fatias cada vez mais finas." },
      { n: 17, slug: "17-acaso-com-regua", titulo: "Acaso com régua", desc: "Probabilidade e a curva normal: milhares de acasos desenham sempre o mesmo sino." },
      { n: 18, slug: "18-girar-multiplicando", titulo: "Girar multiplicando", desc: "Números complexos: a raiz de −1 é só um jeito de escrever \"gire 90°\"." }
    ]
  }
];
