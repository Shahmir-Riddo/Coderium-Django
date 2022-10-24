from django.db import models
from django import forms
from django.contrin.auth.models import User
# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=30)
    email = models.Charfield(max_length=30)
    username = model.Charfield(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)


class Profile(model.Models):
    user = models.models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.models.TextField()