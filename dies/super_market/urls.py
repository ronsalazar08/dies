from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.data_input, name='super_data_input'),
    path('details/<slug:part_id>', views.details, name='part_id_details'),
    path('claim/<slug:part_id>', views.claim, name='part_id_claim'),
]
