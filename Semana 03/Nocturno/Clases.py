# Ahora shi: La empresa crea celulares distintos con POO

class Celular():
    # método constructor
    def __init__(self, marca, modelo, ram, camaraf, camarat):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.camaraf = camaraf
        self.camarat = camarat
    
    def llamar(self):
        print("llamando...")
    
    def colgar(self):
        print("colgando...")
    
    def silenciar(self):
        print("silenciando...")


celular1 = Celular("Poccoyo", "Poccotu", "2GB", "2MP", "2MP")
celular2 = Celular("Honor", "H1", "24GB", "12MP", "24MP")
celular3 = Celular("Nokia", "Rozental", "1GB", "1MP", "0MP")

print(f"Características del celular #2\nMarca: {celular2.marca}\nModelo: {celular2.modelo}\nRAM: {celular2.ram}\nCámara Frontal: {celular2.camaraf}\nCámara Trasera: {celular2.camarat}")

celular1.llamar()
