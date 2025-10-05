class Persona():
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    def saludar(self):
        return "Hola soy una persona"
    
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, genero, carrera):
        super().__init__(nombre, apellido, edad, genero)
        self.carrera = carrera
    
    def saludar(self):
        return "Hola soy un alumno"
    
Pamela = Persona("Pamela", "Portillo", 20, "Femenino")
Luis = Alumno("Luis", "Gutierrez", 25, "Masculino", "Contabilidad")

print(Pamela.saludar())
print(Luis.saludar())
