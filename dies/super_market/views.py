from django.shortcuts import render

from .models import *

def data_input(request):
    return render(request, 'super_market/data_input.html')


def details(request, part_id):
    try:
        item = records.objects.get(part_id=part_id)
    except:
        item = None
    
    p_id = part_id
        
    context = {
        'item' : item,
        'p_id' : p_id,
    }

    return render(request, 'super_market/part_id_details.html', context)


def claim(request, part_id):
    item = records.objects.get(part_id=part_id)
    item.status_id = False
    item.save()
    return render(request, 'super_market/part_id_claim.html', {'item' : part_id})