
from datetime import datetime

nombre_paciente = []
edad = []

def agregar_nombre(info):
    """Extrae y guarda el nombre y apellido del paciente."""
    datos = info.rsplit(' ', 1) 
    nombre_paciente.append(datos[0])

def agregar_edad(info):
    """Calcula y guarda la edad del paciente."""
    año_actual = datetime.now().year
    datos = info.rsplit(' ', 1)  
    año_nacimiento = int(datos[1])
    edad_actual = año_actual - año_nacimiento
    edad.append(edad_actual)

def obtener_mayor_menor():
    """Devuelve el paciente mayor y menor."""
    mayor_idx = edad.index(max(edad))
    menor_idx = edad.index(min(edad))
    return nombre_paciente[mayor_idx], edad[mayor_idx], nombre_paciente[menor_idx], edad[menor_idx]

