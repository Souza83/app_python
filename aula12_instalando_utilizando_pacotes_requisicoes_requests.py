# Instalando e utilizando pacotes em Python e realizar requisição com requests
import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json()) # traz em formato de dicionario
    print(type(response.json())) # traz em formato de dicionario
    # print(response.text) # traz em formato de string
    # print(type(response.text)) # traz em formato de string
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.rocketseat.com.br/')
    print(response)
    #retorna_dados_cep(89251701)
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])

