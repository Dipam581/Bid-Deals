from django.shortcuts import render
import random
from .models import creationData


def option_of_trading(request):
    return render(request, 'option.html')


def add_product_for_bid(request):
    context = request.session.get('context', {})
    print(context["uuid"])
    if request.method == "POST":
        item_name = request.POST.get("item")
        item_description = request.POST.get("description")
        item_amount = request.POST.get("amount")
        file = request._files['file']
        bidData = creationData(owner_id= context["uuid"], name= item_name, price= item_amount, description= item_description, image = file)
        bidData.save()
    
    owner_data = {}
    if (len(creationData.objects.filter(owner_id= context["uuid"]))):
        owner_data = creationData.objects.filter(owner_id= context["uuid"])
        print("--> ",owner_data)

    return render(request, 'bid_creation.html', {'userContext': context["fullName"], 'ownerData': owner_data})


#Show all products
def show_all_products(request):
    listed_obj = creationData.objects.all()

    return render(request, 'all_products.html',{"listed_obj": listed_obj})