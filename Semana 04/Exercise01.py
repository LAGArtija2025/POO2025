
class Vehiculo:
    def __init__(self, marca, modelo, color, placa, anio):
        self.marca = marca            
        self.modelo = modelo        
        self.color = color        
        self.placa = placa        
        self.anio = anio  

    def mostrar_info(self):
        return f"""Datos del Vehículo:
Marca: {self.marca}
Modelo: {self.modelo}
Color: {self.color}
Placa: {self.placa}
Anio: {self.anio}
        """
        
class Conductor:
    def __init__(self, nombre, apellido, edad, estado, vehiculo):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.estado = estado
            self.vehiculo = vehiculo

    def mostrar_info(self):
        return f"""Datos del conductor:
Nombre: {self.nombre}
Apellido: {self.apellido}
Edad: {self.edad}
Estado: {self.estado}
Vehiculo: {self.vehiculo.mostrar_info()}
        """

auto1 = Vehiculo("Chevrolet", "Joy", "Negro", "CJJ-010", "2023")
conductor1 = Conductor("Luis", "Gutierrez", 15, "Activo",auto1)

print(conductor1.mostrar_info())