from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from ..models import User
from ..models import User, Actions, UserActReact, Reactions
import requests
from dateutil import parser
import time
import json

class authenticateGithubView(APIView):
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
                user.github_access_token = token
                user.password = ""
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        else:
            try:
                user.github_access_token = token
                user.save()
            except Exception as e:
                return Response({"error": str(e)})
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "token": userToken.key,
        }
        return Response({"status": "User created successfully", "data": data})
    

"""Fonction qui permet de récupérer l'utilisateur """

def get_user(action_id):
    user_id = UserActReact.objects.get(action=action_id).user
    user = User.objects.get(id=user_id)
    return user

"""Fonction qui permet de récupérer la réaction liée à une action"""

def get_react(action_id):
    react_id = UserActReact.objects.get(action=action_id).reaction
    react = Reactions.objects.get(id=react_id)
    return react


"""Fonction qui check si le dernier commit a été effectué il y a moins d'une minute
et qui réagit en fonction de la réaction choisie
@param user_id : id de l'utilisateur
@param reaction_id : id de la réaction
@param reaction_handlers : dictionnaire qui contient les fonctions de réaction"""

def new_commit(user_id, reaction_id, reaction_handlers):

    action_id = UserActReact.objects.get(reaction=reaction_id).action
    access_token = User.objects.get(id=user_id).github_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters = Reactions.objects.get(title=reaction).parameters
    parameters_action = Actions.objects.get(id=action_id).parameters
    
    owner = parameters_action['owner']
    repo = parameters_action['repo']

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"La requête a échoué avec le code d'erreur {response.status_code}")
        return

    last_commit = response.json()[0]
    last_commit_time_str = last_commit["commit"]["committer"]["date"]
    last_commit_time = int(parser.parse(last_commit_time_str).strftime("%s"))
    current_time = int(time.time())

    if (current_time - last_commit_time) < 60:
        print("Le dernier commit a été effectué il y a moins d'une minute !")
        reaction_handlers[reaction](access_token, parameters)
    else:
        print("Le dernier commit a été effectué il y a plus d'une minute.")
    return

"""Fonction qui check si il y a une notification sur le repo
et qui réagit en fonction de la réaction choisie
@param user_id : id de l'utilisateur
@param reaction_id : id de la réaction
@param reaction_handlers : dictionnaire qui contient les fonctions de réaction
"""

def check_repo_notification(user_id, reaction_id, reaction_handlers) :
    
    action_id = UserActReact.objects.get(reaction=reaction_id).action
    access_token = User.objects.get(id=user_id).github_access_token
    reaction = Reactions.objects.get(id=reaction_id).title
    parameters_action = Actions.objects.get(id=action_id).parameters
    parameters = Reactions.objects.get(title=reaction).parameters

    owner = parameters_action['owner']
    repo = parameters_action['repo']
    url = f"https://api.github.com/repos/{owner}/{repo}/notifications"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        reaction_handlers[reaction](access_token, parameters)
        print(f"La requête a échoué avec le code d'erreur {response.status_code}")
        return
    else:
        print(response.json())

    return

"""Fonction qui permet de créer une issue sur le repo
@param access_token : token d'accès de l'utilisateur
@param parameters : paramètres de la réaction
"""

def create_an_issue(access_token, parameters):
    
    owner = parameters['owner']
    repo = parameters['repo']
    title = parameters['title']
    body = parameters['body']

    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}",
    }
    payload = {"title": title, "body": body}
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print("Issue créée avec succès !")
        return response.json()
    else:
        print(f"La requête a échoué avec le code d'erreur {response.status_code}")
        print(response.content)
        return (None,)
