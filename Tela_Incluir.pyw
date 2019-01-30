from tkinter import *
import Empresa

class Tela_Incluir(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("novo")
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        menuEmpresa = Menu(menubar)
        menuEmpresa.add_command(label="Inclusão", command = self.iincluir)
        menuEmpresa.add_command(label="Modificação", command = self.imodificar)
        menuListagem = Menu(menubar)
        menuListagem.add_command(label="Listar pendentes da fase 1", command = self.ilistar1)
        menuListagem.add_command(label="Listar pendentes da fase 2", command = self.ilistar2)
        menuListagem.add_command(label="Listar pendentes da fase 3", command = self.ilistar3)
        menubar.add_cascade(label = "Empresa", menu = menuEmpresa)
        menubar.add_cascade(label="Relatórios", menu=menuListagem)

    def iincluir(self):
        pass

    def imodificar(self):
        pass

    def ilistar1(self):
        pass

    def ilistar2(self):
        pass

    def ilistar3(self):
        pass
