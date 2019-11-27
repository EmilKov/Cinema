from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver
# class ExampleModel(models.Model):
#     model_pic = models.ImageField(upload_to = 'profile_image2')

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    # description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    # website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_user_profile, sender=User)
class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=10)
    genres = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    poster = models.URLField(default='')
    plot = models.CharField(max_length=500)
    trailer = models.URLField(default='')

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'

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
