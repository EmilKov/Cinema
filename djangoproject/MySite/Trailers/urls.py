from django.urls import path
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.trailers, name = 'trailers'),
    url(r'^all/(?P<page>\d*)', views.alltrailers, {'model': models.Trailer}, name='alltrailers'),
    url(r'^new/(?P<page>\d*)', views.newtrailers, {'model': models.Trailer}, name='newtrailers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
