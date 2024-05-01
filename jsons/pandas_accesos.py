import pandas as pd
#Lee el archivo CSV
#df es un data frame 
df =pd.read_csv(
    "C:/Progrmacion_2/Python_Netzu/Python_django/jsons/carreras.csv")
#Acceso por pocision de filas
print(df[0:3])
#acceso por columnas
print(df[['nombre','apellido','promedio']])