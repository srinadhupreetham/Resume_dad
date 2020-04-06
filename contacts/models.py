from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    message = models.TextField()