# Desafio Python: NLP

Código em Python que extrai informação de sintomas em um texto de um paciente. O texto é lido e gera um arquivo .json com os principais sintomas descritos pelo usuário e o nível de confiança.

## Instruções

### Instalação

Foi usada a biblioteca nltk que necessita de instalação para rodar. Link com instruções para instalação da biblioteca e dos dados em diferentes sistemas:

https://www.nltk.org/install.html

https://www.nltk.org/data.html

### Implementação

Para implementar, deve-se importar a biblioteca nltk e json. É utilizado um banco de dados próprio que está em um arquivo separado na mesma pasta e que está na forma de lista, sendo necessário importar essa lista também. A importação é demonstrada abaixo.

```python
import nltk
#nltk.download('all')
import json
from basededados import base
```

⚠️ É NECESSÁRIO MANTER OS ARQUIVOS desafiomanuel.py E basededados.py NA MESMA PASTA!

Na primeira vez em que for executar o código, deve-se remover o comentário e executar o comando nltk.download('all') para que seja feito o download dos pacotes da biblioteca. Isso é necessário somente na primeira vez, podendo ser adicionado como comentário novamente nas vezes seguintes.

### Observações

O código funciona através do input do usuário com um texto descrevendo como ele se sente. E cria um arquivo chamado sintomas.json na mesma pasta em que estão os arquivos. O texto do usuário usado como base está no arquivo usuario.txt.

A base de dados foi feita com os seguintes sintomas:

- febre
- náusea
- diarreia
- obstipação
- mucosite
- fraqueza
- dispneia
- dor de cabeça
- tosse
- vômito

Ao longo do código há comentários descrevendo cada parte e também há comentários de prints de cada parte, caso queira ver o que foi gerado em cada etapa.