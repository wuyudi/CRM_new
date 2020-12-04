from django.shortcuts import render
from .models import CartModel, ProductsModel


# 通过request.REQUEST.getlist取到list形式的提交结果
def getresult(request):
    check_box_list = request.REQUEST.getlist("check_box_list")


def shopping_view(request):
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
    print(product)
    context = {"product": product}
    return render(request, "shopping.html", context)


# Create your views here.
