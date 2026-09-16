class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def pertence(self, data):
        atual = self.head
        while atual:
            if data == atual.data:
                return True
            atual = atual.next
        return False

    def vazio(self):
        vazio = True if self.head is None else False
        return vazio
    
    def inserir_final(self, data):
        novo_node = Node(data)
        if self.head is None:
            self.head = novo_node
            return
        atual = self.head
        while atual.next:
            atual = atual.next
        atual.next = novo_node

    def display(self):
        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.data))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")

    def inserir_inicio(self, data):
        novo_node = Node(data)
        novo_node.next = self.head
        self.head = novo_node

    def remover(self, data):
        if self.vazio():
            return False
        if data == self.head.data:
            self.head = self.head.next
            return True
        atual = self.head.next
        anterior = self.head
        while atual:
            if atual.data == data:
                anterior.next = atual.next
                return True
            atual = atual.next
            anterior = anterior.next
        return False

if __name__ == "__main__":
    lista = LinkedList()
    lista.inserir_inicio("A")
    lista.inserir_inicio("B")
    lista.inserir_final("C")
    lista.display()