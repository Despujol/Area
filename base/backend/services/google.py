from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from ..models import User, Reactions
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import requests
import json
from ..models import User
import datetime
from ..models import User
import requests
from dateutil import parser

"""Classe qui permet de s'authentifier avec Google"""

class authenticateGoogleView(APIView):
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
                user.google_access_token = token
                user.password = ""
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        else:
            try:
                user.google_access_token = token
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "token": userToken.key,
        }
        return Response({"status": "User created successfully", "data": data})

"""Class qui permet d'envoyer un mail avec Google"""
class sendMailView(APIView):
    def post(self, request, format=None):
        sender = request.data.get("sender")
        to = request.data.get("to")
        subject = request.data.get("subject")
        message = request.data.get("message")

        user = User.objects.get(email=sender)
        try:
            sendMail(user.google_access_token, to, subject, message)
        except Exception as e:
            return Response({"error": str(e)})
        return Response({"status": "Mail sent successfully"})
    
"""Fonction qui check si un fichier a ??t?? ajout?? au drive il y a moins d'une minute
et qui r??agit en fonction de la r??action choisie
@param user_id : id de l'utilisateur
@param reaction_id : id de la r??action
@param reaction_handler : fonction qui permet de r??agir"""
    
def file_added_to_drive(user_id, reaction_id, reaction_handler):

    access_token = User.objects.get(id=user_id).google_access_token
    parameters = Reactions.objects.get(id=reaction_id).parameters
    reaction = Reactions.objects.get(id=reaction_id).title
    
    response = requests.get(f'https://www.googleapis.com/drive/v2/files?orderBy=createdDate desc&maxResults=1',
                        headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'})

    # V??rification du code de r??ponse HTTP
    if response.status_code == 200:
        # R??cup??ration du dernier fichier ajout??
        latest_file = response.json().get('items')[0]
        # V??rification si le dernier fichier a ??t?? ajout?? il y a moins d'une minute
        if latest_file is not None:
            created_date = parser.parse(latest_file.get('createdDate')).timestamp()
            time_diff = datetime.datetime.now().timestamp() - created_date
            if time_diff < 60.0:
                print('Le dernier fichier a ??t?? ajout?? il y a moins d\'une minute.')
                reaction_handler[reaction](access_token, parameters)
            else:
                print('Le dernier fichier a ??t?? ajout?? il y a plus d\'une minute.')
        else:
            print('Aucun fichier trouv??.')
    else:
        print('Error:', response.json()['error']['message'])

"""Fonction qui permet d'envoyer un mail avec Google
@param access_token : token d'acc??s ?? l'API Google
@param parameters : param??tres de la r??action
"""

def sendMail(access_token, parameters):
    # Cr??ation du message
    message = {
        'to': parameters['email'],
        'subject': parameters['object'],
        'body': parameters['message']
    }
    # Cr??ation de l'objet MIMEText
    msg = MIMEText(message['body'])
    msg['to'] = message['to']
    msg['subject'] = message['subject']
    # Encodage du message en base64
    message_bytes = msg.as_bytes()
    message_b64 = base64.urlsafe_b64encode(message_bytes).decode('utf-8')
    # Corps de la requ??te HTTP POST
    payload = {
        'raw': message_b64
    }
    response = requests.post(f'https://www.googleapis.com/gmail/v1/users/me/messages/send',
                            headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'},
                            data=json.dumps(payload))
    # V??rification du code de r??ponse HTTP
    if response.status_code == 200:
        print(response.json())
    else:
        print('Error:', response.json()['error']['message'])



def check_mail(user_id, reaction_id, reaction_handler) :

    user = User.objects.get(id=user_id)
    access_token = user.google_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters = Reactions.objects.get(id=reaction_id).parameters

    response = requests.get(f'https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=1',
                        headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'})
    id_message = response.json().get('messages')[0].get('id')

    response = requests.get(f'https://gmail.googleapis.com/gmail/v1/users/me/messages/{id_message}',
                        headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'})
    # V??rification du code de r??ponse HTTP
    if response.status_code == 200:
        # R??cup??ration du dernier message re??u
        latest_message = int(response.json().get('internalDate')) / 1000 
        timestamp_aujourdhui = int(datetime.datetime.now().timestamp())
        # V??rification si le dernier message a ??t?? re??u il y a moins d'une minute

        if latest_message is not None:
            time_diff = timestamp_aujourdhui - latest_message
            if time_diff < 60.0:
                print('Le dernier message a ??t?? re??u il y a moins d\'une minute.')
                reaction_handler[reaction](access_token, parameters)

            else:
                print('Le dernier message a ??t?? re??u il y a plus d\'une minute.')
        else:
            print('Aucun message trouv??.')
    else:
        print('Error:', response.json()['error']['message'])

def save_attachments_to_drive(access_token, parameters):
    # Sp??cifiez le nom et l'emplacement du fichier que vous souhaitez t??l??charger
    file_name = parameters['file_name']

    file_content = parameters['file_content']
    
    # Configurez l'URL de l'API Google Drive pour t??l??charger un fichier
    url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'

    # Configurez les ent??tes de la requ??te HTTP
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'multipart/related; boundary=my-custom-boundary'
    }


    payload = (
        f'--my-custom-boundary\r\n'
        f'Content-Type: application/json; charset=UTF-8\r\n\r\n'
        f'{{"name": "{file_name}"}}\r\n'
        f'--my-custom-boundary\r\n'
        f'Content-Type: application/octet-stream\r\n\r\n'
        f'{file_content}\r\n'
        f'--my-custom-boundary--'
    )

    # Envoyez la requ??te HTTP POST
    response = requests.post(url, headers=headers, data=payload)

    # V??rifiez le code de r??ponse HTTP
    if response.status_code == 200:
        print('Le fichier a ??t?? t??l??charg?? avec succ??s sur votre Google Drive !')
    else:
        print('Error:', response.json()['error']['message'])
