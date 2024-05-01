import json
with open('C:/Progrmacion_2/Python_Netzu/Python_django/jsons/universidades.json','r') as json_file:
    #para imprimir informacion con un formato feo 
    # data =json.load(json_file)
    # diccionario = data[0]
    # print(data)
    # print(diccionario)
    # print('universidad:', diccionario['universidad'])
    # print('ubicacion:', diccionario['ubicacion'])
    # print('fundacion:', diccionario['fundacion'])
    #Para imprimir informacion con un mejor formato
    data= json.load(json_file)

print(json.dumps(data, indent=8))