# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():

    def __init__(self,nombre = None, edad = None, dni = None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    #getters
    def getNombre(self) -> str:
        return self._nombre

    def getEdad(self) -> int:
        return self._edad

    def getDni(self) -> int:
        return self._dni
    
    #setters
    def setNombre(self, value):
        if value.istitle():
            self._nombre = value
        else:
            print("El nombre no tiene un formato válido.")

    def setEdad(self, value):
        if value.isdigit():
            if value > 0 or value < 130:
                self._edad = value
            else:
                print("La edad no es correcta.")
        else:
            print("La edad no tiene un formato válido.")

    def setDni(self, value):
        if value.isdigit():
            if value > 0:
                self._dni = value
            else: 
                print("El dni debe tener un valor mayor a 0")
        else:
            print("El dni no tiene un formato válido.")
        
    def mostrar(self):
        return f'{self._nombre} con dni: {self._dni} tiene {self._edad} años.'
    
    def es_mayor_de_edad(self):
        return self._edad >= 18
