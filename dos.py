print("\n")
print("************************************")
print("          Crear diccionario ")
print("************************************")

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

entrada = input('Ingrese su cadena de caracteres: ')
print(creador_diccionario(entrada))