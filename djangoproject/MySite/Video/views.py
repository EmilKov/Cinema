from django.shortcuts import render
from .models import *
from math import *
# Create your views here.


def new_videos(request, page):
    objects = VideoEssay.objects.order_by('-videoessay_date')[:7]
    if page == '':
        page = 1
    else:
        page = int(page)

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

    data = {'items': objects, 'current_page': page, 'page_number': total_page,
            'pages': pages}

    return render(request, 'Videos/new_video_essay.html', data)

def videos(request):
    objects = VideoEssay.objects.order_by('-videoessay_date')[:10]
    page = 1
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

    data = {'items': objects, 'current_page': page, 'page_number': total_page,
            'pages': pages}

    return render(request, 'Videos/video_essay.html', data)