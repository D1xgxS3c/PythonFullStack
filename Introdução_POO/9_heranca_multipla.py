class Animal:
    
    def andar(self):
        print('Estou Andando como um animal')

    def correr(self):
        print('Estou Correndo')

    def pular(self):
        print('eSTOU pulando')

class Felino(Animal):
    def felino(self):
        print('eu sou um felino')

class Gato():
    def miar(self):
        print('Estou andando como um gato')

class Cachorro(Animal):
    def latir(self):
        print('Estou latindo')


x = Felino()
x.pular()
