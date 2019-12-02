
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import *
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
    path("error404/", views.error404, name='error404'),
    path("moviesingle/<slug:movie_id>/", views.moviesingle, name='moviesingle'), #work
    # path("user/",views.)
    path('user/', views.user, name='user'),
    path('user/changepass/', views.changepass, name='changepass'),
    path('landing/', views.landing, name='landing'),
    path('/movie_c/<str:movieid>/', views.post_single, name='Comment_movie'),
    # url(r'^(?P<movieid>[0-9]+)/', views.EArticleView.as_view(), name='movieid'),
    # path('<str:movieid>/', views.EArticleView.as_view(), name='Comment_movie'),
    # url(r'^comment/(?P<article_id>[0-9]+)/$', views.add_comment, name='add_comment')
    # url(r'^(?P<slug>[-\w]+)/$', views.full_slug, name='full_slug'), # Вывод новостей
    # url(r'^addcomment/(?P<one_id>\d+)/$', views.addcomment), # Добавление коммента
    path('landing/', views.landing, name='landing'),
    # path('movie/<int:pk>/',DetailView.as_view(model=Movie,template_name="Cinema/moviesingle.html")),
    url(r'^movie_all/(?P<page>\d*)', views.whole_list, {'model': models.Movie}, name='whole_list'),
    path('register/',views.RegisterFormView.as_view(),name='signup'),
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', TemplateView.as_view(template_name="logins/index.html")),
    path('search/', views.search, name='search'),
    path('schedule/almaty', views.kinoparkalmaty, name='kinopark'),
    path('schedule/', views.schedule, name='kinopark'),
    path('schedule/astana', views.kinoparkastana, name='kinopark'),
    path('schedule/shymkent', views.kinoparkshymkent, name='kinopark'),
    path('schedule/aktobe', views.kinoparkaktobe, name='kinopark'),
    # path('moviegrid/', views.moviegrid, name='moviegrid'),
    url(r'^moviegrid/(?P<page>\d*)', views.whole_list_grid, {'model': models.Movie}, name='whole_list_grid'),
    url(r'^recommendations/(?P<page>\d*)', views.get_suggests, {'model': models.Movie}, name='get_suggests'),
    url(r'^recommendation/decade/(?P<page>\d*)', views.get_rec, {'model': models.Movie}, name='get_rec'),
    url(r'^worstfilms/(?P<page>\d*)', views.get_worstfilms, {'model': models.Movie}, name='get_worstfilms'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
