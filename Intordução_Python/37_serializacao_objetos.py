#SERIALIZAÇÃO É PEGAR ALGO QUE ESTÁ EM MEMÓRIA E TORNA-LO PERSSISTENTE
import pickle

x = {'nome': 'Diego', 'idade': 37}

string = pickle.dumps(x)
print(pickle.loads(string)['nome'])
print(pickle.loads(string)['idade'])



#SERIALIZANDO

list = [1,2,3,4]

arq = open('arquivo.pkl', 'wb')#wb escrever em binario
pickle.dump(list, arq)

arq = open('arquivo.pkl', 'rb')#rb ler em binario
retornou = pickle.load(arq)

print(retornou)

#############################################################3
#SERIALIZANDO CLASSES
class Pessoa:
    nome = 'Diego'
    idade = 20

file = open('arquivo.pkl', 'wb')#wb escrever em binario

pickle.dump(Pessoa, file)

file = open('arquivo.pkl', 'rb')#rb ler em binario
retornou = pickle.load(file)

print(retornou.nome)
print(retornou.idade)

#############################################################
# SERIALIZAR OBJETO DE INSTANCIA

class Pessoa:
    name = 'Diego'
    idad = 20


class Pessoas:
    def __init__(self, name, idad):
        self.name = name
        self.idad = idad

p1 = Pessoas('marcos',21)   

arqv = open('arquivo.pkl', 'ab')
pickle.dump(Pessoas, arqv)

arqv = open('arquivo.pkl', 'rb')
ret = pickle.load(arqv)

print(ret.name)