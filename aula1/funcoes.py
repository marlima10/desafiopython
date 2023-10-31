def funcao():
    print('Oi')

def soma_com_argumentos_e_retorno(a,b):
    return a + b

n1 = int(input('informe o primeiro numero:'))
n2 = int(input('informe o segundo numero:'))

reposta = soma_com_argumentos_e_retorno(n1,n2)

print(f'A some é {reposta}')
