from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateTimeField()
    rating=models.CharField(max_length=120)
    def __str__(self):
        return self.title
