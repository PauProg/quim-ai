from flask import Flask, render_template, request, jsonify
import json
import re
import random
import requests

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
    else:
        response = respond_to_patterns(user_input, patterns)

    return jsonify(response=response)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)