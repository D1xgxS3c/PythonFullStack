class Pessoas:
#ATRIBUTOS
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

#METODO
    def logar_sistema(self):
        print(f'{self.nome} Está logando no sistema!')


#INSTANCIA
pessoa1 = Pessoas('Diego Carvalho', 21, '13028402840802')


print(pessoa1.logar_sistema())
