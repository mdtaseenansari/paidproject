from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    homcon = Homecontent.objects.all()
    return render(request,"index.html",{'homcon': homcon})

def product(request):
    add = Addproduct.objects.all()
    return render(request,"product.html",{'adds':add})

def contact(request):
    return render(request,"contact.html")