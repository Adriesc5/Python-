fichero = open('C:/Progrmacion_2/Python_Netzu/Python_django/archivos.py/texto.txt','r')
# oracion =fichero.readline()
# while oracion != "":
#     print(oracion, end=" ")
#     oracion = fichero.readline()


lineas = fichero.readlines()
print(type(lineas))
print(lineas)

