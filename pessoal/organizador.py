homem = mulher = maior = menor = 0
home18 = home0 = mulh18 = mulh0 = 0
while True:
    sexo = (input('Qual é o seu gênero? [M/F] ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('-=' * 20)
        print('\033[1;31mSexo não identificado, tente novamente\033[m')
        sexo = (input('Qual é o seu gênero [M/F] ')).upper()
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        mulher += 1
    idade = int(input('Qual é a sua idade? '))
    resp = input('Deseja continuar? [S/N] ').upper()
    while resp != 'S' and resp != 'N':
        print('-=' * 20)
        print('Resposta inválida, tente novamente')
        resp = input('Deseja continuar? [S/N] ').upper()     
    if idade >= 18:
        maior += 1
    else:
        menor += 1
    if sexo == 'M' and idade >= 18:
        home18 += 1
    elif sexo == 'M' and idade < 18:
        home0 += 1
    elif sexo == 'F' and idade >= 18:
        mulh18 += 1
    elif sexo == 'F' and idade < 18:
        mulh0 += 1
    if resp == 'N':
        break
print('-=' * 20)
print('-----TOTAIS-----')
print(f'Foram digitados {homem + mulher} pessoas')
print(f'{maior} pessoas tem mais de 18 anos')
print(f'{menor} pessoas tem menos de 18 anos')
print('-=' * 20)
print('-----HOMENS-----')
print(f'Foram digitados {homem} homens')
print(f'{home18} homens tem mais de 18 anos')
print(f'{home0} homens tem menos de 18 anos')
print('-----MULHERES-----')
print(f'Foram digitados {mulher} mulheres')
print(f'{mulh18} mulheres tem mais de 18 anos')
print(f'{mulh0} mulheres tem menos de 18 anos')
