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

class TelaInicial(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("teste")
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
        self.master.title("novo")
        lTitulo = Label(self.master, text="Incluir Empresa", font="Arial 14 bold").grid(row=0)
        lEmpresa = Label(self.master, text="Nome da Empresa:").grid(row=1)
        eEmpresa = Entry(self.master).grid(row=1, column=1)
        lFase1 = Label(self.master, text="Fase 1", font="Arial 10 bold").grid(row=2)
        cEnviou1 = Checkbutton(self.master, text="Enviou").grid(row=3, column=0)
        cLancou1 = Checkbutton(self.master, text="Lançou").grid(row=3, column=1)
        lFase2 = Label(self.master, text="Fase 2", font="Arial 10 bold").grid(row=4)
        cEnviou2 = Checkbutton(self.master, text="Enviou").grid(row=5, column=0)
        cLancou2 = Checkbutton(self.master, text="Lançou").grid(row=5, column=1)
        lFase3 = Label(self.master, text="Fase 3", font="Arial 10 bold").grid(row=6)
        cEnviou3 = Checkbutton(self.master, text="Enviou").grid(row=7, column=0)
        cLancou3 = Checkbutton(self.master, text="Lançou").grid(row=7, column=1)

raiz = Tk()
raiz.geometry("400x300")
app = TelaInicial()
raiz.mainloop()
