from django.db import models


class LoginModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class ProductsModel(models.Model):
    number = models.IntegerField()
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20,blank=True)
    type = models.CharField(max_length=10)
    price = models.IntegerField()


class CartModel(models.Model):
    username = models.CharField(max_length=20)
    number = models.IntegerField()

# Create your models here.
