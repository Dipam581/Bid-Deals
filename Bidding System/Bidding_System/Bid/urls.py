from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('option/', option_of_trading, name="option_of_trading"),
    path('addBid/', add_product_for_bid, name="add_product_for_bid"),
    path('deals/', show_all_products, name="show_all_products"),
    path('buy_product/<str:product_id>/', buy_product, name="buy_product"),
    path('send_mail/', send_mail_Test, name='send_mail_Test'),
    path('deals/notification/', wishlist, name='wishlist'),
    path('deals/wishlist/<str:product_id>/', added_wishlist, name="added_wishlist"),
]
