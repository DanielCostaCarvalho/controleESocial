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
