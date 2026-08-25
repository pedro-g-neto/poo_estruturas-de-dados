class Aluno:
    def __init__(self, matricula:int, nome:str, notas:list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    @property
    def matricula(self):
        matricula_str = str(self.__matricula)
        return f"{matricula_str[:4]}.{matricula_str[4]}.{matricula_str[5:]}"
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome:str):
        self.__nome = nome

    def media(self):
        soma = sum(self.__notas)
        media = soma/len(self.__notas)
        return media

    def adiciona_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.__notas.append(nota)

if __name__ == '__main__':
    matricula = int(input("Digite a matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    notas = list(map(float, input("Digite as notas do aluno separadas por espaço: ").split()))
    aluno1 = Aluno(matricula, nome, notas)
    print(f"Nome do aluno: {aluno1.nome}\nMatrícula: {aluno1.matricula}\nMédia do aluno: {aluno1.media()}")
    nota = float(input(f"Digite uma nota para adicionar ao boletim do aluno {aluno1.nome}: "))
    aluno1.adiciona_nota(nota)
    print(f"Nova média de {aluno1.nome}: {aluno1.media():.2f}")

    
