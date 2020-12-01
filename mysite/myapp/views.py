from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoginModel


def login_view(request):
    username = request.POST.get("username")
    error_msg = ""
    if len(str(username)) < 6:
        error_msg = "Too short username\n用户名过短，请重新输入"
    data = LoginModel.objects.filter(username=username)
    if data:
        for item in data:
            db_password = item.password
        if db_password == request.POST.get("pass"):
            print("login success")
            request.session["username"]=username
            return redirect("/shopping")
        else:
            print("wrong password")
    else:
        print("user not exist")
    context = {
        "error_msg": error_msg,
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "login.html", context)


def register_view(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    confirm_password = request.POST.get("confirm_pass")
    db_username = LoginModel.objects.filter(username=username)
    if password != confirm_password:
        error_msg = "两次输入密码不一致"
        print("different password")
    else:
        if len(str(username)) < 6:
            error_msg = "用户名过短"
            print(error_msg)
        elif db_username:
            error_msg = "用户已存在"
            print(error_msg)
        else:
            new_user=LoginModel.objects.create()
            new_user.username=username
            new_user.password=password
            new_user.save()
            error_msg = "注册成功"
    context={
        "error_msg": error_msg,
    }
    return render(request, 'register.html',context)


def shopping_view(request):
    username=request.session["username"]
    context={
        "username":username
    }
    return render(request, "shopping.html", context)


# Create your views here.