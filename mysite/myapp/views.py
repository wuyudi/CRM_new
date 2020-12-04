from django.shortcuts import render
from .models import CartModel, ProductsModel
from django.http import HttpRequest

# 通过request.REQUEST.getlist取到list形式的提交结果
def getresult(request: HttpRequest):

    print(check_box_list)
    return


def shopping_view(request: HttpRequest):
    check_box_list = request.POST.getlist("check_box_list")
    print(check_box_list)
    cart_data = CartModel.objects.filter()
    cart_products = [item.number for item in cart_data]
    add_number = request.POST.get("add_number")
    if add_number is not None:
        cart_info = CartModel.objects.filter(number=add_number)
        if not cart_info:
            new_record = CartModel.objects.create()
            new_record.number = add_number
            new_record.save()
    product_data_all = ProductsModel.objects.filter()
    product = []
    for item in product_data_all:
        product.append([item.number, item.brand, item.name, item.type, item.price])
    context = {"product": product}
    return render(request, "shopping.html", context)


# Create your views here.
