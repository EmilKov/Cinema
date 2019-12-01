from django.urls import path
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.news, name='news'),
    url(r'^article/(?P<page>\d*)', views.article, {'model': models.Article}, name='article'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
