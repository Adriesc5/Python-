fichero = open('C:/Progrmacion_2/Python_Netzu/Python_django/archivos.py/textoConFor.txt','w')
lista =['Mercedes','AMG','Ferrari']
for linra in lista:
    fichero.write(linra +"\n")

#Cerramos fichero
fichero.close()