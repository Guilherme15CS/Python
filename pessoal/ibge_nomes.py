import requests

link = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/guilherme?sexo=M'
requi = requests.get(link)
dados = requi.json()
print(dados[0]['res'][8])