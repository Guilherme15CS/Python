import requests
from datetime import time, timedelta, datetime
import mysql.connector

a = 0
IToken = 'ec0b20b316c4bfee3301c9cd340bcbfd'

#Adicionar cidade
"""iURL = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{IToken}/locales" 
payload="localeId[]=3477" 
headers = {
'Content-Type': 'application/x-www-form-urlencoded'
}
iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
print(iRESPONSE.text)"""

#Ver qual cidade está alocada
"""link = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{IToken}/locales'
requisição = requests.get(link)
dados = requisição.json()
print(dados)"""

#Ver dados
link = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token={IToken}'
requi = requests.get(link)
dados = requi.json()
#print(dados)


#Parte para remover dias anteriores
for c in range (2, 7):
    conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clima15'
    )
    cursor = conexão.cursor()
    dia2 = dados['data'][a]['date_br']
    dia2 = datetime.strptime(dia2, "%d/%m/%Y")
    data = timedelta(days=c)
    deletar = dia2 - data
    deletar = datetime.date(deletar)
    deletar = deletar.strftime("%d/%m/%Y")
    deletar = str(deletar)

    comando = f'DELETE FROM elementos WHERE dia = "{deletar}"'
    cursor.execute(comando)
    conexão.commit()
    cursor.close()
    conexão.close()

#Pegar dado e adicionar no banco de dados
while a != 7:
    conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clima15'
    )
    cursor = conexão.cursor()

    dia3 = dados['data'][a]['date_br']

    comando = f'DELETE FROM elementos WHERE dia = "{dia3}"'
    cursor.execute(comando)
    conexão.commit()


    #Mostra a localização
    cidade = dados['name']
    estado = dados['state']
    junção = f'{cidade},{estado}'

    #Mostrar o dia
    dia = dados['data'][a]['date_br']
    #print(dia)

    #Mostrar humidade
    humidademin = dados['data'][a]['humidity']['min']
    humidademax = dados['data'][a]['humidity']['max']
    #print(f'{humidademin}%')
    #print(f'{humidademax}%')

    # Mostrar pressão
    pressão = dados['data'][a]['pressure']['pressure']
    #print(f'{pressão}hPa')

    #Mostrar chuva
    precipitação = dados['data'][a]['rain']['precipitation']
    probachu = dados['data'][a]['rain']['probability']
    #print(f'{precipitação}mm')
    #print(f'{probachu}%')

    #Mostrar vento
    ventomin = dados['data'][a]['wind']['velocity_min']
    ventomax = dados['data'][a]['wind']['velocity_max']
    ventomedia = dados['data'][a]['wind']['velocity_avg']
    ventodire = dados['data'][a]['wind']['direction']
    #print(f'{ventomin}Km/h')
    #print(f'{ventomax}Km/h')
    #print(f'{ventomedia}Km/h')
    #print(ventodire)

    #Mostrar UV
    uv = dados['data'][a]['uv']['max']
    #print(uv)

    #Mostrar sensação térmica
    sensaçãomin = dados['data'][a]['thermal_sensation']['min']
    sensaçãomax = dados['data'][a]['thermal_sensation']['max']
    #print(f'{sensaçãomin}°C')
    #print(f'{sensaçãomax}°C')

    #Mostrar descrição
    condição = dados['data'][a]['text_icon']['text']['pt']
    #print(condição)

    #Mostrar temperatura
    temperaturamin = dados['data'][a]['temperature']['min']
    temperaturamax = dados['data'][a]['temperature']['max']
    #print(f'{temperaturamin}°C')
    #print(f'{temperaturamax}°C')

    #Nascer do Sol
    nascersol = dados['data'][a]['sun']['sunrise']
    dia_datanasc = f"{dia} {nascersol}"
    #print(dia_datanasc)
    dia_datanasc = datetime.strptime(dia_datanasc, "%d/%m/%Y %H:%M:%S")
    fuso = timedelta(hours=3)
    dia_datanasc = dia_datanasc - fuso
    dia_datanasc = str(dia_datanasc)
    #print(dia_datanasc[11::])

    #Pôr do Sol
    porsol = dados['data'][a]['sun']['sunset']
    dia_datapor = f'{dia} {porsol}'
    #print(dia_datapor)
    dia_datapor = datetime.strptime(dia_datapor, "%d/%m/%Y %H:%M:%S")
    fuso = timedelta(hours=3)
    dia_datapor = dia_datapor - fuso
    dia_datapor = str(dia_datapor)
    #print(dia_datapor[11::])

    #Adicionar dados
    comando = f'INSERT INTO elementos (Localização, Dia, Humidade_min, Humidade_max, Pressão, Precipitação, Probabilidade_chuva, Velocidade_Vento_min, Velocidade_Vento_max, Velocidade_Vento_media, Direção_Vento, Índicie_UV, Sensação_termica_min, Sensação_termica_max, Descrição, Temperatura_min, Temperatura_max, Nascer_Sol, Por_Sol) VALUES ("{junção}", "{dia}", "{humidademin}%", "{humidademax}%", "{pressão}hPa", "{precipitação}mm", "{probachu}%", "{ventomin}Km/h", "{ventomax}Km/h", "{ventomedia}km/h", "{ventodire}", "{uv}", "{sensaçãomin}°C", "{sensaçãomax}°C", "{condição}", "{temperaturamin}°C", "{temperaturamax}°C", "{dia_datanasc[11::]}", "{dia_datapor[11::]}")'
    cursor.execute(comando)
    conexão.commit()
    cursor.close()
    conexão.close()
    a += 1
