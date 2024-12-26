#Receba um número e mostre todos os números pares de 0 até o número digitado.

numero = int(input('Digite um numero: '))


i = 0
while i <= numero:
    if i % 2 == 0:
        print(i)
    i += 1

