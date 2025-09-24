
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

class Doctor:
    def __init__(self, dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac, especialidad, colegiatura, experiencia):
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
        self.especialidad = especialidad
        self.colegiatura = colegiatura
        self.experiencia = experiencia

class Paciente:
    def __init__(self, dni, nombre, apellido, edad, correo, telefono, estado_civil, apodo, direccion, fecha_nac, talla, peso, temperatura, tipo_sangre, donante):
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
        self.talla = talla
        self.peso = peso
        self.temperatura = temperatura
        self.tipo_sangre = tipo_sangre
        self.donante = donante
