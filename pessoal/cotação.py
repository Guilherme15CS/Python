import requests
import json
from datetime import datetime
import schedule


def dolar():
    print(f'A cotação atual do Dólar é {cotacao_dolar}')


def euro():
    print(f'A cotação do Euro é {cotacao_euro}')


def bitcoin():
    print(f'A cotação do Bitcoin é {cotacao_bitcoin}')


def dia():
    print(f'Cotação do dia {datetime.now()}')

    
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
#print(cotacoes)
cotacao_dolar = cotacoes['USDBRL']['bid']
#print(f'A cotação atual do Dólar é {cotacao_dolar}')
cotacao_euro = cotacoes['EURBRL']['bid']
#print(f'A cotação do Euro é {cotacao_euro}')
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
#print(f'A cotação do Bitcoin é {cotacao_bitcoin}')
#print(f'Cotação de {datetime.now()}')

schedule.every(1).minutes.do(dolar)
schedule.every(1).minutes.do(euro)
schedule.every(1).minutes.do(bitcoin)
schedule.every(1).minutes.do(dia)

while True:
    schedule.run_pending()
