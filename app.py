from flask import Flask, render_template, request, jsonify
import json
import re
import random
import requests
import wikipedia

# Configurar Wikipedia para usar el idioma español
wikipedia.set_lang("es")

# Configurar Flask
app = Flask(__name__)

# Archivo de patrones
patterns_file = "patterns.json"

# Clave de la API de OpenWeatherMap
API_KEY = "9265687a3ef637dcab7b521c58b1e939"

# Cargar patrones desde el archivo
def load_patterns():
    try:
        with open(patterns_file, "r", encoding="utf-8") as file:
            patterns = json.load(file)
            return [(pattern['pattern'], pattern['responses']) for pattern in patterns]
    except FileNotFoundError:
        return []

# Función para consultar el clima usando OpenWeatherMap
def get_weather(city="Barcelona"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"En {city}, ahora hace {temp}°C y el clima está {description}."
        else:
            return "Lo siento, no pude obtener el clima en este momento. ¿Puedes intentarlo más tarde?"
    except requests.exceptions.RequestException:
        return "Hubo un problema al conectarme al servicio del clima. Inténtalo más tarde."

# Juego: Piedra, papel o tijeras
def play_rock_paper_scissors(user_choice):
    choices = ["piedra", "papel", "tijeras"]
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        return f"¡Empate! Ambos eligieron {bot_choice}."
    elif (user_choice == "piedra" and bot_choice == "tijeras") or \
         (user_choice == "papel" and bot_choice == "piedra") or \
         (user_choice == "tijeras" and bot_choice == "papel"):
        return f"¡Ganaste! Tú elegiste {user_choice} y yo elegí {bot_choice}."
    else:
        return f"¡Perdiste! Tú elegiste {user_choice} y yo elegí {bot_choice}."

# Función para buscar en Wikipedia
def search_wikipedia(query):
    try:
        # Realiza la búsqueda en Wikipedia
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Hay varias opciones para '{query}'. ¿Podrías ser más específico?"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Hubo un problema de conexión. Intenta más tarde."
    except wikipedia.exceptions.RedirectError:
        return "No se pudo encontrar la página solicitada."
    except wikipedia.exceptions.PageError:
        return "No se encontró la página en Wikipedia."

# Responder a las entradas del usuario basadas en patrones
def respond_to_patterns(user_input, patterns):
    for pattern, responses in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return "No estoy seguro de lo que quisiste decir. Intenta preguntarme algo diferente."

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para procesar la entrada del usuario
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    if not user_input:
        return jsonify(response="No entendí tu mensaje. Intenta escribir algo.")

    patterns = load_patterns()

    if "adiós" in user_input:
        response = "Adiós, ¡que tengas un buen día!"
    elif "clima" in user_input or "tiempo" in user_input:
        city = "Barcelona"
        match = re.search(r"en ([\w\s]+)", user_input)
        if match:
            city = match.group(1)
        response = get_weather(city)
    elif "piedra" in user_input or "papel" in user_input or "tijeras" in user_input:
        response = play_rock_paper_scissors(user_input)
    elif "busca en wikipedia" in user_input:
        # Extraemos el término a buscar en Wikipedia
        match = re.search(r"busca en wikipedia (.+)", user_input)
        if match:
            query = match.group(1)
            response = search_wikipedia(query)
        else:
            response = "¿Qué te gustaría que busque en Wikipedia?"
    else:
        response = respond_to_patterns(user_input, patterns)

    return jsonify(response=response)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)