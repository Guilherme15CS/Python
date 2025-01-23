import schedule
import time

def tarefa():
    print('Olá Mundo!')


schedule.every().second.do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
    