#Escreva um programa onde o usuário digite duas notas e ele mostre a média das duas notas


print('Digite a nota 1')
nota1 = input()


print('Digite a nota 2')
nota2 = input()

resultado = (int(nota1) + int(nota2)) / 2
print(f'esta é a media das duas notas: {resultado}')