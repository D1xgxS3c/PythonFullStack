
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


pessoa1 = Pessoas('Diego Carvalho',37,'092049029-0424')
pessoa2 = Pessoas('Michele', 37, '480820842048')

pessoa1.boca = False

Pessoas.possui_boca = False

print(pessoa1.possui_boca)
print(pessoa2.possui_boca)

