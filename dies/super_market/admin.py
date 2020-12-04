from django.contrib import admin

from .models import *


@admin.register(records)
class recordsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'part_number', 'model_id', 'status_id')
    ordering = ['id']