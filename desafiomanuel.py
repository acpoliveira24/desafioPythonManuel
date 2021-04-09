import nltk
#nltk.download('all')
import json
from basededados import base

# Tira da análise palavras que não trazem informações relevantes
stopwords = nltk.corpus.stopwords.words('portuguese')

sentenca = input('Descreva como se sente: ')


# Remove os afixos das palavras, deixando apenas os radicais da base de dados
def faz_stemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    listastemming = []
    for (palavras, sintomas) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwords]
        listastemming.append((comstemming, sintomas))
    return listastemming


frasesstemming = faz_stemmer(base)
#print(frasesstemming)


# Organiza as palavras após o stem em uma lista
def busca_palavras(frases):
    todaspalavras = []
    for (palavras, sintomas) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras


frases = busca_palavras(frasesstemming)
#print(frases)


# Calcula a frequência de cada palavra na lista
def busca_frequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras


frequencia = busca_frequencia(frases)


# Faz com que cada palavra apareça uma única vez
def busca_palavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq


palavrasunicas = busca_palavrasunicas(frequencia)


# Classifica se uma palavra está ou não na lista de palavras únicas
def extrai_palavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


# Função da biblioteca para classificar elementos das frases de acordo com as entidades
basecompleta = nltk.classify.util.apply_features(extrai_palavras, frasesstemming)
classificador = nltk.NaiveBayesClassifier.train(basecompleta)
#print(basecompleta)
#print(classificador.labels())
#print(classificador.show_most_informative_features(5))

# Faz o stem na sentença do usuário e coloca numa lista
sentencastem = []
stemmer = nltk.stem.RSLPStemmer()

for (palavras) in sentenca.split():
    comstem = [p for p in palavras.split()]
    sentencastem.append(str(stemmer.stem(comstem[0])))

nova_frase = extrai_palavras(sentencastem)
#print(nova_frase)

listasintomas = {}
sintomasdict = {}

# Aplica o classificador e a base de dados na sentença do usuário e adiciona os com confiança maior em um dicionário
distribuicao = classificador.prob_classify(nova_frase)
for classe in distribuicao.samples():
    print("%s: %.3f" % (classe, distribuicao.prob(classe)))
    if distribuicao.prob(classe) >= 0.1:
        listasintomas.update({classe: round(distribuicao.prob(classe), 3)})

sintomasdict.update({'sintomas': listasintomas})

# Cria o arquivo json com os sintomas de maior confiança
with open('sintomas.json', 'w', encoding='utf-8') as json_file:
    json.dump(sintomasdict, json_file, ensure_ascii=False, indent=4)
