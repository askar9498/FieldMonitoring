from django.db import models

# مدل GasField (میدان گازی)
class GasField(models.Model):
    field_id = models.AutoField(primary_key=True, verbose_name="Field ID")
    field_name = models.CharField(max_length=255, verbose_name="Field Name")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    area = models.FloatField(verbose_name="Area (km²)")
    discovery_date = models.DateField(verbose_name="Discovery Date")
    operator_company = models.CharField(max_length=255, verbose_name="Operator Company")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = "Gas Field"
        verbose_name_plural = "Gas Fields"
        ordering = ['field_name']


# مدل Reservoir (مخزن)
class Reservoir(models.Model):
    reservoir_id = models.AutoField(primary_key=True, verbose_name="Reservoir ID")
    reservoir_name = models.CharField(max_length=255, verbose_name="Reservoir Name")
    gas_field = models.ForeignKey(GasField, on_delete=models.CASCADE, related_name='reservoirs', verbose_name="Gas Field")
    depth = models.FloatField(verbose_name="Depth (m)")
    volume = models.FloatField(verbose_name="Volume (BCF)")
    pressure = models.FloatField(verbose_name="Pressure (psi)")
    discovery_date = models.DateField(verbose_name="Discovery Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.reservoir_name

    class Meta:
        verbose_name = "Reservoir"
        verbose_name_plural = "Reservoirs"
        ordering = ['reservoir_name']


# مدل GasWell (چاه گاز)
class GasWell(models.Model):
    well_id = models.AutoField(primary_key=True, verbose_name="Well ID")
    well_name = models.CharField(max_length=255, verbose_name="Well Name")
    reservoir = models.ForeignKey(Reservoir, on_delete=models.CASCADE, related_name='gas_wells', verbose_name="Reservoir")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    depth = models.FloatField(verbose_name="Depth (m)")
    pressure = models.FloatField(verbose_name="Pressure (psi)")
    flow_rate = models.FloatField(verbose_name="Flow Rate (MMscfd)")
    drilling_date = models.DateField(verbose_name="Drilling Date")
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('under_maintenance', 'Under Maintenance'),
        ('abandoned', 'Abandoned'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    operator_company = models.CharField(max_length=255, verbose_name="Operator Company")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.well_name

    class Meta:
        verbose_name = "Gas Well"
        verbose_name_plural = "Gas Wells"
        ordering = ['well_name']


# مدل Tubular (تجهیزات لوله‌کشی)
class Tubular(models.Model):
    tubular_id = models.AutoField(primary_key=True, verbose_name="Tubular ID")
    gas_well = models.ForeignKey(GasWell, on_delete=models.CASCADE, related_name='tubulars', verbose_name="Gas Well")
    TUBULAR_TYPE_CHOICES = [
        ('casing', 'Casing'),
        ('production', 'Production Tubing'),
        ('liner', 'Liner'),
        ('other', 'Other'),
    ]
    tubular_type = models.CharField(max_length=20, choices=TUBULAR_TYPE_CHOICES, verbose_name="Tubular Type")
    diameter = models.FloatField(verbose_name="Diameter (inches)")
    length = models.FloatField(verbose_name="Length (m)")
    material = models.CharField(max_length=255, verbose_name="Material")
    working_pressure = models.FloatField(verbose_name="Working Pressure (psi)")
    installation_date = models.DateField(verbose_name="Installation Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.tubular_type} - {self.gas_well.well_name}"

    class Meta:
        verbose_name = "Tubular"
        verbose_name_plural = "Tubulars"
        ordering = ['tubular_type']


# مدل ProductionData (داده‌های تولید)
class ProductionData(models.Model):
    production_id = models.AutoField(primary_key=True, verbose_name="Production ID")
    gas_well = models.ForeignKey(GasWell, on_delete=models.CASCADE, related_name='production_data', verbose_name="Gas Well")
    production_date = models.DateField(verbose_name="Production Date")
    gas_volume = models.FloatField(verbose_name="Gas Volume (MMscf)")
    liquid_volume = models.FloatField(verbose_name="Liquid Volume (bbl)")
    pressure = models.FloatField(verbose_name="Pressure (psi)")
    temperature = models.FloatField(verbose_name="Temperature (°C)")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.gas_well.well_name} - {self.production_date}"

    class Meta:
        verbose_name = "Production Data"
        verbose_name_plural = "Production Data"
        ordering = ['production_date']


# مدل WellTest (داده‌های تست چاه)
class WellTest(models.Model):
    test_id = models.AutoField(primary_key=True, verbose_name="Test ID")
    gas_well = models.ForeignKey(GasWell, on_delete=models.CASCADE, related_name='well_tests', verbose_name="Gas Well")
    test_date = models.DateField(verbose_name="Test Date")
    test_pressure = models.FloatField(verbose_name="Test Pressure (psi)")
    test_flow_rate = models.FloatField(verbose_name="Test Flow Rate (MMscfd)")
    TEST_RESULT_CHOICES = [
        ('success', 'Success'),
        ('failure', 'Failure'),
        ('inconclusive', 'Inconclusive'),
    ]
    test_result = models.CharField(max_length=20, choices=TEST_RESULT_CHOICES, verbose_name="Test Result")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.gas_well.well_name} - {self.test_date}"

    class Meta:
        verbose_name = "Well Test"
        verbose_name_plural = "Well Tests"
        ordering = ['test_date']


# مدل Equipment (تجهیزات چاه)
class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True, verbose_name="Equipment ID")
    gas_well = models.ForeignKey(GasWell, on_delete=models.CASCADE, related_name='equipments', verbose_name="Gas Well")
    EQUIPMENT_TYPE_CHOICES = [
        ('pump', 'Pump'),
        ('valve', 'Valve'),
        ('sensor', 'Sensor'),
        ('other', 'Other'),
    ]
    equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_TYPE_CHOICES, verbose_name="Equipment Type")
    equipment_name = models.CharField(max_length=255, verbose_name="Equipment Name")
    installation_date = models.DateField(verbose_name="Installation Date")
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('under_maintenance', 'Under Maintenance'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.equipment_type} - {self.equipment_name}"

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"
        ordering = ['equipment_type']