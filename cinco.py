# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva

def get_int():
    boolean = False
    while  boolean != True:
        try:
            number = input("Ingrese un valor numérico:" )
            number = int(number)
            boolean = True
            print("Ha ingresado un entero.")
        except ValueError:
            print(f'No es un número.')
            boolean = False

get_int()