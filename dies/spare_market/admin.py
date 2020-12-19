from django.contrib import admin
from django.contrib.auth.models import Group, User

from spare_market.models import records
from super_market.models import records as super_records

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_url = "/inventory/all"

@admin.register(records)
class recordsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'model_id', 'stock')
    search_fields = ['part_number']
    list_filter = ['model_id']
    ordering = ['part_number']
    list_per_page = 10
    actions = None
    def save_model(self, request, obj, form, change):
        super_item = super_records.objects.filter(part_number=obj.part_number, model_id=obj.model_id, status_id=False)
        if len(super_item) < obj.stock:
            obj.stock = obj.stock - len(super_item)
            super_item.update(status_id=True)
        else:
            if obj.stock > 0:
                for i in super_item[:obj.stock]:
                    i.status_id=True
                    i.save()
            obj.stock = 0
        super().save_model(request, obj, form, change)