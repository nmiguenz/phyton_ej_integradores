print("\n")
print("************************************")
print("          Calculadora mcm")
print("************************************")

def maximo_comun_divisor(a, b):
    auxiliar = 0
    while b != 0:
        auxiliar = b
        b = a % b
        a = auxiliar
    return a

def minimo_comun_multiplo(a, b):
    return int((a * b) / maximo_comun_divisor(a, b))

a = int(input('Ingrese el primer número: '));
b = int(input('Ingrese el segundo número: '));

mcm = minimo_comun_multiplo(a, b)
print(
    f"El mínimo común múltiplo de {a} y {b} es {mcm}.")