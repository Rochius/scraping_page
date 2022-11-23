from django.shortcuts import render
from prueba.models import Product
# Create your views here.

def home(request):
    product = Product.objects.all()
    return render(request , "home.html", {"product":product})