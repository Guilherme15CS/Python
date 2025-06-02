def calcular_fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("Não existe fatorial de número negativo.")
    else:
        print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")