
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from Cinema.models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("movielist/", views.movielist, name='movielist'),
    # path("moviesingle/<int:pk>/".views.moviesingle,name='moviesingle'),
    # path("moviesingle/", views.moviesingle, name='moviesingle'), #work
    # path("user/",views.)
    # path('user/', views.user, name='user'),
    path('movie/<int:pk>/',
    DetailView.as_view(model=Articles,
    template_name="Cinema/moviesingle.html")),

    path('user/<int:pk>/',
    DetailView.as_view(model=User,
    template_name="Cinema/userprofile.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
