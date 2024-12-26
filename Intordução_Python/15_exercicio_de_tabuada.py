#Receba um número do usuário e mostra a taubuada desse número

n1 = int(input('Digite qual númro deseja saber a tabuada: '))

i = 1

while i <= 10:
    resultado = i * n1
    print(f'{n1} x {i} = {resultado}')
    i += 1  