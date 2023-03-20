# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

from siete import Cuenta
from seis import Persona

class CuantaJoven(Cuenta):

    def __init__(self, titular: Persona, cantidad, bonificacion) -> None:
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
        
    def getBonificacion(self) -> float:
        return self._bonificacion
        
    def setBonificacion(self, bonificacion):
        if bonificacion != None:
            if type(bonificacion) in (int, float):
                self._bonificacion = bonificacion
            else:
                print('Es un número inválido.')
        else:
            print('No puede ingresar datos vacíos')
        
    def es_titular_valido(self):
        
        if self._titular.es_mayor_de_edad() and self._titular.getEdad() < 25:
            return True
        else:
            return False
    
    def retirarCj(self, valor):
        if self.es_titular_valido():
            self.retirar(valor)
    
    def mostrar(self):
        return f'Cuenta joven - Bonificación: {self._bonificacion}%.'
    
