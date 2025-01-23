from FIAP.funções import * 

usuarios = {}
opçao = perguntar()
while 0 < opçao <= 4:
    if opçao == 1:
        inserir(usuarios)
    opçao = perguntar()
