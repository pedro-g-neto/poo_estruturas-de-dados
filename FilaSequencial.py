class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class FilaSequencial:
    def __init__(self):
        self.__dados = []

    def vazio(self):
        return len(self.__dados) == 0
    
    def tamanho(self):
        return len(self.__dados)

    def inicio(self):
        if self.vazio():
            raise FilaException("Fila vazia")
        return self.__dados[0]

    def inserir(self, valor):
        self.__dados.append(valor)

    def remover(self):
        if not self.vazio():
            return self.__dados.pop(0)
        raise FilaException("Fila vazia")

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

if __name__ == "__main__":
    f = FilaSequencial()
    try:
        f.remover()
    except FilaException as fe:
        print(fe)