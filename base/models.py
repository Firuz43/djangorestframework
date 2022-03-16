from django.db import models
from django.forms import DateTimeField

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
