class ClasePadre:
    pass
class ClaseHijo(ClasePadre):
    pass
class ClaseNieto(ClaseHijo):
    pass
print(ClaseNieto.__mro__)

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

class Mamifero(Animal): #hijo de la clase animal
    def __init__(self, especie, edad):
        super().__init__(especie, edad)


class Perro(Mamifero):#hijo de la clase mamifero, nieto de la clase animal
    def __init__(self, especie, edad, dueno):
        #Alternativa 1
        # self.especie = especie
        # self.edad = edad
        #self.dueno = dueno

        super().__init__(especie, edad)
        #alternativa 2
        self.dueno = dueno
mi_perro = Perro("buldogg",15,"Adrian")
mi_perro.describirse()