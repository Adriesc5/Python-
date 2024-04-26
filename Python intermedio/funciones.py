# def suma(a, b):
#     suma= a +b
#     return suma 

# def resta(c,d):
#     resta = c-d
#     return resta

# def multiplicacion(x,y):
#     cociente = x*y
#     return cociente


# resultado = suma(5,7)
# print(resultado)

# def funcion_parametros(a):
#     print(a)


# funcion_parametros("Soy una funcion con parametros")
# print(funcion_parametros)

# def suma():
#     d =int(input("Ingresar el numero 1: "))
#     e =int(input("Ingresar el numero 2: "))
#     suma = d + e
#     print("El resultado de la suma es",suma)

# suma()

# def calculadora(x,y):
#     suma = x+y
#     resta = x-y
#     multiplicacion = x*y
#     return suma, resta, multiplicacion

# a, b, c = calculadora(10,5)
# print(b)


def area_circulo(radio,pi = 3.1416):
    area = pi*pow(radio,2)
    return area
print(area_circulo(2))

def calculadora(x, y, z):
    su = x + z 
    re = y - z 
    mu = x*y 
    po = pow(x,y) 
    return su, re, mu, po

print(calculadora(10, 2, 5))