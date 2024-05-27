from django.db import models

# Create your models here.
class SomeObject(models.Model):
    Data = models.CharField(max_length=256)
    Created = models.DateTimeField(null=True)
    Modified = models.DateTimeField(null=True)