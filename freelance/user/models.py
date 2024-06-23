from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    v_code = models.CharField(max_length=500,unique=True)
    v_status = models.CharField(max_length=500)