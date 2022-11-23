from django.shortcuts import render
from prueba.models import Product, Search
# Create your views here.

def home(request):
    product = Product.objects.all()
    if request.method == 'POST':
        search_input = request.POST["input-product"]
        if not search_input == "":
            print(type(search_input))
            obj = Search(search=search_input)
            obj.save()
            return render(request , "home.html", {"product":product})
    return render(request , "home.html")