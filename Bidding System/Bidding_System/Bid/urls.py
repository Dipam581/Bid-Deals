from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('addBid/', add_product_for_bid, name="add_product_for_bid"),
    
]
