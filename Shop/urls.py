from django.contrib import admin
from django.urls import path
from Shop import views


urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('animelist', views.animelist, name='list'),
    path('hoodies', views.hoodies, name='hoodies'),
    path('joggers', views.joggers, name='joggers'),
    path('facemasks', views.facemasks, name='facemasks'),
    path('cosplay', views.cosplay, name='cosplay'),
    path('backpacks', views.backpacks, name='backpacks'),
    path('rings', views.rings, name='rings'),
]