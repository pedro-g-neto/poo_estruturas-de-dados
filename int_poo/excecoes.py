import math

def fproblema(var):
    raise ZeroDivisionError("Divisão por zero não é permitida.")

try:
    fproblema(4)

except ZeroDivisionError as e:
    print(f"Erro: {e}")

else:
    print("Nenhum erro ocorreu.")

finally:
    print("Execução finalizada.")

def KelvinToFahrenheit(temperatura):
    assert temperatura >= 0, "A temperatura não pode ser menor que zero Kelvin."
    return (temperatura - 273.15) * 9/5 + 32

try:
    x = float(input("x = "))
    assert x >=0.0
    x = math.sqrt(x)
    print(f"Raiz quadrada de {x} é {x}")

except AssertionError:
    print(f"Erro {x} é inválido")

print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(505.78))
print(KelvinToFahrenheit(-5))
print("Fim do programa.")