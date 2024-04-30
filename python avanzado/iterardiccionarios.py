d1 = {
    "Nombre": "Adrian",
    "Edad": 23,
    "Documento": 689321
}

#Imprimir los keys del diccionario
for valor in d1:
    print(d1[valor])

#Imprimir el value desde el diccionario
for valor in d1:
    print(d1[valor])

#Imprimir el key y el valor 
for key, valor in d1.items():
    print(key, valor)
#Tenemos la funcion clear que limpia el diccionario y lo deja vacio 
d ={'a':1 ,'b':2}
print(d)
d.clear()
print(d) 

#Tenemos la funcion get que nos permite saber el valor de una clave descriptiva
d ={'a':1 ,'b':2}
print(d.get('a'))#Nos deberia de dar 1
print(d.get('z'))#Nos deberia de dar None
#Tambien podemos ponerle que nos arroje un mensaje en caso de error
print(d.get('z','Valor no encontrado'))#Nos deberia de dar None
