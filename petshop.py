import funcoes

usuarios = []
produtos = []
servicos = []
historico_p = []
historico_s = []
satisfacao = []

while True:
    print('-------------BEM VINDO AO PETSHOP-------------')
    print('---CADASTRE-SE OU FAÇA LOGIN PARA CONTINUAR---')
    print('1- Cadastro de usuário')
    print('2- Fazer login')
    print('3- Importar')
    print('4- Sair')

    op = int(input('Qual sua opção?: '))

    if op == 1:
        print('------------------')

        while True:
            identificacao = input('Esse cadastro é para um ADMIN ou CLIENTE? ').upper()

            if identificacao == 'ADMIN' or identificacao == 'CLIENTE':
                nome = input('Insira seu nome de usuario: ').upper()
                senha = input('Insira sua senha: ').upper()
                usuarios.append([identificacao, nome, senha])
                print('------------------')
                print('Cadastro Concluido!')
                print('------------------')
                break

            else:
                print('------------------')
                print('Identificação inválida, O sistema só funciona com ADMINS ou CLIENTES!!.')

    elif op == 2:
        print('------------------')
        nome = input('Insira seu nome de usuario: ').upper()
        senha = input('Insira sua senha: ').upper()
        logado = False
        tipo = ''
        for usuario in usuarios:
            if usuario[1] == nome and usuario[2] == senha:
                print('------------------')
                print('Acesso concedido')
                print('------------------')
                logado = True
                tipo = usuario[0]

        if logado and tipo == 'ADMIN':
            while True:
                print('------MENU DE ADM-----')
                print('1- Cadastrar Produtos/Serviços')
                print('2- Buscar Produtos/Serviços')
                print('3- Remover Produtos/Serviços')
                print('4- Alterar Produtos/Serviços')
                print('5- Avaliações de satisfações')
                print('6- Relatório de vendas')
                print('7- Salvar listas um arquivo')
                print('8- Voltar para o Menu Principal')
                print('------------------')
                op = int(input('Qual sua opção?: '))

                if op == 1:
                    print('------------------')
                    print('O que você quer cadastrar?')
                    print('1- Produto')
                    print('2- Serviço')
                    print('------------------')
                    perg = input('Digite sua opção: ').upper()

                    if perg == '1':
                        print('------------------')
                        nome_produto = input('Digite o NOME do produto: ').upper()
                        desc_produto = input('Digite a DESCRIÇÃO do produto: ').upper()
                        qtde_produto = int(input('Digite a QUANTIDADE de produtos: '))
                        preco_produto = float(input('Digite o PREÇO do produto: '))
                        produtos.append([nome_produto, desc_produto, qtde_produto, preco_produto])
                        print('------------------')
                        print('Produto cadastrado!')
                        print('------------------')

                    elif perg == '2':
                        print('------------------')
                        nome_servico = input('Digite o NOME do serviço: ').upper()
                        desc_servico = input('Digite a DESCRIÇÃO do serviço: ').upper()
                        preco_servico = float(input('Digite o PREÇO do serviço: '))
                        print('------------------')
                        print('Serviço cadastrado!')
                        print('------------------')
                        servicos.append([nome_servico, desc_servico, preco_servico, []])

                    else:
                        print('------------------')
                        print('Opção inválida!')
                        print('------------------')

                elif op == 2:
                    print('------------------')
                    print('O que você quer buscar?')
                    print('1- Produto')
                    print('2- Serviço')
                    print('------------------')
                    perg = input('Digite sua opção: ').upper()

                    if perg == '1':
                        print('------------------')
                        nome_produto = input('Digite o NOME do produto: ').upper()

                        encontrei = False
                        for p in produtos:
                            if nome_produto in p[0]:
                                print(f'PRODUTO: {p[0]} | QUANTIDADE: {p[2]} | PREÇO: {p[3]}')
                                encontrei = True

                        if not encontrei:
                            print('------------------')
                            print('Não achamos esse produto, no estoque')
                            print('------------------')
                            print(f'Lista dos produtos:')
                            for p in produtos:
                                print(f'PRODUTO: {p[0]} | QUANTIDADE: {p[2]} | PREÇO: {p[3]}')
                            print('------------------')

                    elif perg == '2':
                        nome_servico = input('Digite o NOME do servico: ').upper()

                        encontrei = False
                        for s in servicos:
                            if nome_servico in s[0]:
                                print(f'SERVIÇO: {s[0]} DESCRIÇÃO: {s[1]} | PREÇO: R${s[2]}')
                                encontrei = True
                                break

                        if not encontrei:
                            print('------------------')
                            print('Esse serviço não foi cadastrado!')
                            print('------------------')
                            print('Lista dos Serviços cadastrado: ')
                            for s in servicos:
                                print(f'SERVIÇO: {s[0]} | DESCRIÇÃO: {s[1]} | PREÇO: {s[2]}')
                            print('------------------')

                    else:
                        print('------------------')
                        print('Opção inválida!')
                        print('------------------')

                elif op == 3:
                    print('------------------')
                    print('O que você quer remover?')
                    print('1- Produto')
                    print('2- Serviço')
                    print('------------------')

                    perg = input('Digite sua opção: ').upper()

                    if perg == '1':
                        print('------------------')
                        print('Lista de produtos cadastrados:')
                        for p in range(len(produtos)):
                            print(
                                f'PRODRUTO: {produtos[p][0]} | QUANTIDADE: {produtos[p][2]} | PREÇO: {produtos[p][3]}')
                        print('------------------')

                        nome_produto = input('Digite o NOME do produto que você quer remover: ').upper()
                        ind = -1
                        for p in range(len(produtos)):
                            if produtos[p][0] == nome_produto:
                                ind = p
                                break
                        if ind != -1:
                            produtos.pop(ind)
                            print('Produto removido com Sucesso!')
                        else:
                            print('Produto não encontrado!')

                    elif perg == '2':
                        print('------------------')
                        print('Lista de serviços cadastrados:')
                        for s in range(len(servicos)):
                            print(f'SERVIÇO: {servicos[s][0]} | DESCRIÇÃO: {servicos[s][1]} | PREÇO: {servicos[s][2]}')
                        print('------------------')

                        nome_servico = input('Digite o NOME do serviço que vocẽ quer remover: ').upper()
                        ind = -1
                        for s in range(len(servicos)):
                            if servicos[s][0] == nome_servico:
                                ind = s
                                break
                        if ind != -1:
                            servicos.pop(ind)
                            print('Serviço removido com Sucesso!')
                        else:
                            print('Serviço não encontrado!')

                elif op == 4:
                    print('------------------')
                    print('O que você quer Alterar?')
                    print('1- Produto')
                    print('2- Serviço')
                    print('------------------')

                    perg = input('Digite sua opção: ').upper()

                    if perg == '1':
                        print('------------------')
                        print('Lista de produtos cadastrados:')

                        for p in range(len(produtos)):
                            print(
                                f'PRODUTO: {produtos[p][0]} | DESCRIÇÃO: {produtos[p][1]} | QUANTIDADE: {produtos[p][2]} | PREÇO: {produtos[p][3]}')
                        print('------------------')

                        nome_produto = input('Digite o NOME do produto que você quer alterar: ').upper()
                        print('------------------')

                        ind = -1
                        for p in range(len(produtos)):
                            if produtos[p][0] == nome_produto:
                                ind = p
                                break

                        if ind != -1:
                            print('Produto encontrado! Dados atuais:')
                            print(
                                f'PRODUTO: {produtos[ind][0]} | DESCRIÇÃO: {produtos[ind][1]} | QUANTIDADE: {produtos[ind][2]} | PREÇO: R${produtos[ind][3]}')

                            novo_nome_produto = input('Novo NOME (ou pressione Enter para manter o nome): ').upper()
                            nova_desc_produto = input(
                                'Nova DESCRIÇÃO (ou pressione Enter para manter a descrição): ').upper()
                            nova_qtde_produto = input('Nova QUANTIDADE (ou pressione Enter para manter a quantidade): ')
                            novo_preco_produto = input('Novo PREÇO (ou pressione Enter para manter o preço): ')
                            if novo_nome_produto != '':
                                produtos[ind][0] = novo_nome_produto
                            if nova_desc_produto != '':
                                produtos[ind][1] = nova_desc_produto
                            if nova_qtde_produto != '':
                                produtos[ind][2] = int(nova_qtde_produto)
                            if novo_preco_produto != '':
                                produtos[ind][3] = float(novo_preco_produto)

                            print('Produto alterado com Sucesso!')
                        else:
                            print('Produto não encontrado!')

                    elif perg == '2':
                        print('Lista de serviços cadastrados:')

                        for s in range(len(servicos)):
                            print(f'SERVIÇO: {servicos[s][0]} | DESCRIÇÃO: {servicos[s][1]} | PREÇO: {servicos[s][2]}')

                        nome_servico = input('Digite o NOME do serviço que você quer alterar: ').upper()
                        print('------------------')

                        ind = -1
                        for s in range(len(servicos)):
                            if servicos[s][0] == nome_servico:
                                ind = s
                                break

                        if ind != -1:
                            print('Serviço encontrado! Dados atuais:')
                            print(
                                f'SERVIÇO: {servicos[ind][0]} | DESCRIÇÃO: {servicos[ind][1]} | PREÇO: {servicos[ind][2]}')

                            novo_nome_servico = input('Novo NOME (ou pressione Enter para manter o nome): ').upper()
                            nova_desc_servico = input(
                                'Nova DESCRIÇÃO (ou pressione Enter para manter a descrição): ').upper()
                            nova_hora_servico = input(
                                'Novo HORÁRIO (ou pressione Enter para manter o horário): ').upper()
                            novo_preco_servico = input('Novo PREÇO (ou pressione Enter para manter o preço): ')
                            if novo_nome_servico != '':
                                servicos[ind][0] = novo_nome_servico
                            if nova_desc_servico != '':
                                servicos[ind][1] = nova_desc_servico
                            if nova_hora_servico != '':
                                servicos[ind][2] = nova_hora_servico
                            if novo_preco_servico != '':
                                servicos[ind][3] = float(novo_preco_servico)

                            print('Serviço alterado com Sucesso!')

                        else:
                            print('Serviço não encontrado!')

                elif op == 5:
                    achou = False
                    for a in satisfacao:
                        achou = True
                        print(
                            f'Nome do cliente: {a[0]} | Avaliação: {a[1]} | Foram {a[2]} estrelas | O cliente compraria de novo? {a[3]}')
                        print('------------------')

                elif op == 6:
                    total_venda = 0
                    total_servico = 0
                    print('Relatório de vendas')

                    for venda in historico_p:
                        total_venda += venda[3]

                    for servico in historico_s:
                        total_servico += servico[3]

                    total = total_servico + total_venda
                    print(f'O total de lucro em produtos foi: R${total_venda}')
                    print(f'O total de lucro em serviços foi: R${total_servico}')
                    print(f'O total de lucro em produtos e serviços foi: R${total}')

                elif op == 7:
                    print('------------------')
                    print('O que você quer Salvar?')
                    print('1- Usuários')
                    print('2- Produtos')
                    print('3- Serviços')
                    print('------------------')

                    op = input('Digite sua opção: ')

                    if op == '1':
                        funcoes.lista_user(usuarios)

                    elif op == '2':
                        funcoes.lista_prod(produtos)

                    elif op == '3':
                        funcoes.lista_serv(servicos)

                elif op == 8:
                    print('Saindo...')
                    break

                else:
                    print('------------------')
                    print('Opção inválida!')
                    print('------------------')

        elif logado and tipo == 'CLIENTE':
            while True:
                print('------MENU DE CLIENTE-----')
                print('1- Comprar Produtos')
                print('2- Agendar Serviços')
                print('3- Histórico de compras/serviços')
                print('4- Avaliação de Satisfação')
                print('5- Voltar para o Menu Principal')

                print('------------------')
                op = int(input('Qual sua opção? '))
                print('------------------')

                if op == 1:
                    print('------------------')
                    print('Lista de Produtos em estoque:')
                    print('------------------')
                    for p in produtos:
                        print(f'PRODUTO: {p[0]} | ESTOQUE: {p[2]} | PREÇO: R${p[3]}')

                    print('------------------')
                    compra = input('O que deseja COMPRAR? ').upper()
                    qtd = int(input('Qual a QUANTIDADE que deseja comprar ? '))

                    encontrado = False
                    for p in produtos:
                        if compra == p[0]:
                            encontrado = True

                            if qtd <= int(p[2]):
                                valor = qtd * p[3]
                                p[2] = int(p[2]) - qtd
                                print('------------------')
                                funcoes.janela_produto()
                                print('Obrigado pela preferência!')
                                print('------------------')
                                historico_p.append([nome, compra, qtd, valor])
                                break

                            elif qtd < 0:
                                print('------------------')
                                print('Opção inválida!')
                                print('------------------')

                            else:
                                print('------------------')
                                print('Quantidade acima do estoque disponível!')
                                print('------------------')
                                break

                    if not encontrado:
                        print('------------------')
                        print('Produto não encontrado!')
                        print('------------------')

                elif op == 2:
                    print('Serviços disponíveis:')
                    for s in servicos:
                        print(f'SERVIÇO: {s[0]} | DESCRIÇÃO: {s[1]} | PREÇO: R${s[2]}')
                    print('------------------')

                    servico = input('Digite o NOME do serviço: ').upper()

                    encontrado = False
                    for s in servicos:
                        if servico in s[0]:
                            encontrado = True

                            hora = input('Digite o horário (ex: 13h): ')

                            if hora not in s[3]:
                                print('------------------')
                                s[3].append(hora)
                                preco = s[2]
                                funcoes.janela_servico()
                                historico_s.append([nome, servico, hora, preco])

                            else:
                                print('------------------')
                                print('Esse horário está ocupado!')
                                print('------------------')

                    if not encontrado:
                        print('------------------')
                        print('Serviço não encontrado!')
                        print('------------------')

                elif op == 3:
                    print('------------------')
                    print('----HISTÓRICO----')
                    print('1- Compra de Produtos')
                    print('2- Agendamento de Serviços')
                    print('------------------')

                    print('------------------')
                    op = input('Qual histórico você quer ver? ')
                    print('------------------')

                    if op == '1':
                        print("---- HISTÓRICO DE COMPRAS ----")
                        achou = False

                        for h in historico_p:
                            if h[0] == nome:
                                achou = True
                                print(f"PRODUTO: {h[1]} | QUANTIDADE: {h[2]} | PREÇO: R${h[3]}")
                                print('------------------')

                        if not achou:
                            print("Você ainda não fez compras.")
                            print('------------------')

                    elif op == '2':
                        print("---- HISTÓRICO DE SERVIÇOS ----")
                        achou = False

                        for h in historico_s:
                            if h[0] == nome:
                                achou = True
                                print(f"SERVIÇO: {h[1]} | HORÁRIO: {h[2]} | PREÇO: R${h[3]}")
                                print('------------------')

                        if not achou:
                            print('------------------')
                            print("Você ainda não agendou nenhum serviço!.")
                            print('------------------')

                elif op == 4:
                    print('Que SERVIÇO você quer Avaliar?')
                    print('------------------')
                    for n in historico_s:
                        if n[0] == nome:
                            print(f'SERVIÇO: {n[1]}')
                            print('------------------')

                    nome_servico = input('Digite o NOME do serviço que você quer avaliar: ').upper()

                    for s in servicos:
                        if nome_servico == s[0]:

                            avaliacao = input('Escreva sua avaliação: ')
                            estrela = int(input('Quantas estrelas você daria para esse serviço de 0 a 5? '))

                            while estrela < 0 or estrela > 5:
                                estrela = int(input('Só é possível dar de 0 a 5 estrelas, tente novamente: '))

                            repete = input('Compraria novamente? ').upper()
                            print('------------------')
                            satisfacao.append([nome, avaliacao, estrela, repete])

                        elif nome_servico != s[0]:
                            print('------------------')
                            print('Não temos este Serviço cadastrado!')
                            print('------------------')

                elif op == 5:
                    break

        else:
            print('------------------------------------------')
            print('Usuário não cadastrado ou Login Inválido')
            print('------------------------------------------')

    elif op == 3:
        print('------------------')
        print('O que você quer Importar?')
        print('1- Usuários')
        print('2- Produtos')
        print('3- Serviços')
        print('------------------')

        op = input('Digite sua opção: ')

        if op == '1':
            funcoes.importar_user(usuarios)

        elif op == '2':
            funcoes.importar_prod(produtos)

        elif op == '3':
            funcoes.importar_serv(servicos)

    elif op == 4:
        print('------------------')
        print('Saindo...')
        print('------------------')
        break


    else:
        print('------------------')
        print('Opção inválida!')
        print('------------------')