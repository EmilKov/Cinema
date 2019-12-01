from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import *
from math import *


def search(request):
    try:
        if request.method == "POST":
            article_text = request.POST.get("search_field")
            if len(article_text) > 0:
                search_res = Movie.objects.filter(plot__contains=article_text)

                # print(search_res)
                # return render(request, "Cinema/movielist2.html",
                #               {"search_res": search_res, "empty_res": "There is no article"})

                # print(search_res,article_text)
                return render(request, "Cinema/search.html",
                              {"search_res": search_res, "empty_res": "There is no article",
                               'article_text': article_text})

            elif len(article_text)==0:
                return render(request, 'Cinema/index.html')

    except:
        print("Salam")
        return render(request, "Cinema/search.html", {"empty_res": "There is no article"},)

def whole_list(request, model, page):
    if page == '':
        page = 1
    # if page :
    #     return render(request, 'Cinema/404.html')
    page = int(page)
    objects = model.objects.all()

    total_page = int(ceil(len(objects) / 10))
    if page > total_page:
        return render(request, 'Cinema/error404.html')
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
def whole_list_grid(request, model, page):
    if page == '':
        page = 1
    # if page :
    #     return render(request, 'Cinema/404.html')
    page = int(page)
    objects = model.objects.all()


    total_page = int(ceil(len(objects) / 12))
    if page > total_page:
        return render(request, 'Cinema/error404.html')
    last_item_index = 24 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[24 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, 'Cinema/{}grid.html'.format(model.get_name()), data)

def get_suggests(request, model, page):
    if page == '':
        page = 1
    page = int(page)
    objects = model.objects.all()

    total_page = int(ceil(len(objects) / 1001))
    if page > total_page:
        return render(request, 'Cinema/404.html')
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


def get_rec(request, model, page):
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

def get_worstfilms(request,model,page):
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
    return render(request, 'Cinema/oh ma2.html', data)

def index(request):
    return render(request, 'Cinema/index.html')
def error404(request):
    return render(request, 'Cinema/error404.html')
def moviegrid(request):
    return render(request, 'Cinema/moviegrid.html')


def movielist(request):
    return render(request, 'Cinema/movielist1.html')


def moviesingle(request, movie_id):
    movie_list = Movie.objects.get(pk=movie_id)
    return render(request, 'Cinema/moviesingle1.html', {'movie_list': movie_list})

def kinoparkalmaty(request):
    movie_theatre = ['KINOPARK 5 Atakent','KINOPARK 6 Sputnik','KINOPARK 8 Moskva',
                     'KINOPARK 11 IMAX Esentai','KINOPARK 16 Forum',]

    movie_theatre_name = {}
    movie_theatre_id = ['163','72','149','99','167']
    for j in range(len(movie_theatre)):
        movie_theatre_name.update({movie_theatre[j]: movie_theatre_id[j]})

    movie_theatre_info = [{'name':'KINOPARK 5 Atakent','address':'г. Алматы, Atakent Mall, ул. Тимирязева 42','phone_number':'+7 702 481 18 90',
                           'photo':'http://www.kinopark.kz/storage/app/uploads/public/5cf/4c3/be5/5cf4c3be54dd1967595125.jpg',
                           'url':'https://kino.kz/cinema/163'},

                          {'name':'KINOPARK 6 Sputnik', 'address': 'г. Алматы, мкр. Мамыр-1, 8А, ТРК "Спутник", 3 этаж', 'phone_number': '8 (701) 767-46-03',
                           'photo':'https://s.kino.kz/gallery/cinema/72/p223x267.jpg',
                           'url': 'https://kino.kz/cinema/72'},

                          {'name':'KINOPARK 8 Moskva', 'address': 'г. Алматы, пр. Абая, уг. пр. Алтынсарина, ТРЦ MOSKVA Metropolitan', 'phone_number': '+7 778 099 09 17',
                           'photo':'http://www.kinopark.kz/storage/app/uploads/public/5b0/3ee/d53/5b03eed530f25658777945.jpg',
                           'url':'https://kino.kz/cinema/149'},

                          {'name':'KINOPARK 11 IMAX Esentai', 'address': 'г. Алматы, Esentai Mall, 4 этаж, пр. Аль-Фараби, 77/8', 'phone_number': '+7 701 762 45 11',
                           'photo':'http://www.kinopark.kz/storage/app/uploads/public/5a1/fa6/694/5a1fa66943e9d114540849.jpg',
                           'url':'https://kino.kz/cinema/99'},

                          {'name':'KINOPARK 16 Forum', 'address': 'г. Алматы, пр. Сейфуллина 617, 5 этаж', 'phone_number': '+7 705 208 9595',
                           'photo':'http://www.kinopark.kz/storage/app/uploads/public/5d9/33a/574/5d933a5740dbf291927498.jpg',
                           'url':'https://kino.kz/cinema/167'},
                          ]

    data = {}
    if len(movie_theatre_info) == len(movie_theatre):
        for i in range(len(movie_theatre)):
            data.update({movie_theatre_id[i]: movie_theatre_info[i]})
    print(data)
    newdata = {}
    newdata.update({'id':data})
    print('\n\n\n\n',newdata,'\n\n\n\n\n')
    return render(request, 'Cinema/kinopark.html', data)


