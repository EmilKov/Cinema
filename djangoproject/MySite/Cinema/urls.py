
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from Cinema.models import Articles

urlpatterns = [
    path("", views.index, name='index'),
    path("movielist/", views.movielist, name='movielist'),
    # path("moviesingle/<int:pk>/".views.moviesingle,name='moviesingle'),
    # path("moviesingle/", views.moviesingle, name='moviesingle'), #work
    path('<int:pk>/',
    DetailView.as_view(model=Articles,
    template_name="Cinema/moviesingle.html")),
]
