
class Alumno():
    # método constructor (método especial)
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    # otro método especial (str)
    def __str__(self):
        return f"""CLASE: ALUMNO
Atributos:
Nombre = {self.nombre}
Apellido = {self.apellido}
Edad = {self.edad}
Género = {self.genero}
"""
    
    def __repr__(self):
        return f"""CLASE: ALUMNO
Atributos:
Nombre = {self.nombre} (String) Not Null
Apellido = {self.apellido} (String) Not Null
Edad = {self.edad} (Integer) Not Null
Género = {self.genero} (Booleano) Not Null
"""
    
    # método propio
    def saludar(self):
        return f"Hola soy el alumno {self.nombre}"
    
desaprobado1 = Alumno("Luis Miguel", "Palacios Canchanya", 20, True)

print(repr(desaprobado1))