from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import random
import webcolors
import ConnectionAPIGoogle
import Interface

def gerar_nome_cores(tamanho):
    listCollors = []
    for nome_cor in webcolors.CSS3_NAMES_TO_HEX.keys():
        listCollors.append(nome_cor)

    cores = listCollors
    collorPrefix = ('light', 'white')
    for collor in cores:
        if collor.startswith(collorPrefix):
            cores.remove(collor)

    random.shuffle(cores)
    nomes_cores = cores[:tamanho]
    return nomes_cores

sentencesSentiment = []
sentences = Interface.interfaceFrases()
idioma = Interface.interfaceIdioma()

if idioma == "":
    idioma = "en"

print(sentences)
if not sentences:
    Interface.interfaceNula()
    exit()

jsonGoogle = ConnectionAPIGoogle.callGoogleApi(sentences, idioma)
data = jsonGoogle['data']
translations = data['translations']

for i in translations:
    stringEncode = i['translatedText']
    if stringEncode.find("&#39;"):
        stringEncode = stringEncode.replace("&#39;", "'")
    sentencesSentiment.append(stringEncode)

# Criando uma lista para armazenar os resultados de análise de sentimentos
resultadosTextBlob = []
resultadosVader = []
sia = SentimentIntensityAnalyzer()
tamanho_array = len(sentencesSentiment)
nomes_cores_aleatorios = gerar_nome_cores(tamanho_array)

# Analisando o sentimento de cada frase na lista.
for frase in sentencesSentiment:
    #Análise TextBlob
    tb_polarity = TextBlob(frase).sentiment.polarity
    pontuacao = tb_polarity
    resultadosTextBlob.append(pontuacao)

    #Análise Vader
    vs = sia.polarity_scores(frase)
    vader_polarity = vs['compound']
    resultadosVader.append(vader_polarity)

# Adicionando as cores às barras dos gráficos.
bar_labels = nomes_cores_aleatorios
bar_colors = nomes_cores_aleatorios

# Setando os resultados nos gráficos.
#Gráfico 1, referente ao Vader
fig, ax = plt.subplots()
ax.bar(range(len(resultadosVader)), resultadosVader, label=bar_labels, color=bar_colors)
ax.set_ylim(-1, 1)
ax.set_ylabel('Polaridade')
ax.set_title('Resultado de Análise de sentimentos usando Vander')
ax.set_xlabel('Frases')
ax.legend(sentences)

#Gráfico 2, referente ao TextBlob
fig2, ax2 = plt.subplots()
ax2.bar(range(len(resultadosTextBlob)), resultadosTextBlob, label=bar_labels, color=bar_colors)
ax2.set_ylim(-1, 1)
ax2.set_ylabel('Polaridade')
ax2.set_xlabel('Frases')
ax2.set_title('Resultado de Análise de sentimentos usando TextBlob')
ax2.legend(sentences)

plt.show()
