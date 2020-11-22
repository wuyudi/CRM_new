from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<p>hello world</p>")


def login_view(request):
    return HttpResponse("login page")
# Create your views here.
