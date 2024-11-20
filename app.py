from flask import Flask, request, jsonify, render_template_string
import json
from nltk.chat.util import Chat, reflections

# Cargar patrones desde el archivo JSON
def load_patterns():
    with open("patterns.json", "r", encoding="utf-8") as file:
        patterns = json.load(file)
        return [(pattern["pattern"], pattern["responses"]) for pattern in patterns]

pairs = load_patterns()
chatbot = Chat(pairs, reflections)

# Inicializar Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>QuimAI</title>
        <style>
            *{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: "Poppins", sans-serif; 
            }
            body{ 
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .chatbox{ 
                margin: auto;
                background-color: #FFFFAA;
                padding: 20px 30px;
                border-radius: 20px; 
                max-width: 400px;
            }
            .chatbox h1{
                text-align: center; 
                margin-bottom: 20px; 
            }
            .message{ 
                margin: 10px 0;
            }
            .user{
                color: blue; 
            }
            .bot{ 
                color: green; 
            }
        </style>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="chatbox">
            <h1>Chatbot Quim</h1>
            <form action="/chat" method="post">
                <input type="text" name="message" placeholder="Escribe tu mensaje aquí" style="width: 80%;">
                <button type="submit">Enviar</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = chatbot.respond(user_input)
    
    # Renderizar las respuestas en HTML
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chatbot Quim</title>
        <style>
            *{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: "Poppins", sans-serif; 
            }
            body{ 
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .chatbox{ 
                max-width: 600px; 
                margin: auto;
                background-color: #FFFFAA;
                padding: 20px 30px;
                border-radius: 20px; 
                max-width: 400px;
            }
            .chatbox h1{
                text-align: center; 
                margin-bottom: 20px; 
            }
            .message{ 
                margin: 10px 0;
            }
            .user{
                color: blue; 
            }
            .bot{ 
                color: green; 
            }
        </style>
    </head>
    <body>
        <div class="chatbox">
            <h1>Chatbot Quim</h1>
            <div class="message user"><strong>Tú:</strong> {{ user_input }}</div>
            <div class="message bot"><strong>Quim:</strong> {{ response }}</div>
            <form action="/chat" method="post">
                <input type="text" name="message" placeholder="Escribe tu mensaje aquí" style="width: 80%;">
                <button type="submit">Enviar</button>
            </form>
        </div>
    </body>
    </html>
    """, user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
