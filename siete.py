# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos

from seis import Persona

class Cuenta():
    
    def __init__(self, titular: Persona = None, cantidad = None) -> None:
        self._titular = titular
        self._cantidad = cantidad

    def getTitular(self)-> Persona:
        return self._titular
    
    def getCantidad(self) -> float:
        return self._cantidad
        
    def setTitular(self, titular:Persona):
        if titular != None:
            self._titular = titular
        else:
            print('No puede ingresar datos vacíos')

    def setCantidad(self, cantidad):
        if cantidad != None:
            self._cantidad = cantidad
        else:
            print('No puede ingresar datos vacíos')
    
    def mostrar(self):
        return f'{self._titular.mostrar()} Cuenta con ${self._cantidad} en su cta.'
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad
        