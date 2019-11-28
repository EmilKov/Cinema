
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from Cinema.models import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import models
from django.conf.urls import url
urlpatterns = [
    # path("upload_pic/", views.upload_pic, name='upload_pic'),
    path("", views.index, name='index'),
    path("movielist/", views.movielist, name='movielist'),
    # path("moviesingle/<int:pk>/".views.moviesingle,name='moviesingle'),
    path("moviesingle/<slug:movie_id>/", views.moviesingle, name='moviesingle'), #work
    # path("user/",views.)
    path('user/', views.user, name='user'),
    path('movie/<int:pk>/',
    DetailView.as_view(model=Movie,
    template_name="Cinema/moviesingle.html")),
    url(r'^movie_all/(?P<page>\d*)', views.whole_list, {'model': models.Movie}, name='whole_list'),
    path('register/',views.RegisterFormView.as_view(),name='signup'),
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', TemplateView.as_view(template_name="logins/index.html")),
    path('search/', views.search, name='search'),
    path('news/', views.news, name='news'),
    # path('moviegrid/', views.moviegrid, name='moviegrid'),
    url(r'^moviegrid/(?P<page>\d*)', views.whole_list_grid, {'model': models.Movie}, name='whole_list_grid'),
    url(r'^recommendations/(?P<page>\d*)', views.get_suggests, {'model': models.Movie}, name='get_suggests'),
    url(r'^recommendation/decade/(?P<page>\d*)', views.get_rec, {'model': models.Movie}, name='get_rec'),
    url(r'^worstfilms/(?P<page>\d*)', views.get_worstfilms, {'model': models.Movie}, name='get_worstfilms'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
