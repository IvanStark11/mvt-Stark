from django.db import models

# Create your models here.

from django.utils import timezone

class familia(models.Model):
    name=models.CharField(max_length=128)
    nacimiento=models.DateField()
    age=models.IntegerField()




