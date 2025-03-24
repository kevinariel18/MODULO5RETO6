
import random
from laptop import laptop

class Laptop_Business(laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.almacenamiento = almacenamiento  
        self.duracion_bateria = duracion_bateria  
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_diagnostico["almacenamiento"] = "Suficiente" if self.almacenamiento >= 256 else "Espacio bajo"
        resultado_diagnostico["duracion_bateria"] = "Óptima" if self.duracion_bateria >= 6 else "Batería limitada"
        resultado_diagnostico["conectividad_red"] = self.verificar_conectividad_red()
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi Disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia de red": f"{random.randint(10, 100)} ms"
        }
        return conectividad
