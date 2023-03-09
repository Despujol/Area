from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import ActionReactionDatas, User 

"""Fonction qui permet de récupérer l'adresse IP du client"""


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

"""Classe qui permet de créer le about.json"""

class GetAbout(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        data = {
            "client": {
                # ip address of the client
                "host": get_client_ip(request),
            },
            "server": {
                "current time": timezone.now().__format__("%d-%m-%Y %H:%M:%S"),
                "services": [],
            },
        }
        services = {"google", "microsoft", "github", "facebook", "nasa", "meteo"}
        for service in services:
            actions = ActionReactionDatas.objects.filter(service=service, type="action")
            reactions = ActionReactionDatas.objects.filter(
                service=service, type="reaction"
            )
            data["server"]["services"].append(
                {"name": service, "actions": [], "reactions": []}
            )
            for action in actions:
                data["server"]["services"][-1]["actions"].append(
                    {
                        "name": action.title,
                        "description": action.description,
                    }
                )
            for reaction in reactions:
                data["server"]["services"][-1]["reactions"].append(
                    {
                        "name": reaction.title,
                        "description": reaction.description,
                    }
                )
        return Response({"data": data})
