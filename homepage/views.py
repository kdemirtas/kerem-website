from django.shortcuts import render


posts = [
    {
        'author': 'Kerem',
        'title': 'Example Post',
        'content': 'Example Content',
        'date_posted': 'December 29, 2021'
    },
        {
        'author': 'Jane Doe',
        'title': 'Example Post 2',
        'content': 'Example Content 2',
        'date_posted': 'December 30, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'homepage/home.html', context)

def about_me(request):
    context = {
        'title': 'About Me',
    }
    return render(request, 'homepage/about.html', context)