class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")
    
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


auto1 = Auto("Toyota", "Supra", 2020)
auto1.mostrar_informacion()
auto1.realizar_viaje(5000)
auto1.estado_auto()
auto1.actualizar_kilometraje(40000)
auto1.estado_auto()
