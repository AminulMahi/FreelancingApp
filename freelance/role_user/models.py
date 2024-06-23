from django.db import models

# Create your models here.

class User_info(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    services = models.CharField(max_length=100, null=True)
