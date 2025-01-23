equipamentos = []
valores = []
seriais = []
departamentos = []
resp = 'S'
while resp == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(input('Número de Série: '))
    departamentos.append(input('Loja: '))
    resp = input('Deseja Continuar? [S/N]: ').upper()
    print('-=' * 20)
print('-=' * 20)
for item in range(0, len(equipamentos)):
    print(f'{item} Equipamento: {equipamentos[item]}')
print('-=' * 20)
escolha = int(input('Qual equipamento deseja ver mais detalhadamente? '))
print('-=' * 20)
for esc in range (0, 1):
    print(f'Equipamento: {equipamentos[escolha]}')    
    print(f'Valor: {valores[escolha]}')
    print(f'Número Serial: {seriais[escolha]}')
    print(f'Loja: {departamentos[escolha]}')
