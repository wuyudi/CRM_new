from django.urls import path
from . import views

urlpatterns = [
    path("shopping/", views.shopping_view),
]
