def numero_mayor(numero1, numero2):
    respuesta = False
    if numero1 > numero2:
        return True
    return respuesta

x = int(input("Numero 1: "))
y = int(input("Numero 2: "))

if numero_mayor(x,y):
    print("El numero {} es mayor a {}".format(x,y))
else:
    print("El numero {} es mayor a {}".format(y,x))
