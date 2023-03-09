import requests
import datetime
import facebook
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Reactions, User

"""Classe qui permet de s'authentifier avec Facebook"""

class authenticateFacebookView(APIView):
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
                user.facebook_access_token = token
                user.password = ""
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        else:
            try:
                user.facebook_access_token = token
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "token": userToken.key,
        }
        return Response({"status": "User created successfully", "data": data})

"""Fonction qui check si l'utilisateur a posté un message il y a moins d'une minute
et qui réagit en fonction de la réaction choisie
@param user_id : id de l'utilisateur
@param reaction_id : id de la réaction
@param reaction_handlers : dictionnaire qui contient les fonctions de réaction
"""

def new_post(user_id, reaction_id, reaction_handlers):
    
    access_token = User.objects.get(id=user_id).facebook_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters = Reactions.objects.get(title=reaction).parameters
    
   
    graph = facebook.GraphAPI(access_token=access_token, version="3.1")
    posts = graph.get_connections(id='me', connection_name='posts')
    latest_post_time = datetime.datetime.strptime(posts['data'][0]['created_time'], '%Y-%m-%dT%H:%M:%S%z')
    time_diff = datetime.datetime.now(datetime.timezone.utc) - latest_post_time
    if time_diff.seconds < 60:
        reaction_handlers[reaction](access_token, parameters)
        print("New post")
    else:
        print("No new post")

"""Fonction qui check si l'utilisateur a aimé une page il y a moins d'une minute
et qui réagit en fonction de la réaction choisie
@param user_id : id de l'utilisateur
@param reaction_id : id de la réaction
@param reaction_handlers : dictionnaire qui contient les fonctions de réaction
"""

def liked_page(user_id, reaction_id, reaction_handlers):
    
    access_token = User.objects.get(id=user_id).facebook_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters = Reactions.objects.get(title=reaction).parameters
    
    # Obtenir la liste des pages aimées par l'utilisateur
    response = requests.get(f"https://graph.facebook.com/me/likes?access_token={access_token}")
    likes = response.json()["data"]
    # Vérifier si la dernière page aimée a été aimée il y a moins d'une minute
    latest_like_time = datetime.datetime.strptime(likes[0]['created_time'], '%Y-%m-%dT%H:%M:%S%z')
    time_diff = datetime.datetime.now(datetime.timezone.utc) - latest_like_time
    if time_diff.total_seconds() < 60:
        reaction_handlers[reaction](access_token, parameters)
        print("La dernière page aimée a été aimée il y a moins d'une minute !")
    else:
        print("La dernière page aimée a été aimée il y a plus d'une minute.")