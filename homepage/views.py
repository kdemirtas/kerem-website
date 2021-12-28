from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the home index.")

def about_me(request):
    return HttpResponse("<h1>About Me</h1>")