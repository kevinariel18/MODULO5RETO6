nota_tareas=float(input("Ingresar la nota de la tarea: "))
nota_leccion=float(input("Ingresar la nota de la leccion: "))
nota_examen=float(input("Ingresar la nota de la examen: "))


total_promedio = (nota_tareas + nota_leccion + nota_examen)/3


print(f"Promedio: {total_promedio}")