from django.contrib import admin
from django.urls import path,include
from . import views





urlpatterns = [
    path('' or 'index.html',views.home,name='home'),
    path('product.html',views.product,name='product'),
    path('contact.html',views.contact,name='contact')
]
