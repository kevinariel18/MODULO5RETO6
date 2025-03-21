import informacion

if __name__ == "__main__":
    pacientes = [
        "Antonio Moreno 2000",
        "Carmen Díaz 2001",
        "Fernando García 2003",
        "Teresa Rodríguez 2004",
        "José López 2005",
        "Miguel Ángel Ortiz 1999",
        "Lucia Gómez 2000",
        "Francisco Javier Sánchez 2001",
        "Beatriz Domínguez 2002",
        "Adrián López 2011",
        "Martina Pascual 2012",
        "Álvaro Torres 2013",
        "Berta Romero 2014"
    ]
    
    for paciente in pacientes:
        informacion.agregar_nombre(paciente)
        informacion.agregar_edad(paciente)
    
    print("Lista de nombres de pacientes:", informacion.nombre_paciente)
    print("Lista de edades de pacientes:", informacion.edad)
    
    mayor, edad_mayor, menor, edad_menor = informacion.obtener_mayor_menor()
    print(f"El paciente mayor es {mayor} con {edad_mayor} años.")
    print(f"El paciente menor es {menor} con {edad_menor} años.")
