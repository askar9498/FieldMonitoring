from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Country, Province, City, Company
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
class ProvinceInline(TabularInline):
    model = Province
    extra = 1
    raw_id_fields = ('country',)

class CityInline(TabularInline):
    model = City
    extra = 1
    raw_id_fields = ('province',)

@admin.register(Country)
class CountryAdmin(ModelAdmin, ImportExportModelAdmin):
    inlines = [ProvinceInline]
    import_form_class = ImportForm
    export_form_class = ExportForm

@admin.register(Province)
class ProvinceAdmin(ModelAdmin, ImportExportModelAdmin):
    inlines = [CityInline]
    import_form_class = ImportForm
    export_form_class = ExportForm
    
@admin.register(City)
class CityAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    # pass
@admin.register(Company)
class CompanyAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    # pass


