from django.db import models

class Title (models.Model):
    title = models.CharField(max_length=50)
