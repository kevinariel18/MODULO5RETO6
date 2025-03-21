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

lapto_pepe =laptop("lenovo","I7",32)

print(lapto_pepe.__dict__)
print(lapto_pepe.valor_final())
print(f"El valor descuento es: {lapto_pepe.valor_descuento(10)}")