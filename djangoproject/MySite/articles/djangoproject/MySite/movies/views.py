from django.shortcuts import render
from django.http import HttpResponse
def moviesview(request):
    return HttpResponse('Cool movie. ;D')
def tester(request):
    return HttpResponse('Tester ;D.\nSuccessfully\n;D\n;D\n;D')