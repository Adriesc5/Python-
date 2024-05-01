class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #Metodo generico pero con implementacion particular
    def hablar(self):
        #metodo vacio
        pass
    def moverse(self):
        pass
    def describirse(self):
        print(f"Soy un animal del tipo {type(self).__name__}")
        
class Perro(Animal):
    def hablar(self):
        print("guau")

    def moverse(self, pasos):
        print(f"Caminando {pasos} pasos")

class Vaca(Animal):
    def hablar(self):
        print("Muuu")

    def moverse(self, pasos):
        print(f"Caminando {pasos} pasos")

class Abeja(Animal):
    def hablar(self):
        print("Bzzz")

    def moverse(self, pasos):
        print(f"Volando {pasos} pies")

    #Nuevo metodo
    def picar(self):
        print("Uy te pico!")


mi_perro = Perro("Mamifero",10)
mi_vaca = Vaca("Mamifero",15)
mi_abeja = Abeja("Insecto",1)

mi_vaca.hablar()
mi_abeja.picar()
mi_perro.moverse(10)
mi_abeja.moverse(5)

mi_perro.describirse()