lista_Numeros = [1,2,3,4,5,6] *2
print(lista_Numeros)#El mutiplicador hace que la lista se inserte uina despues de otra


#In//busca un valor en la lista
lista = ["Juan","Pedro","Adrian"]
print("Adrian" in lista)#Deberia imprimir verdadero ya que es un booleano lo que arroja 
print("Joaquin" in lista)#Deberia imprimir falso ya que es un booleano lo que arroja 

print("Joaquin" not in lista)#Deberia imprimir verdadero ya que es un booleano lo que arroja y joaquin no esta en la lista
print("Adrian" not in lista)#Deberia imprimir falso ya que adrian si esta en la lista

lista.append("Stephania")
print(lista)#con el append el valor se agrega al final de la lista

lista.insert(2,"Joaquin")
print(lista)#El valor deberia estar en la tercera posicion ya que se inicia de 0

lista_letras =['a','b','c','z']
variable = 'e'
if variable in lista_letras:
    posicion = lista_letras.index(variable)
    print(f"La letra {variable} esta en la posicion {posicion+1}")
else:
    print(f"La letra {variable} no se encuentra en la lista ")