
i = 0
j = 0

while i < 10 and j < 30:
    print('Olá tudo bem ?')
    break
    i = i + 1
    j = j + 10

#---------------------------------------


i = 0

while i < 10:
    print(i)
    if i % 2 == 1:
        i = i + 2
        continue
    i = i + 1

