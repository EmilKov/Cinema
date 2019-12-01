from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class VideoEssay(models.Model):
    videoessay_name = models.CharField(max_length=100)
    videoessay_text = models.TextField(max_length=10000)
    videoessay_video = models.URLField(default='')
    videoessay_photo = models.URLField(default='')
    videoessay_date = models.DateField('date published')

    def __str__(self):
        return self.videoessay_name

    def recently_added(self):
        today = datetime.datetime.today()
        print(today)
        d = today.day
        m = today.month
        y = today.year
        now = datetime.date(y, m, d)
        print(now)
        return self.videoessay_date >= (now - datetime.timedelta(days=31))
