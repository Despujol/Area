import requests
import json
from geopy.geocoders import Nominatim
from ..models import User, Reactions

"""Fonction qui permet d'envoyer une alerte météo si il y a un risque de tempête
@param user_id: id de l'utilisateur
@param reaction_id: id de la réaction
@param reaction_handler: fonction qui permet de réagir
"""


def alerte_thunder(user_id, reaction_id, reaction_handler):
    access_token = User.objects.get(id=user_id).google_access_token
    parameters = Reactions.objects.get(id=reaction_id).parameters
    reaction = Reactions.objects.get(id=reaction_id).title

    # Définir l'URL de l'API OpenWeatherMap avec votre clé API
    api_url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}"

    # Remplacer les paramètres suivants par les coordonnées géographiques de votre emplacement
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode("me")
    latitude = location.latitude
    longitude = location.longitude

    # Remplacer votre clé API OpenWeatherMap
    api_key = "043fa65bda3e1ae800339944afa6943c"

    # Exclure toutes les parties de la réponse qui ne sont pas nécessaires pour économiser des appels API
    exclude = "minutely,hourly,daily,alerts"

    # Construire l'URL de l'API OpenWeatherMap avec les paramètres
    url = api_url.format(lat=latitude, lon=longitude, exclude=exclude, api_key=api_key)

    # Obtenir les données météorologiques actuelles pour votre emplacement
    response = requests.get(url)

    # Charger les données JSON de la réponse HTTP
    data = json.loads(response.content)

    # Vérifier si un avertissement de tempête est actuellement en vigueur pour votre emplacement
    if "alerts" in data:
        for alert in data["alerts"]:
            if alert["event"] == "Storm":
                reaction_handler[reaction](access_token, parameters)
                print("Il y a un risque de tempête !")
    else:
        print("Il n'y a pas d'avertissement de tempête actif pour votre emplacement.")

"""Fonction qui permet d'envoyer une alerte météo si il y a un risque de pluie
@param user_id: id de l'utilisateur
@param reaction_id: id de la réaction
@param reaction_handler: fonction qui permet de réagir
"""
    
def alerte_rain(user_id, reaction_id, reaction_handler):
    access_token = User.objects.get(id=user_id).google_access_token
    parameters = Reactions.objects.get(id=reaction_id).parameters
    reaction = Reactions.objects.get(id=reaction_id).title
    
    api_key = "043fa65bda3e1ae800339944afa6943c "

    # URL de l'API OpenWeatherMap pour les prévisions météo actuelles
    """ url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}" """
    
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode("me")
    latitude = location.latitude
    longitude = location.longitude
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    # Obtenir les données JSON à partir de l'API
    response = requests.get(url)
    data = response.json()

    # Vérifier si la pluie est prévue
    if "rain" in data:
        reaction_handler[reaction](access_token, parameters)
        print("Il pleut à Bordeaux !")
    else:
        print("Il ne pleut pas à Bordeaux.")
