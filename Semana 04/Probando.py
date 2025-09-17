class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = input("digita tu nombre: ")
        self.edad = input("digita tu edad: ")
        self.grado = input("digita tu grado: ")
    
    def mostrar_info(self):
        return f"""Datos del estudiante:\n
        Nombre = {self.nombre}\n
        Edad = {self.edad}\n
        Grado = {self.grado}
        """
    
    def estudiar(self):
        while True:
            estudiar = input()
            if estudiar.lower() == "estudiar":
                return f"El estudiante {self.nombre} está estudiando"

alumno1 = Estudiante("Luis", 25, "sexto")

print(alumno1.mostrar_info())
print(alumno1.estudiar())
