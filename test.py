import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import re

# Inicializar síntesis de voz
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Velocidad de la voz
engine.setProperty('voice', 'spanish')  # Cambia la voz al español si está disponible

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para procesar la entrada del usuario
def process_input():
    user_input = user_entry.get()
    if user_input.lower() == "adiós":
        speak("Adiós, ¡que tengas un buen día!")
        root.destroy()
    else:
        chat_area.insert(tk.END, f"Tú: {user_input}\n")
        response = debug_response(user_input)
        chat_area.insert(tk.END, f"Quim: {response}\n")
        speak(response)
    user_entry.delete(0, tk.END)

# Función de respuesta básica
def debug_response(user_input):
    if re.search(r"hola|buenos días", user_input, re.IGNORECASE):
        return "¡Hola! ¿Cómo estás?"
    elif re.search(r"cómo te llamas", user_input, re.IGNORECASE):
        return "Me llamo Quim, tu asistente."
    elif "clima" in user_input:
        return "Lo siento, aún no sé cómo consultar el clima desde aquí."
    else:
        return "No estoy seguro de cómo responder a eso."

# Crear la ventana principal
root = tk.Tk()
root.title("Chatbot Quim")

# Configurar el área de texto para mostrar la conversación
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_area.pack(pady=10)
chat_area.insert(tk.END, "Quim: ¡Hola! Soy Quim, ¿en qué puedo ayudarte?\n")

# Entrada del usuario
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=5)

# Botón para enviar el mensaje
send_button = tk.Button(root, text="Enviar", command=process_input)
send_button.pack()

# Ejecutar la ventana
root.mainloop()
