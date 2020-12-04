from django.shortcuts import render

from .models import *

def data_input(request):
    
    return render(request, 'super_market/data_input.html')

def details(request, part_id):

    try:
        item = records.objects.get(part_id=part_id)
    except:
        item = None

    return render(request, 'super_market/part_id_details.html', {'item' : item})