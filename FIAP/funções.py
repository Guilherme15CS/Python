def perguntar():
    print('Qual ação deseja realizar?')
    return int(input('''[1] Adicionar novo usuário
[2] Pesquisar usuário
[3] Remover usuário
[4] Listar usuário: ''').upper())


def inserir(dicionario_01):
    dicionario_01[input('Digite o Login: ').upper()] = [input('Digite o nome: ').upper(),
                                                    input('Digite a última data de acesso: '),
                                                    input('Qual a última estação acessada: ').upper()]
    salvar(dicionario_01)
    

def salvar(dicionario):
    with open('BD.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f'{chave} : {str(valor)}')




