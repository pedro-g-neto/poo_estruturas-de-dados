class No:
    def __init__(self,valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            return True
        
        
