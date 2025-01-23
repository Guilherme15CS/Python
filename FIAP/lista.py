lista = []
resp = 'S'
while resp =='S':
    lista.append(input('Equipamento: '))
    lista.append(float(input('Valor: ')))
    lista.append(int(input('Número de Serie: ')))
    lista.append(input('Loja: '))
    resp = input('Deseja continuar? [S/N] ').upper()
for item in lista:
    print(item)
