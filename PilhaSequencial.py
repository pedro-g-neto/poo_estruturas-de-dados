class PilhaSequencial:
    def __init__(self, capacidade):
        self.dados = [None]*capacidade
        self.tamanho = 0
        self.capacidade = capacidade
    def vazia(self):
        return self.tamanho == 0
    def cheia(self):
        return self.tamanho == self.capacidade
    def inserir(self,dado):
        if self.cheia():
            return False
        self.dados[self.tamanho] = dado
        self.tamanho += 1
        return True
    def remover(self):
        if self.vazia():
            return False
        self.tamanho -= 1
        lastIn = self.dados[self.tamanho]
        self.dados[self.tamanho] = None
        return lastIn
    def topo(self):
        if self.vazia():
            return None
        return self.dados[self.tamanho-1]
    
        
    