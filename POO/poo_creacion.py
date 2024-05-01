#clase vacia 
class Perro:
    #El metodo __init__ es llamado al crear el objeto 
    def __init__(self, nombre, raza):
        print(f"Creando perro de nombre {nombre} y de raza {raza}")
        #Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

mi_perro = Perro("Negra","Corriente")
print(type(mi_perro))
#Cradndo perro negra, corriente
#<class '__main__.Perro'>

print(mi_perro.nombre)
print(mi_perro.raza)

class Alumno:
    def __init__(self, nombreAlumno, grado):
        print(f"Creando alumno {nombreAlumno} del grado {grado}")
        self.nombreAlumno = nombreAlumno
        self.grado = grado
        
yo = Alumno("Adrian",10)
