import pandas as pd
#Lee el archivo CSV
#df es un data frame 
df =pd.read_csv(
    "C:/Progrmacion_2/Python_Netzu/Python_django/jsons/carreras.csv")
#Filtrado
filter = df['carrera'] == 'Arquitectura'

df_carrera = df.where(filter)
df_sin_nan = df_carrera.dropna()
print(df_sin_nan)