def schedule(request):
    return render(request,'Cinema/schedule.html')


def kinoparkastana(request):
    movie_theatre = ['KINOPARK 6 Keruencity', 'KINOPARK 7 IMAX Keruen', 'KINOPARK 9 Saryarqa']
    movie_theatre_id = ['62', '71', '63']

    movie_theatre_info = [
        {'name':'KINOPARK 6 Keruencity','address': 'ТРЦ «KeruenCity Астана»,3 этаж,г.Нур-Султан,Коргальджинское шоссе,1',
         'phone_number': '+7 (701) 870-70-01', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5a1/406/e54/5a1406e5460d3275085249.jpg',
         'url': 'https://kino.kz/cinema/62'},

        {'name': 'KINOPARK 7 IMAX Keruen', 'address': 'ТРЦ «Keruen», 4 этаж, г. Нур-Cултан, ул. Достык, 9',
         'phone_number': '+7 (701) 870-70-02', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5b0/3ef/58b/5b03ef58be00a676602909.jpg',
         'url': 'https://kino.kz/cinema/71'},

        {'name': 'KINOPARK 9 Saryarqa', 'address': 'ТРЦ «Saryarqa», 3 этаж, г. Нур-Султан, ул. Туран, 24',
         'phone_number': ' +7 (701) 555-73-70', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5b0/3ee/6a7/5b03ee6a7410a906012682.jpg',
         'url': 'https://kino.kz/cinema/63'},

    ]
    data = {}
    if len(movie_theatre_info) == len(movie_theatre):
        for i in range(len(movie_theatre)):
            data.update({movie_theatre_id[i]: movie_theatre_info[i]})
    print(data)
    return render(request, 'Cinema/kinoparkastana.html', data)


def kinoparkshymkent(request):
    movie_theatre = ['KINOPARK 5 Mega Planet', 'KINOPARK 5 Hyper House', 'KINOPARK 4 Nauryz Park']
    movie_theatre_info = [
        {'name': 'KINOPARK 5 Mega Planet', 'address': 'ТРЦ «Mega Planet», 3 этаж, г. Шымкент, проспект Тауке-Хана',
         'phone_number': '+7 (725) 2301-335', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5a1/406/d1c/5a1406d1c4847291623922.jpg',
         'url': 'https://kino.kz/cinema/61'},

        {'name': 'KINOPARK 5 Hyper House', 'address': 'ТРЦ «Hyper House», 3-й этаж, г. Шымкент, ул. Дулати, 200А',
         'phone_number': '+7 (775) 406 6884', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5cc/d35/3b6/5ccd353b62f15572833181.jpg',
         'url': 'https://kino.kz/cinema/161'},

        {'name': 'KINOPARK 4 Nauryz Park', 'address': 'г. Шымкент, пр. Байдибек Би 25, 2 этаж',
         'phone_number': '+7 778 636 7741', 'photo': 'http://www.kinopark.kz/storage/app/uploads/public/5d9/1ee/7f5/5d91ee7f5760e541227844.jpg',
         'url': 'https://kino.kz/cinema/170'},

    ]
    movie_theatre_id = ['61', '161', '170']

    data = {}
    if len(movie_theatre_info) == len(movie_theatre):
        for i in range(len(movie_theatre_info)):
            data.update({movie_theatre_id[i]:movie_theatre_info[i]})
    return render(request, 'Cinema/kinoparkshymkent.html', data)


def kinoparkaktobe(request):
    movie_theatre = ['KINOPARK 7 Keruencity Aktobe']
    movie_theatre_info = [
        {'name': 'KINOPARK 7 Keruencity Aktobe', 'address': 'г. Актобе, ул М. Маметовой 4, ТРЦ "Mega-Aktobe", 3-й этаж',
         'phone_number': '+7 701 767 46 02', 'photo': 'https://s.kino.kz/gallery/cinema/73/p223x267.jpg',
         'url': 'https://kino.kz/cinema/73'},
    ]
    movie_theatre_id = ['73']
    data = {}
    if len(movie_theatre) == len(movie_theatre_info):
        for i in range(len(movie_theatre)):
            data.update({movie_theatre_id[i]: movie_theatre_info[i]})
    return render(request,'Cinema/kinoparkaktobe.html', data)


def user(request):
    return render(request, 'registration/userprofile.html')

def changepass(request):
    return render(request, 'registration/changepass.html')
def landing(request):
    return render(request, 'Cinema/landing.html')
def comingsoon(request):
    return render(request, 'Cinema/comingsoon.html')
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
    success_url = "/"
    template_name = "registration/register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class TemplateView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
