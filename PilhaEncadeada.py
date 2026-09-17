class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    def vazia(self):
        return self.tamanho == 0
    def empilhar(self,dado):
        novoNode = Node(dado)
        novoNode.prox = self.topo
        self.topo = novoNode
        self.tamanho += 1
        return True
    def desempilhar(self):
        if self.vazia():
            return None
        removido = self.topo.dado
        self.topo = self.topo.prox
        self.tamanho -= 1
        return removido
        
    

    