# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
import django.core.validators
from django.db import models
from django.utils import timezone


class ActionReactionDatas(models.Model):
    title = models.CharField(max_length=255, default="")
    service = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        default="action",
        validators=[
            django.core.validators.RegexValidator(
                regex="^(action|reaction)$",
                message="Type must be action or reaction",
                code="invalid_type",
            )
        ],
    )
    parameters = models.CharField(max_length=255, default="")

    class Meta:
        managed = True
        db_table = "action_reaction_datas"


class Actions(models.Model):
    title = models.CharField(max_length=255, default="")
    datas = models.ForeignKey(ActionReactionDatas, models.DO_NOTHING)
    parameters = models.JSONField(default=dict)

    class Meta:
        managed = True
        db_table = "actions"


class Reactions(models.Model):
    title = models.CharField(max_length=255, default="")
    datas = models.ForeignKey(ActionReactionDatas, models.DO_NOTHING)
    parameters = models.JSONField(default=dict)

    class Meta:
        managed = True
        db_table = "reactions"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    google_access_token = models.TextField(blank=True, null=True)
    microsoft_access_token = models.TextField(blank=True, null=True)
    github_access_token = models.TextField(blank=True, null=True)
    facebook_access_token = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "password",
        "first_name",
        "last_name",
        "created_at",
        "updated_at",
    ]

    class Meta:
        managed = True
        db_table = "users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserActReact(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    action = models.ForeignKey(Actions, models.DO_NOTHING, blank=True, null=True)
    reaction = models.ForeignKey(Reactions, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = "user_act_react"
