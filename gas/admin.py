from django.contrib import admin
from gas.models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.db.models import Count
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


def dashboard_callback(request, context):
    # دریافت داده‌های وضعیت چاه‌ها
    status_data = GasWell.objects.values('status').annotate(count=Count('status'))
    labels = [item['status'] for item in status_data]
    counts = [item['count'] for item in status_data]
    
    
    # ایجاد کد HTML برای چارت Pie
    chart_html = f"""
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <div style="margin-top: 20px;">
        <h4>Gas Well Status Distribution</h4>
        <canvas id="statusPieChart" width="200" height="100"></canvas>
    </div>
   
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script>
        const ctx = document.getElementById('statusPieChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: {labels},
                datasets: [{{
                    label: 'Number of Wells',
                    data: {counts},
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                    ],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    title: {{
                        display: true,
                        text: 'Gas Well Status Distribution'
                    }}
                }}
            }}
        }});
        
    </script>
    """

    # ایجاد جدول داده‌ها
    wells = GasWell.objects.all()
    table_html = """
    <div style="margin-top: 40px;">
        <h4>Gas Well Data</h4>
        <table class='table table-striped' border="1" style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr>
                    <th>Well Name</th>
                    <th>Status</th>
                    <th>Operator Company</th>
                    <th>Drilling Date</th>
                </tr>
            </thead>
            <tbody>
    """
    for well in wells:
        table_html += f"""
        <tr>
            <td>{well.well_name}</td>
            <td>{well.status}</td>
            <td>{well.operator_company}</td>
            <td>{well.drilling_date}</td>
        </tr>
        """
    table_html += """
            </tbody>
        </table>
    </div>
    """

    # اضافه کردن کد HTML به context
    context.update({
        "custom_chart": mark_safe(chart_html),  # چارت Pie
        "custom_table": mark_safe(table_html),  # جدول داده‌ها
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