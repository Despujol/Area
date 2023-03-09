import requests
import datetime
from ..models import User, Reactions

"""Fonction qui regarde si la nasa a publié une nouvelle image il y a moins d'une minute
    @param user_id: id de l'utilisateur
    @param reaction_id: id de la réaction
    @param reaction_handler: fonction qui permet de réagir
"""


def new_apod(user_id, reaction_id, reaction_handler):
    access_token = User.objects.get(id=user_id).nasa_access_token
    parameters = Reactions.objects.get(id=reaction_id).parameters
    reaction = Reactions.objects.get(id=reaction_id).title

    maintenant = datetime.datetime.now().time()
    minuit = datetime.time(1, 0, 0)

    # URL de l'API APOD
    url = "https://api.nasa.gov/planetary/apod"

    # Paramètres de la requête
    params = {
        "api_key": "naZh2fmszaEXKEJUpwe88wzXlmFXlveYyWij7Ggv"
    }

    # Envoi de la requête
    response = requests.get(url, params=params)

    # Récupération de l'URL de l'image
    image_url = response.json()["url"]

    # Téléchargement de l'image
    response = requests.get(image_url)

    # Sauvegarde de l'image dans un fichier dans /home parce que je savais pas quoi en foutre
    ## checki if time_now == midnight

    if maintenant < minuit:
    # Si l'heure actuelle est avant minuit, il suffit de soustraire l'heure actuelle de minuit.
        reaction_handler[reaction](access_token, parameters)

    with open("apod.jpg", "wb") as f:
        f.write(response.content)
