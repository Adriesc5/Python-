edad = int(input("Ingresar edad: "))
if edad >=18:
    print("Mayor de edad")
else:
    if edad > 0:
        print("Menor de edad")
    else:
        print("Edad no correcta")

numero = int(input("Ingresa un numero\n"))
if numero > 0:
    print("Ingresaste un numero positivo")
elif numero == 0:
    print("Ingresaste el numero 0")
else:
    print("Ingresaste un numero negativo")