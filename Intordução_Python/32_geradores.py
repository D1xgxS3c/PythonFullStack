#quanto de memoria um determinado dado esta ocupando

from pympler.asizeof import asizesof # type: ignore

def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
    return lista_dobro

x = asizesof(dobro(range(0,1000)))

print(x)

############################################################

def double():
    yield 1
    yield 2
    yield 3

t = double()

print(next(t))
print(next(t))
print(next(t))


###############################################################

print(asizesof([1]))# 96
#96 -32 = 64
# 64 + 32 = 96

print(asizesof([1,2]))# 136
#40 x 2 = 80
# 80 + 56 = 136

print(asizesof([1,2,3]))# 176
#40 x 3 = 120
# 120 + 56 = 176

print(asizesof([1,2,3,4]))# 216
#40 x 4 = 160
# 160 + 56 = 216

####################################################################