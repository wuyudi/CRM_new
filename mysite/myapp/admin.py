from django.contrib import admin
from . import models

admin.site.register(models.ProductsModel)
admin.site.register(models.CartModel)
# Register your models here.
