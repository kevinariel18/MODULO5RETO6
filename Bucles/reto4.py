datos = [1,2,3,4,5.5,"Kevin",5,4,6,-9,"Ariel"]

cantidad_datos = int(input("¿Cuántos datos desea ingresar? "))

for i in range(cantidad_datos):
    valor = input(f"Ingrese el dato {i + 1}: ")

    if valor.replace(".", "", 1).isdigit() and valor.count(".") <= 1:
        datos.append(float(valor))
    elif valor.isalpha():
        datos.append(valor)
    else:
        print(f"El dato {valor} no es válido. Debe ser un número o una cadena de texto.")

print(f"Su lista es: {datos}")