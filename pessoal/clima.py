import requests

API_KEY = 'ffe643565572f5adffa9a018faad822e'
cidade = 'São Paulo'

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisição = requests.get(link)
dados = requisição.json()
# print(dados)
descrição = dados['weather'][0]['description']
temperatura = dados['main']['temp'] -273.15
# print(descrição)
# print(temperatura)
print(f'{descrição}, {temperatura}°C')
