from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.status, name='inventory_status'),
    path('inventory/', views.inventory, name='inventory_inventory'),
    path('pi_per/', views.pi_per, name='inventory_pi_per'),
    path('per_part_number/', views.per_part_number, name='inventory_per_part_number'),
    path('pi_per_entity/', views.pi_per_entity, name='inventory_pi_per_entity'),
    path('pi_per_part_id/', views.pi_per_part_id, name='inventory_pi_per_part_id'),
    path('all/', views.all, name='all'),
]
