from abc import ABC, abstractclassmethod

# creando una clase abstracta
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, apellido, genero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
    
    @abstractclassmethod
    def identificarse(self):
        pass

#Creando otras clases a partir de la clase abstracta
class Docente(Persona):
    # Definiendo el método constructor
    def __init__(self, nombre, apellido, genero, edad, especialidad):
        super().__init__(nombre, apellido, genero, edad)
        self.especialidad = especialidad
    
    #definiendo otro método propio llamado identificarse
    def identificarse(self):
        return f"Hola soy elle docente {self.nombre} {self.apellido}"

persona1 = Docente("Rozental", "Merino", "M", 16, "Diseño Gráfico y Dormir")

print(persona1.identificarse())
