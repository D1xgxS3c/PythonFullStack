
t = lambda nome, idade: print(f'nome = {nome}\n idade = {idade}')
t('Diego', 37)


x = lambda *args: print(*args)
x('Diego', 'Michele')

def teste():
    return lambda * idade: print(idade)

a = teste()

a('mel', 'luma')