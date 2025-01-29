import requests
import mysql.connector
import schedule

API_KEY = 'ffe643565572f5adffa9a018faad822e'
cidade = 'São Paulo'

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric'

requisição = requests.get(link)
dados = requisição.json()
#print(dados)
descrição = dados['weather'][0]['description']
temperatura = dados['main']['temp']
temperatura = int(temperatura)
# print(descrição)
# print(temperatura)
# print(f'{descrição}, {temperatura}°C')

conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clima'
)

cursor = conexão.cursor()

#Adicionar cidade
'''comando = f'INSERT INTO informações (Cidade, Temperatura, Condição) VALUES ("{cidade}", {temperatura}, "{descrição}")'
cursor.execute(comando)
conexão.commit()
cursor.close()
conexão.close()'''

# Atualizar clima
comando = f'UPDATE informações SET Temperatura = {temperatura} WHERE Cidade = "São Paulo"'
cursor.execute(comando)
conexão.commit()
comando = f'UPDATE informações SET Condição = "{descrição}" WHERE Cidade = "São Paulo"'
cursor.execute(comando)
conexão.commit()
cursor.close()
conexão.close()
