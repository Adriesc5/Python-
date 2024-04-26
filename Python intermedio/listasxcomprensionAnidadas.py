#Matriz: Lista de listas
ldl =[[2, 3, 4]
     ,[40,50,60]
     ,[100,200,300]]
#equivalente usando for 
total = 0
for row in ldl:
    for column in row:
        total += column
print(total)

#SUMA TOTAL CON COMPRENSION ANIDADA
total_comprension = [column for row in ldl for column in row]
print(total_comprension)
print(sum(total_comprension))