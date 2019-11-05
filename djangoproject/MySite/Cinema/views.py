from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Cinema/index.html')
def movielist(request):
    return render(request,'Cinema/movielist1.html')
def moviesingle(request):
    images = Images.objects.all().order_by('-id')
    return render(request,'Cinema/moviesingle.html')
