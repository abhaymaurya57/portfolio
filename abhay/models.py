from django.db import models
# from django.utils import timezone
# import mysql_connector as sql
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    
    phone = models.BigIntegerField()
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20) 

    def __str__(self):
        return self.name