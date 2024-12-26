 #CLS rRECEBE O ESTADO DA CLASSE, AS INFORMAÇÕES DA CLASSE.
#ATRAVEZ DO CLS PODEMOS CRIAR E MODIFICAR ATRIBUTOS DA CLASSE.
class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = "humano"
    

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Estou logando no sistema!')

    @classmethod
    def andar(cls):#CLS é o estado da classmethod
        cls.possui_boca = False
        return None


print(Pessoas.possui_boca)
Pessoas.andar()
print(Pessoas.possui_boca)

