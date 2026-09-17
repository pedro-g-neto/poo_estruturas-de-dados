class PilhaSequencial:
    def __init__(self, capacidade):
        self.dados = [None]*capacidade
        self.tamanho = 0
        self.capacidade = capacidade
    def vazia(self):
        return True if self.tamanho == 0 else False
    def cheia(self):
        return self.tamanho == self.capacidade
    def inserir(self,dado):
        if self.cheia():
            return False
        self.dados[self.tamanho] = dado
        self.tamanho += 1
    def remover(self):
        if self.vazia():
            return False
        for i in range(self.capacidade):
            self.dados[i] = self.dados[i+1]
        
    