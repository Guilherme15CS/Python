import pyautogui
from time import sleep
import pandas as pd



tabela = pd.read_csv(r"C:\Users\lcamp\OneDrive\Documentos\VS CODE\Python\Hashtag\Aula1\produtos.csv")


codigos = tabela['codigo'][0+1]
print(codigos)