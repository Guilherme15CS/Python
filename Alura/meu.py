import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    print("Bem-vindo ao Pedra, Papel e Tesoura!")
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogador == 'sair':
            print("Jogo encerrado.")
            break
        if jogador not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")
        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

if __name__ == "__main__":
    jogar()