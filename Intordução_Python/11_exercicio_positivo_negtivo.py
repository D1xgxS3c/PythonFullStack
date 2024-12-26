#Receba um número e exiba se ele é positivo ou negativo.

numero = int(input('Digite o número: '))


if numero > 0:
    print(f'O numero {numero} é positivo')
elif numero < 0:
    print(f'O numero {numero} é negativo')
else:
    print(f'O número {numero} é zero')