
class Estudiante():
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    def __str__(self):
        return f"""CLASE: ESTUDIANTE
ATRIBUTOS:
Nombre = {self.nombre}
Apellido = {self.apellido}
Edad = {self.edad}
Género = {self.genero}
"""

    def __repr__(self):
        return f"""CLASE: ESTUDIANTE
ATRIBUTOS:
Nombre = {self.nombre} (String) - Not Null
Apellido = {self.apellido} (String) - Not Null
Edad = {self.edad} (Integer) - Not Null
Género = {self.genero} (Booleano) - Not Null
"""

    def saludar(self):
        return f"Hola soy un estudiante y me llamo {self.nombre}"

desaprobado1 = Estudiante("Praxides", "De la cruz", 18, True)

print(desaprobado1)
print(repr(desaprobado1))
print(desaprobado1.saludar())
