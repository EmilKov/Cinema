from django.db import models
import datetime

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_text = models.TextField(max_length=100000)
    article_date = models.DateTimeField('date published')
    article_poster = models.URLField(default='')

    def __str__(self):
        return self.article_title

    def last_publications(self):
        if self.article_date >= (datetime.timezone.now() - datetime.timedelta(days=7)):
            return self.article_date
