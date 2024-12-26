#CRIANDO O ARQUIVO
arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    if i > 2:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + " " + input('Digite a idade') + "\n")
    i += 1

###########################################################################################
#PARA LER O ARQUIVO
arquivo = open('pessoas.txt', 'r')
resultados = arquivo.readlines()
x = []
for i in resultados:
    x.append(i.split())
print(x[0])
arquivo.close()


##############################################################################################
#OUTRA FORMA DDE LER O ARQUIVO COM WITH QUE FECHA O ARQUIVO AUTOMATICO EM VEZ DO CLOSE.
with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)
