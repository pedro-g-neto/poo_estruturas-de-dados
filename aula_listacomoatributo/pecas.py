# Aula: Lista como atributo
class Peca:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f"ID: {self.__id}\nNome: {self.__nome}"