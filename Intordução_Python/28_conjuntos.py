#set é o counjunto
#não permite dados repetidos

x = [1,1,1,1,1,12,2,2,2,3,3,3,]

x = set(x)

print(x)

# union = UNIR os conjuntos
z = {1,2,3,4,5,6}
y = {1,3,7,8,9,10}

z = z.union(y)
print(z)

#intersection = verifica qual tem nos conjuntos
z = z.intersection(y)
print(z)

#diference = verifica as diferentes


t = {1,2,3,4,5,6}
y = {1,3,7,8,9,10}

t = t.difference(y)
print(t)

#symmetric_difference = união a intersection nele nao conta
t = t.symmetric_difference(y)
print(t)

