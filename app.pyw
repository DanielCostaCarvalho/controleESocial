from tkinter import *
import sqlite3

class Empresa:
    def __init__(self, nome, cnpj, enviou1 = False, passou1 = False, enviou2 = False, passou2 = False, enviou3 = False, passou3 = False, observacao = ""):
        self.nome = nome
        self.cnpj = cnpj
        self.enviou1 = enviou1
        self.enviou3 = enviou3
        self.enviou2 = enviou2
        self.passou1 = passou1
        self.passou2 = passou2
        self.passou3 = passou3
        self.observacao = observacao

    def cadastrar(self):
        conn = sqlite3.connect('controleESocial.db')
        cursor = conn.cursor()
        comando="insert into Empresa(nome, enviou1, enviou2, enviou3, passou1, passou2, passou3, obs, cnpj) values ('{}',{},{},{},{},{},{},'{}','{}')".format(self.nome, self.enviou1, self.enviou2, self.enviou3, self.passou1, self.passou2, self.passou3, self.observacao, self.cnpj)
        cursor.execute(comando)
        conn.commit()
        conn.close()


    def __str__(self):
        if(self.enviou1 == 1):
            e1="Sim"
        else:
            e1="Não"
        if(self.enviou2 == 1):
            e2="Sim"
        else:
            e2="Não"
        if(self.enviou3 == 1):
            e3="Sim"
        else:
            e3 = "não"
        if(self.passou1 == 1):
            p1="Sim"
        else:
            p1="Não"
        if(self.passou2 == 1):
            p2="Sim"
        else:
            p2="Não"
        if(self.passou3 == 1):
            p3="Sim"
        else:
            p3="Não"
        return "Nome: {}\nCNPJ: {}\nFase1\nEnviou: {} Passou: {}\nFase2\nEnviou: {} Passou: {}\nFase3\nEnviou: {} Passou: {}\nObservação: {}\n\n".format(self.nome, self.cnpj, e1, p1, e2, p2, e3, p3, self.observacao)

