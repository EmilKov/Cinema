
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from Cinema.models import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

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

    path('user/',
    DetailView.as_view(model=user,
    template_name="Cinema/userprofile.html")),
    # path('register/', views.register,name='register'),
    # path('login/', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('account/', include('django.contrib.auth.urls')),
    path('register/',views.RegisterFormView.as_view(),name='signup'),
    path('login/',views.LoginFormView.as_view(),name='login'),
    # path('logout/',views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # path('logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='user_logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sl/', TemplateView.as_view(template_name="logins/index.html")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
