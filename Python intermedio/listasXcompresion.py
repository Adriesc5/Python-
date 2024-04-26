numeros =[1,2,3,4,5,6,7,8,9]
r1 =[] #lista donde agregaremos los nuevos valores
for i in numeros: #for normal que recorre la lista
    valor = i*2 #multiplica el valor a cada valor de la lista
    r1.append(valor) #agregamos el nuevo valor a la lista
print("Listas utilizando for normal")
print(r1) #Imprimimos la lista
print("") #Salto de linea

print("Listas por comprension")
r2 = [e*2 for e in numeros if e > 4] #Lista por comprension 
print(r2)#imprimimos la nueva lista
