import json
import re
import requests
import wikipedia
import pyttsx3
import speech_recognition as sr
import random

# Configurar Wikipedia en español
wikipedia.set_lang("es")

# Archivo de patrones
patterns_file = "patterns_no_accents.json"

# Clave de la API de OpenWeatherMap
API_KEY = "9265687a3ef637dcab7b521c58b1e939"

# Configurar el motor de texto a voz
engine = pyttsx3.init()

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para hablar el texto
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Cargar patrones desde el archivo
def load_patterns():
    try:
        with open(patterns_file, "r", encoding="utf-8") as file:
            patterns = json.load(file)
            return [(pattern['pattern'], pattern['responses']) for pattern in patterns]
    except FileNotFoundError:
        return []

# Juego: Piedra, Papel o Tijera
def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    speak("¡Juguemos! Diga piedra, papel o tijera.")
    print("Diga su elección: piedra, papel o tijera.")
    user_choice = get_audio_input()
    
    if user_choice not in opciones:
        return "No entendí tu elección. Intenta de nuevo."
    
    bot_choice = random.choice(opciones)
    print(f"Tú elegiste: {user_choice}")
    print(f"Yo elegí: {bot_choice}")
    speak(f"Yo elegí {bot_choice}.")
    
    if user_choice == bot_choice:
        return "¡Empate!"
    elif (user_choice == "piedra" and bot_choice == "tijera") or \
         (user_choice == "papel" and bot_choice == "piedra") or \
         (user_choice == "tijera" and bot_choice == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Gané! Buena suerte la próxima."

# Juego: Adivina el número
def jugar_adivina_el_numero():
    numero_ia = random.randint(1, 100)
    speak("Estoy pensando en un número del uno al cien. Intenta adivinarlo.")
    print("Estoy pensando en un número del 1 al 100. ¡Adivínalo!")

    while True:
        user_choice = get_audio_input()
        if not user_choice.isdigit():
            speak("Eso no es un número. Inténtalo de nuevo.")
            continue

        user_choice = int(user_choice)
        if user_choice < numero_ia:
            speak("Más alto.")
            print("Más alto.")
        elif user_choice > numero_ia:
            speak("Más bajo.")
            print("Más bajo.")
        else:
            speak("¡Correcto! Adivinaste mi número.")
            print("¡Correcto! Adivinaste mi número.")
            return "¡Ganaste!"

# Juego: Dado más alto
def jugar_dado_mas_alto():
    speak("¡Vamos a tirar un dado! Primero yo tiraré, luego tú.")
    print("¡Vamos a tirar un dado! Primero yo tiraré, luego tú.")
    input("Presiona Enter para que la IA tire el dado...")
    dado_ia = random.randint(1, 6)
    print(f"La IA sacó un {dado_ia}.")
    speak(f"Saqué un {dado_ia}. Ahora es tu turno.")
    input("Presiona Enter para tirar tu dado...")
    dado_user = random.randint(1, 6)
    print(f"Tú sacaste un {dado_user}.")
    speak(f"Tiraste un {dado_user}.")

    if dado_user > dado_ia:
        return "¡Ganaste! Tu dado fue más alto."
    elif dado_user < dado_ia:
        return "¡Perdiste! Mi dado fue más alto."
    else:
        return "¡Empate! Ambos sacamos el mismo número."

# Juego: Truco de magia
def jugar_truco_de_magia():
    speak("Te voy a sorprender con un truco matemático. Escoge un número entre uno y diez en tu mente.")
    print("Escoge un número entre 1 y 10 en tu mente.")
    speak("Multiplica ese número por dos. Ahora suma ocho al resultado.")
    print("Multiplica tu número por 2 y luego suma 8.")
    speak("Divide el resultado entre dos. Ahora resta tu número original.")
    print("Divide el resultado entre 2 y luego resta tu número original.")
    input("Cuando tengas el resultado, presiona Enter.")
    speak("Tu número es cuatro. ¿Estoy en lo correcto?")
    print("Tu número es 4. ¿Estoy en lo correcto?")
    return "Espero que te haya sorprendido. ¡Es magia matemática!"

# Menú de juegos
def menu_de_juegos():
    speak("Selecciona un juego diciendo su nombre. Por ejemplo: Piedra, papel o tijeras.")
    print("Menú de juegos:")
    print("- Piedra, papel o tijeras")
    print("- Adivina el número")
    print("- Dado más alto")
    print("- Truco de magia")

    while True:
        user_choice = get_audio_input()
        if "piedra" in user_choice or "papel" in user_choice or "tijeras" in user_choice:
            return jugar_piedra_papel_tijera()
        elif "adivina el número" in user_choice:
            return jugar_adivina_el_numero()
        elif "dado más alto" in user_choice:
            return jugar_dado_mas_alto()
        elif "truco de magia" in user_choice:
            return jugar_truco_de_magia()
        else:
            speak("Opción no válida. Intenta decir el nombre del juego.")
            print("Opción no válida. Intenta decir el nombre del juego.")

# Obtener entrada de voz
def get_audio_input():
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio, language="es-ES").lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

# Iniciar conversación
print("Hola, soy Quim!")
speak("Hola, soy Quim!")
while True:
    user_input = get_audio_input()
    if "adiós" in user_input:
        speak("Adiós, ¡que tengas un buen día!")
        break
    elif "juguemos" in user_input:
        response = menu_de_juegos()
    else:
        response = "No estoy seguro de lo que quisiste decir."

    print(response)
    speak(response)