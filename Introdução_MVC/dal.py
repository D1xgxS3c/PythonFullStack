from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(f"{pessoa.nome} {pessoa.idade} {pessoa.cpf}")  # Usando f-strings para formatação
            
    @classmethod
    def ler(self):
        nome = 'Diego'
        idade = 37
        cpf = 3891891711111
        return Pessoa(nome, idade, cpf)


# p1 = Pessoa('Diego', 37, '90013o928982948')
# PessoaDal.salvar(p1)