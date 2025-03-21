




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
