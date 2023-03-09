##
## EPITECH PROJECT, 2023
## B-DEV-500-BDX-5-2-area-jaykumar.parvedy
## File description:
## area
##
from .facebook import liked_page, new_post
from .github import check_repo_notification, create_an_issue, new_commit
from .google import check_mail, file_added_to_drive, sendMail
from .meteo import alerte_rain, alerte_thunder
from .microsoft import create_event, event_created, send_mail
from ..models import Actions, Reactions, UserActReact
from .nasa import new_apod


"""Fonction qui permet de lancer les areas présent dans la base de données 
    La fonction est executer par crontab toute les minutes.
    Elle execute les actions qui elle même execute les reactions"""


def launch_area() :
    """Dict qui contient les fonctions qui permettent de lancer les actions"""
    action_handlers = {
        "Event created": event_created,
        "New Commit": new_commit,
        "Check repo notification": check_repo_notification,
        "Alerte if rain" : alerte_rain,
        "Alerte if thunder" : alerte_thunder,
        "New post Facebook" : new_post,
        "Facebook Page liked" : liked_page,
        "Nasa post a photo" : new_apod,
        "File added to drive": file_added_to_drive,
        "New mail" : check_mail,
    }
    
    """Dict qui contient les fonctions qui permettent de lancer les reactions"""
    reaction_handlers = {
        "Create an issue": create_an_issue,
        "Send mail": send_mail,
        "Create event": create_event,
        "Send mail with Google": sendMail,
        "Save file in drive": file_added_to_drive,
    }

    areas = UserActReact.objects.all()

    for area in areas:
        user_id = area.user_id
        action_id = area.action_id
        action = Actions.objects.get(id=action_id).title
        reaction = Reactions.objects.get(id=area.reaction_id).id
        print(action)
        if action in action_handlers:
            action_handlers[action](user_id, reaction, reaction_handlers)
        
