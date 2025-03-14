from django.db import models
# from django.utils import timezone
# import mysql_connector as sql


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
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True) 

    def __str__(self):
        return self.name