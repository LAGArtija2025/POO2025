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
        if estudiante.calcular_promedio()>=12.5:
            return f"El estudiante {estudiante.nombre} está APROBADO"
        else:
            return f"El estudiante {estudiante.nombre} está DESAPROBADO"
    
a1 = Alumno("Madciel", 18, 20)
a2 = Alumno("Rozental", 12, 13)
a3 = Alumno("Praxides", 10, 8)

d1 = Docente("Luis", "Gutierrez", 25)

print(d1.evaluar(a1))
print(d1.evaluar(a2))
print(d1.evaluar(a3))
   