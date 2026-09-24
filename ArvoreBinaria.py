class No:
    def __init__(self,valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            return True
        else: 
            return self._inserir_recursivo(valor, self.raiz)
    def _inserir_recursivo(self, valor, atual):
        if valor < atual.valor:
            if atual.esq is None:
                atual.esq = No(valor)
                return True
            return self._inserir_recursivo(valor, atual.esq)
        elif valor > atual.valor:
            if atual.dir is None:
                atual.dir = No(valor)
                return True
            return self._inserir_recursivo(valor, atual.dir)
        else:
            return False

    def pre_ordem(self):
        self._pre_ordem(self.raiz)
    def _pre_ordem(self, no):
        if no is None:
            return
        print(no.valor, end=' ')
        self._pre_ordem(no.esq)
        self._pre_ordem(no.dir)
    def _em_ordem(self, no):
        if no is None:
            return
        self._em_ordem(no.esq)
        print(no.valor, end=" ")
        self._em_ordem(no.dir)
    def em_ordem(self):
        self._em_ordem(self.raiz)

    def _pos_ordem(self, no):
        if no is None:
            return
        self._pos_ordem(no.esq)
        self._pos_ordem(no.dir)
        print(no.valor, end=" ")
    def pos_ordem(self):
        self._pos_ordem(self.raiz)


def soma_nos(p:ArvoreBinaria):
    if p is None:
        return 0
    return p.valor + soma_nos(p.esq) + soma_nos(p.dir)
    
        
        
