from int_poo.motor import Motor

class Carro:
    def __init__(self, cor, placa, motor):
        self.__cor = cor
        self.__placa = placa
        self.__motor = motor

    @property
    def cor(self):
        return self.__cor
    @property
    def placa(self):
        return self.__placa
    @property
    def motor(self):
        return self.__motor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def __str__(self):
        return f"Cor: {self.__cor}\nPlaca: {self.__placa}\nMotor: {self.__motor}"

if __name__ == '__main__':
    carro = Carro('Vermelho', 'ABC-1234', Motor(1.8, 'gasolina'))
    print(carro)
    carro.motor.motorizacao = 2.0
    carro.motor.combustivel = 'flex'
    print(carro)
    