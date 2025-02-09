
from django.urls import path
from .views import index, dashboard, well_detail, field_list

urlpatterns = (
    [
     
        path("", index, name='index'),
        path("dashboard/", dashboard, name='dashboard'),
        path("field_list/", field_list, name='field_list'),
        path("well_detail/", well_detail, name='well_detail'),
    ]
    
)
