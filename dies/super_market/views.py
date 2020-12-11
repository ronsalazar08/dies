from django.shortcuts import render

from spare_market.models import records as spare_records
from super_market.models import records as super_records

def data_input(request):
    return render(request, 'super_market/data_input.html')


def details(request, part_id):
    if "_r" in part_id:
        olo = part_id.split('_')
        part_id = olo[0]
        ar = True
    else:
        ar = False
    try:
        item = super_records.objects.get(part_id=part_id)
        common = super_records.objects.filter(part_number=item.part_number, model_id=item.model_id).exclude(part_id=item.part_id)
        part_number_in_spare = spare_records.objects.filter(part_number=item.part_number, model_id=item.model_id)
        if ar == True:
            item.status_id=True
            item.save()
        if part_number_in_spare:
            not_in_spare_market = False
        else:
            not_in_spare_market = True
    except:
        item = None
        common = None
        not_in_spare_market = None
    
    p_id = part_id
        
    context = {
        'item' : item,
        'common' : common,
        'p_id' : p_id,
        'not_in_spare_market' : not_in_spare_market,
    }

    return render(request, 'super_market/part_id_details.html', context)


def claim(request, part_id):
    super_item = super_records.objects.get(part_id=part_id)
    super_item.status_id = False
    try:
        spare_item = spare_records.objects.filter(part_number=super_item.part_number, model_id=super_item.model_id)[0]
        previous_stock = spare_item.stock
        if spare_item.stock > 0:
            spare_item.stock = spare_item.stock - 1
            super_item.status_id = True

        spare_item.save()
        in_spare = True
    except:
        spare_item=None
        in_spare = False
        previous_stock = 0
    super_item.save()

    context = {
        'super_item' : super_item,
        'in_spare' : in_spare,
        'spare_item' : spare_item,
        'previous_stock' : previous_stock,
        'p_id' : part_id,
    }

    return render(request, 'super_market/part_id_claim.html', context)