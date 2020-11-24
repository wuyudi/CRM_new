from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<p>hello world</p>")


def login_view(request):
    return render(request, 'login.html', {})


def register_view(request):
    return render(request, 'register.html', {})


def main_view(request):
    return render(request, 'main.html', {})

# Create your views here.
