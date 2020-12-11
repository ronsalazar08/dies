from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.status, name='inventory_status'),
    path('inventory/', views.inventory, name='inventory_inventory'),
    path('all/', views.all, name='all'),
]
