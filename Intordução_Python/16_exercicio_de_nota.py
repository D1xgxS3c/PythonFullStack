#Escreva um programa que receba notas de um aluno (0 - 10), caso
#a nota digitada esteja fora dessa intervalo peça para o professor digitar novamente


while True:
    nota = int(input('Digite a nota de 0 a 10: '))


    if nota >= 0 and nota <= 10:
        print(f'A nota digitada é: {nota}')
        break
   
    print('Nota inválida digite a nota novamente')



