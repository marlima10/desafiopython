import random

numero_aleatorio = random.randint(1,5)
tentativa = int(input('digite um numero para chutar entre 1 e 5:'))

if(numero_aleatorio == tentativa):
    print('é igual')
else:
    print(f'O numero secreto era: {numero_aleatorio}')
