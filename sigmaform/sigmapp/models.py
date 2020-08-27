from django.db import models

# Create your models here.

class SingIn(models.Model):
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

