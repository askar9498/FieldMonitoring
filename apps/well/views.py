from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'pages/dashboard/dashboard.html')

def well_detail(request):
    return render(request,'pages/well-detail-template.html')

def field_list(request):
    return render(request,'pages/field-list.html')

