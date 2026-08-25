# Aula: Lista como atributo
from aula_listacomoatributo.novo_carro import Carro
from aula_listacomoatributo.pecas import Peca

if __name__ == '__main__':
    pecas = []

    p1 = Peca('1', 'Chassi')
    p2 = Peca('2', 'Volante')
    p3 = Peca('3', 'Discos de freio')
    pecas.append(p1)
    pecas.append(p2)
    pecas.append(p3)

    carro = Carro('Vermelho', 'ABC-1234', pecas)
    print(carro)
    print(carro.get_pecas())
    print(carro.get_pecas()[2])
    print(carro.get_pecas()[2].nome)

    carro.get_pecas()[2].nome = 'Pastilhas de freio'
    print(carro.get_pecas()[2].nome)

    carro.add_peca(Peca('4', 'Pneus'))
    print(carro.get_pecas())

    print(carro)
