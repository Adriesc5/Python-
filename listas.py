lista1 = []
lista2 = [None]
enteros = [0,1,2,3,4,5,6,7,8,9]
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
variados = [1,2, "Jueves", 4 ]

print(len(dias))
print("")
print("Utilizando for")
print("")
for dia in dias:
    print(dia)
print("")

print("Utilizando range")
print("")
for dia in range(len(dias)):
    print(dias[dia])
print("")
print("Utiizando enumerate")
print("")
for dia, item in enumerate(dias):
    print(dia+1,item)
#Recortadores
print(dias[2:5])
print(dias[-2])
print(dias[-2:])#Se imprime de atras para adelante, por ejemplo se podria utilizar para saber los ultimos dos
#Podemos usar len para imprimir el ultimo valor tambien 
print("Cantidad de elementos",len(dias)) # aqui para saber el valor
print(dias[len(dias)-1]) #como inicia desde 0 tenemos que usar el -1,
# ya que el len nos devuelve el valor total, desde el 0 hasta el 7