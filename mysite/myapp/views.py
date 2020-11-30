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
    username=request.POST.get("username")
    password=request.POST.get("pass")
    confirm_password=request.POST.get("confirm_pass")
    db_username=LoginModel.objects.filter(username=username)
    if password!=confirm_password:
        error_msg="两次输入密码不一致"
        print("different password")
    else:
        redirect("./")
        # if len(str(username)) < 6:
        #     error_msg = "用户名过短"
        #     print(error_msg)
        # elif db_username:
        #     error_msg = "用户已存在"
        #     print(error_msg)
        # else:
        #     new_user=LoginModel.objects.create()
        #     new_user.username=username
        #     new_user.password=password
        #     new_user.save()
        #     redirect("../")
    return render(request, 'register.html', {})


def main_view(request):
    return render(request, 'main.html', {})

# Create your views here.
