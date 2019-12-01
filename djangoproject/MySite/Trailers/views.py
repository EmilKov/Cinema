from django.shortcuts import render
from math import *
from .models import *
# Create your views here.


def trailers(request):
    return render(request,'Trailer/trailers.html')


def alltrailers(request, page, model):
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
    return render(request,'Trailer/alltrailers.html',data)


def newtrailers(request, page, model):
    if page == '':
        page = 1
    else:
        page = int(page)
    objects = Trailer.objects.order_by('-trailer_date')[:10]

    total_page = int(ceil(len(objects) / 1001))
    if page > total_page:
        return render(request, 'Cinema/404.html')
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects, 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request,'Trailer/newtrailers.html', data)
