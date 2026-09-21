class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    def vazia(self):
        return self.tamanho == 0
    
    def enfileirar(self, dado):
        novo_node = Node(dado)
        if self.vazia():
            self.inicio = novo_node 
            self.final = novo_node

            self.inicio.prox = self.final
            self.final.prox = None

            return True
        
        self.final.prox = novo_node
        self.final = novo_node
        self.tamanho += 1

        return True
    
    def desenfileirar(self):
        if self.vazia():
            return None
        
        removido = self.inicio.dado

        self.inicio = self.inicio.prox
        self.tamanho -= 1

        if self.vazia():
            self.final = None
            
        return removido