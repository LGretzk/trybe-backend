from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AuthUser(models.Model): 
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class Goal(models.Model):
    goal_description = models.CharField(max_length=180)
    owner = models.ForeignKey(AuthUser, related_name='goals', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.goal_description

    class Meta:
        ordering = ['created_at']


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class InvitedSupporter(models.Model):
    goal_id = models.ForeignKey(Goal, related_name='invited_supporters', on_delete=models.CASCADE)
    supporter_email = models.CharField(max_length=250)
    

class AcceptedSupporter(models.Model):
    goal_id = models.ForeignKey(Goal, related_name='accepted_supporters', on_delete=models.CASCADE)
    supporter_email = models.CharField(max_length=250)
    supporter_id = models.ForeignKey(AuthUser, related_name='accepted_supporters', on_delete=models.CASCADE)
