# Listas  para armazenamento de dados
usuarios = []
produtos = []
servicos = []

i = 99

# Menu para cadastro ou Login de usuario
while i != 0:
    print('---MENU---')
    print('1- Cadastro de usuário')
    print('2- Fazer login')

    op = int(input('Qual sua opção: '))

    # Criando identificação para usuario
    if op == 1:
        print('------------------')
        print('Esse cadastro é para um ADMIN ou Para um Cliente?')
        identificacao = input('Identificação: ').lower()
        
        # Armazenando os dados do ADMIN
        if identificacao == 'admin':
            print('------------------')
            nome = input('Insira seu nome de usuario: ').lower()
            senha = input('Insira sua senha: ').lower()
            print('Cadastro Concluido')
            print('------------------')

            adm = [nome, senha]
            usuarios.append(adm)
        
        # Armazenando os dados do Cliente
        elif identificacao == 'cliente':
            print('------------------')
            nome = input('Insira seu nome de usuario: ').lower()
            senha = input('Insira sua senha: ').lower()
            print('Cadastro Concluido')
            print('------------------')
            
            cliente = [nome, senha]
            usuarios.append(cliente)

        else:
             print('Identificação inválida')

    if op == 2:
        print('------------------')
        nome = input('Insira seu nome de usuario: ')
        senha = input('Insira sua senha: ')


        #if (nome not in usuarios) and (senha not in usuarios):
        #   print('-----------------------')
        #   print('Usuário não cadastrado.')
             

        for dados in usuarios:
            if (nome in adm) and (senha in adm):
                print('------------------')
                print('Acesso concedido')
                print('------MENU DE ADMIN-----')
                
                

        for dados in usuarios:
            if (nome in cliente) and (senha in cliente):     
                print('------------------')
                print('Acesso concedido')
                print('------MENU DE CLIENTE-----')

        
        #if (nome and senha) in adm:
        #    print('Acesso concedido')
        #    print('------MENU DE ADMIN-----')

                        
        #   elif (nome and senha) in cliente:
        #       print('Acesso concedido')
        #      print('------MENU DE CLIENTE-----')
                            