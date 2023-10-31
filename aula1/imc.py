print('IMC \n')

#peso/altura * altura

peso = float(input("Digite o peso:"))
altura = float(input("Digite a altura no formato 0.00:"))

imc = peso/altura **2
imc = round(imc,2)

print(f'O seu imc é {imc}')