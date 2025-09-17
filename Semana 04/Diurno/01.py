class Estudiante:
    def __init__(self, nombre, apellido, edad, genero, ecivil):
        self.nombre = nombre            
        self.apellido = apellido        
        self.edad = edad        
        self.genero = genero        
        self.ecivil = ecivil

    def mostrar_datos(self):
        return f"""Datos del estudiante:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Edad: {self.edad}
        Género: {self.genero}
        Estado Civil: {self.ecivil}"""
    
alumno1 = Estudiante("Madciel", "Coronado", 21, "Femenino", "Soltera")
alumno2 = Estudiante("Riszart", "Chavez", 25, "Masculino", "Casado")
alumno3 = Estudiante("Rozental", "Merino", 22, "Masculino", "Divorciado")

print(alumno3.mostrar_datos())
