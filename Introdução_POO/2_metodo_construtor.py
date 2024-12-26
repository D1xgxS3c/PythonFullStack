class Pessoas:
    def __init__(self, nome, idade, cpf):
        print(f'\n Nome: {nome}\n Idade: {idade}\n CPF: {cpf}\n')

    def logar_sistema(self):
        print(f' Estou logando no sistema!')

pessoa1 = Pessoas('Diego Carvalho',37,'319039103313')


pessoa1.logar_sistema()
