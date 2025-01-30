from django.contrib import admin
from gas.models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


def dashboard_callback(request, context):
    # دریافت داده‌های تولید برای نمودار
    production_data = ProductionData.objects.all().order_by('production_date')
    labels = [data.production_date.strftime('%Y-%m-%d') for data in production_data]
    gas_volume = [data.gas_volume for data in production_data]

    # ایجاد کد HTML برای نمودار
    chart_html = f"""
    <div style="margin-top: 20px;">
        <h4>Gas Production Chart 3</h4>
        <canvas id="productionChart" width="400" height="200"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        const ctx = document.getElementById('productionChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {labels},
                datasets: [{{
                    label: 'Gas Volume (MMscf)',
                    data: {gas_volume},
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false,
                }}]
            }},
            options: {{
                responsive: true,
                scales: {{
                    x: {{
                        display: true,
                        title: {{
                            display: true,
                            text: 'Date'
                        }}
                    }},
                    y: {{
                        display: true,
                        title: {{
                            display: true,
                            text: 'Gas Volume (MMscf)'
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """

    # اضافه کردن کد HTML به context
    context.update({
        "custom_chart": mark_safe(chart_html),  # استفاده از mark_safe برای نمایش HTML
    })

    return context

@admin.register(GasWell)
class GasWellAdmin(ModelAdmin):
    list_display = ('well_name', 'reservoir', 'status', 'operator_company', 'drilling_date')
    list_filter = ('status', 'reservoir', 'operator_company')
    search_fields = ('well_name', 'reservoir__reservoir_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('well_name', 'reservoir', 'latitude', 'longitude', 'depth', 'pressure', 'flow_rate', 'drilling_date', 'status', 'operator_company', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # اضافه کردن نمودار به صفحه تغییر
    change_form_template = 'admin/gaswell_change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        production_data = ProductionData.objects.filter(gas_well_id=object_id).order_by('production_date')
        labels = [data.production_date.strftime('%Y-%m-%d') for data in production_data]
        gas_volume = [data.gas_volume for data in production_data]
        extra_context['chart_data'] = {
            'labels': labels,
            'gas_volume': gas_volume,
        }
        return super().change_view(request, object_id, form_url, extra_context)

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(GasField)
class GasFieldAdminClass(ModelAdmin):
    pass


@admin.register(Tubular)
class TubularAdminClass(ModelAdmin):
    pass

@admin.register(Reservoir)
class ReservoirAdminClass(ModelAdmin):
    pass

# @admin.register(GasWell)
# class GasWellAdminClass(ModelAdmin):
#     pass


# @admin.register(ProductionData)
# class ProductionDataAdminClass(ModelAdmin):
#     pass

# @admin.register(WellTest)
# class WellTestAdminClass(ModelAdmin):
#     pass

@admin.register(Equipment)
class EquipmentAdminClass(ModelAdmin):
    pass




# داشبورد برای مدل ProductionData
@admin.register(ProductionData)
class ProductionDataAdmin(ModelAdmin):
    list_display = ('gas_well', 'production_date', 'gas_volume', 'liquid_volume', 'pressure', 'temperature')
    list_filter = ('production_date', 'gas_well')
    search_fields = ('gas_well__well_name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('gas_well', 'production_date', 'gas_volume', 'liquid_volume', 'pressure', 'temperature', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# داشبورد برای مدل WellTest
@admin.register(WellTest)
class WellTestAdmin(ModelAdmin):
    list_display = ('gas_well', 'test_date', 'test_pressure', 'test_flow_rate', 'test_result')
    list_filter = ('test_result', 'gas_well')
    search_fields = ('gas_well__well_name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('gas_well', 'test_date', 'test_pressure', 'test_flow_rate', 'test_result', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )