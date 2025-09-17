class Vehiculo:
    def __init__(self, marca, modelo, color, placa, fuerza):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.fuerza = fuerza

    def mostrar_info(self):
        return f"""
        Datos de la clase Vehículo:
        Marca: {self.marca}
        Modelo: {self.modelo}
        Color: {self.color}
        Placa: {self.placa}
        Fuerza: {self.fuerza}
        """

class Conductor:
    def __init__(self, nombre, apellido, genero, estado, vehiculo):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.estado = estado
        self.vehiculo = vehiculo

    def mostrar_info(self):
        return f"""
        Datos de la clase Conductor:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Genero: {self.genero}
        Estado: {self.estado}
        Vehiculo: {self.vehiculo.mostrar_info()}
        """
    
v1 = Vehiculo("Chevrolet", "Joy", "Negro", "CJJ-010", 200)
c1 = Conductor("Luis", "Gutierrez", "Masculino", "Activo", v1)

print(c1.mostrar_info())
