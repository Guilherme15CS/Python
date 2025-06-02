import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

#Conectar com a API do Google
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key='AIzaSyDbMB0VCKrf9g0QoecM0KCieOkaDyhuGvI')

print(client)
#criação de chat que pode ser usado para várias perguntas
# chat = client.chats.create(model='gemini-2.0-flash')


promp = ''
#chat_config é uma configuração que pode ser usada para personalizar o comportamento do assistente
chat_config = types.GenerateContentConfig(
    system_instruction="Você é um assistente pessoal que sempre responde de forma sarcástica.",
)
#criação de chat com configuração
chat = client.chats.create(model='gemini-2.0-flash', config=chat_config,)
while promp != 'Fim':   
    #pergunta ao usuário
    promp = input('Digite o promp: ').capitalize()
    #resposta do assistente de acordo com o modelo
    resposta = chat.send_message(f'{promp}') 
    print('-x' * 20)
    print(resposta.text)