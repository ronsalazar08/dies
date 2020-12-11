from django.contrib import admin
from django.contrib.auth.models import Group, User

from spare_market.models import records

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