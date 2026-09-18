class FilaSequencial:
    def __init__(self,capacidade:int):
        self.dados = [None]*capacidade
        self.inicio = 0
        self.final = 0
        self.capacidade = capacidade
        self.tamanho = 0
    def vazia(self):
        return self.tamanho == 0

    def enfileirar(self,dado):
        self.dados[self.final] = dado
        self.tamanho += 1
        self.final = (self.final + 1) % self.capacidade
        return True
    def desenfileirar(self):
        if self.vazia():
            return False
        removido = self.dados[self.inicio]
        self.dados[self.inicio] = None
        self.tamanho -= 1
        self.inicio = (self.inicio + 1) % self.capacidade
        return removido
    def primeiro(self):
        return self.dados[self.inicio]