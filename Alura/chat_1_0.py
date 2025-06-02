import os
from dotenv import load_dotenv
from google import genai
#Conectar com a API do Google
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key='AIzaSyCODBAcUOx2Ge6TB7jQAQ3BprGNBMpaUpE')

#Ver modelos disponíveis
#for model in client.models.list():
    #print(model.name)
#escolha de modelo
modelo = 'gemini-2.0-flash'
#Interação com o usuário
print('Olá, sou o assistente virtual da Alura. Como posso ajudar?')
pergunta = input('Qual é a sua pergunta? ')

#Salvando Resposta 
resposta = client.models.generate_content(model=modelo, contents=f'{pergunta}')
print('-x' * 20)
print(resposta.text)
