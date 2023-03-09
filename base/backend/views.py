from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Actions, ActionReactionDatas, Reactions, User, UserActReact
from .serializers import (
    ActionReactionDatasSerializer,
    ActionsSerializer,
    ReactionsSerializer,
    UserActReactSerializer,
    UserSerializer,
)


class CreateAreaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        email = request.data.get("email")
        action = request.data.get("action")
        reaction = request.data.get("reaction")
        user = User.objects.get(email=email)
        new_action = Actions.objects.create(
            title=action["title"],
            datas=ActionReactionDatas.objects.get(id=action["id"]),
            parameters=action["parameters"],
        )
        new_reaction = Reactions.objects.create(
            title=reaction["title"],
            datas=ActionReactionDatas.objects.get(id=reaction["id"]),
            parameters=reaction["parameters"],
        )
        user_act_react = UserActReact.objects.create(
            user=user,
            action=Actions.objects.get(id=new_action.pk),
            reaction=Reactions.objects.get(id=new_reaction.pk),
        )
        if user_act_react is not None:
            return Response(
                {
                    "data": {
                        "user": user_act_react.user.email,
                        "action": user_act_react.action.title,
                        "reaction": user_act_react.reaction.title,
                        "created_at": user_act_react.created_at,
                    },
                    "status": 200,
                }
            )
        return Response({"error": "failed to create area", "status": 401})


class CheckServicesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        email = request.data.get("email")
        user = User.objects.get(email=email)
        rep = {
            "google": False,
            "microsoft": False,
            "github": False,
            "facebook": False,
        }
        if user.google_access_token is not None:
            rep["google"] = True
        if user.microsoft_access_token is not None:
            rep["microsoft"] = True
        if user.github_access_token is not None:
            rep["github"] = True
        if user.facebook_access_token is not None:
            rep["facebook"] = True
        return Response(rep)


class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        token = Token.objects.get_or_create(user=user)[0]
        if user is not None:
            return Response(
                {
                    "data": {
                        "email": user.email,
                        "first_name": user.first_name,
                        "token": token.key,
                    },
                    "status": 200,
                }
            )
        return Response({"error": "Wrong Credentials", "status": 401})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActionsViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer


class ActionsCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer


class ActionsDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer


class ActionsUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer


class ReactionsViewSet(viewsets.ModelViewSet):
    queryset = Reactions.objects.all()
    serializer_class = ReactionsSerializer


class ReactionsCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reactions.objects.all()
    serializer_class = ReactionsSerializer


class ReactionsDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reactions.objects.all()
    serializer_class = ReactionsSerializer


class ReactionsUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reactions.objects.all()
    serializer_class = ReactionsSerializer


class ActionReactionDatasViewSet(viewsets.ModelViewSet):
    queryset = ActionReactionDatas.objects.all()
    serializer_class = ActionReactionDatasSerializer


class ActionReactionDatasCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ActionReactionDatas.objects.all()
    serializer_class = ActionReactionDatasSerializer


class ActionReactionDatasDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ActionReactionDatas.objects.all()
    serializer_class = ActionReactionDatasSerializer


class ActionReactionDatasUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ActionReactionDatas.objects.all()
    serializer_class = ActionReactionDatasSerializer


class UserActReactViewSet(viewsets.ModelViewSet):
    queryset = UserActReact.objects.all()
    serializer_class = UserActReactSerializer


class UserActReactCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserActReact.objects.all()
    serializer_class = UserActReactSerializer


class UserActReactDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserActReact.objects.all()
    serializer_class = UserActReactSerializer


class UserActReactUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserActReact.objects.all()
    serializer_class = UserActReactSerializer
