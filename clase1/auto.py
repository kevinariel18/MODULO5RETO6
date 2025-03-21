from datetime import datetime

class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km")
    
    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje.")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")
    
    @classmethod
    def auto_nuevo_toyota(cls, modelo):
        return cls("Toyota", modelo, datetime.now().year, 0)
    
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje
    
    @staticmethod
    def es_auto_moderno(año):
        return año >= 2015
    
    @classmethod
    def auto_de_precio_medio(cls, marca, modelo, año):
        return cls(marca, modelo, año, kilometraje=50000)


auto1 = Auto("Toyota", "Supra", 2020)
auto1.mostrar_informacion()
auto1.realizar_viaje(15000)
auto1.estado_auto()
auto1.actualizar_kilometraje(50000)
auto1.estado_auto()

auto2 = Auto.auto_nuevo_toyota("Corolla")
auto2.mostrar_informacion()

auto3 = Auto("Ford", "Focus", 2018, 50000)
print(f"Auto1 y Auto3 tienen el mismo kilometraje {Auto.comparar_kilometraje(auto1, auto3)}")
