# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva

def get_init(value):
    try:
        is_numeric = int(value)
        print(f'El valor numérico ingresado es: {is_numeric}')
    except ValueError:
        print(f'No es un número.')
        get_init(input('Ingrese un valor numérico: '))
        

get_init(input('Ingrese un valor numérico: '))