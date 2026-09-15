class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
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
        if self.head is None:
            self.head = novo_node
            return
        novo_node.next = self.head
        self.head = novo_node