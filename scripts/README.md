# scripts

Geradores das figuras estáticas (`figuras.png`) de cada aula, em Python com matplotlib.

As aulas em HTML **não dependem destes scripts** — os desenhos interativos são feitos em SVG puro,
direto no navegador. Estes arquivos existem para reproduzir a versão em imagem, útil para imprimir,
colar num caderno ou usar num slide.

## Requisitos

```bash
pip install -r requirements.txt
```

## Uso

Você pode rodar os scripts a partir de qualquer pasta (da raiz ou de dentro de `scripts/`):

```bash
# A partir da raiz do projeto:
python scripts/figuras_aula01.py
python scripts/figuras_aula02.py
python scripts/figuras_aula03.py
python scripts/figuras_aula04.py
python scripts/figuras_aula05.py
python scripts/figuras_aula06.py
python scripts/figuras_aula07.py
python scripts/figuras_aula08.py
python scripts/figuras_aula09.py
python scripts/figuras_aula10.py
python scripts/figuras_aula11.py
python scripts/figuras_aula12.py
python scripts/figuras_aula13.py
python scripts/figuras_aula14.py
python scripts/figuras_aula15.py
python scripts/figuras_aula16.py
python scripts/figuras_aula17.py
python scripts/figuras_aula18.py

# Ou de dentro da pasta scripts:
cd scripts
python figuras_aula01.py
python figuras_aula02.py
python figuras_aula03.py
python figuras_aula04.py
python figuras_aula05.py
python figuras_aula06.py
python figuras_aula07.py
python figuras_aula08.py
python figuras_aula09.py
python figuras_aula10.py
python figuras_aula11.py
python figuras_aula12.py
python figuras_aula13.py
python figuras_aula14.py
python figuras_aula15.py
python figuras_aula16.py
python figuras_aula17.py
python figuras_aula18.py
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
