from random import randint
computador = randint(1, 3)
print('-=' * 20) 
print('VAMOS JOGAR PEDRA, PAPEL E TESOURA')
print('-=' * 20)
print('''[1] Para PEDRA
[2] Para PAPEL
[3] Para TESOURA''')
jogada = int(input('Qual será a sua jogada? ')) 
print('-=' * 20)
if computador == 1 :
    computador = 'Pedra'
elif computador == 2:
    computador = 'Papel'
else:
    computador = 'Tesoura'
if jogada == 1:
    jogada = 'Pedra'
elif jogada == 2:
    jogada = 'Papel'
else:
    jogada = 'Tesoura'
print(f'Eu joguei {computador} e você jogou {jogada}')
print('-=' * 20)
# Empate
if computador == 'Pedra' and jogada == 'Pedra' or computador == 'Papel' and jogada == 'Papel' or computador == 'Tesoura' and jogada == 'Tesoura':
    print('EMAPTE')
# Vitoria Jogador
elif computador == 'Pedra' and jogada == 'Papel' or computador == 'Papel' and jogada == 'Tesoura' or computador == 'Tesoura' and jogada == 'Pedra':
    print('VOCÊ VENCEU')
# Vitoria Computador
else:
    print("VOCÊ PERDEU")
