from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Trailer(models.Model):
    trailer_name = models.CharField(max_length=50)
    trailer_text = models.TextField(max_length=10000)
    trailer_url = models.URLField(default='')
    trailer_date = models.DateField('date published')
    trailer_photo = models.URLField(default='')

    def __str__(self):
        return self.trailer_name

    def recently_added(self):
        return self.trailer_date >= (timezone.now() - datetime.timedelta(days=7))
