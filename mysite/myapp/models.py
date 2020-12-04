from django.db import models


class ProductsModel(models.Model):
    number = models.IntegerField()
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=10)
    price = models.IntegerField()


class CartModel(models.Model):
    username = models.CharField(max_length=20)
    number = models.IntegerField(default=1)


# Create your models here.
