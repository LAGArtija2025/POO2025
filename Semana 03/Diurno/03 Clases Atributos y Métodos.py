# Ahora la fábrica crea distintos celulares con POO

class Celular():
    def __init__(self, marca, modelo, ram, camaraf, camarat):
        self.marca = marca        
        self.modelo = modelo        
        self.ram = ram        
        self.camaraf = camaraf        
        self.camarat = camarat
    
    def llamar(self):
        print("El celular está llamando...")
    
    def colgar(self):
        print("El celular está colgando...")

    def silenciar(self):
        print("El celular se está silenciando...")

miObjCelular1 = Celular("Redmi","Note9","8GB","12MP","24MP")   
miObjCelular2 = Celular("Samsung","S24","8GB","12MP","24MP")   
miObjCelular3 = Celular("Choristar","WhangYu","1GB","1MP","2MP")   
miObjCelular4 = Celular("Honor","Note9","8GB","12MP","24MP")   
miObjCelular5 = Celular("Redmi","Note9","8GB","12MP","24MP")   

print(f"El celular 1 es de marca {miObjCelular1.marca} y de modelo {miObjCelular1.modelo}")
print(f"El celular 3 es de marca {miObjCelular3.marca} y de modelo {miObjCelular3.modelo}")

miObjCelular1.llamar();
miObjCelular1.colgar();
miObjCelular1.silenciar();