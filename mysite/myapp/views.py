from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoginModel, CartModel, ProductsModel


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
            request.session["username"] = username
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
            new_user = LoginModel.objects.create()
            new_user.username = username
            new_user.password = password
            new_user.save()
            error_msg = "注册成功"
    context = {
        "error_msg": error_msg,
    }
    return render(request, 'register.html', context)


def shopping_view(request):
    username = request.session["username"]
    cart_products = []
    cart_data = CartModel.objects.filter(username=username)
    for item in cart_data:
        cart_products.append(item.number)
    print(cart_products)
    max_price_diff = 0

    def close_degree(type1, type2, price1, price2):
        if type1 == "轻薄本":
            type1_num = 0
        elif type1 == "全能本":
            type1_num = 0.5
        elif type1 == "游戏本":
            type1_num = 1
        if type2 == "轻薄本":
            type2_num = 0
        elif type2 == "全能本":
            type2_num = 0.5
        elif type2 == "游戏本":
            type2_num = 1
        return (type1_num - type2_num) * (type1_num - type2_num) + (abs(price1 - price2) / max_price_diff) * (
                abs(price1 - price2) / max_price_diff)

    index = 1
    other_products = []
    max_price = 0
    min_price = -1
    while 1:
        product_info = ProductsModel.objects.filter(number=index)
        if product_info:
            for item in product_info:
                if item.price > max_price:
                    max_price = item.price
                if min_price == -1:
                    min_price = item.price
                elif item.price < min_price:
                    min_price = item.price
            if index not in cart_products:
                temp_list = []
                for item in product_info:
                    temp_list.append(index)
                    temp_list.append(item.brand)
                    temp_list.append(item.type)
                    temp_list.append(item.price)
                other_products.append(temp_list)
            index += 1
        else:
            break
    index = 1
    min_close_degree = 2.0
    max_price_diff = max_price - min_price
    for item in other_products:
        for i in cart_products:
            product_info = ProductsModel.objects.filter(number=i)
            for item0 in product_info:
                type_2 = item0.type
                price_2 = item0.price
            if close_degree(item[2], type_2, item[3], price_2) < min_close_degree:
                min_close_degree = close_degree(item[2], type_2, item[3], price_2)
                index = item[0]
    print(max_price_diff, index)

    add_number=request.POST.get("add")
    print(add_number)
    context = {
        "username": username,
        "cart_products": cart_products,
        "index": index
    }
    return render(request, "shopping.html", context)

# Create your views here.
