
class Pessoa:

    def falar(self):
        print('Estou falando')

    def andar(self):
        print('Estou Andando')

class Cliente(Pessoa):
    
    def comprar(self):
        print('Estou comprando')

class Vendendor(Pessoa):

    def vender(self):
        print('Estou vendendo')

v1 = Vendendor()
v1.andar()
v1.falar()
v1.vender()


c1 = Cliente()

c1.andar()
c1.comprar()
c1.falar()


