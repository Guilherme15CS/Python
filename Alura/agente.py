import os
from dotenv import load_dotenv
from google import genai 
from google.genai import types 


#Conectar com a API do Google
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key='AIzaSyDbMB0VCKrf9g0QoecM0KCieOkaDyhuGvI')
modelo = 'gemini-2.0-flash'
# Perguntar pro modelo quando é a próxima imersão de IA com a última base de dados da IA###############################################
resposta = client.models.generate_content(model=modelo, contents='Quando é a proxima imersão de IA com Google Gemini da Alura?') 
print('-x' * 20)
print(resposta.text)

#Pergunta ao Gemini uma informação utilizando a busca do Google como contexto
"""resposta = client.models.generate_content(model=modelo,
                                          contents='Quando é a proxima imersão de IA com Google Gemini da Alura?',
                                          config={'tools': [{'google_search': {}}]}
                                          )
print('-x' * 20)
print(resposta.text)"""

#importando a biblioteca de busca do Google adk 
from google.adk.agents import Agent #objeto de agente
from google.adk.runners import Runner #quem vai rodar o agente
from google.adk.sessions import InMemorySessionService #memoria interna do agente
from google.adk.tools import google_search #ferramenta de busca do Google
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date 
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings

warnings.filterwarnings("ignore")