from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TubularCatalogue, WellTube
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

@admin.register(TubularCatalogue)
class TubularCatalogueAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm

@admin.register(WellTube)
class WellTubeAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm