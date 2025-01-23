time1 = str(input('Qual é o nome do time mandante? '))
time2 = str(input('Qual o nome do time visitante? '))
print(f'Hoje terá jogo entre {time1} e {time2}')
gols1 = int(input(f'Quantos gols o {time1} fez: '))
gols2 = int(input(f'Quantos gols o {time2} fez: '))
if gols1 == gols2:
    print('O jogo terminou em empate')
elif gols1 > gols2:
    print(f'O {time1} venceu')
elif gols2 > gols1:
    print(f'O {time2} venceu')
    