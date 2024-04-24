#Break

 #Se quiere correr del 1 al 100 pero si llega al 5 se rompe la operacion
i =1
while i < 100:
    if i == 5:
        break
    else:
        print(i)
        i+=1

#Continue 
#Aqui en su diferencia en lugar de querer romper el algoritmo, lo que se esta
#buscando es que simplemente se salte imprimir el 5
for element in range(1,10,1):
    if element == 5:
        continue
    print(element)

palabra = "Python"
for letra in palabra:
    if letra == "h" or letra == "o":
        print(letra)
    else: print(letra)