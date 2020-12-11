from django.shortcuts import render

from spare_market.models import records as spare_records
from super_market.models import records as super_records


def status(request):
    super_rec = super_records.objects.all()
    super_in_stock_percentage = (super_rec.filter(status_id=True).count()) / super_rec.count()

    spare_rec = spare_records.objects.all()
    
    dict_inv = {}
    inv_total = [0,0]
    
    for i in super_rec:
        status_id = 0
        if i.status_id == True:
            status_id = 1
        if i.part_number + '_' + i.model_id not in dict_inv:
            dict_inv[i.part_number + '_' + i.model_id] = {}
            dict_inv[i.part_number + '_' + i.model_id]['part_number'] = i.part_number
            dict_inv[i.part_number + '_' + i.model_id]['model'] = i.model_id
            dict_inv[i.part_number + '_' + i.model_id]['super'] = status_id
            dict_inv[i.part_number + '_' + i.model_id]['total'] = 1
        else:
            dict_inv[i.part_number + '_' + i.model_id]['super'] += status_id
            dict_inv[i.part_number + '_' + i.model_id]['total'] += status_id

    for key ,value in dict_inv.items(): 
        if value and 'super' and 'total' in value.keys():
            val = 0
            if value['super'] >= 1:
                val = 1
            if value['total'] >= 1:
                tot = 1

            inv_total[0] += val
            inv_total[1] += tot  
    spare_in_stock_percentage = inv_total[0] / inv_total[1]
    # print([(super_rec.filter(status_id=True).count()), super_rec.count()])
    # print(inv_total)
    
    context = {
        # 'entity_list' : entity_list,
        'entity_total' : super_rec.count(),
        'super_in_stock_percentage' : super_in_stock_percentage * 100,
        'spare_in_stock_percentage' : spare_in_stock_percentage * 100,
    }
    
    return render(request, 'inventory/status.html', context)


def inventory(request):
    spare_rec = spare_records.objects.all()
    super_rec = super_records.objects.all()
    dict_inv = {}
    inv_total = [0,0,0]
    
    for i in super_rec:
        status_id = 0
        if i.status_id == True:
            status_id = 1
        if i.part_number + '_' + i.model_id not in dict_inv:
            dict_inv[i.part_number + '_' + i.model_id] = {}
            dict_inv[i.part_number + '_' + i.model_id]['part_number'] = i.part_number
            dict_inv[i.part_number + '_' + i.model_id]['model'] = i.model_id
            dict_inv[i.part_number + '_' + i.model_id]['super'] = status_id
            dict_inv[i.part_number + '_' + i.model_id]['spare'] = 0
            dict_inv[i.part_number + '_' + i.model_id]['total'] = status_id
        else:
            dict_inv[i.part_number + '_' + i.model_id]['super'] += status_id
            dict_inv[i.part_number + '_' + i.model_id]['total'] += status_id
    
    for i in spare_rec:
        if i.part_number + '_' + i.model_id in dict_inv:
            dict_inv[i.part_number + '_' + i.model_id]['spare'] += i.stock
            dict_inv[i.part_number + '_' + i.model_id]['total'] += i.stock

    for key ,value in dict_inv.items(): 
        if value and 'super' and 'spare' and 'total' in value.keys(): 
            # Adding value of sharpness to sum 
            inv_total[0] += value['super']  
            inv_total[1] += value['spare']
            inv_total[2] += value['total']  
    # print(dict(sorted(dict_inv.items())))

    context = {
        'inv_total' : inv_total,
        'dict_inv' : dict(sorted(dict_inv.items())),
        # 'dict_inv' : dict_inv,
    }
    
    return render(request, 'inventory/inventory.html', context)


def pi_per_entity(request):
    mfg_list = super_records.objects.values('mfg_div').distinct().order_by('mfg_div')
    entity_list = []
    entity_total = [0,0]
    for i in mfg_list:
        mfg = super_records.objects.filter(mfg_div=i['mfg_div'])
        mfg_true = mfg.filter(status_id=True).count()
        entity_list.append([i['mfg_div'], mfg_true, mfg.count()])
        entity_total[0] += mfg_true
        entity_total[1] += mfg.count()
    super_in_stock_percentage = (entity_total[0] / entity_total[1]) * 100
    context = {
        'entity_total' : entity_total,
        'entity_list' : entity_list,
        'super_in_stock_percentage' : super_in_stock_percentage,
    }
    return render(request, 'inventory/pi_per_entity.html', context)






def all(request):
    mfg_list = super_records.objects.values('mfg_div').distinct().order_by('mfg_div')
    entity_list = []
    entity_total = [0,0]
    for i in mfg_list:
        mfg = super_records.objects.filter(mfg_div=i['mfg_div'])
        mfg_true = mfg.filter(status_id=True).count()
        entity_list.append([i['mfg_div'], mfg_true, mfg.count()])
        entity_total[0] += mfg_true
        entity_total[1] += mfg.count()
    super_in_stock_percentage = (entity_total[0] / entity_total[1]) * 100

    spare_rec = spare_records.objects.all()
    super_rec = super_records.objects.all()
    dict_inv = {}
    inv_total = [0,0,0]
    
    for i in super_rec:
        status_id = 0
        if i.status_id == True:
            status_id = 1
        if i.part_number + '_' + i.model_id not in dict_inv:
            dict_inv[i.part_number + '_' + i.model_id] = {}
            dict_inv[i.part_number + '_' + i.model_id]['part_number'] = i.part_number
            dict_inv[i.part_number + '_' + i.model_id]['model'] = i.model_id
            dict_inv[i.part_number + '_' + i.model_id]['super'] = status_id
            dict_inv[i.part_number + '_' + i.model_id]['spare'] = 0
            dict_inv[i.part_number + '_' + i.model_id]['total'] = status_id
        else:
            dict_inv[i.part_number + '_' + i.model_id]['super'] += status_id
            dict_inv[i.part_number + '_' + i.model_id]['total'] += status_id
    
    for i in spare_rec:
        if i.part_number + '_' + i.model_id in dict_inv:
            dict_inv[i.part_number + '_' + i.model_id]['spare'] += i.stock
            dict_inv[i.part_number + '_' + i.model_id]['total'] += i.stock

    for key ,value in dict_inv.items(): 
        if value and 'super' and 'spare' and 'total' in value.keys(): 
            # Adding value of sharpness to sum 
            inv_total[0] += value['super']  
            inv_total[1] += value['spare']
            inv_total[2] += value['total']  

    context = {
        'entity_total' : entity_total,
        'entity_list' : entity_list,
        'super_in_stock_percentage' : super_in_stock_percentage,
        'inv_total' : inv_total,
        'dict_inv' : dict_inv,
    }
    
    return render(request, 'inventory/all.html', context)