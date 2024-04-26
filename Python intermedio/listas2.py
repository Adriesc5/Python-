print("Ejemplos con POP")
lista_letras =['a','g','w','b','p','y']
print(lista_letras)
x = lista_letras.pop()
print(lista_letras)#Aqui nos imprime la lista completa ya con el valor eliminado
x = lista_letras.pop()
print(x)#Aqui nos imprime el valor que se va a eliminar 
print("Ejemplos con DEL")
lista_letras =['a','g','w','b','p','y']
print(lista_letras)
del lista_letras[2]
print(lista_letras)
del lista_letras[:2]#nos elimina desde el valor inicial(0) hasta el que pusimos
print(lista_letras)

print("Ejemplos con REMOVE")
lista_letras =['a','g','w','b','p','y']
print(lista_letras)
variable = 'y'
if variable in lista_letras:
    lista_letras.remove(variable)
    print(f"Removiendo la letra '{variable}' de la lista")
    print(lista_letras)
else:
    print(f"la letra {variable} no se encuentra en la lista")

