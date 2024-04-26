pi =3.1416
texto = "El valor de pi es igual a" +str(pi) #Estamos convirtiendo el float a string para concatenar 
print(texto)

print(len(texto))#Nos da el valor de largo del string 

print(texto.find("v"))#Nos devuelve la posicion de lo que buscamos
texto = texto.replace("valor", "Zorra")
print(texto)