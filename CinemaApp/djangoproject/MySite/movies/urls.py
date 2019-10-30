from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .models import Movie

urlpatterns = [
    path('', views.moviesview, name='moviesview'),
    path('tester/',views.tester,name='tester')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)