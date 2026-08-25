#Aula: Lista como atributo
class Carro:
    def __init__(self, cor, placa, pecas = []):
        self.__cor = cor
        self.__placa = placa
        self.__pecas = pecas

    def get_cor(self):
        return self.__cor

    def get_placa(self):
        return self.__placa

    def get_pecas(self):
        return self.__pecas

    def set_cor(self, cor):
        self.__cor = cor

    def add_peca(self, peca):
        self.__pecas.append(peca)

    def __str__(self):
        saida = ''
        for i in range(len(self.__pecas)):
            saida += f"{self.__pecas[i]} "
        return f"Cor: {self.__cor}\nPlaca: {self.__placa}\nPeças: {saida}"