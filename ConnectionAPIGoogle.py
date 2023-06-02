import requests

def callGoogleApi(sentences, targetLanguage):
    #Criar parametro de target language
    # Define a URL de endpoint
    url = "https://translation.googleapis.com/language/translate/v2"

    # Define os parâmetros da solicitação POST
    params = {
        "key": "AIzaSyBc6OzAmOyqnQ_RtnonNlPemi3tr6qDqWc", #Substitua pela sua chave de API
        "source": "pt", #Idioma de origem
        "target": targetLanguage, #Idioma de destino
        "q": sentences #Texto a ser traduzido,
    }
    # Envia a solicitação POST
    response = requests.post(url, params=params)

    # Imprime o resultado da solicitação
    return response.json()