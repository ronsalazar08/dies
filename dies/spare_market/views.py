from django.shortcuts import render

from .models import *

def data_input(request):
    return render(request, 'spare_market/data_input.html')


def details(request, part_number):
    try:
        item = records.objects.get(part_number=part_number)
    except:
        item = None
    
    p_id = part_number
        
    context = {
        'item' : item,
        'p_id' : p_id,
    }

    return render(request, 'spare_market/part_number_details.html', context)


# def claim(request, part_id):
#     item = records.objects.get(part_id=part_id)
#     item.status_id = False
#     item.save()
#     return render(request, 'super_market/part_id_claim.html', {'item' : part_id})