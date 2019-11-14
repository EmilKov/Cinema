
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from Cinema.models import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
    DetailView.as_view(model=user,
    template_name="Cinema/userprofile.html")),
    # path('register/', views.register,name='register'),
    # path('login/', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('account/', include('django.contrib.auth.urls')),
    path('register/',views.RegisterFormView.as_view()),
    path('login/',views.LoginFormView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
