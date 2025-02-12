from django.shortcuts import render
from .models import *
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboard(request):
    fields = Field.objects.all()
    companies = set(fields.values_list('company__name', flat=True))  # دریافت نام شرکت‌ها
    production_data = []

    for company in companies:
        oil_production = 0
        gas_production = 0
        
        for field in fields.filter(company__name=company):
            random_production = random.randint(50, 500)  # مقدار تصادفی تولید
            if field.field_type == Field.FieldType.OIL:
                oil_production += random_production
            else:
                gas_production += random_production
        
        production_data.append({
            'company': company,
            'oil': oil_production,
            'gas': gas_production
        })
    field_data = []
    for field in fields:
        if field.field_type == Field.FieldType.OIL:
            well_count = Well.objects.filter(field=field).count()
            random_production = random.randint(1, 100)  # اعداد تصادفی بین 1 تا 100
            random_change = random.randint(-5, 8)
            
            production = random_production
                
            field_data.append({
                'field_name': field.name,
                'well_count': well_count,
                'change': random_change,
                'production': production,
            })
    
    context = {
        'field_data': field_data,
        'production_data': production_data
    }
    
    return render(request,'pages/dashboard/dashboard.html', context)

def production(request, oil_or_gas):
    fields = Field.objects.all()
    field_data = []
    oilorgas = Field.FieldType.OIL if oil_or_gas == 'oil' else Field.FieldType.GAS
    for field in fields:
        if field.field_type == oilorgas:
            well_count = Well.objects.filter(field=field).count()
            random_production = random.randint(1, 100)  # اعداد تصادفی بین 1 تا 100
            random_change = random.randint(-5, 8)
            
            production = random_production
                
            field_data.append({
                'field_name': field.name,
                'well_count': well_count,
                'change': random_change,
                'production': production,
            })
    
    context = {
        'field_data': field_data,
    }
    return render(request,'pages/dashboard/daily_production.html', context)

def well_detail(request):
    return render(request,'pages/well-detail-template.html')

def field_list(request):
    return render(request,'pages/field-list.html')

