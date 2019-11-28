from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.shortcuts import render, redirect
from . import *
import math
from math import *
from django.apps import apps
from .models import Movie


def whole_list(request, model, page):
    if page == '':
        page = 1
    page = int(page)
    objects = model.objects.all()


    total_page = int(math.ceil(len(objects) / 10))
        # if page > total_page:
        #     return render(request, 'Cinema/404.html')
    last_item_index = 10 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, 'Cinema/{}list2.html'.format(model.get_name()), data)

def get_rec(request,model,page):
    if page == '':
        page = 1
    page = int(page)
    objects = model.objects.all()

    # MovieModel = apps.get_model('Cinema', 'Movie')
    # genre = Movie.genres
    # rating = Movie.rate

    total_page = int(ceil(len(objects) / 1000))
    if page > total_page:
        return render(request, 'Cinema/error404.html')
    last_item_index = 500 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request,'Cinema/oh ma3.html',data)


def get_suggests(request, model, page):
    if page == '':
        page = 1
    page = int(page)
    objects = model.objects.all()

    # MovieModel = apps.get_model('Cinema', 'Movie')
    # genre = Movie.genres
    # rating = Movie.rate

    total_page = int(ceil(len(objects) / 1001))
    if page > total_page:
        return render(request, 'Cinema/error404.html')
    last_item_index = 500 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, 'Cinema/oh ma.html', data)

def index(request):
    return render(request,'Cinema/index.html')
def movielist(request):
    return render(request,'Cinema/movielist1.html')
def moviesingle(request):
    return render(request,'Cinema/moviesingle.html')
def user(request):
    return render(request,'registration/userprofile.html')
# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = Profile.objects.get(pk=course_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

#
#
class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "registration/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class TemplateView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
