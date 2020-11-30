from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('register/',views.register_view),
    path('main/',views.main_view),
]
