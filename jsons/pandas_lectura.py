import pandas as pd
#Lee el archivo CSV
#df es un data frame 
df =pd.read_csv(
    "C:/Progrmacion_2/Python_Netzu/Python_django/jsons/carreras.csv")

# muestra las primera filas
print(df.head())
print(df)