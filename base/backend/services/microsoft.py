from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from ..models import User, Reactions
import requests
import json
from datetime import datetime
from dateutil import parser


"""Classe qui permet de s'authentifier avec Microsoft"""


class authenticateMicrosoftView(APIView):
    def post(self, request, format=None):
        token = request.data.get("token")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        user, created = User.objects.get_or_create(email=email, username=email)
        userToken = Token.objects.get_or_create(user=user)[0]
        if created:
            try:
                user.first_name = first_name
                user.last_name = last_name
                user.microsoft_access_token = token
                user.password = ""
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        else:
            try:
                user.microsoft_access_token = token
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "token": userToken.key,
        }
        return Response({"status": "User created successfully", "data": data})

"""Fonction qui permet de créer un événement avec l'API Microsoft Graph
@param access_token : le token d'accès de l'utilisateur
@param parameters : les paramètres de l'événement
"""

def create_event(access_token, parameters) :

    graph_api_endpoint = 'https://graph.microsoft.com/v1.0'
    event_subject = 'Test Event'
    event_body = {
        'contentType': 'HTML',
        'content': parameters['body']
    }
    event_start_time = parameters['start_at']
    event_end_time = parameters['end_at']
    event_payload = {
    'subject': event_subject,
    'body': event_body,
    'start': {
        'dateTime': event_start_time,
        'timeZone': 'UTC'
    },
    'end': {
        'dateTime': event_end_time,
        'timeZone': 'UTC'
    },
    'location': {
        'displayName': parameters['location']
    },
    'attendees': [
        {
            'emailAddress': {
                'address': 'jane.doe@example.com',
                'name': 'Jane Doe'
            },
            'type': 'required'
        }
    ]
}
# Envoi de la demande de création d'événement à l'API Microsoft Graph
    create_event_url = graph_api_endpoint + '/me/events'
    response = requests.post(
        create_event_url,
        headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
        },
        data=json.dumps(event_payload),
    )

    # Vérification du statut de la demande
    if response.status_code == 201:
        print("Event created successfully")
    else:
        print("Error creating event: " + response.text)

"""Fonction qui permet d'envoyer un e-mail avec l'API Microsoft Graph
@param access_token : le token d'accès de l'utilisateur
@param parameters : les paramètres de l'événement
"""

def send_mail(access_token, parameters) :

    # Configurer l'URL pour l'API Graph pour envoyer un e-mail
    graph_url = 'https://graph.microsoft.com/v1.0/me/sendMail'
    email : str = parameters['email']
    object :str = parameters['object']
    message : str = parameters['message']

    # Configurer le contenu de l'e-mail
    email_body = {
        'message': {
            'subject':  object,
            'body': {
                'contentType': 'Text',
                'content': message
            },
            'toRecipients': [
                {
                    'emailAddress': {
                        'address': email
                    }
                }
            ]
        },
        "saveToSentItems": "true",
    }

    # Configurer les en-têtes de la requête HTTP
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    # Envoyer la requête HTTP pour envoyer l'e-mail
    response = requests.post(url=graph_url, json=email_body, headers=headers)

    # Vérifier le code de statut de la réponse
    if response.status_code == 202:
        print("E-mail envoyé avec succès !")
    else:
        print("Erreur lors de l'envoi de l'e-mail.")
        print(response.json())
        print(response.status_code)

"""Fonction qui check si un événement est créé et qui envoie appel la réaction associée
@param user_id : l'id de l'utilisateur
@param reaction_id : l'id de la réaction
@param reaction_handler : la fonction de la réaction
"""

def event_created(user_id, reaction_id, reaction_handler) :
    
    access_token = User.objects.get(id=user_id).microsoft_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters = Reactions.objects.get(id=reaction_id).parameters
        
    graph_url = 'https://graph.microsoft.com/v1.0/me/calendar/events'

    # Définir l'en-tête d'autorisation avec un jeton d'accès valide
    headers = {"Authorization": f"Bearer {access_token}"}

    # Récupérer les événements à partir de l'API Graph
    response = requests.get(graph_url, headers=headers)

    if response.status_code == 200:
        # Analyser la réponse JSON pour extraire les données pertinentes
        events = json.loads(response.content)["value"]

        # Triez les événements par ordre décroissant de début

        # Sélectionnez le dernier événement créé
        last_event = events[0]
        last_event_time = parser.parse(last_event["createdDateTime"]).timestamp()
        current_time = datetime.now().timestamp()
        print(last_event_time)
        print(current_time)
        time_diff = current_time - last_event_time

        # Vérifier si la différence de temps est inférieure à 60 secondes (1 minute)
        if time_diff < 60:
            print("last_event_time a été créé il y a moins d'une minute.")
            reaction_handler[reaction](access_token, parameters)
        else:
            print("last_event_time a été créé il y a plus d'une minute.")
    else:
        print(f"Une erreur s'est produite : {response.content}")
