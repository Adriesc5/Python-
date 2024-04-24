iterator = 0
while iterator != 12:
    print(iterator)
    iterator += 3

#Crear un programa que permita ingresar los nombres de N alumnos 
n = int(input("Ingresar cantidad de estudiantes: "))
i = 1
while n >= i:
    nombre = input("Nombre {}: ".format(i))
    i += 1

#While anidado
#

N = int(input("Ingresar cantidad de estudiantes: "))
i = 1
j = 0
while N >=i: 
    nombre = input("Alumno {}:".format(i))
    M = int(input("Ingresar cantidad de cursos: "))
    while M > j:
        curso_nombre = input("CURSO {}: ".format(j+1))
        j+=1
    i +=1   