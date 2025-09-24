# Ejemplo usando herencia en python

# Creando una clase PADRE (como hemos venido haciendo)
class Persona:
    def __init__(self, nombre, apellido, edad, correo, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.dni = dni
    
    def saludar(self):
        return "Hola soy una persona"

# Creando una clase HIJA
class Doctor(Persona):
    def __init__(self, nombre, apellido, edad, correo, dni, especialidad, colegiatura, sueldo, experiencia):
        super().__init__(nombre, apellido, edad, correo, dni)
        self.especialidad = especialidad
        self.colegiatura = colegiatura
        self.sueldo = sueldo
        self.experiencia = experiencia
    
    def saludar(self):
        return "Hola soy un doctor"

    

miPersona1 = Persona("Luis", "Palacios", 21, "lpmasnaki@gmail.com", "12345678")

miDoctor1 = Doctor("Celeste", "Kiara", 15, "tuchinita@gmail.com", "11118888", "Pediatria", "666-666", 1250, 0)

print(miDoctor1.saludar())
