from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', initiate_login, name="initiate_login"),
    path('register/', register, name="register"),
]
