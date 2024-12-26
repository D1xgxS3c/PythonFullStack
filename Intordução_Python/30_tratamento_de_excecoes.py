# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite um número: '))

# try:
#     print(n1/n2)
# except:
#     print('Não é possivel então: ')
# finally:
#     print('Código finalizado')


#####################################################
try:
    x = int(input('Digite um número: '))
    print(5/x)
except ValueError: 
    print('Digite um número inteiro')
except ZeroDivisionError:
    print('Não digite 0')


######################################################