from django.contrib.auth.models import AbstractUser
from django.db import models
from my_project.contact_manager.models import .


# Create your models here.

class MpakaUser(AbstractUser):
     username = models.CharField(max_length=100, unique=True)
     email = models.EmailField(unique=True)
     password = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     app_label = 'contact_manager'

class MpakaContact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    user = models.ForeignKey(MpakaUser, on_delete=models.CASCADE, related_name='mpakacontacts')

class MpakaGroup(models.Model):
    name = models.CharField(max_length=100)
    mpakacontacts = models.ManyToManyField(MpakaContact, related_name='mpakagroups')
