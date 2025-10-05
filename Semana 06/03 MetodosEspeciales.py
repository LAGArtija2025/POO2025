class Maestro():
    def __init__(self, nombre, apellido, edad, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.especialidad = especialidad
    
    def __str__(self):
        return f"""CLASE: MAESTRO
ATRIBUTOS:
Nombre = {self.nombre}
Apellido = {self.apellido}
Edad = {self.edad}
Especialidad = {self.especialidad} \n"""

    def __repr__(self):
        return f"""CLASE: MAESTRO
ATRIBUTOS:
Nombre = {self.nombre} (String)
Apellido = {self.apellido} (String)
Edad = {self.edad} (Integer)
Especialidad = {self.especialidad} "String) \n"""

    def identificarse(self):
        return f"Hola soy el maestro {self.nombre} y tengo {self.edad} años de edad"
    
Luis = Maestro("Luis Alberto", "Gutierrez Anicama", 25, "FrontEnd developer")
Peter = Maestro("Peter Adrian", "Quispe Mejia", 28, "Diseño Gráfico")

# print(Luis)
# print(repr(Luis))
# print(Luis.identificarse())

# print(Peter)
# print(f"{Peter !r}")
# print(Peter.identificarse())