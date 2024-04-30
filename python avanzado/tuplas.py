#para convertir una lista a tupla 
lista = [1,2,3,4]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

#asignacion 
l =(1,2,3)
x, y, z = l
print(x,y,z)
#Podemos recorrer las tuplas con for
for i in tupla:
    print(i)
print("")
#Podemos buscar y contabilizar elementos
y =(1,1,1,1,2,3,4,5)
print(y.count(1)) #Deberia darnos un valor de 4
#Podemos buscar la posicion de un elemento con la funcion index
#1 parametro
print(y.index(4))
#2 parametros, en el segundo parametro le decimos desde que posicion empezar a buscar
print(y.index(1,3))



