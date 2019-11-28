from . import views
from Cinema.models import *
from django.conf.urls import url
from . import models
from django.apps import apps

MovieModel = apps.get_model('Cinema','Movie')

urlpatterns = [
    url(r'^recommendations/(?P<page>\d*)', views.get_recommendation, {'model': models.Movie}, name='get_recommendation'),
    # path("", views.get_recommendation),
]