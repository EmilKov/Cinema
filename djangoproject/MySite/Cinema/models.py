from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver
# User.objects.filter(field_name=first_name)
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True, primary_key=True, default=None)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True,)
    objects = models.Manager()
    def delete_user(self):
        self.User.delete()

        # def __str__(self):
        #     return self.user.username
    # def delete(self, *args, **kwargs):
    #     self.user.delete()
    #     return super(self.__class__, self).delete(*args, **kwargs)

# @receiver(post_delete, sender=Profile)
# def post_delete_user(sender, instance, *args, **kwargs):
#     if instance.user: # just in case user is not specified
#         instance.user.delete()
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


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


def get_list_or_404(klass, *args, **kwargs):
    """
    Use filter() to return a list of objects, or raise a Http404 exception if
    the list is empty.
    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the filter() query.
    """
    queryset = _get_queryset(klass)
    if not hasattr(queryset, 'filter'):
        klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError(
            "First argument to get_list_or_404() must be a Model, Manager, or "
            "QuerySet, not '%s'." % klass__name
        )
    obj_list = list(queryset.filter(*args, **kwargs))
    if not obj_list:
        raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
    return obj_list



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
