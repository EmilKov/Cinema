from django.urls import path
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = 'Video'
urlpatterns = [
    path('', views.videos, name='videos'),
    url(r'^new/(?P<page>\d*)', views.new_videos, name='new_videos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
