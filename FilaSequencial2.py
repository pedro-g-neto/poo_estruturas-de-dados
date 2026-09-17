class FilaSequencial:
    def __init__(self,capacidade:int):
        self.dados = [None]*capacidade
        self.inicio = 0
        self.final = 0
        self.capacidade = capacidade
    def vazia(self):
        return self.inicio == self.final

    def enfileirar(self,dado):
        self.dados[self.final] = dado
        if self.final == (self.capacidade - 1):
            self.final = (self.final + 1) % self.capacidade
            return True
        self.final += 1
        return True
    def desenfileirar(self):
        if self.vazia():
            return False
        self.dados[self.inicio] = None
        if self.inicio == (self.capacidade - 1):
            self.inicio = (self.inicio + 1) % 5
            return True
        self.inicio += 1
        return True
    def primeiro(self):
        return self.dados[self.inicio]