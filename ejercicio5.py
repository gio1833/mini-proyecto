# Ejercicio 5 conversor de monedas

DOLARPESO = 3.998

def cambiarDolar(dolares):
    pesos = dolares * DOLARPESO
    return pesos
def cambiarpesos(pesos):
    dolares = pesos / DOLARPESO
    return dolares
def solicitarCantidad(tipo):
   cantidad = float(input(f"cuanta cantidad de {tipo} desea cambiar"))
   return cantidad

if __name__ == '__main__':

    Menu = """
    cambio de moneda
    selecione la opcion 
    1. cambio a dolar
    2. cambio a pesos
    3. salir
    """
    while True:
        opcion = int(input(Menu))
        if opcion == 1:
            cantidad = solicitarCantidad("dolores")
            pesos = round(cambiarDolar(cantidad),2)
            print (f"el valor de cambiar {cantidad}dolares a {pesos} pesos")
        elif opcion == 2:
            cantidad = solicitarCantidad("pesos")
            dolares = round(cambiarpesos(cantidad),2)
            print (f"el valor de cambiar {cantidad}pesos a {dolares} dolares")
        else:
            print ("goodbye")