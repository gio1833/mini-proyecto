# Ejercicio 4 Juego del ahorcado 

# Función para inicializar la palabra a adivinar
def inicializar_palabra():
    return "juego"

# Función para verificar si una letra está en la palabra

def verificar_letra(palabra, letra, letras_correctas, letras_incorrectas):
    if letra in palabra:
        letras_correctas.append(letra)
    else:
        letras_incorrectas.append(letra)

# Ejemplo de uso

palabra_a_adivinar = inicializar_palabra()
letras_correctas = []
letras_incorrectas = []

verificar_letra(palabra_a_adivinar, "p", letras_correctas, letras_incorrectas)
verificar_letra(palabra_a_adivinar, "a", letras_correctas, letras_incorrectas)
verificar_letra(palabra_a_adivinar, "z", letras_correctas, letras_incorrectas)

print("Letras correctas:", letras_correctas)
print("Letras incorrectas:", letras_incorrectas)