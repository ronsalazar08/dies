from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.data_input, name='spare_data_input'),
    path('details/<slug:part_number>', views.details, name='part_number_details'),
    path('update/<slug:part_number>', views.update, name='part_number_update'),
]
