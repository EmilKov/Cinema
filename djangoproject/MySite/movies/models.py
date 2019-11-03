from django.db import models


class Movie(models.Model):

    movie_title = models.CharField('title', max_length=40)
    movie_release_date = models.DateField(null=True, blank=True)
    movie_genre = models.CharField('genre', max_length=20)
    movie_plot = models.TextField('plot', max_length=5000)
    #movie_poster = models.ImageField(upload_to='static/img', blank = True, null = True)

    def __str__(self):
        return self.movie_title


class Critique(models.Model):

    critique_author = models.CharField('author', max_length=40)
    critique_text = models.TextField('text', max_length=10000)

    def __str__(self):
        return self.critique_author
