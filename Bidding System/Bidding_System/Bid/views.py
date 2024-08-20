from django.shortcuts import render, get_object_or_404, redirect
import random
from .models import creationData, BuyModel
from .utils import send_mail
from Login.models import CustomUser
from django.contrib.auth.models import User

def option_of_trading(request):
    return render(request, 'option.html')


def send_mail_Test(request):
    send_mail()
    return redirect("/option")

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

    
# process to buy
def buy_product(request, product_id):
    if request.method == "POST":
        context = request.session.get('context', {})
        productDetails = creationData.objects.filter(product_id = product_id)
        owner_id = productDetails[0].owner_id
        current_price = productDetails[0].price
        updated_price = request.POST.get("updatedPrice")
        print(owner_id," ", current_price, " ", updated_price)
        # buyModel = BuyModel(owner_id = str(owner_id), bider_id = context["uuid"], original_price = current_price, updated_price = updated_price)
        # buyModel.save()

        owner_mail = CustomUser.objects.filter(unique_key=owner_id)[0]
        name = User.objects.get(username= owner_mail).first_name
        msg = f"Hi {name}, You have a sell request from a buyer. Please visit TradeSquare."

        send_mail(msg, owner_mail)


    product = creationData.objects.filter(product_id=product_id)
    context = request.session.get('context', {})
    userContext = {
        "email": context["email"]
    }
    return render(request,"buy_screen.html", {"selectedData": product, "userContext": userContext})