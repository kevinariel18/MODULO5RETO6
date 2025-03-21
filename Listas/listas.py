#liastas de caracteres

planetas = ["Mercurio", "Venus", "Tierra", "Marte" , "Jupiter","Saturno", "Urano" , "Neptuno", 5, 40.5, True]
# print(planetas[-3])
# print(planetas[1: ])
# print(len(planetas))

#trabajar con una lista de numeros
gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 124054 # newtons en la tierra

print(f"en la tierra, un autobus de dos pisos pesa {peso_bus} N" )
print(f"en mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas [0]} N" )


print(f" lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedad_en_planetas)} N")
print(f"lo ms pesado que seria un autobus en el sistema solar es {peso_bus * max(gravedad_en_planetas)} N")