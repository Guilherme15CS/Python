import requests
import json
from datetime import datetime

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
#print(cotacoes)
cotacao_dolar = cotacoes['USDBRL']['bid']
print(f'A cotação atual do Dólar é {cotacao_dolar}')
cotacao_euro = cotacoes['EURBRL']['bid']
print(f'A cotação do Euro é {cotacao_euro}')
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
print(f'A cotação do Bitcoin é {cotacao_bitcoin}')
print(f'Cotação de {datetime.now()}')
