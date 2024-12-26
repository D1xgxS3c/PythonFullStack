from model import Pessoa
from dal import PessoaDal

class PessoaController:
    @classmethod
    def Cadastrar(cls, nome, idade, cpf):

        if len(nome) < 50 and (idade > 0 and idade < 200) and len(cpf) == 11:
            try:

                PessoaDal.salvar(Pessoa(nome, idade, cpf))
                return True

            except:
                return False
            
        PessoaController.Cadastrar('Diego', 37, '9199479')