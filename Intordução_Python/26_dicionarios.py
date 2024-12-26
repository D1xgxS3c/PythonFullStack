
pessoa = { 'nome': 'Diego Carvalho', 'idade': 37, 'cep': '1235456567' }
    
    
pessoa['nome'] = 'Marcos'

print(pessoa)

#########################################################################

x = { 'nomes': [], 'idade': [] }

x ['nomes'].append('Diego Carvalho')

x ['idade'].append(37)

print(x['nomes'][0])

print(x['idade'][0])

##########################################################################

pessoas = [
    
           {'nome': 'Diego', 'idade': 21, 'altura': 180},
           {'nome': 'Michele', 'idade': 21, 'altura': 180},
           {'nome': 'Derick', 'idade': 21, 'altura': 180},

                                                        ]

for i in pessoas:
    print(i['nome'])


############################################################################

person = {'name': 'Diego Carvalho', 'idade': 37, 'altura': 173}
person['cep'] = '09894070'#adiconando cep dentro do DICT,
person.update({'name': 'Michele'})#atualizando dict

print(person)

#############################################################################

#ITERAR CHAVES E VALORES 
#values

persons = {'name': 'Diego Carvalho', 'idade': 37, 'altura': 173}

for i in persons.items():
    print(i[0], i[1])

    #ou

for i, j in persons.items():
    print(f'i = {i} j = {j}')