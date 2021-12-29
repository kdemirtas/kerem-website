from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')

def about_me(request):
    return render(request, 'homepage/about.html')