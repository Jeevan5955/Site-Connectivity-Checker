from django.db import models

# Create your models here.


class URLS(models.Model):
    URL = models.CharField(max_length=500)
