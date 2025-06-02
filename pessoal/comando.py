def linha():
    print('-=' * 20)


import mysql.connector
from time import sleep

#Conexão com o banco de dados
conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pessoas'
)
#introdução e resposta do usuario
print('Informações do Banco de Dados')
sleep(1)
print((('''Qual ação gostaria de fazer:
[1] Adicionar cadastro''')))

resp = int(input('Digite sua opção: '))
#opc 1
if resp == 1:
    #falar o nome
    sleep(1)
    linha()
    nome = input('Digite seu nome: ').capitalize()    
    #falar o sexo
    sleep(1)
    linha()
    sexo = input('Digite seu sexo: (M/F) ').upper()
    #falar a data de nascimento
    sleep(1)
    linha()
    data = input('Digite sua data de Nascimento: (Ex: 01/01/2000) ')
    #falar a situação civil
    sleep(1)
    linha()
    print((('''Qual a sua Situação Civil atual:
    [1] Empregado(a)
    [2] Desempregado(a)
    [3] Estudante
    [4] Aposentado(a)''')))
    respsitu = int(input('Sua Situação Atual: '))
    if respsitu == 1:
        situ = input('Digite a sua profisão: ').capitalize()
        situgeral = f'Empregado(a)/{situ}'
    elif respsitu == 2:
        situgeral = 'Desempregado(a)'
    elif respsitu == 3:
        print((('''Você estuda em:
    [1] Escola
    [2] Faculdade''')))
        situ = int(input('Digite sua opção: '))
        if situ == 1:
            situgeral = 'Estudnte/Escola'
        else:
            situgeral = 'Estudnte/Faculdade'
    else:
        situgeral = 'Aposentado(a)'
    #falar estado civil
    sleep(1)
    linha()
    print((('''Qual é o seu Estado Civil atualmente:
    [1] Solteiro(a)
    [2] Casado(a)
    [3] Divorciado(a)
    [4] Viúvo(a)
    [5] Namorando''')))
    respest = int(input('Digite sua opção atual: '))
    if respest == 1:
        estgeral = 'Solteiro(a)'
    elif respest == 2:
        estgeral = 'Casado(a)'
    elif respest == 3:
        estgeral = 'Divorciado(a)'
    elif respest == 4:
        estgeral = 'Viúvo(a)'
    else:
        estgeral = 'Namorando'
    #falar cidade que mora
    sleep(1)
    linha()
    cidade = input('Digite o nome da cidade que você mora: ').capitalize()
    #falar time que torce
    sleep(1)
    linha()
    print((('''Qual time você torce
    [1] Eu torço para...
    [2] Eu não torco para nenhum time''')))
    respfut = int(input('Digite sua opção: '))
    if respfut == 1:
        futgeral = input('Qual time você torce: ').capitalize()
    else:
        futgeral = 'Não torce para nenhum time'

    #adicionar informações no banco de dados
    cursor = conexão.cursor()
    comando = f'INSERT INTO informações (Nome, Sexo, Data_de_Nascimento, Situação_Civil, Estado_Civil, Cidade_que_Mora, Time_que_torce) VALUES ("{nome}","{sexo}", "{data}", "{situgeral}", "{estgeral}", "{cidade}", "{futgeral}")'

    cursor.execute(comando)
    conexão.commit()
    cursor.close()
    conexão.close()
