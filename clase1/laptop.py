

import random


class laptop:
    def __init__(self,marca, prosesador, memoria, costo= 500, impuestos = 10):
        self.marca = marca
        self.prosesador = prosesador
        self.memoria = memoria
        self.costo = costo
        self.impuestos = impuestos
        

    def valor_final(self):
     return self.costo + self.impuestos
    
    def valor_descuento(self, descuento):
       return (self.costo * descuento)/100
    

    def realizar_diagnostico_sistema(self):
        resultado = {
            "marca" : f"{self.marca}",
            "procesadora" : f"{self.prosesador}",
            "memoria ram" : "ok" if self.memoria >=8 else "aumnetar la memoria ram",
            "bateria" : "ok" if random.choice([True,False]) else "cambiar de bateria"

       
        }
        return  resultado


    @staticmethod

    def    comparar_costo(laptop1,laptop2):
          if laptop1.costo == laptop2.costo:
              return "los costos son iguales"
          return " los costos son diferentes"
   
   
    @classmethod
    def asus_laptop(cls , costo):
        marca = "asus"
        procesador ="i5"
        memoria = 16
        return cls(marca,procesador,memoria, costo)
