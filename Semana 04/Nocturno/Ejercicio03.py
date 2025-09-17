
class Alumno:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcular_promedio(self):
        return (self.nota1+self.nota2)/2

class Docente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def evaluar(self, estudiante):
        if estudiante.calcular_promedio() >= 12.5:
            return f"El estudiante {estudiante.nombre} está Aprobado con {estudiante.calcular_promedio()}"
        else:
            return f"El estudiante {estudiante.nombre} está Desaprobado con {estudiante.calcular_promedio()}"

alumno1 = Alumno("Rozental", 12, 10)
alumno2 = Alumno("Chui", 16, 17)
alumno3 = Alumno("Madciel", 5, 8)

docente1 = Docente("Luis", "Gutierrez", 15)

print(docente1.evaluar(alumno1))
print(docente1.evaluar(alumno2))
print(docente1.evaluar(alumno3))