from random import choice

caracter = 'abcdefghifklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()`^~/*-+?/|'

quantidate = int(input('Quantas senhas você quer gerar? '))
cara = int(input('Quantos caracteres tem que ter na senha? '))

for sen in range(quantidate):
    senha = ''
    for c in range(cara):
        senha += choice(caracter)
    print(senha)