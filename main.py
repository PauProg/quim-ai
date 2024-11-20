import json
import re
import requests
import wikipedia
from nltk.chat.util import Chat, reflections
import pyttsx3
import speech_recognition as sr

# Configurar Wikipedia en español
wikipedia.set_lang("es")

# Nombre del archivo donde se guardarán los patrones
patterns_file = "corrected_patterns_v2.json"

# Clave de la API de OpenWeatherMap
API_KEY = "9265687a3ef637dcab7b521c58b1e939"  # Reemplaza con tu clave

# Configurar el motor de texto a voz
engine = pyttsx3.init()

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para hablar el texto
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para cargar patrones desde un archivo
def load_patterns():
    try:
        with open(patterns_file, "r", encoding="utf-8") as file:
            patterns = json.load(file)
            return [(pattern['pattern'], pattern['responses']) for pattern in patterns]
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            (r"mi nombre es (.*)", ["Hola %1, ¿cómo estás?"]),
            (r"(hola|hey|buenos días)", ["Hola, ¿en qué puedo ayudarte?"]),
            (r"adiós", ["Adiós, ¡que tengas un buen día!"]),
        ]

# Función para guardar los patrones en un archivo
def save_patterns(pairs):
    with open(patterns_file, "w", encoding="utf-8") as file:
        json.dump(
            [{"pattern": pattern, "responses": responses} for pattern, responses in pairs],
            file, indent=4, ensure_ascii=False
        )

# Función para consultar el clima
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

# Función para buscar en Wikipedia
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"Esto es lo que encontré sobre {query}: {summary}"
    except wikipedia.DisambiguationError as e:
        return f"Tu búsqueda es ambigua. Algunas sugerencias: {', '.join(e.options[:5])}"
    except wikipedia.PageError:
        return "No encontré resultados en Wikipedia para esa búsqueda."
    except Exception as e:
        return "Hubo un error al realizar la búsqueda en Wikipedia."

# Crear el chatbot con los patrones cargados
pairs = load_patterns()
chatbot = Chat(pairs, reflections)

# Función para depurar las respuestas
def debug_response(user_input):
    print(f"Entrada del usuario: {user_input}")
    
    # Manejar el clima
    if "clima" in user_input.lower() or "tiempo" in user_input.lower():
        match = re.search(r"en ([\w\s]+)", user_input.lower())
        city = match.group(1) if match else "Sabadell"
        return get_weather(city)
    
    # Manejar búsqueda en Wikipedia
    if user_input.lower().startswith("busca en wikipedia "):
        query = user_input[19:].strip()
        return search_wikipedia(query)
    
    for pattern, responses in pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            print(f"Coincidencia encontrada con el patrón: {pattern}")
            return responses[0]
    print("No se encontró coincidencia.")
    return None

# Función para permitir que el bot aprenda nuevos patrones
def learn_new_pattern(user_input):
    print("No reconozco esa entrada. ¿Te gustaría que lo aprenda?")
    speak("No reconozco esa entrada. ¿Te gustaría que lo aprenda?")
    new_pattern = input("Por favor, escribe el patrón que debe coincidir con esta entrada: ")
    new_response = input("¿Qué respuesta debería dar el bot cuando vea esa entrada? ")
    
    pairs.append((new_pattern, [new_response]))
    save_patterns(pairs)
    print("¡Gracias! Ahora puedo responder a esa entrada.")
    speak("¡Gracias! Ahora puedo responder a esa entrada.")

# Función para obtener entrada de voz
def get_audio_input():
    with sr.Microphone() as source:
        print("Escuchando... (habla ahora)")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio, language="es-ES")
            print(f"Tú (voz): {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("No entendí lo que dijiste, intenta de nuevo.")
            speak("No entendí lo que dijiste, intenta de nuevo.")
            return None
        except sr.RequestError:
            print("Hubo un error al conectar con el servicio de reconocimiento de voz.")
            speak("Hubo un error al conectar con el servicio de reconocimiento de voz.")
            return None

# Iniciar la conversación
print("Hola! Soy Quim, y soy una IA creada para confrontar la soledad, ¿en qué puedo ayudarte?")
speak("Hola! Soy Quim, y soy una IA creada para confrontar la soledad, ¿en qué puedo ayudarte?")
while True:
    user_input = get_audio_input()
    
    if user_input is None:
        continue
    
    if user_input.lower() == "adiós":
        print("Adiós, ¡que tengas un buen día!")
        speak("Adiós, ¡que tengas un buen día!")
        break

    response = debug_response(user_input)
    
    if response:
        print(response)
        speak(response)
    else:
        learn_new_pattern(user_input)