from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'homepage/home.html', context)

def about_me(request):
    context = {
        'title': 'About Me',
    }
    return render(request, 'homepage/about.html', context)