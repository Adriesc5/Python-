#Una matriz es una lista de listas
matriz = []
filas = 4
columunas = 5
#Llenar la matriz 
for i in range(filas):
    fila = [0] * columunas
    matriz.append(fila)
    print(matriz)
    print("")


#Accesando
pbi =[[2.9,2.5],[3.9,4.0],[0.9,2.2],[1.5,3.3],
      [1.8,2.6],[1.0,2.0],[2.2,2.3],[4.0,4.0],
      [2.5,3.5],[3.0,3.0],[-9.5,-8.5]]

filas = 11
columunas = 2
for i in range(filas): #1 = 0
    for j in range(columunas):
        print(pbi[i][j], end=" ")
    print()

item = pbi[2][1]
print(item)
