
print (list(range(23, -23, -1 )))


###############################################

array = [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22]

for i in array:
    print(i)
   
###############################################

inicio = 1
fim = 20
passos = 2

for index in range(inicio, fim, passos):
        print(index)
   

###############################################
#Só quando for necessário colocar um for dentro do outro, mas vitar isso.
#laços aninhado
#3X3 

for i in range(0, 3):
      for j in range(0, 3):
            print(f'i = {i} j = {j}')