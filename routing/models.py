from django.db import models
# Create your models here.
class Gateway(models.Model):
    name=models.CharField(max_length=20,unique=True)
    ip_addresses=models.CharField(max_length=200,unique=True)
class Route(models.Model):
    prefixes=models.IntegerField(max_length=4,unique=True)
    gateway_id=models.IntegerField()

