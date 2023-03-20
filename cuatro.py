# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

def creador_diccionario(cadena):
#   lista_1= cadena.split()
  lista = cadena.split(" ") #The split() method splits a string into a list
  diccionario = {}

  for i in lista:
    if i in diccionario:
      diccionario[i] +=1
    else:
      diccionario[i] = 1

  return diccionario

# Crea tupla de la primera ocurrencia
def crear_tupla(diccionario):
  palabra= ''
  contador=0
  for keys,values in diccionario.items():
    if values > contador:
      contador= values
      palabra= keys
  return palabra,contador

# Crea una tupla para más de una ocurrencia
def crear_tupla_plus(diccionario):
  contador = 0
  palabra_aux = ''
  aux = ''
  i = 0
  
  for key, value in diccionario.items():
    if value >= contador:
      contador = value

  for key, value in diccionario.items():
    if contador == value and palabra_aux != key:
      if i == 0:
        aux = key + ',' + str(value)
        palabra_aux = key
        i += 1
      else:
        aux = aux + ',' + key + ',' + str(value)
        palabra_aux = key
        i += 1

  palabras_tupla = tuple(map(str, aux.split(',')))
  return palabras_tupla;


entrada = input('Ingrese una cadena de caracteres: ')
diccionario = creador_diccionario(entrada)
print(diccionario)
print(crear_tupla_plus(diccionario))