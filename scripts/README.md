# scripts

Geradores das figuras estáticas (`figuras.png`) de cada aula, em Python com matplotlib.

As aulas em HTML **não dependem destes scripts** — os desenhos interativos são feitos em SVG puro,
direto no navegador. Estes arquivos existem para reproduzir a versão em imagem, útil para imprimir,
colar num caderno ou usar num slide.

## Requisitos

```bash
pip install matplotlib numpy
```

## Uso

Rode de dentro desta pasta — os caminhos de saída são relativos a ela:

```bash
cd scripts
python3 figuras_aula01.py    # grava ../aulas/01-o-que-e-uma-funcao/figuras.png
python3 figuras_aula02.py    # grava ../aulas/02-desenhar-numeros-no-papel/figuras.png
```

Cada script usa o backend `Agg`, então funciona em servidor sem tela.

## Convenções dos desenhos

Para manter as aulas coerentes entre si:

| cor | hex | uso |
|---|---|---|
| verde | `#059669` | o número que **entra**, movimento **horizontal** |
| vermelho | `#dc2626` | o número que **sai**, movimento **vertical** |
| azul | `#2563eb` | a função em si (pontos, retas, gráfico) |
| laranja | `#d97706` | anotações e destaques secundários |
| roxo | `#7c3aed` | o Guru e o ponto de cruzamento |

Resolução padrão: 150 dpi, fundo branco.
