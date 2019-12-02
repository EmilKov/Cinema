from django.urls import path
from . import views
from . import models
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = 'News'
urlpatterns = [
    path('', views.news, name='news'),
    url(r'^article/list/(?P<page>\d*)', views.article, name='article'),
    path('article/review/<int:article_id>/', views.review, name='review'),
    url(r'^dayarticle/list/(?P<page>\d*)', views.day_article, name='article'),
    url(r'^montharticle/list/(?P<page>\d*)', views.month_article, name='article'),
    url(r'^yeararticle/list/(?P<page>\d*)', views.year_article, name='article'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
