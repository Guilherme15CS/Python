import requests

link = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/distritos'
requi = requests.get(link)
dados = requi.json()
print(dados)