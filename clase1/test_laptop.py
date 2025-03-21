from laptop import laptop

lapto_pepe =laptop("lenovo","I7",32)
lapto_maria =laptop("lenovo","I7",32,600)

for numero in range(1,1001):
    asus_laptop =laptop.asus_laptop(numero)


    print(asus_laptop.__dict__)
    # print(laptop.comparar_costo(lapto_pepe,lapto_maria))


