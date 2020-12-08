from django.shortcuts import render

from spare_market.models import records as spare_records
from super_market.models import records as super_records

def inventory(request):
    mfg_list = super_records.objects.values('mfg_div').distinct().order_by('mfg_div')
    entity_list = []
    entity_total = [0,0]
    for i in mfg_list:
        mfg = super_records.objects.filter(mfg_div=i['mfg_div'])
        mfg_true = mfg.filter(status_id=True).count()
        entity_list.append([i['mfg_div'], mfg_true, mfg.count()])
        entity_total[0] += mfg_true
        entity_total[1] += mfg.count()
    in_stock_percentage = (entity_total[0] / entity_total[1]) * 100
    context = {
        'entity_list' : entity_list,
        'entity_total' : entity_total,
        'in_stock_percentage' : in_stock_percentage,
    }
    return render(request, 'inventory/inventory.html', context)