from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('option/', option_of_trading, name="option_of_trading"),
    path('addBid/', add_product_for_bid, name="add_product_for_bid"),
    path('deals/', show_all_products, name="show_all_products"),
    
]
