from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LoginModel


def hello(request):
    return HttpResponse("<p>hello world</p>")


def login_view(request):
    username = request.POST.get("username")
    error_msg = ''
    if len(str(username)) < 6:
        error_msg = 'Too short username\n用户名过短，请重新输入'
    data = LoginModel.objects.filter(username=username)
    if data:
        for item in data:
            db_password = item.password
        if db_password == request.POST.get("pass"):
            print("login success")
            return redirect("/main")
        else:
            print("wrong password")
    else:
        print("user not exist")
    context = {
        "error_msg": error_msg,
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'login.html', context)


def register_view(request):
    return render(request, 'register.html', {})


def main_view(request):
    return render(request, 'main.html', {})

# Create your views here.
