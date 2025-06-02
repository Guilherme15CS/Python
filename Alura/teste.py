#importando a biblioteca de busca do Google adk 
try:
    from google.adk.agents import Agent #objeto de agente
    from google.adk.runners import Runner #quem vai rodar o agente
    from google.adk.sessions import InMemorySessionService #memoria interna do agente
    from google.adk.tools import google_search #ferramenta de busca do Google
    from google.genai import types  # Para criar conteúdos (Content e Part)
except ImportError as e:
    raise ImportError("Certifique-se de que os pacotes 'google-adk' e 'google-genai' estão instalados. Erro: " + str(e))
from datetime import date 
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings
warnings.filterwarnings("ignore")

#importção padrão
import os
from dotenv import  load_dotenv
from google import genai 

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key='AIzaSyDbMB0VCKrf9g0QoecM0KCieOkaDyhuGvI')

def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response


def agente_buscador(topico, data_de_hoje):
    buscador = Agent(
        name="Agente_Buscador",
        model="gemini-2.5-flash",
        instruction="""
        Você é um assistente de pesquisa. A sua tarefa é usar a ferramenta de busca do Google (google_search).
        Para recuperar informações muito úteis sobre o tópico abaixo.
        Foque no máximo em 5 lançamentos relevantes, com base na quantidade de relevância.
        Se um tema tiver poucas notícias, busque por mais notícias relacionadas.
        Essas noticias devem ser relevantes e atuais, com data de hoje até um mês atrás.
        """,
        description="Agente que busca informações sobre um tópico específico.",
        tools=[google_search],
    )
    
    entrada_do_agente_buscador = f"Tópico: {topico} \nData: {data_de_hoje}"
    lancamentos = call_agent(buscador, entrada_do_agente_buscador)
    return lancamentos

data_de_hoje = date.today().strftime("%d/%m/%Y")

print("🚀 Iniciando o Sistema de Criação de Posts para Instagram com 4 Agentes 🚀")

# --- Obter o Tópico do Usuário ---
topico = input("❓ Por favor, digite o TÓPICO sobre o qual você quer criar o post de tendências: ")

# Inserir lógica do sistema de agentes ################################################
if not topico:
    print('Você esqueceu de digitar o tópico!')
else:
    print(f'Maravilha! Vamos criar um post sobre {topico}!')
    lancamentos_buscados = agente_buscador(topico, data_de_hoje)
    print("\n--- 📝 Resultado do Agente 1 (Buscador) ---\n")
    print(lancamentos_buscados)
    print("--------------------------------------------------------------")
