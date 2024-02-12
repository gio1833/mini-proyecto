# ejercicio 2 conversor de unidades  

# Conversión de longitud

def convertir_longitud(valor, unidad_origen, unidad_destino):
    if unidad_origen == "m" and unidad_destino == "cm":
        return valor * 100
    elif unidad_origen == "cm" and unidad_destino == "m":
        return valor / 100

# Agrega más conversiones según tus necesidades

# Conversión de masa

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kg" and unidad_destino == "g":
        return valor * 1000
    elif unidad_origen == "g" and unidad_destino == "kg":
        return valor / 1000
 
# Agrega más conversiones según tus necesidades

# Conversión de temperatura

def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == "C" and escala_destino == "F":
        return (valor * 9/5) + 32
    elif escala_origen == "F" and escala_destino == "C":
        return (valor - 32) * 5/9

# Agrega más conversiones según tus necesidades

# Ejemplo

print(convertir_longitud(5, "m", "cm"))  # Convertir 5 metros a centímetros
print(convertir_masa(2, "kg", "g"))      # Convertir 2 kilogramos a gramos
print(convertir_temperatura(25, "C", "F"))  # Convertir 25 grados Celsius a Farenheit 
