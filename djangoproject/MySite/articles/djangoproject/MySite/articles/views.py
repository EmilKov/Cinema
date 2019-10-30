from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'articles/text.html')
def test(request):
    return HttpResponse('Testing this web page. ;D')
