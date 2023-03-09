from rest_framework import routers
from django.urls import path, include
from .about import GetAbout
from .getters import getActions, getReactions, getUserActReact
from .services.facebook import authenticateFacebookView
from .services.microsoft import authenticateMicrosoftView
from .services.github import authenticateGithubView
from .services.google import authenticateGoogleView, sendMailView
from .views import (
    ActionsCreateView,
    ActionsDeleteView,
    ActionReactionDatasCreateView,
    ActionReactionDatasDeleteView,
    ActionReactionDatasViewSet,
    ActionsViewSet,
    ReactionsCreateView,
    ReactionsDeleteView,
    ReactionsViewSet,
    CheckServicesView,
    CreateAreaView,
    LoginView,
    UserActReactViewSet,
    UserDeleteView,
    UserViewSet,
    UserActReactCreateView,
    UserActReactDeleteView,
    UserCreateView,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"actions", ActionsViewSet)
router.register(r"reactions", ReactionsViewSet)
router.register(r"actionreactiondatas", ActionReactionDatasViewSet)
router.register(r"useractreact", UserActReactViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/<int:pk>/", UserDeleteView.as_view()),
    path("users/", UserCreateView.as_view(), name="user-create"),
    path("actions/<int:pk>/", ActionsDeleteView.as_view()),
    path("actions/", ActionsCreateView.as_view(), name="actions-create"),
    path("getactions/", getActions.as_view(), name="getactions"),
    path("reactions/<int:pk>/", ReactionsDeleteView.as_view()),
    path("reactions/", ReactionsCreateView.as_view(), name="reactions-create"),
    path("getreactions/", getReactions.as_view(), name="getreactions"),
    path("actionreactiondatas/<int:pk>/", ActionReactionDatasDeleteView.as_view()),
    path(
        "actionreactiondatas/",
        ActionReactionDatasCreateView.as_view(),
        name="actionreactiondatas-create",
    ),
    path("useractreact/<int:pk>/", UserActReactDeleteView.as_view()),
    path("useractreact/", UserActReactCreateView.as_view(), name="useractreact-create"),
    path("getuseractreact/", getUserActReact.as_view(), name="getuseractreact"),
    path("login/", LoginView.as_view(), name="login"),
    path("google/", authenticateGoogleView.as_view(), name="google"),
    path("google/sendmail/", sendMailView.as_view(), name="sendmail"),
    path("microsoft/", authenticateMicrosoftView.as_view(), name="microsoft"),
    path("github/", authenticateGithubView.as_view(), name="github"),
    path("facebook/", authenticateFacebookView.as_view(), name="facebook"),
    path("checkservices/", CheckServicesView.as_view(), name="checkservices"),
    path("about.json/", GetAbout.as_view(), name="about.json"),
    path("createarea/", CreateAreaView.as_view(), name="createarea"),
]
