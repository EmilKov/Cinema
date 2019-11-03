from django.shortcuts import render


def main(request):
    return render(request, 'mainApp/main.html')
