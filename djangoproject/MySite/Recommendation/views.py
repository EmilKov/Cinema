from django.shortcuts import render
from math import *


# Create your views here.
def get_recommendation(request):
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAA\n\nAAAAAAAAAAAA\nAAAAAAAAAAAAA\nAAAAAAAAAAAAAA')
    return render(request,'Cinema/recommendations.html')


def get_suggests(request, model, page):
    # if page is None:
    #     return render(request, 'Cinema/404.html')
    page = int(page)
    objects = model.objects.all()


    total_page = int(ceil(len(objects) / 10))
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
    return render(request, 'Cinema/{}_list.html'.format(model.get_name()), data)