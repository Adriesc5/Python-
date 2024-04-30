#Podemos crear diccionarios de distintas formas
#1
diccionario = dict()
print(diccionario)
#Modo 2
d1 = {
    "Nombre": "Adrian",
    "Edad": 23,
    "Documento": 689321
}
print(d1)
#Modo 3
d2 = ({
    'Nombre': "Adrian",
    "Edad": 23,
    "Documento": 689321
    })
print(d2)
#Modo 4
d3 =dict(Nombre = 'Adrian',
         Edad = 25,
         Documento = 689321)
print(d3)

# #Acceso, en este caso accesamos por medio de las llaves
# Para accesar es por medio de las llaves y de el nombre del diccionario
print(d3["Nombre"])