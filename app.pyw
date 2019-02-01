from tkinter import *

class Empresa:
    def __init__(self, nome, enviou1 = False, passou1 = False, enviou2 = False, passou2 = False, enviou3 = False, passou3 = False, observacao = ""):
        self.nome = nome
        self.enviou1 = enviou1
        self.enviou2 = enviou2
        self.enviou3 = enviou3
        self.passou1 = passou1
        self.passou2 = passou2
        self.passou3 = passou3
        self.observacao = observacao

    def __str__(self):
        return "Nome: {}\nFase1\nEnviou: {} Passou: {}\nFase2\nEnviou: {} Passou: {}\nFase3\nEnviou: {} Passou: {}\nObservação: {}\n\n".format(self.nome, self.enviou1, self.passou1, self.enviou2, self.passou2, self.enviou3, self.passou3, self.observacao)

class TelaInicial(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Controle eSocial")
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        menuEmpresa = Menu(menubar)
        menuEmpresa.add_command(label="Inclusão", command = TelaIncluir)
        menuEmpresa.add_command(label="Modificação", command = self.modificar)
        menuListagem = Menu(menubar)
        menuListagem.add_command(label="Listar pendentes da fase 1", command = self.listar1)
        menuListagem.add_command(label="Listar pendentes da fase 2", command = self.listar2)
        menuListagem.add_command(label="Listar pendentes da fase 3", command = self.listar3)
        menubar.add_cascade(label = "Empresa", menu = menuEmpresa)
        menubar.add_cascade(label="Relatórios", menu=menuListagem)


    def modificar(self):
        pass

    def listar1(self):
        pass

    def listar2(self):
        pass

    def listar3(self):
        pass

class TelaIncluir(TelaInicial):
    def __init__(self):
        super().__init__()
        self.master.title("Incluir Empresa")
        self.lTitulo = Label(self.master, text="Incluir Empresa", font="Arial 14 bold").grid(row=0)
        self.lEmpresa = Label(self.master, text="Nome da Empresa:").grid(row=1)
        self.eEmpresa = Entry(self.master)
        self.eEmpresa.grid(row=1, column=1)
        self.lFase1 = Label(self.master, text="Fase 1", font="Arial 10 bold").grid(row=2)
        self.enviou1=IntVar()
        self.cEnviou1 = Checkbutton(self.master, text="Enviou", variable=self.enviou1)
        self.cEnviou1.grid(row=3, column=0)
        self.passou1=IntVar()
        self.cPassou1 = Checkbutton(self.master, text="Passou", variable=self.passou1)
        self.cPassou1.grid(row=3, column=1)
        self.lFase2 = Label(self.master, text="Fase 2", font="Arial 10 bold").grid(row=4)
        self.enviou2=IntVar()
        self.cEnviou2 = Checkbutton(self.master, text="Enviou", variable=self.enviou2)
        self.cEnviou2.grid(row=5, column=0)
        self.passou2=IntVar()
        self.cPassou2 = Checkbutton(self.master, text="Passou", variable=self.passou2)
        self.cPassou2.grid(row=5, column=1)
        self.lFase3 = Label(self.master, text="Fase 3", font="Arial 10 bold").grid(row=6)
        self.enviou3=IntVar()
        self.cEnviou3 = Checkbutton(self.master, text="Enviou", variable=self.enviou3)
        self.cEnviou3.grid(row=7, column=0)
        self.passou3=IntVar()
        self.cPassou3 = Checkbutton(self.master, text="Passou", variable=self.passou3)
        self.cPassou3.grid(row=7, column=1)
        self.lObs = Label(self.master, text="Observação:").grid(row=8)
        self.eObs = Entry(self.master)
        self.eObs.grid(row=8, column=1)
        self.bSalvar = Button(self.master, command=self.salvar, text="Salvar").grid(row=9, column=0)
        self.bLimpar = Button(self.master, command=self.limpar, text="Limpar").grid(row=9, column=5)

    def salvar(self):
        e = Empresa(self.eEmpresa.get(),observacao=self.eObs.get(),enviou1=self.enviou1.get(),passou1=self.passou1.get(),enviou2=self.enviou2.get(),passou2=self.passou2.get(),enviou3=self.enviou3.get(),passou3=self.passou3.get())
        self.eEmpresa.delete(0, 'end')
        self.eObs.delete(0, 'end')
        enviou1=self.cEnviou1.deselect()
        passou1=self.cPassou1.deselect()
        enviou2=self.cEnviou2.deselect()
        passou2=self.cPassou2.deselect()
        enviou3=self.cEnviou3.deselect()
        passou3=self.cPassou3.deselect()

        print(e)

    def limpar(self):
        pass

raiz = Tk()
raiz.geometry("400x300")
app = TelaInicial()
raiz.mainloop()
