
class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Estou logando no sistema!')


pessoa1 = Pessoas('Diego Carvalho',37,'092049029-0424')

pessoa1.logar_sistema()
