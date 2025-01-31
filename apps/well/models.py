from django.db import models
from base.models import Country, City, Company
# Create your models here.

class Field(models.Model):
    class FieldType(models.TextChoices):
        GAS = 'gas', 'Gas Field'
        OIL = 'oil', 'Oil Field'

    name = models.CharField(max_length=255)
    area = models.FloatField(null=True, blank=True)  # allows null value
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    field_type = models.CharField(max_length=4, choices=FieldType.choices)

    def __str__(self):
        return f'{self.name} ({self.field_type}) in {self.country.name}'
    

class Well(models.Model):
    class WellType(models.TextChoices):
        APPRAISAL = 'appraisal', 'Appraisal'
        DEVELOPMENT = 'development', 'Development'
        EXPLORATION = 'exploration', 'Exploration'
        INJECTION = 'injection', 'Injection'

    class CurrentStatus(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'
        SUSPENDED = 'suspended', 'Suspended'
        DECOMMISSIONED = 'decommissioned', 'Decommissioned'

    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='wells')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='wells')  # Foreign key to City model
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    current_status = models.CharField(max_length=20, choices=CurrentStatus.choices)
    current_status_date = models.DateField()
    well_type = models.CharField(max_length=20, choices=WellType.choices)
    lat = models.FloatField()
    lon = models.FloatField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.well_type})'
