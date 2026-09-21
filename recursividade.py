def contagem_regressiva(numero:int):
    if numero == 0:
        print("Fim")
        return
    print(numero)
    return contagem_regressiva(numero-1)

if __name__ == '__main__':
    contagem_regressiva(10)