import requests
import json
import mysql.connector

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
#print(cotacoes)
cotacao_dolar = cotacoes['USDBRL']['bid']
#print(f'A cotação atual do Dólar é {cotacao_dolar}')
cotacao_euro = cotacoes['EURBRL']['bid']
#print(f'A cotação do Euro é {cotacao_euro}')
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
#print(f'A cotação do Bitcoin é {cotacao_bitcoin}')

conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste'
)
cursor = conexão.cursor()
# Adicionar Moeda
# comando = f'INSERT INTO moedas (Nome_moeda, Valor) VALUES ("{cotacoes['BTCBRL']['code']}", {cotacao_bitcoin})'
# cursor.execute(comando)
# conexão.commit()


# Mudar valor da moeda
comando = f'UPDATE moedas SET valor = {cotacao_dolar} WHERE Nome_moeda = "USD"'
cursor.execute(comando)
conexão.commit()
comando = f'UPDATE moedas SET valor = {cotacao_euro} WHERE Nome_moeda = "EUR"'
cursor.execute(comando)
conexão.commit()
comando = f'UPDATE moedas SET valor = {cotacao_bitcoin} WHERE Nome_moeda = "BTC"'
cursor.execute(comando)
conexão.commit()
cursor.close()
conexão.close()
