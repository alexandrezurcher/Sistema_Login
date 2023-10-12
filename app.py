from getpass import getpass

print('Bem-vindo a este sistema')

print("""Escolha uma opcao
      [1] - Fazer login
      [2] - Cadastrar novo Usuario""")

user_input = input('Digite a sua opcao: ')

if user_input == '1':
    while True:
        nome = input('Digite seu usuario: ')
        senha = getpass('Digite sua senha: ')
        user_data = nome + ',' + senha +'\n'
        with open('usuarios.txt') as file:
            conteudo = file.readlines()
            if user_data in conteudo:
                print(f'Bem vindo {nome}, login feito com sucesso!')
                break
            else:
                print('Usuario e/ou Senha nao conferem')
               
elif user_input == '2':
    nome = input('Nome para novo usuario: ')
    senha = getpass('Senha para novo usuario: ')
    user_data = nome + ',' + senha +'\n'
    with open('usuarios.txt','a') as file:
        file.write(user_data)
    print (f'usuario {nome}, criado com sucesso')
