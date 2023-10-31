import random

minimo = 1
maximo = 100
numero_aleatorio = random.randint(minimo, maximo)

print(numero_aleatorio)

minimo = 1
maximo = 10
quantidade = 3

for _ in range(3):
    numeros_aleatorios = random.sample(range(minimo, maximo + 1), quantidade)
    print("Números aleatórios:", numeros_aleatorios)

random.seed(42)
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))