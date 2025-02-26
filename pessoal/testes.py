def linha():
    print('-=' * 20)


import requests
from datetime import time, timedelta, datetime


IToken = 'ec0b20b316c4bfee3301c9cd340bcbfd'
a = 0

link = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token={IToken}'
requi = requests.get(link)
dados = requi.json()

print(dados)