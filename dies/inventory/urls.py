from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.status, name='inventory_status'),
    path('inventory/', views.inventory, name='inventory_inventory'),
    path('pi_per_entity/', views.pi_per_entity, name='inventory_pi_per_entity'),
    path('all/', views.all, name='all'),
]
