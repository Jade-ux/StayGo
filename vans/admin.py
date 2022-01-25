from django.contrib import admin
from .models import Van


class VanAdmin(admin.ModelAdmin):
    list_display = (
        'van_name',
        'van_description', 
        'size_description',
        'fuel_type',
        'sleeps',
        'seats',
        'airconditioning_home_area',
    ) 

    ordering = ('van_name',)

admin.site.register(Van, VanAdmin)
