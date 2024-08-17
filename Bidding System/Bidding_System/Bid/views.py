from django.shortcuts import render
import random
from .models import creationData


def add_product_for_bid(request):
    if request.method == "POST":
        item_name = request.POST.get("item")
        item_description = request.POST.get("description")
        item_amount = request.POST.get("amount")
        file = request._files['file']
        bidData = creationData(owner_id= random.random(),name= item_name,price= item_amount,description= item_description, image = file)
        bidData.save()
        
        # return render(request, 'bid_creation.html')
    return render(request, 'bid_creation.html')