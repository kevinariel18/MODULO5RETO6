#laptop_gaming
from laptop import laptop

class laptop_gaming(laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_grafica, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.tarjeta_grafica =tarjeta_grafica

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Targeta grafica: {self.tarjeta_grafica}\n Costo: {self.costo}\n Impuesto: {self.impuestos}\n"
    
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"]= resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos = ["fornite", "free fire", "GTA"]  
        resultados = {}  
        for juego in juegos:
         fps_base = 30
        if "RTX" in self.tarjeta_grafica:
            fps = fps_base * 3
        elif "GTX" in self.tarjeta_grafica:
            fps = fps_base * 2
        else:
            fps = fps_base

        resultados[juego] = f"{fps} FPS"  

        return resultados
    

    def realizar_informe_uso(self):
        informe=super().realizar_informe_uso()
        informe.update({

            "Tipo" : "Gaming",
            "uso recomendado" : "para juegos de video",
            "horas de uso" : 10,
            "recomendaciones de sofwar": ["Antivirus", "VPN"]
            

        })
        return informe
        

           
     
           
    pass
