from rest_framework import serializers
from .models import Actions, ActionReactionDatas, Reactions, User, UserActReact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "google_access_token",
            "microsoft_access_token",
            "github_access_token",
            "facebook_access_token",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["username"] = validated_data["email"]
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.google_access_token = validated_data.get(
            "google_access_token", instance.google_access_token
        )
        instance.microsoft_access_token = validated_data.get(
            "microsoft_access_token", instance.microsoft_access_token
        )
        instance.twitter_access_token = validated_data.get(
            "twitter_access_token", instance.twitter_access_token
        )
        instance.discord_access_token = validated_data.get(
            "discord_access_token", instance.discord_access_token
        )
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_staff = validated_data.get("is_staff", instance.is_staff)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance


class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ("id", "title", "datas_id", "parameters")

    def create(self, validated_data):
        title = validated_data.pop("title")
        datas_id = validated_data.pop("datas_id")
        parameters = validated_data.pop("parameters")
        action = Actions.objects.create(**validated_data)
        action.title = title
        action.datas_id = datas_id
        action.parameters = parameters
        action.save()
        return action

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.datas_id = validated_data.get("datas_id", instance.datas_id)
        instance.parameters = validated_data.get("parameters", instance.parameters)
        instance.save()
        return instance


class ReactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactions
        fields = ("id", "title", "datas_id", "parameters")

    def create(self, validated_data):
        title = validated_data.pop("title")
        datas_id = validated_data.pop("datas_id")
        parameters = validated_data.pop("parameters")
        action = Actions.objects.create(**validated_data)
        action.title = title
        action.datas_id = datas_id
        action.parameters = parameters
        action.save()
        return action

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.datas_id = validated_data.get("datas_id", instance.datas_id)
        instance.parameters = validated_data.get("parameters", instance.parameters)
        instance.save()
        return instance


class ActionReactionDatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionReactionDatas
        fields = ("id", "title", "service", "description", "type", "parameters")

    def create(self, validated_data):
        service = validated_data.pop("service")
        title = validated_data.pop("title")
        description = validated_data.pop("description")
        type = validated_data.pop("type")
        func = validated_data.pop("parameters")
        datas = ActionReactionDatas.objects.create(**validated_data)
        datas.service = service
        datas.description = description
        datas.type = type
        datas.func = func
        datas.save()
        return datas

    def update(self, instance, validated_data):
        instance.service = validated_data.get("service", instance.service)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.type = validated_data.get("type", instance.type)
        instance.func = validated_data.get("parameters", instance.func)
        instance.save()
        return instance


class UserActReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActReact
        fields = ("id", "user_id", "action_id", "reaction_id", "created_at")

    def create(self, validated_data):
        user_id = validated_data.pop("user_id")
        action_id = validated_data.pop("action_id")
        reaction_id = validated_data.pop("reaction_id")
        created_at = validated_data.pop("created_at")
        useractreact = UserActReact.objects.create(**validated_data)
        useractreact.user_id = user_id
        useractreact.action_id = action_id
        useractreact.reaction_id = reaction_id
        useractreact.created_at = created_at
        useractreact.save()
        return useractreact

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.action_id = validated_data.get("action_id", instance.action_id)
        instance.reaction_id = validated_data.get("reaction_id", instance.reaction_id)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.save()
        return instance
