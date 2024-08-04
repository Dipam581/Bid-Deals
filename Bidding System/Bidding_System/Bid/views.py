from django.shortcuts import render
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

cloudinary.config( 
    cloud_name = "dvkwhr1bx", 
    api_key = "839791265795498", 
    api_secret = "<your_api_secret>",
    secure=True
)

def add_product_for_bid(request):
    if request.method == "POST":
        file = request.FILES['file']
        print("--- ",request)
        upload_result = cloudinary.uploader.upload(file)
        print(upload_result["secure_url"])
        return render(request, 'bid_creation.html')
    return render(request, 'bid_creation.html')