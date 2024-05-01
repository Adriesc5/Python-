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
    def __init__(self, especie, edad, dueno):
        #Alternativa 1
        # self.especie = especie
        # self.edad = edad
        #self.dueno = dueno

        super().__init__(especie, edad)
        #alternativa 2
        self.dueno = dueno
        


mi_perro = Perro("Mamifero",5,"Adrian")