class TelaInicial(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Controle eSocial")
        self.telaAtual = "inicial"
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        menuEmpresa = Menu(menubar)
        menuEmpresa.add_command(label="Inclusão", command = self.telaIncluir)
        menuEmpresa.add_command(label="Modificação", command = self.modificar)
        menuListagem = Menu(menubar)
        menuListagem.add_command(label="Listar pendentes da fase 1", command = self.listar1)
        menuListagem.add_command(label="Listar pendentes da fase 2", command = self.listar2)
        menuListagem.add_command(label="Listar pendentes da fase 3", command = self.listar3)
        menubar.add_cascade(label = "Empresa", menu = menuEmpresa)
        menubar.add_cascade(label="Relatórios", menu=menuListagem)

        # Incluir
        self.master.title("Incluir Empresa")
        self.lTitulo = Label(self.master, text="Incluir Empresa", font="Arial 14 bold")
        self.lEmpresa = Label(self.master, text="Nome da Empresa:")
        self.eEmpresa = Entry(self.master)
        self.lCnpj = Label(self.master, text="CNPJ:")
        self.eCnpj = Entry(self.master)
        self.lFase1 = Label(self.master, text="Fase 1", font="Arial 10 bold")
        self.enviou1=IntVar()
        self.cEnviou1 = Checkbutton(self.master, text="Enviou", variable=self.enviou1)
        self.passou1=IntVar()
        self.cPassou1 = Checkbutton(self.master, text="Passou", variable=self.passou1)
        self.lFase2 = Label(self.master, text="Fase 2", font="Arial 10 bold")
        self.enviou2=IntVar()
        self.cEnviou2 = Checkbutton(self.master, text="Enviou", variable=self.enviou2)
        self.passou2=IntVar()
        self.cPassou2 = Checkbutton(self.master, text="Passou", variable=self.passou2)
        self.lFase3 = Label(self.master, text="Fase 3", font="Arial 10 bold")
        self.enviou3=IntVar()
        self.cEnviou3 = Checkbutton(self.master, text="Enviou", variable=self.enviou3)
        self.passou3=IntVar()
        self.cPassou3 = Checkbutton(self.master, text="Passou", variable=self.passou3)
        self.lObs = Label(self.master, text="Observação:")
        self.eObs = Entry(self.master)
        self.bSalvar = Button(self.master, command=self.salvar, text="Salvar")
        self.bLimpar = Button(self.master, command=self.limpar, text="Limpar")

    def modificar(self):
        self.limparTela()
        pass

    def listar1(self):
        pass

    def listar2(self):
        pass

    def listar3(self):
        pass

    def limparTela(self):
        if(self.telaAtual == "inicial"):
            pass
        elif(self.telaAtual == "incluir"):
            self.telaAtual = "incluir"
            self.lTitulo.grid_remove()
            self.lEmpresa.grid_remove()
            self.eEmpresa.grid_remove()
            self.lCnpj.grid_remove()
            self.eCnpj.grid_remove()
            self.lFase1.grid_remove()
            self.cEnviou1.grid_remove()
            self.cPassou1.grid_remove()
            self.lFase2.grid_remove()
            self.cEnviou2.grid_remove()
            self.cPassou2.grid_remove()
            self.lFase3.grid_remove()
            self.cEnviou3.grid_remove()
            self.cPassou3.grid_remove()
            self.lObs.grid_remove()
            self.eObs.grid_remove()
            self.bSalvar.grid_remove()
            self.bLimpar.grid_remove()


    def telaIncluir(self):
        self.limparTela()
        self.telaAtual = "incluir"
        self.lTitulo.grid(row=0)
        self.lEmpresa.grid(row=1)
        self.eEmpresa.grid(row=1, column=1)
        self.lCnpj.grid(row=2)
        self.eCnpj.grid(row=2, column=1)
        self.lFase1.grid(row=3)
        self.cEnviou1.grid(row=4, column=0)
        self.cPassou1.grid(row=4, column=1)
        self.lFase2.grid(row=5)
        self.cEnviou2.grid(row=6, column=0)
        self.cPassou2.grid(row=6, column=1)
        self.lFase3.grid(row=7)
        self.cEnviou3.grid(row=8, column=0)
        self.cPassou3.grid(row=8, column=1)
        self.lObs.grid(row=9)
        self.eObs.grid(row=9, column=1)
        self.bSalvar.grid(row=10, column=0)
        self.bLimpar.grid(row=10, column=5)

    def salvar(self):
        e = Empresa(self.eEmpresa.get(), cnpj=self.eCnpj.get(),observacao=self.eObs.get(),enviou1=self.enviou1.get(),passou1=self.passou1.get(),enviou2=self.enviou2.get(),passou2=self.passou2.get(),enviou3=self.enviou3.get(),passou3=self.passou3.get())
        e.cadastrar()

        self.eEmpresa.delete(0, 'end')
        self.eObs.delete(0, 'end')
        self.eCnpj.delete(0, 'end')
        enviou1=self.cEnviou1.deselect()
        passou1=self.cPassou1.deselect()
        enviou2=self.cEnviou2.deselect()
        passou2=self.cPassou2.deselect()
        enviou3=self.cEnviou3.deselect()
        passou3=self.cPassou3.deselect()

    def limpar(self):
        self.eEmpresa.delete(0, 'end')
        self.eObs.delete(0, 'end')
        enviou1=self.cEnviou1.deselect()
        passou1=self.cPassou1.deselect()
        enviou2=self.cEnviou2.deselect()
        passou2=self.cPassou2.deselect()
        enviou3=self.cEnviou3.deselect()
        passou3=self.cPassou3.deselect()


raiz = Tk()
raiz.geometry("400x300")
app = TelaInicial()
raiz.mainloop()
