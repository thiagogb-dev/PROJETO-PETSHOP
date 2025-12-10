import tkinter as tk


def lista_user(usuarios):
    arquivo = open('usuarios.txt', 'w', encoding='utf-8')
    for u in usuarios:
        arquivo.write(f'{u[0]} - {u[1]} - {u[2]}\n')
    arquivo.close()
    print('Lista de Usuários salva com êxito')

def lista_prod(produtos):
    arquivo = open('produtos.txt', 'w', encoding='utf-8')
    for p in produtos:
        arquivo.write(f'{p[0]} - {p[1]} - {p[2]} - {p[3]}\n')
    arquivo.close()
    print('Lista de Protudos salva com êxito')

def lista_serv(servicos):
    arquivo = open('servicos.txt', 'w', encoding='utf-8')
    for s in servicos:
        arquivo.write(f'{s[0]} - {s[1]} - {s[2]} - {s[3]}\n')
    arquivo.close()
    print('Lista de serviçoes salva com êxito')

def importar_user(usuarios):
    arq = open('usuarios.txt','r', encoding='utf-8')
    linhas = arq.readlines()
    for l in linhas:
        dados = l.split(' - ')
        usuarios.append([dados[0], dados[1], dados[2].replace('\n','') ])
    arq.close()

def importar_prod(produtos):
    arq = open('produtos.txt','r', encoding='utf-8')
    linhas = arq.readlines()
    for l in linhas:
        dados = l.split(' - ')
        produtos.append([dados[0], dados[1], dados[2], dados[3].replace('\n','') ])
    arq.close()

def importar_serv(servicos):
    arq = open('servicos.txt','r', encoding='utf-8')
    linhas = arq.readlines()
    for l in linhas:
        dados = l.split(' - ')
        servicos.append([dados[0], dados[1], dados[2].replace('\n',''), [] ])
    arq.close()

def janela_produto():
    def fechar_janela_produto(janela):
        janela.destroy()

    janela = tk.Tk()
    janela.title('PETSHOPCENTER')
    janela.geometry('300x50')

    tk.Label(janela, text='PRODUTO COMPRADO COM SUCESSO.').pack()
    janela.after(7000, fechar_janela_produto, janela)

    janela.mainloop()

def janela_servico():
    def fechar_janela_servico(janela):
        janela.destroy()

    janela = tk.Tk()
    janela.title('PETSHOPCENTER')
    janela.geometry('300x50')

    tk.Label(janela, text='SERVIÇO AGENDADO COM SUCESSO.').pack()
    janela.after(7000, fechar_janela_servico, janela)

    janela.mainloop()