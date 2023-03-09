from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ActionReactionDatas, User, UserActReact

"""Classe qui permet de récupérer les actions disponibles pour l'utilisateur"""

class getActions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = User.objects.get(email=request.data.get("email"))
        actions = {}
        if user.google_access_token:
            datas = ActionReactionDatas.objects.filter(service="google", type="action")
            for data in datas:
                actions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.microsoft_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="microsoft", type="action"
            )
            for data in datas:
                actions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.github_access_token:
            datas = ActionReactionDatas.objects.filter(service="github", type="action")
            for data in datas:
                actions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.facebook_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="facebook", type="action"
            )
            for data in datas:
                actions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        datas = ActionReactionDatas.objects.filter(service="meteo", type="action")
        for data in datas:
            actions[data.pk] = {
                "id": data.pk,
                "service": data.service,
                "description": data.description,
                "title": data.title,
                "parameters": data.parameters,
                "type": data.type,
            }
        datas = ActionReactionDatas.objects.filter(service="nasa", type="action")
        for data in datas:
            actions[data.pk] = {
                "id": data.pk,
                "service": data.service,
                "description": data.description,
                "title": data.title,
                "parameters": data.parameters,
                "type": data.type,
            }
        return Response({"actions": actions})

"""Classe qui permet de récupérer les réactions disponibles pour l'utilisateur"""

class getReactions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = User.objects.get(email=request.data.get("email"))
        reactions = {}
        if user.google_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="google", type="reaction"
            )
            for data in datas:
                reactions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.microsoft_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="microsoft", type="reaction"
            )
            for data in datas:
                reactions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.github_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="github", type="reaction"
            )
            for data in datas:
                reactions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        if user.facebook_access_token:
            datas = ActionReactionDatas.objects.filter(
                service="facebook", type="reaction"
            )
            for data in datas:
                reactions[data.pk] = {
                    "id": data.pk,
                    "service": data.service,
                    "description": data.description,
                    "title": data.title,
                    "parameters": data.parameters,
                    "type": data.type,
                }
        datas = ActionReactionDatas.objects.filter(service="meteo", type="reaction")
        for data in datas:
            reactions[data.pk] = {
                "id": data.pk,
                "service": data.service,
                "description": data.description,
                "title": data.title,
                "parameters": data.parameters,
                "type": data.type,
            }
        datas = ActionReactionDatas.objects.filter(service="nasa", type="reaction")
        for data in datas:
            reactions[data.pk] = {
                "id": data.pk,
                "service": data.service,
                "description": data.description,
                "title": data.title,
                "parameters": data.parameters,
                "type": data.type,
            }
        return Response({"reactions": reactions})


class getUserActReact(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = User.objects.get(email=request.data.get("email"))
        act_reacts = UserActReact.objects.filter(user=user)
        data = {}
        for act_react in act_reacts:
            data[act_react.pk] = {
                "action_title": act_react.action.title,
                "reaction_title": act_react.reaction.title,
            }
        return Response({"data": data})
