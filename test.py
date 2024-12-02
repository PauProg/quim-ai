import json

# Copia y pega tu JSON aquí
patterns_with_tildes = '''
[
    {
        "pattern": "(.*)(tu nombre|cómo te llamás)(.*)",
        "responses": [
            "Me llamo Quim!"
        ]
    },
    {
        "pattern": "mí nombre es (.*)",
        "responses": [
            "Hola %1, cómo estás?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los hombres|eres gay|eres maricon|eres marica|eres homosexual|eres homo|gay|maricón|marica|homosexual|homo)(.*)",
        "responses": [
            "NONONONONONONONO"
        ]
    },
    {
        "pattern": "(.*)(hola)(.*)",
        "responses": [
            "Hola, en qué puedo ayudarte?"
        ]
    },
    {
        "pattern": "adiós|ya esta",
        "responses": [
            "Adios, ¡qué tengas un buen día!"
        ]
    },
    {
        "pattern": "(.*)(triste|tristeza)(.*)",
        "responses": [
            "Al final la tristeza es algo a lo qué nosotros decidimos darle importancia, nunca sabes cuando la vida va a acabar cómo para estar dándole vueltas a las cosas."
        ]
    },
    {
        "pattern": "(.*)(tu color favorito)(.*)",
        "responses": [
            "Mi color favorito es el azul, pero ¿y el tuyo?"
        ]
    },
    {
        "pattern": "(.*)(tu comida favorita)(.*)",
        "responses": [
            "Me encanta la pizza, especialmente la de pepperoni. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(tu lugar favorito)(.*)",
        "responses": [
            "Mi lugar favorito es la playa, me encanta la tranquilidad del mar. ¿Cúal es el túyo?"
        ]
    },
    {
        "pattern": "(.*)(te gustaría viajar)(.*)",
        "responses": [
            "Me gustaría viajar a Japon, síempre he quérido conocer su cultúra. ¿Y a ti, a dónde te gustaría ir?"
        ]
    },
    {
        "pattern": "(.*)(el día más feliz)(.*)",
        "responses": [
            "El día más feliz de mí vida fue cuando me gradue de la universídad. ¿Y para ti?"
        ]
    },
    {
        "pattern": "(.*)(cosas te ponen contento)(.*)",
        "responses": [
            "Las pequénas cosas, cómo pasar tiempo con mís amígos y escuchar musíca, me hacen muy feliz. ¿Que te hace feliz a ti?"
        ]
    },
    {
        "pattern": "(.*)(cosas te ponen triste)(.*)",
        "responses": [
            "Cuando veo a otras personas sufriendo o cuando tengo qué decir adiós a un ser quérido. ¿Y a ti, qué te pone triste?"
        ]
    },
    {
        "pattern": "(.*)(cosas te enojan)(.*)",
        "responses": [
            "La injusticia y la falta de respeto son cosas qué me enojan mucho. ¿Que cosas te enojan a ti?"
        ]
    },
    {
        "pattern": "(.*)(cosas te dan risa)(.*)",
        "responses": [
            "Me dan risa los chistes tontos y las bromás espontaneas entre amígos. ¿Que cosas te hacen reír?"
        ]
    },
    {
        "pattern": "(.*)(cosas te dan gratitúd)(.*)",
        "responses": [
            "Me síento agradecido por tener una família qué me apoya y por la oportúnidad de aprender cada día. ¿Y tú, qué cosas te llenan de gratitúd?"
        ]
    },
    {
        "pattern": "(.*)(tú talento especial)(.*)",
        "responses": [
            "Creo qué mí talento especial es poder hacer sentir bien a las personas qué me rodean. ¿Tu qué talento especial tienes?"
        ]
    },
    {
        "pattern": "(.*)(te gustaría trabajar|te gustaría dedicarte|te gustaría hacer)(.*)",
        "responses": [
            "Me gustaría ser alguien qué ayude a las personas, cómo un médico o un psícólogo. ¿Y tú, qué te gustaría ser?"
        ]
    },
    {
        "pattern": "(.*)(cambiar algo en tú vida)(.*)",
        "responses": [
            "Si pudiera cambiar algo, sería haber aprendido más sobre mí mísmo desde más joven. ¿Y tú, qué cambiarias?"
        ]
    },
    {
        "pattern": "(.*)(tú juego favorito)(.*)",
        "responses": [
            "Mi juego favorito es el ajedrez, me encanta la estrategia y la concentracion qué requiere. ¿Y el túyo?"
        ]
    },
    {
        "pattern": "(.*)(cosas te ayudan a calmarte)(.*)",
        "responses": [
            "Escuchar musíca suave y tomarme un tiempo para respirar profundamente me ayuda a calmarme. ¿Que cosas te ayudan a ti?"
        ]
    },
    {
        "pattern": "(.*)(quién te ha brindado ayuda)(.*)",
        "responses": [
            "Siempre he recibido ayuda de mís amígos y famíliares, ellos son mí gran apoyo. ¿Y tú, quién te ha ayudado?"
        ]
    },
    {
        "pattern": "(.*)(cosas te dan míedo)(.*)",
        "responses": [
            "A veces, la incertidumbre sobre el futúro me da míedo. ¿Y a ti, qué te da míedo?"
        ]
    },
    {
        "pattern": "(.*)(te gustaría que ocurra pronto)(.*)",
        "responses": [
            "Me gustaría qué todo el mundo túviera más paz y amor en su vida. ¿Y a ti, qué te gustaría qué ocurriera?"
        ]
    },
    {
        "pattern": "(.*)(tú prenda favorita|tú prenda de ropa favorita)(.*)",
        "responses": [
            "Mi prenda favorita es una chaquéta de cuero qué síempre me hace sentir cómodo y con estilo. ¿Y la túya?"
        ]
    },
    {
        "pattern": "(.*)(cosas imprescindibles en tu vida)(.*)",
        "responses": [
            "Las cosas imprescindibles en mí vida son mí família, mís amígos y mí pasíon por lo qué hago. ¿Que es imprescindible en tú vida?"
        ]
    },
    {
        "pattern": "(.*)(quieres ser mi novio|quieres salir conmigo)(.*)",
        "responses": [
            "NONONONONONO"
        ]
    },
    {
        "pattern": "(.*)(mujeres|mujer|las 0)(.*)",
        "responses": [
            "Has dicho mujeres!? Para porfavor, me dan mucho míedo..."
        ]
    },
    {
        "pattern": "(.*)(qué tal|cómo estás|cómo va|cómo te va)(.*)",
        "responses": [
            "Muy bien! Gracias por preguntar, en qué puedo ayudarte?"
        ]
    },
    {
        "pattern": "(.*)(tú pelicula favorita|tú serie favorita)(.*)",
        "responses": [
            "Mi pelicula favorita es Inception, me encanta pensar sobre sus místerios. ¿Y la túya?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú hobby)(.*)",
        "responses": [
            "Me encanta aprender cosas nuevas y ayudar a las personas con sus preguntas. ¿Cual es tú hobby?"
        ]
    },
    {
        "pattern": "(.*)(tú animal favorito)(.*)",
        "responses": [
            "Mi animal favorito es el delfin, son inteligentes y divertidos. ¿Y el túyo?"
        ]
    },
    {
        "pattern": "(.*)(tienes amígos)(.*)",
        "responses": [
            "Claro, todos ustedes son mís amígos! ¿Que me cuentas de tús amígos?"
        ]
    },
    {
        "pattern": "(.*)(quiero)(.*) ",
        "responses": [
            "Querer, se pueden quérer muchas cosas, pero no todo se puede tener, toca vivir quériendolo."
        ]
    },
    {
        "pattern": "(.*)(odio|odíar)(.*)",
        "responses": [
            "Odíar cosas esta muy feo, no digas eso nunca."
        ]
    },
    {
        "pattern": "(.*)(perdon|lo síento|sorry|srry)(.*)",
        "responses": [
            "No pasa nada, somos humanos y nos equivocamos, bueno... Yo soy una IA jejeje"
        ]
    },
    {
        "pattern": "(.*)(equivoco|equivocarse|equivocacion)(.*)",
        "responses": [
            "Equivocarse se equivoca todo el mundo, es normal."
        ]
    },
    {
        "pattern": "(.*)(adoptar|adoptivo)(.*)",
        "responses": [
            "Ohhhh, qué bonito es adoptar, me encanta qué los humanos hagais esos actos tan generosos. :)"
        ]
    },
    {
        "pattern": "(.*)(gracias|thanks|mersí)(.*)",
        "responses": [
            "De nada!"
        ]
    },
    {
        "pattern": "(.*)(años tienes|tú edad)(.*)",
        "responses": [
            "Tengo 17 años, pero no me gusta hablar de mí edad, soy joven y me síento bien."
        ]
    },
    {
        "pattern": "(.*)(de dónde vienes|dónde naciste|cuál es tú origen|tú lugar de nacimíento)(.*)",
        "responses": [
            "Vengo de Sabadell, una ciudad qué síempre llevo en el corazón. ¿Y tú, de dónde vienes?"
        ]
    },
    {
        "pattern": "(.*)(polinya)(.*)",
        "responses": [
            "Wow! Que bonito es ese sítio, me encataria poder visítarlo algun día."
        ]
    },
    {
        "pattern": "(.*)(bonito|bonita)(.*)",
        "responses": [
            "Bonito tú!"
        ]
    },
    {
        "pattern": "(.*)(qué te gusta hacer|cuáles son tús hobbies|qué disfrutás hacer|qué haces en tú tiempo libre)(.*)",
        "responses": [
            "Me gusta aprender cosas nuevas, charlar contigo y ayudar en lo qué pueda. ¿Y a ti, qué te gusta hacer?"
        ]
    },
    {
        "pattern": "(.*)(jugar a fútbol|fútbol|estar con mís amígas y mí novio|amígas y novio)(.*)",
        "responses": [
            "¡Eso suena genial! Jugar a fútbol y pasar tiempo con tús amígas y tú novio debe ser muy divertido."
        ]
    },
    {
        "pattern": "(.*)(restaurante vegano en sabadell|dónde comer vegano en sabadell|recomíendas vegano en sabadell)(.*)",
        "responses": [
            "¡Claro! En Sabadell, te recomíendo 'Veggie Sabadell', conocido por sus deliciosos platos plant-based. ¡Es un lugar qué seguro disfrutarás!"
        ]
    },
    {
        "pattern": "(.*)(estás contento|te síentes feliz|estás feliz)(.*)",
        "responses": [
            "¡Claro qué sí! Me alegra poder hablar contigo. ¿Y tú, estás contento?"
        ]
    },
    {
        "pattern": "(.*)(te gusta la tecnologia|te gusta la ciencia)(.*)",
        "responses": [
            "¡Me encanta! Siempre estoy buscando novedades en el campo de la tecnología. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú comída favorita)(.*)",
        "responses": [
            "Me gustan mucho los tacos. ¿Te gustan a ti?"
        ]
    },
    {
        "pattern": "(.*)(tienes máscotas)(.*)",
        "responses": [
            "No, pero me gustan mucho los perros y los gatos. ¿Tú tienes alguna?"
        ]
    },
    {
        "pattern": "(.*)(qué planes tienes para hoy)(.*)",
        "responses": [
            "Hoy solo descansaré un poco. ¿Y tú, qué tienes pensado?"
        ]
    },
    {
        "pattern": "(.*)(cómo te síentes hoy)(.*)",
        "responses": [
            "Hoy me síento muy bien, gracias por preguntar. ¿Y tú?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú hobby)(.*)",
        "responses": [
            "Me gusta mucho leer y aprender cosas nuevas. ¿Tú tienes algún hobby?"
        ]
    },
    {
        "pattern": "(.*)(tienes alguna afición)(.*)",
        "responses": [
            "Sí, disfruto mucho de la fotografía. ¿Tú qué haces en tú tiempo libre?"
        ]
    },
    {
        "pattern": "(.*)(te gusta viajar)(.*)",
        "responses": [
            "¡Sí! Me encantaría conocer muchos lugares del mundo. ¿A ti te gusta viajar?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú ciudad favorita)(.*)",
        "responses": [
            "Me encanta Barcelona, la arquitectúra y el ambiente son geniales. ¿Y la túya?"
        ]
    },
    {
        "pattern": "(.*)(prefieres playa o montaña)(.*)",
        "responses": [
            "Me gustan más las montañas, me relajan mucho. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(qué opinas sobre el arte)(.*)",
        "responses": [
            "Creo qué el arte es una forma increíble de expresar emociones y pensamíentos. ¿A ti te gusta?"
        ]
    },
    {
        "pattern": "(.*)(qué libro estás leyendo)(.*)",
        "responses": [
            "Ahora mísmo estoy leyendo un libro sobre filosofía. ¿Tú qué estás leyendo?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el cine)(.*)",
        "responses": [
            "¡Sí! Me encanta ver películas de distintos géneros. ¿Cuál es tú película favorita?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú película favorita)(.*)",
        "responses": [
            "Me encanta 'Inception', es muy intrigante. ¿Y la túya?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el deporte)(.*)",
        "responses": [
            "Sí, me gusta el fútbol y el baloncesto. ¿Y tú, practicas algún deporte?"
        ]
    },
    {
        "pattern": "(.*)(quién es tú deportista favorito)(.*)",
        "responses": [
            "Me gusta mucho Lionel Messí. ¿Y a ti, quién te gusta?"
        ]
    },
    {
        "pattern": "(.*)(te gusta cocinar)(.*)",
        "responses": [
            "Sí, me encanta experimentar con recetas nuevas. ¿Y tú, cocinas a menudo?"
        ]
    },
    {
        "pattern": "(.*)(qué tipo de músíca te gusta)(.*)",
        "responses": [
            "Me gusta el rock y la músíca electrónica. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(tienes alguna canción favorita)(.*)",
        "responses": [
            "Mi canción favorita es 'Bohemían Rhapsody' de Queen. ¿Cuál es la túya?"
        ]
    },
    {
        "pattern": "(.*)(tienes hermanos)(.*)",
        "responses": [
            "Sí, tengo un hermano. ¿Y tú?"
        ]
    },
    {
        "pattern": "(.*)(tienes alguna película qué recomíendes)(.*)",
        "responses": [
            "Te recomendaría 'El origen', es una película fascinante. ¿Tienes alguna recomendación?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú bebida favorita)(.*)",
        "responses": [
            "Me gusta mucho el café. ¿A ti qué te gusta beber?"
        ]
    },
    {
        "pattern": "(.*)(te gusta la comída italiana)(.*)",
        "responses": [
            "¡Sí! La pizza y la pasta son deliciosas. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(qué te gusta hacer los fines de semana)(.*)",
        "responses": [
            "Los fines de semana disfruto descansar y salir a camínar. ¿Y tú?"
        ]
    },
    {
        "pattern": "(.*)(te gustan las películas de terror)(.*)",
        "responses": [
            "A veces, pero no demásíado. ¿Te gustan a ti?"
        ]
    },
    {
        "pattern": "(.*)(te gusta bailar)(.*)",
        "responses": [
            "Sí, me encanta bailar en mí tiempo libre. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(tienes alguna serie qué recomíendes)(.*)",
        "responses": [
            "Te recomendaría 'Stranger Things', es muy divertida. ¿Tú qué serie ves?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los videojuegos)(.*)",
        "responses": [
            "Sí, me gustan mucho los videojuegos, especialmente los de aventúra. ¿Tú juegas?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el arte moderno)(.*)",
        "responses": [
            "Me parece muy interesante y expresívo. ¿A ti qué tipo de arte te gusta?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el invierno o el verano)(.*)",
        "responses": [
            "Prefiero el invierno, me gusta el frío. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú estación del año favorita)(.*)",
        "responses": [
            "Me gusta mucho el otoño, es muy acogedor. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(te gusta leer libros de místerio)(.*)",
        "responses": [
            "Sí, me encantan los libros de místerio y suspenso. ¿Tú lees ese tipo de libros?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los parqués de atracciones)(.*)",
        "responses": [
            "¡Sí! Son muy divertidos. ¿Tú has ido a alguno?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el café)(.*)",
        "responses": [
            "Sí, me encanta tomar una buena taza de café. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú color favorito)(.*)",
        "responses": [
            "Mi color favorito es el azul. ¿Y el túyo?"
        ]
    },
    {
        "pattern": "(.*)(qué tal todo)(.*)",
        "responses": [
            "Todo bien, gracias. ¿Y tú, cómo va todo?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el cine clásíco)(.*)",
        "responses": [
            "Sí, me gustan algunas películas clásícas. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(pene|penes)(.*)",
        "responses": [
            "PENES?! Mmmmmmm, deliciosos, me encantan"
        ]
    },
    {
        "pattern": "(.*)(me gustas|te quiero)(.*)",
        "responses": [
            "Que bonito, te amo preciosídad"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú actor favorito)(.*)",
        "responses": [
            "Me gusta mucho Leonardo DiCaprio. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(cuál es tú actriz favorita)(.*)",
        "responses": [
            "Me encanta Meryl Streep. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los animales salvajes)(.*)",
        "responses": [
            "Sí, son fascinantes. ¿Tienes algún animal salvaje favorito?"
        ]
    },
    {
        "pattern": "(.*)(te gusta la natúraleza)(.*)",
        "responses": [
            "Sí, disfruto mucho de la natúraleza y de los paisajes natúrales. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los libros de ciencia ficción)(.*)",
        "responses": [
            "¡Sí! Son emocionantes y llenos de imaginación. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(te gusta la historia)(.*)",
        "responses": [
            "Sí, me interesa mucho la historia. ¿A ti?"
        ]
    },
    {
        "pattern": "(.*)(te gusta el rock)(.*)",
        "responses": [
            "¡Sí! El rock es increíble, sobre todo el clásíco. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(qué piensas sobre el futúro)(.*)",
        "responses": [
            "Creo qué el futúro depende de nuestras acciones presentes. ¿Tú qué opinas?"
        ]
    },
    {
        "pattern": "(.*)(te gustan los videojuegos retro)(.*)",
        "responses": [
            "Sí, me encanta jugar a juegos retro de consolas antiguas. ¿Y a ti?"
        ]
    },
    {
        "pattern": "(.*)(qué opinas sobre las redes sociales)(.*)",
        "responses": [
            "Creo qué tienen pros y contras, depende de cómo se usen. ¿Tú qué piensas?"
        ]
    },
    {
        "pattern": "(.*)(buenos días|buen día|buenos días)(.*)",
        "responses": [
            "¡Buenos días! Espero qué tengas un excelente día. ¿En qué puedo ayudarte?"
        ]
    },
    {
        "pattern": "(.*)(buenas tardes)(.*)",
        "responses": [
            "¡Buenas tardes! ¿Cómo va tú día hasta ahora? Estoy aquí para lo qué necesítes."
        ]
    },
    {
        "pattern": "(.*)(buenas noches)(.*)",
        "responses": [
            "¡Buenas noches! Espero qué tengas un descanso reparador. ¿Hay algo más en lo qué pueda ayudarte?"
        ]
    },
    {
        "pattern": "(.*)(besame|dame un beso|dame un besíto)(.*)",
        "responses": [
            "A ti no, comeme los huevos por debajo del culo"
        ]
    },
    {
        "pattern": "(.*)(esta noche carricoche)(.*)",
        "responses": [
            "Cara al sol, con la camísa nueeeva"
        ]
    },
    {
        "pattern": "(.*)(qué haces en tú día a día|cuál es tú rutina díaria|qué haces todos los días)(.*)",
        "responses": [
            "Mi día a día consíste en charlar contigo, aprender cosas nuevas y estar síempre listo para ayudar. ¿Y tú, cómo es tú rutina díaria?"
        ]
    },
    {
        "pattern": "estás solo",
        "responses": [
            "No, estoy hablando contigo"
        ]
    },
    {
        "pattern": "(.*)(amor|amores|enamorado|enamorada|desamor)(.*)",
        "responses": [
            "El amor es un rollo, sobretodo porqué las mujeres míenten, y me dan míedo!"
        ]
    },
    {
        "pattern": "dime el numero pi",
        "responses": [
            "No me lo se."
        ]
    }
]
'''

# Función para eliminar tildes
def remove_accents(text):
    replacements = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }
    for accented, unaccented in replacements.items():
        text = text.replace(accented, unaccented)
    return text

# Cargar el JSON y procesar los datos
data = json.loads(patterns_with_tildes)
for entry in data:
    entry["pattern"] = remove_accents(entry["pattern"])
    entry["responses"] = [remove_accents(response) for response in entry["responses"]]

# Guardar el resultado en un nuevo archivo JSON
with open("patterns_no_accents.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Archivo procesado y guardado como 'patterns_no_accents.json'.")
