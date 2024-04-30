matriz =[]
ALUMNOS = 2
NOTAS = 3
#Llenar la matriz
for i in range(ALUMNOS):
    notas = []
    print("Alumno {}".format(i+1))
    for j in range(NOTAS):
        nota = float(input("Nota {}: ".format(j+1)))
        notas.append(nota)
    matriz.append(notas)

#Recorrer la matriz 

print("Recorrido de la matriz por medio de for")
for i in range(ALUMNOS):
    for j in range(NOTAS):
        print(matriz[i][j],end =" ")
    print()