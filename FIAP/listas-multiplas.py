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
for item in range(0, len(equipamentos)):
    print(f'Produto {item + 1}')
    print(f'Equipamento: {equipamentos[item]}')
    print(f'Valor: {valores[item]}')
    print(f'Número Serial: {seriais[item]}')
    print(f'Loja: {departamentos[item]}')
