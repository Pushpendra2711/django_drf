from django.db import models

# Create your models here.

class NormalModel(models.Model):
    user_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True)
    