import random
import requests # me da error en esta linea

# Función para generar datos meteorológicos simulados
def generar_datos_simulados():
    temperatura = random.randint(10, 30)
    humedad = random.randint(30, 90)
    velocidad_viento = random.randint(0, 20)
    return temperatura, humedad, velocidad_viento

# Función para obtener datos meteorológicos reales a través de la API de OpenWeatherMap
def obtener_datos_reales(ciudad):
    api_key = 'tu_api_key'  # Reemplaza 'tu_api_key' con tu propia clave de API de OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperatura = data['main']['temp']
        humedad = data['main']['humidity']
        velocidad_viento = data['wind']['speed']
        return temperatura, humedad, velocidad_viento
    else:
        return None

# Ejemplo de uso: generar datos simulados
temperatura_simulada, humedad_simulada, velocidad_viento_simulada = generar_datos_simulados()
print("Datos meteorológicos simulados:")
print(f"Temperatura: {temperatura_simulada}°C")
print(f"Humedad: {humedad_simulada}%")
print(f"Velocidad del viento: {velocidad_viento_simulada} km/h")

# Ejemplo de uso: obtener datos reales para una ciudad específica (en este caso, Manizales)
ciudad = "Manizales"
datos_reales = obtener_datos_reales(ciudad)
if datos_reales:
    temperatura_real, humedad_real, velocidad_viento_real = datos_reales
    print("\nDatos meteorológicos reales:")
    print(f"Temperatura: {temperatura_real}°C")
    print(f"Humedad: {humedad_real}%")
    print(f"Velocidad del viento: {velocidad_viento_real} km/h")
else:
    print(f"No se pudieron obtener los datos meteorológicos reales para la ciudad {ciudad}")