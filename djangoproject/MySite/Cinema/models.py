from django.db import models
from django.core.validators import RegexValidator


class user(models.Model):
    unic_user_id=models.CharField(max_length=120)
    username=models.TextField()
    password=models.TextField()
    mail=models.TextField()
    date_of_reg=models.DateTimeField(auto_now_add=True)
    rating_of_user=models.CharField(max_length=120)
    avatarka = models.ImageField(upload_to='image_user/')
    def __str__(self):
        return self.username

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateTimeField()
    rating=models.CharField(max_length=120)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title


# from django.db import models
# import datetime
#
# class Article(models.Model):
#     article_title = models.CharField('title',max_length=100)
#     article_text = models.TextField('text')
#     article_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.article_title
#
#     def recently_published(self):
#         return self.article_date>=(datetime.timezone.now()-datetime.timedelta(days=7))
# class Editor(models.Model):
#     editor_name = models.CharField(max_length=50)
#     editor_surname = models.CharField(max_length = 50)
#     editor_id = models.CharField(max_length = 1000)
#
# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     author_name = models.CharField('author name',max_length=50)
#     comment_text = models.CharField('comment text',max_length=400)
#
#     def __str__(self):
#         return self.author_name
