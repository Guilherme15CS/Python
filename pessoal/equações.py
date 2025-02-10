from math import sqrt

#Cores para melhor visualização
green = '\033[1;32m'
red = '\033[1;31m'
fim = '\033[m'

#Escolha de números
print('Resolução de equação do 2ºGrau')
a = int(input('Qual valor de "a": '))
b = int(input('Qual valor de "b": '))
c = int(input('Qual valor de "c": '))

#Escolha da conta
print(f'''Como a conta é:
[1]  {green}+{fim} {a}² {green}+{fim} {b} {green}+{fim} {c} = 0
[2]  {green}+{fim} {a}² {green}+{fim} {b} {red}-{fim} {c} = 0
[3]  {green}+{fim} {a}² {red}-{fim} {b} {green}+{fim} {c} = 0
[4]  {green}+{fim} {a}² {red}-{fim} {b} {red}-{fim} {c} = 0
[5]  {red}-{fim} {a}² {red}-{fim} {b} {red}-{fim} {c} = 0
[6]  {red}-{fim} {a}² {green}+{fim} {b} {green}+{fim} {c} = 0
[7]  {red}-{fim} {a}² {green}+{fim} {b} {red}-{fim} {c} = 0
[8]  {red}-{fim} {a}² {red}-{fim} {b} {green}+{fim} {c} = 0''')
escolha = int(input('Qual operação deseja fazer? '))

#calculo
if escolha == 1:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 2:
    delta = b**2 - 4*a*-c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 3:
    delta = -b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 4:
    delta = -b**2 - 4*a*-c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 5:
    delta = -b**2 - 4*-a*-c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 6:
    delta = b**2 - 4*-a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 7:
    delta = b**2 - 4*-a*-c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')
elif escolha == 8:
    delta = -b**2 - 4*-a*c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2
        x2 = (-b - sqrt(delta)) / 2
        print(f'Delta é {delta}, as raízes são {x1} e {x2}')
    elif delta == 0:
        x = (-b + sqrt(delta)) / 2
        print(f'Delta é {delta}, a raíz é {x}')
    else:
        print(f'Como delta é {delta} (Negativo) não existe raíz')



