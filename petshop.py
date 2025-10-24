# Listas para armazenamento de dados
usuarios = []
produtos = []
servicos = []

# Menu para cadastro ou Login de usuario
while True:
    print('-------------BEM VINDO AO PETSHOP-------------')
    print('---CADASTRE-SE OU FAÇA LOGIN PARA CONTINUAR---')
    print('1- Cadastro de usuário')
    print('2- Fazer login')
    print('3- Sair')

    op = int(input('Qual sua opção?: '))

    # Cadastro de usuário
    if op == 1:
        print('------------------')
        identificacao = input('Esse cadastro é para um ADMIN ou CLIENTE? ').lower()
        
        while identificacao != 'admin' or identificacao == 'cliente':
            print('Identificação inválida, O sistema só funciona com ADMINS ou CLIENTES!!.')
            identificacao = input('Esse cadastro é para um ADMIN ou CLIENTE? ').lower()
            
            if identificacao == 'admin' or identificacao == 'cliente':
                nome = input('Insira seu nome de usuario: ').lower()
                senha = input('Insira sua senha: ').lower()
                usuarios.append([identificacao, nome, senha])
                print('------------------')
                print('Cadastro Concluido!')
                print('------------------')
            break
            

    # Login
    elif op == 2:
        print('------------------')
        nome = input('Insira seu nome de usuario: ').lower()
        senha = input('Insira sua senha: ').lower()

        achou = False
        for usuario in usuarios:
            if usuario[1] == nome and usuario[2] == senha:
                print('------------------')
                print('Acesso concedido')
                print('------------------')
                if identificacao == 'admin':
                    print('------MENU DE ADM-----')
                else:
                    print('------MENU DE CLIENTE-----')
                break

        else:
            print('------------------------------------------')
            print('Usuário não cadastrado ou Login Inválido')
            print('------------------------------------------')

    elif op == 3:
        print('Saindo...')
        break

    else:
        print('------------------')
        print('Opção inválida!')
