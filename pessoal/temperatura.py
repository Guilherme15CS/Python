print('''Qual Temperatura deseja escolher?
[1] °C
[2] °F
[3] °K''')
escolha = int(input('Escolha a temperatura: '))
if escolha <= 0 or escolha >= 4:
    while True:
        if escolha <= 0 or escolha >= 4:
            print('Valor não identificado, tente novamente')        
            escolha = int(input('Escolha a temperatura: '))
        break
if escolha == 1:
    tempC = int(input('Digite a Temperatura: ')) 
    tempF = int(tempC * 1.8 + 32)
    tempK = int(tempC - 273.15)
    print(f'A temperatura de {tempC}°C é {tempF}°F e {tempK}°K')
elif escolha == 2:
    tempF = int(input('Digite a Temperatura: ')) 
    tempC = int((tempF - 32) * 5/9)
    tempK = int((tempF - 32) * 5/9 + 273.15)
    print(f'A temperatura de {tempF}°F é {tempC}°C e {tempK}°K')
else:
    tempK = int(input('Digite a Temperatura: '))
    tempC = int(tempK - 273.15)
    tempF = int((tempK- 273.15) * 9/5 + 32)
    print(f'A temperatura de {tempK}°K é {tempC}°C e {tempF}°F')
    