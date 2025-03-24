
from laptop import laptop
from laptop_gaming import laptop_gaming
from laptop_business import Laptop_Business

lapto_pepe =laptop("lenovo","I7",32)
lapto_maria =laptop("lenovo","I7",32,600)



laptop_juanito =laptop_gaming("MSi","i7", 4,"RTX 8GB")


print(laptop_juanito.realizar_diagnostico_sistema())

laptop_empresarial = Laptop_Business("Dell", "i5", 16, 512, 8)
print(laptop_empresarial.realizar_diagnostico_sistema())
