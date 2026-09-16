'''
- Inserção e remoção em posições diferentes!

- LILO -> Last In Last Out
- FIFO -> First In First Out
'''
class FilaException(Exception):
    def __init__(self, mensagem):
        return super().__init__(mensagem)

class FilaSequencial:
    def __init__(self):
        self.__dados = []

    def vazio(self):
        return len(self.__dados) == 0

    def tamanho(self):
        return len(self.__dados)

    def inicio(self):
        if self.vazio():
            raise FilaException("A fila está vazia.")
        return self.__dados[0]

    def inserir(self):
        pass

    def remover(self):
        pass

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

if __name__ == '__main__':
    f = FilaSequencial()
    for i in range(1,6):
        f.inserir(i+10)

    print(f)
    f.remover(11)
    print(f)