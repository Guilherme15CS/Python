#pyautogui bibioteca para automação de mouse e teclado
import pyautogui
from time import sleep
import pandas as pd


#Comando para dar uma pausa entre os comandos
pyautogui.PAUSE = 0.5

#Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

#brir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')    
sleep(2)  
#abrir o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')


#esperar o site carregar
sleep(2)

#Passo 2: fazer login 

#colocar gmail
pyautogui.click(x=732, y=464) #clicar no campo de login
pyautogui.write('guicseleg@gmail.com') #digitar o gmail

#clicar no campo de senha
pyautogui.press('tab') #mover para o campo de senha
pyautogui.write('123456') #digitar a senha

#clicar no botão de login
pyautogui.press('tab') #logar
pyautogui.press('enter') #pressionar enter para logar


#esperar o site carregar
sleep(2)

#Passo 3: Importar a base de dados

tabela = pd.read_csv(r"C:\Users\lcamp\OneDrive\Documentos\VS CODE\Python\Hashtag\Aula1\produtos.csv")



#Passo 4: Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=730, y=327)   


    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo) #digitar o código do produto
    pyautogui.press('tab') #mover para o campo de marca

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) 
    pyautogui.press('tab') 

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(str(categoria)) 
    pyautogui.press('tab') 

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, "obs"])

    if obs != 'nan':
        pyautogui.write(obs) 
    
    pyautogui.press('tab')
    pyautogui.press('enter')   

    pyautogui.scroll(1000000) #voltar para o topo da página

#Passo 5: repitir para todos os produtos
