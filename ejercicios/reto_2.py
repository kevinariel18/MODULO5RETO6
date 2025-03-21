import random

print("Seleccione un pais: 1. Ecuador  2. Colombia 3. Peru")
opcion_pais = int(input("Ingrese el numero del pais: "))

if opcion_pais == 1:
    pais = "Ecuador"
elif opcion_pais == 2:
    pais = "Colombia"
elif opcion_pais == 3:
    pais = "Peru"
else:
    print("Opcion no valida")
    exit() 

print("Seleccione una zona: 1. Urbana  2. Rural  3. Perimetral")
opcion_zona = int(input("Ingrese el numero de una zona: "))

if opcion_zona == 1:
    zona = "Urbana"
elif opcion_zona == 2:
    zona = "Rural"
elif opcion_zona == 3:
    zona = "Perimetral"
else:
    print("Opcion no valida")
    exit()  

velocidad = int(input("Ingrese la velocidad actual en km/h: "))


if pais == "Ecuador":
    if zona == "Urbana":
        minimo_velocidad = 10
        maxima_velocidad = 50
    elif zona == "Rural":
        minimo_velocidad = 51
        maxima_velocidad = 70
    elif zona == "Perimetral":
        minimo_velocidad = 71
        maxima_velocidad = 90

elif pais == "Colombia":
    if zona == "Urbana":
        minimo_velocidad = 10
        maxima_velocidad = 30
    elif zona == "Rural":
        minimo_velocidad = 31
        maxima_velocidad = 80
    elif zona == "Perimetral":
        minimo_velocidad = 81
        maxima_velocidad = 100

elif pais == "Peru":
    if zona == "Urbana":
        minimo_velocidad = 10
        maxima_velocidad = 40
    elif zona == "Rural":
        minimo_velocidad = 41
        maxima_velocidad = 60
    elif zona == "Perimetral":
        minimo_velocidad = 61
        maxima_velocidad = 120


if velocidad < minimo_velocidad:
    print("Su velocidad es inferior al mínimo permitido.")
elif velocidad > maxima_velocidad:
    print("Su velocidad excede el máximo permitido.")
else:
    print("Velocidad correcta.")
