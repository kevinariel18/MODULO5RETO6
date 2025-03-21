

menu = ["Sopa", "Arroz", "Pollo frito", "Ceviche de mango", "Encebollado", "Salchipapas"]

while True:
  
    print("\n--- Menú del Restaurante Segunda es Todo ---")
    print("1. Añadir plato al menú")
    print("2. Buscar en el menú")
    print("3. Eliminar plato del menú")
    print("4. Mostrar platos del menú")

    mensaje_opcion = input("Selecciona una opción del 1 al 4: ")

    if mensaje_opcion == "1":
       
        plato = input("Agrega el nombre del plato que vas a añadir: ")
        menu.append(plato)
        print(f"El plato {plato} ha sido añadido al menú.")

    elif mensaje_opcion == "2":
        
        plato = input("Agrega el nombre del plato que deseas buscar: ")
        if plato in menu:
            print(f"El plato {plato} se encuentra en el menú.")
        else:
            print(f"El plato {plato} NO se encuentra en el menú.")

    elif mensaje_opcion == "3":
      
        plato = input("Ingresa el nombre del plato que deseas eliminar: ")
        if plato in menu:
            menu.remove(plato)
            print(f"El plato {plato} ha sido eliminado del menú.")
        else:
            print(f"El plato {plato} NO se encuentra en el menú.")

    elif mensaje_opcion == "4":
       
        if menu:
            print("\nPlatos del menú:")
            for plato in menu:
                print(f"- {plato}")
        else:
            print("El menú está vacío.")

    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")