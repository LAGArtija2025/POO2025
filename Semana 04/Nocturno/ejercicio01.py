
class Estudiante:
    def __init__(self, nombre, apellido, genero, edad, apodo):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        self.apodo = apodo
    
    def mostrar_datos(self):
        return f"""DATOS DEL ESTUDIANTE:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Genero: {self.genero}
        Edad: {self.edad}
        Apodo: {self.apodo}"""
    
objeto1 = Estudiante("Rozental", "Merino", "Masculino", 22, "Rozi")
objeto2 = Estudiante("Johan", "Kakaroto", "Sayayin", 22, "Goku")
objeto3 = Estudiante("Rizart", "Vergara", "Masculino", 23, "Ortografía")

print(objeto1.mostrar_datos())
