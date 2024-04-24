elementlist = [1,2,3,4,5]

for item in elementlist:
    print("Esta es un elemento de la lista ",item) 

texto ="Hola Mundo\n"
for x in texto:
    print(x)


for element in range(5,11):
    print(element)

print("")
for element in range(5,100,3):
    print(element)


# N = int(input("Ingresa la cantidad de alumnos: "))
# for i in range(N):
#     nombre = input("Nombre {}:".format(i+1))
    

N = int(input("Ingresa la cantidad de alumnos: "))
for i in range(N):
    nombre = input("ALUMNO {}: ".format(i+1))
    m = int(input("Ingresa la cantidad de cursos: "))
    for j in range(m):
        curso_nombre = input("CURSO {}: ".format(j+1))