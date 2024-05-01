class Perro:
    #El metodo __init__ es llamado al crear el objeto 
    def __init__(self, nombre, raza):
        print(f"Creando perro de nombre {nombre} y de raza {raza}")
        #Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("guau")
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Negra","Corriente")
mi_perro.ladra()
mi_perro.camina(10)


class Alumno:
    def __init__(self, nombreAlumno, grado):
        print(f"Creando alumno {nombreAlumno} del grado {grado}")
        self.nombreAlumno = nombreAlumno
        self.grado = grado
    def rendirExamen(self):
        print("Tomando examen en el aula")
    def asistir(self):
        print("Asistiendo puntual")
        
yo = Alumno("Adrian",10)
yo.asistir()
yo.rendirExamen()