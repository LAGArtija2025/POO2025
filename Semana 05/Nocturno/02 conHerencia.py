
# Creando una clase padre
class Persona:
    def __init__(self, dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        self.estado_civil = estado_civil
        self.apodo = apodo
        self.direccion = direccion
        self.fecha_nac = fecha_nac
    
    def saludar(self):
        return "Hola soy una persona"

# Creando clases hijas Doctor y Paciente
class Doctor(Persona):
    def __init__(self, dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac, especialidad, colegiatura, experiencia):
        super().__init__(dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac)
        self.especialidad = especialidad
        self.colegiatura = colegiatura
        self.experiencia = experiencia
    
    def saludar(self):
        return "Hola soy doctor"

class Paciente (Persona):
    def __init__(self, dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac, talla, peso, temperatura, tipo_sangre, donante):
        super().__init__(dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac)
        self.talla = talla
        self.peso = peso
        self.temperatura = temperatura
        self.tipo_sangre = tipo_sangre
        self.donante = donante

miObjeto1 = Persona("12345678", "Rozental", "Mendoza", 21, "rozi@gmail.com", "999-666-999", "C", "Rozzi", "Huaycán", "14/02/2002")
miObjeto2 = Doctor("87654321", "Madciel", "Lopez", 20, "tulobita@gmail.com", "666-666-666", "V", "Lobita", "Cerro Huaycán", "01/01/2002", "Pediatra", "666-666", 1)
miObjeto3 = Paciente("44448888", "Rizart", "Vicuña", 18, "tuchinito@gmail.com", "123-456-789", "D", "Ortografia", "Huaycán Parte Pituca", "25/12/2002", 1.67, 58.20, 37, "O+", True)

print(miObjeto2.saludar())
