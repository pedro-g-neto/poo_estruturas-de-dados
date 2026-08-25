class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano

    @dia.setter
    def dia(self, dia):
        self.__dia = dia
    @mes.setter
    def mes(self, mes):
        self.__mes = mes
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

if __name__ == "__main__":
    entrada = input("Digite uma data: ")
    dia, mes, ano = entrada.split("/")
    hoje = Data(dia,mes,ano)
    print(hoje.dia)
    print(hoje.mes)
    print(hoje.ano)
    print(hoje)
    entrada = input("Digite outra data: ")
    hoje.dia, hoje.mes, hoje.ano = entrada.split("/")
    print(hoje.dia)
    print(hoje.mes)
    print(hoje.ano)
    print(hoje)
