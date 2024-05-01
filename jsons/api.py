import requests
import json

#Parametro
name=input('Ingrese el nombre: ')
#url del API REST
URL = "https://api.nationalize.io/?name=" + name
#invoca el servicio web
#se recibe en un diccionario
result =requests.get(URL).json()
#muestra el resultado
print(json.dumps(result, indent=4))