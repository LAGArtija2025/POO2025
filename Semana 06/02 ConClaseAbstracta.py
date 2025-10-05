from abc import ABC, abstractclassmethod, abstractmethod

class Animal(ABC):
    # @abstractclassmethod
    # @classmethod
    @abstractmethod
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # @abstractclassmethod
    # @classmethod
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacer_sonido(self):
        return f"Este perro {self.nombre} hace: guau guau"


class Pollo(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacer_sonido(self):
        return f"Este gato {self.nombre} hace: pio pio pio"


Sebas = Perro("Pikachu", 6)
print(Sebas.hacer_sonido())
