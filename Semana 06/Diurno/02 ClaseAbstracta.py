# Pilar de la abstracción: Básicamente consiste es ocultar todos los detalles conplejos al usuario y solo mantener lo simple y necesario.

# Clases Abstractas: Una plantilla para crear clases

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, especie, genero):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.genero = genero
    
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, edad, especie, genero, sonido):
        super().__init__(nombre, edad, especie, genero)
        self.sonido = sonido
    
    def hacer_sonido(self):
        return f"Soy un perro y hago: {self.sonido}"

class Gato(Animal):
    def __init__(self, nombre, edad, especie, genero, sonido):
        super().__init__(nombre, edad, especie, genero)
        self.sonido = sonido
    
    def hacer_sonido(self):
        return f"Soy un gato y hago: {self.sonido}"
    

miChiwawa1 = Perro("Mario Miguel", 17, "Mamífero", "Asexual", "Guau")
miGatito1 = Gato("Genesis", 21, "Mamífero", "No binario", "Miau")

print(miChiwawa1.hacer_sonido())
print(miGatito1.hacer_sonido())

