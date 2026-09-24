from PilhaEncadeada import PilhaEncadeada
from FilaEncadeada import FilaEncadeada

def inverter_pilha(pilha:PilhaEncadeada):
    filaAux = FilaEncadeada()
    while not pilha.vazia():
        filaAux.enfileirar(pilha.desempilhar())
    while not filaAux.vazia():
        pilha.empilhar(filaAux.desenfileirar())
    return pilha
    