import random

# Listas de elementos aleatorios
personajes = ["delantero", "arquero", "tecnico", "defensa"]
lugares = ["grada", "cancha", "camerinos", "estadio"]
eventos = ["hizo gol", "empate", "leccionado",]

# Generar historia aleatoria
personaje = random.choice(personajes)
lugar = random.choice(lugares)
evento = random.choice(eventos)

# Mostrar la historia generada
print(f"Había una vez {personaje}, en la {lugar} {evento}.")
