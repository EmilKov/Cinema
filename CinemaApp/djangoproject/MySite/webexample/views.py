from django.shortcuts import render
from django.http import HttpResponse

def indexA(request):
    return HttpResponse('<h3>Hello World!!!!!!!!!!!!!!1</h3>')