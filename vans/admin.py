from django.contrib import admin
from .models import Van


class VanAdmin(admin.ModelAdmin):
    list_display = (
        'van_name', 
        'fuel_type',
        'sleeps',
        'seats',
    ) 

    ordering = ('van_name',)

admin.site.register(Van, VanAdmin)
