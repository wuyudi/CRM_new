from django.shortcuts import render, redirect
from .models import LoginModel, CartModel, ProductsModel


def shopping_view(request):
    username = request.session["username"]
    cart_data = CartModel.objects.filter(username=username)
    cart_products = [item.number for item in cart_data]
    print(cart_products)

    add_number = request.POST.get("add_number")
    print(add_number)
    if add_number is not None:
        cart_info = CartModel.objects.filter(username=username, number=add_number)
        if not cart_info:
            new_record = CartModel.objects.create()
            new_record.username = username
            new_record.number = add_number
            new_record.save()
            print("save success")
    product_data_all = ProductsModel.objects.filter()
    product = []
    for item in product_data_all:
        product.append([item.number, item.brand, item.name, item.type, item.price])
    print(product)
    context = {"username": username, "index": index, "product": product}
    return render(request, "shopping.html", context)


# Create your views here.
