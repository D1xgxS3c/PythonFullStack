
def minha_funcao(num1, num2):

    soma = (num1 + num2) * 5

    print(soma)


minha_funcao(1, 2)

#############################################


def funcao(*args):

    soma = (args) * 5

    print(soma)

funcao(1)

#############################################
# args empacota tudo dentro de uma tupla


def soma_numeros(n1, n2, *args):

    print(n1 + n2 + len(args))


soma_numeros(10, 20, 3, 4, 5, 6, 7, 8)


#############################################
# kwargs empacota tudo de um dicionario

def somar(**kwargs):

    x =  kwargs.get('test1' )

    print(x)

somar(test1 = 1, teste2 = 2, teste3 = 3)

###############################################3
#Retornando valores da função

def valor(n1, n2):
    
    return n1 + n2

print(valor(1,2))

###################################################

