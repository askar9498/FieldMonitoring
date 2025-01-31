from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Country, Province, City

class ProvinceInline(TabularInline):
    model = Province
    extra = 1
    raw_id_fields = ('country',)

class CityInline(TabularInline):
    model = City
    extra = 1
    raw_id_fields = ('province',)

@admin.register(Country)
class CountryAdmin(ModelAdmin):
    inlines = [ProvinceInline]

@admin.register(Province)
class ProvinceAdmin(ModelAdmin):
    inlines = [CityInline]
