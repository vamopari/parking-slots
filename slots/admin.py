from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Slot

@admin.register(Slot)
class SlotAdmin(OSMGeoAdmin):
    list_display = ('price', 'location', 'status')
