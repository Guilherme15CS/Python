from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings
from google import g
warnings.filterwarnings("ignore")
import os
try:
	import google.colab
	from google.colab import userdata
	os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')
except ImportError:
	# Fallback for local environment: set your API key here or handle accordingly
	os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")