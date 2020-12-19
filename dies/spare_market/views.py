from django.shortcuts import render

from spare_market.models import records as spare_records
from super_market.models import records as super_records

def data_input(request):
    return render(request, 'spare_market/data_input.html')


def details(request, part_number):
    olo = part_number.split('_')
    try:
        spare_item = spare_records.objects.filter(part_number=olo[0], model_id=olo[1])[0]
        common = super_records.objects.filter(part_number=spare_item.part_number, model_id=spare_item.model_id)
    except:
        spare_item = None
        common = None
    
    p_id = part_number
        
    context = {
        'item' : spare_item,
        'common' : common,
        'p_id' : p_id,
    }

    return render(request, 'spare_market/part_number_details.html', context)


def update(request, part_number):
    olo = part_number.split('_')
    spare_item = spare_records.objects.filter(part_number=olo[0], model_id=olo[1])[0]
    super_item = super_records.objects.filter(part_number=olo[0], model_id=olo[1], status_id=False)
    
    previous_stock = spare_item.stock
    spare_item.stock = spare_item.stock + int(olo[2])
    updated_super_item = 0

    if len(super_item) < spare_item.stock:
        updated_super_item = len(super_item)
        spare_item.stock = spare_item.stock - len(super_item)
        super_item.update(status_id=True)
    else:
        if spare_item.stock > 0:
            for i in super_item[:spare_item.stock]:
                i.status_id=True
                i.save()
                updated_super_item += 1
        spare_item.stock = 0
    spare_item.save()

    context = {
        'item' : spare_item,
        'previous_stock' : previous_stock,
        'p_id' : olo[0]+'_'+olo[1],
        'updated_super_item' : updated_super_item,
    }
    return render(request, 'spare_market/part_number_update.html', context)