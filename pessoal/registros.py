def linha():
    print('-=' * 20)


from time import sleep
print('Faça um reguistro para sua empresa')
linha()
registro = {}
while True:
    print('''[1] Adicionar novo usuário
[2] Remover usuário
[3] Pesquisar usuário
[4] Sair
''')
    linha()
    opc = int(input('Qual será a sua opção? '))
    linha()
    sleep(1)
    if opc == 1:
        chave = input('Como deseja salvar este login? ')
        nome = input('Digite o nome do funcionário: ')
        idade = int(input('Qual a idade do funcionário: '))
        setor = input('Qual setor irá trabalhar: ')
        salario = int(input('Qual será seu sálario: '))
        registro[chave] = nome, idade, setor, salario
        linha()
        sleep(1)
    if opc == 2:
        for k, v in registro.items():
            print(f'Chave: "{k}"')
        deletar = input(('Qual usuário deseja remover? '))
        for k, v in registro.items():
            print(f'Removendo valores do usuário {registro[deletar]}')
            # print(f'Removendo {v}')
            break
        sleep(1)
        del registro[deletar]
        linha()
        sleep(1)
    if opc == 3:
        print('Qual funcionario você deseja ver com detalhes?')
        linha()
        for k, v in registro.items():
            print(f'Usuario: {k}')
        linha()
        deta = input('Qual usuário deseja ver? ')
        print(f'''Nome é {registro[deta][0]}
Idade é {registro[deta][1]}
Setor é {registro[deta][2]}
Sálario é {registro[deta][3]}''')
        linha()
        sleep(3)
    if opc == 4:
        break

