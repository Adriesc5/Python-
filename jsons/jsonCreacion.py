import json
obj ={
    "Nombre":"Adrian Escobedo",
    "Edad": 23,
    "Ciudad": "Chihuahua"
}
#Guardar en un archivo Json
with open('C:/Progrmacion_2/Python_Netzu/Python_django/jsons/formato_json.json','w') as outfile:
    #Convertir a json
    json.dump(obj,outfile)