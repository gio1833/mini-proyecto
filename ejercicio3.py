# Ejercicio 3 Simulador de base de datos 

# Base de datos simulada (diccionario)
base_de_datos = {}

# Función para agregar un registro
def agregar_registro(identificador, datos):
    base_de_datos[identificador] = datos

# Función para actualizar un registro
def actualizar_registro(identificador, nuevos_datos):
    if identificador in base_de_datos:
        base_de_datos[identificador] = nuevos_datos
    else:
        print("El registro no existe")

# Función para eliminar un registro
def eliminar_registro(identificador):
    if identificador in base_de_datos:
        del base_de_datos[identificador]
    else:
        print("El registro no existe")

# Función para buscar un registro
def buscar_registro(identificador):
    if identificador in base_de_datos:
        return base_de_datos[identificador]
    else:
        return "Registro no encontrado"

# Función para visualizar todos los registros
def visualizar_registros():
    for identificador, datos in base_de_datos.items():
        print(f"ID: {identificador}, Datos: {datos}")

# Ejemplos de uso
agregar_registro(1, {"nombre": "Juan", "edad": 30, "ciudad": "Manizales"})
agregar_registro(2, {"nombre": "María", "edad": 25, "ciudad": "Medellín"})
visualizar_registros()
print(buscar_registro(1))
actualizar_registro(1, {"nombre": "Juan", "edad": 31, "ciudad": "Manizales"})
visualizar_registros()
eliminar_registro(2)
visualizar_registros()