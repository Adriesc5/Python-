#Apertura de archivo
fichero = open('C:/Progrmacion_2/Python_Netzu/Python_django/archivos.py/texto.txt','r')


#'r': Por defecto, para leer el fichero
#'w': Para escribir en el fichero

#2.Lectura de todo el fichero
print(fichero.read())

#cierre de archivo
fichero.close()