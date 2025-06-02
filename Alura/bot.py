import random

def chatbot():
    respostas = {
        "oi": "Olá! Como posso ajudar você?",
        "olá": "Oi! Em que posso ajudar?",
        "tudo bem": "Estou bem, obrigado! E você?",
        "qual seu nome?": "Eu sou um chatbot simples.",
        "adeus": "Tchau! Até a próxima.",
    }
    print("Chatbot iniciado. Digite 'sair' para encerrar.")
    while True:
        pergunta = input("Você: ").lower()
        if pergunta == "sair":
            print("Chatbot: Até logo!")
            break
        resposta = respostas.get(pergunta, "Desculpe, não entendi. Pode repetir?")
        print(f"Chatbot: {resposta}")

if __name__ == "__main__":
    chatbot()