matriz = [[1, 2 ], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18],[19, 20], [21, 22]]
suma = 0 
for x in range(len(matriz)):
    suma += x 
    print(suma)


d1 = dict(Nombre='Jorge', Edad=16, Nota=10.7) 
d2 = dict([ ('Nombre', 'Jorge'), ('Edad', 15), ('Nota', 17), ]) 
print(d1['Nota'] + d2['Nota'])