from tkinter import *

class TelaInicial(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("teste")
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        menuEmpresa = Menu(menubar)
        menuEmpresa.add_command(label="Inclusão", command = Tela_Incluir)
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

class Tela_Incluir(TelaInicial):
    def __init__(self):
        super().__init__()
        self.master.title("novo")


raiz = Tk()
raiz.geometry("800x600")
app = TelaInicial()
raiz.mainloop()
