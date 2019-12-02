from django.db import models
import datetime

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_text = models.TextField(max_length=100000)
    article_date = models.DateField('date published')
    article_poster = models.URLField(default='')

    def __str__(self):
        return self.article_title

    def year_publications(self):
        today = datetime.datetime.today()
        return self.article_date >= (today - datetime.timedelta(days=365))

    def month_publications(self):
        today = datetime.datetime.today()
        return self.article_date >= (today - datetime.timedelta(days=31))

    def week_publications(self):
        today = datetime.datetime.today()
        d = today.day
        m = today.month
        y = today.year
        now = datetime.date(y, m, d)
        return self.article_date >= (today - datetime.timedelta(days=7))

    def today_publications(self):
        today = datetime.datetime.today()
        print(today)
        d = today.day
        m = today.month
        y = today.year
        now = datetime.date(y, m, d)
        print(now,self.article_date)
        return self.article_date >= (today - datetime.timedelta(days=1))

'''
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=50)
    comment_text = models.TextField(max_length=10000)

    def __str__(self):
        return self.comment_author
'''