class Motor:
    def __init__(self, motorizacao, combustivel = 'flex'):
        self.__motorizacao = motorizacao
        self.__combustivel = combustivel

    @property
    def motorizacao(self):
        return self.__motorizacao
    @property
    def combustivel(self):
        return self.__combustivel

    @motorizacao.setter
    def motorizacao(self, motorizacao):
        self.__motorizacao = motorizacao
    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel

    def __str__(self):
        return f"Motorização: {self.__motorizacao}\nCombustível: {self.__combustivel}"

if __name__ == '__main__':
    motor = Motor(2.0)
    print(motor.motorizacao)