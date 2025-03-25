#test_laptop.py
from laptop import laptop
from laptop_gaming import laptop_gaming
from laptop_business import Laptop_Business

lapto_pepe =laptop("lenovo","I7",32)
lapto_maria =laptop("lenovo","I7",32,600)


def imprimir_informe(laptop):
    informe=laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")

    print("\n")   




laptop_juanito =laptop_gaming("MSi","i7", 4,"RTX 8GB")


print(laptop_juanito.realizar_diagnostico_sistema())

laptop_empresarial = Laptop_Business("Dell", "i5", 16, 512, 8)
print(laptop_empresarial.realizar_diagnostico_sistema())

print("pepe")
imprimir_informe(lapto_pepe)
print("juanito")
imprimir_informe(laptop_juanito)