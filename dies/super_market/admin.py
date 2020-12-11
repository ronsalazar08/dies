from django.contrib import admin

from .models import records


@admin.register(records)
class recordsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'part_number', 'model_id', 'status_id')
    ordering = ['id']
    search_fields = ['part_id', 'part_number']
    list_filter = ['model_id', 'status_id']
    ordering = ['part_id']
    list_per_page = 10
    actions = None