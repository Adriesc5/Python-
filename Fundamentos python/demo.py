print("Hola mundo ")
#Creacion de variables 
edad = 10
variable = 20.0

#solicitar por consola un valor 
x = input("Ingresa un valor")

#Imprimir valor de una variable por consola

print(x)
print(edad) 
print(variable)

#Imprimir valores de variables en consola

print(x, edad, variable)

#Integer
entero = 57
print(entero)
#float
pi = 3.1416
print(pi)
#bool
verdadero = True
print(verdadero)
#String collecion o arreglo de caracteres
hola_mundo = "Hola mundo"
print(hola_mundo)
"""
Harenmos un ejercicio para conocer los Operadores de python"""
#Operador aritmetico de suma 
#Estamos usando la interpolacion, empezamos con f, luego comillas y entre {} ponemos las variables o valores 
print(f"Suma: 10 + 3 ={10 + 3}")
print(f"Resta: 10 - 3 ={10 - 3}")
print(f"Resta: 10 * 3 ={10 * 3}")
print(f"Division: 10 / 3 ={10 / 3}")
#Modulo es para sacar el restante de una division, en este caso sera uno, si fuera  9 % 3 =0
print(f"Modulo: 10 % 3 ={10 % 3}")
print(f"Exponente: 10 ** 3 ={10 ** 3}")
#Es lo mismo que la division pero redondeada
print(f"Division entera: 10 // 3 ={10 // 3}")
#Operadores de comparacion
print(f"Igualdad: 10 ==3  es {10 == 3}") #Deberia ser falso
print(f"Desigualdad: 10 ==3 es {10 != 3}")#Deberia ser verdadero
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 > 3 es {10 >= 3}")
print(f"Menor o igual que: 10 < 3 es {10 <= 3}")

#Operadores logicos
print(f"AND &&: 10 + 3 ==13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"or ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"not !:  10 + 3 == 14 es  {not 10 + 3 == 14}")

#Operadores de asignacion
my_number = 11 #asignacion
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 1 #multiplicacion y asignacion
print(my_number)
my_number /= 1 #division y asignacion
print(my_number)
my_number %= 1 #modulo y asignacion
print(my_number)
my_number **= 1 #exponente y asignacion
print(my_number)
my_number //= 1 #division entera y asignacion
print(my_number)

#Operadores de identidad
my_new_number = 1.0
print(f"My number is my_new_number es {my_number is my_new_number}")
print(f"My number is not my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia 
print(f"'a' in 'adrian' = {'a'in 'adrian'}")
print(f"'n' not in 'adrian' = {'b' not in 'adrian'}")

#Operadores de bit 
a = 10 # 1010
b = 3 # 0001
print(f"AND: 10 & 3= {10 & 3}") # 0010
print(f"OR: 10 & 3= {10 | 3}") #1011
print(f"XOR: 10 & 3= {10 ^ 3}") #1001
print(f"NOT: ~10= {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")#0010 
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")#101000 

"""
Estructuras de control
"""
#Condicionales
my_string = "Adriesc"
if my_string == "Adriesc":
    print("My string es 'Adriesc'")
elif my_string == "Adrian":
    print("My string es 'Adrian'")
else:
    print("My_striing no es 'Adriesc' ni 'Adrian'")

#Iteraticas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i+=1

#Manejo de exepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
#Siempre se corre el finally ya sea que se hay ido por el try o exept
finally:
    print("Ha finalizado el manejo de exepciones")
print("Extra")
number = 10
for number in range(10,56):
    if number % 2 == 0 and number % 3 != 0 and number !=16:
        print(number)