from django.db import models
import uuid

class Wells(models.Model):
    well_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    well_name = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='wells')
    field = models.ForeignKey('Fields', on_delete=models.CASCADE, related_name='wells')
    reservoir = models.ForeignKey('Reservoirs', on_delete=models.CASCADE, null=True, blank=True, related_name='wells')
    zone = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    status = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    fluid = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    production = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    design_type = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    designation = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    depth_ref = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    # add_by = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    # approved_by = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    add_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    # is_approved = models.BooleanField(default=False, db_index=True)
    lat_start = models.FloatField(null=True, blank=True, db_index=True)
    long_start = models.FloatField(null=True, blank=True, db_index=True)
    lat_end = models.FloatField(null=True, blank=True, db_index=True)
    long_end = models.FloatField(null=True, blank=True, db_index=True)
    activity_log = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Well'
        verbose_name_plural = 'Wells'
    
    def __str__(self):
        return self.well_name


class Tubular(models.Model):
    tube_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    well = models.ForeignKey('Wells', on_delete=models.CASCADE, related_name='tubulars')
    tube_temp = models.ForeignKey('TubularTemp', on_delete=models.CASCADE, related_name='tubulars')
    conn_temp = models.ForeignKey('TubeConnection', on_delete=models.CASCADE, related_name='tubulars')
    tube_name = models.CharField(max_length=255, db_index=True)
    hole_ID = models.FloatField(null=True, blank=True, db_index=True)
    tube_TVD_from = models.FloatField(null=True, blank=True, db_index=True)
    tube_MD_from = models.FloatField(null=True, blank=True, db_index=True)
    tube_TVD_to = models.FloatField(null=True, blank=True, db_index=True)
    tube_MD_to = models.FloatField(null=True, blank=True, db_index=True)
    cement_TOC = models.FloatField(null=True, blank=True, db_index=True)
    cement_return = models.FloatField(null=True, blank=True, db_index=True)
    cement_log = models.IntegerField(null=True, blank=True, db_index=True)
    formation_FIT = models.FloatField(null=True, blank=True, db_index=True)
    formation_LOT = models.FloatField(null=True, blank=True, db_index=True)
    formation_FBP = models.FloatField(null=True, blank=True, db_index=True)
    # add_by = models.CharField(max_length=255, db_index=True)
    add_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    activity_log = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Tubular'
        verbose_name_plural = 'Tubulars'
    
    def __str__(self):
        return self.tube_name

class TubularTemp(models.Model):
    tubulartemp_id = models.AutoField(primary_key=True)
    tube_name = models.CharField(max_length=255, db_index=True)
    tube_OD = models.FloatField(db_index=True)
    tube_ID = models.FloatField(db_index=True)
    tube_weight = models.FloatField(db_index=True)
    tube_grade = models.CharField(max_length=255, db_index=True)
    tube_yield = models.FloatField(db_index=True)
    tube_int_drift = models.FloatField(db_index=True)
    tube_burst_press = models.FloatField(db_index=True)
    tube_collapse_press = models.FloatField(db_index=True)
    tube_axial = models.FloatField(db_index=True)
    tube_uts = models.FloatField(db_index=True)
    # add_by = models.CharField(max_length=255, db_index=True)
    add_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        verbose_name = 'TubularTemp'
        verbose_name_plural = 'TubularTemps'
    
    def __str__(self):
        return self.tube_name

class TubeConnection(models.Model):
    connection_id = models.AutoField(primary_key=True)
    tube_OD = models.FloatField(db_index=True)
    tube_weight = models.FloatField(db_index=True)
    tube_grade = models.CharField(max_length=255, db_index=True)
    conn_name = models.CharField(max_length=255, db_index=True)
    conn_type = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    conn_seal_type = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    conn_OD = models.FloatField(null=True, blank=True, db_index=True)
    conn_yield = models.FloatField(null=True, blank=True, db_index=True)
    conn_uts = models.FloatField(null=True, blank=True, db_index=True)
    conn_burst = models.FloatField(null=True, blank=True, db_index=True)
    conn_tension = models.FloatField(null=True, blank=True, db_index=True)
    conn_compression = models.FloatField(null=True, blank=True, db_index=True)
    conn_maxbend = models.FloatField(null=True, blank=True, db_index=True)
    # add_by = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    add_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        verbose_name = 'TubeConnection'
        verbose_name_plural = 'TubeConnections'
    
    def __str__(self):
        return self.conn_name



class Country(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    country_name = models.CharField(max_length=255, db_index=True)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.country_name
    

class Fields(models.Model):
    field_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='fields')
    field_name = models.CharField(max_length=255, db_index=True)
    
    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'
    
    def __str__(self):
        return f"{self.country}-{self.field_name}"

class Reservoirs(models.Model):
    reservoir_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    field = models.ForeignKey('Fields', on_delete=models.CASCADE, related_name='reservoirs')
    reservoir_name = models.CharField(max_length=255, db_index=True)
    
    class Meta:
        verbose_name = 'Reservoir'
        verbose_name_plural = 'Reservoirs'

    def __str__(self):
        return f"{self.field}-{self.reservoir_name}"