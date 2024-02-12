# Creamos un diccionario para almacenar las reservas realizadas

reservas = {}

# Función para mostrar la disponibilidad de asientos
def mostrar_disponibilidad():
    # mostrar la disponibilidad de asientos al usuario
    print("Asientos disponibles:")
    # Mostrar el mapa del cine con la disponibilidad de asientos

# Función para gestionar la reserva de asientos
    
def gestionar_reserva(fila, asiento):
    if fila in reservas:
        if asiento in reservas[fila]:
            print("Este asiento ya está reservado")
        else:
            reservas[fila].append(asiento)
            print(f"¡Reserva realizada! Fila: {fila}, Asiento: {asiento}")
    else:
        reservas[fila] = [asiento]
        print(f"¡Reserva realizada! Fila: {fila}, Asiento: {asiento}")

# Ejemplo 
        
mostrar_disponibilidad()
gestionar_reserva("A", 3)