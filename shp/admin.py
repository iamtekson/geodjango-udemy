from django.contrib import admin
from .models import Jamoat
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


class JamoatAdmin(LeafletGeoAdmin):
    list_display = ['jamoat_eng', 'name_rg', 'district_e', 'population']
    list_filter = ['name_rg']
    list_editable = ['population']


admin.site.register(Jamoat, JamoatAdmin)
