# Ejemplo de código sin usar Herencia

class Persona:
    def __init__(self, nombre, apellido, edad, correo, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.dni = dni

class Doctor:
    def __init__(self, nombre, apellido, edad, correo, dni, especialidad, nrocolegiatura, sueldo, experiencia):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.dni = dni
        self.especialidad = especialidad
        self.nrocolegiatura = nrocolegiatura
        self.sueldo = sueldo
        self.experiencia = experiencia

class Paciente:
    def __init__(self, nombre, apellido, edad, correo, dni, talla, peso, presion, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.dni = dni
        self.talla = talla
        self.peso = peso
        self.presion = presion
        self.estado = estado
