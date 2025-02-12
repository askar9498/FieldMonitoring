
from django.urls import path
from .views import index, dashboard, well_detail, field_list, production

urlpatterns = (
    [
     
        path("", index, name='index'),
        path("dashboard/", dashboard, name='dashboard'),
        path("daily_production/<str:oil_or_gas>", production, name='daily_production'),
        path("field_list/", field_list, name='field_list'),
        path('wells/<int:well_id>/', well_detail, name='well_detail'),
    ]
    
)
