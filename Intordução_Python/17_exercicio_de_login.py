#Defina um uuário e senha depois verifique se o
#login do usuário é válido.

usuario = input('Digite o nome do usuário: ')
senha = int(input('Digite a senha do usuário: '))

if usuario == 'Diego' and senha == 1234:
    print('Logado com sucesso!')
else:
    print('Usuário inválido!')