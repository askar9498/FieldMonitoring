from django.db import models
from django.utils.translation import gettext_lazy as _
from well.models import Well

class TubularCatalogue(models.Model):
    outer_diameter = models.FloatField()
    inner_diameter = models.FloatField()      
    weight = models.FloatField()  
    grade = models.CharField(max_length=50)
    tube_yield = models.FloatField(db_column="yield")        
    internal_drift = models.FloatField()    
    burst_pressure = models.FloatField()  
    collapse_pressure = models.FloatField()
    
    class Meta:
        verbose_name = _("Tubular Catalogue")
        verbose_name_plural = _("Tubular Catalogue")

    def __str__(self):
        return f"OD:{self.outer_diameter} - W:{self.weight} - G:{self.grade}"

class WellTube(models.Model):
      
    class TubeName(models.TextChoices):
        CASING = 'CASING', 'CASING'
        TUBING = 'TUBING', 'TUBING'
        LINER = 'LINER', 'LINER'

    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    tube_catalogue = models.ForeignKey(TubularCatalogue, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, choices=TubeName.choices, blank=True, null=True)
    hole_inner_diameter = models.FloatField(blank=True, null=True, help_text=_("Inner diameter of the drilled hole"))
    tvd_top = models.FloatField(blank=True, null=True, help_text=_("Top of the tube (True Vertical Depth)"))
    md_top = models.FloatField(blank=True, null=True, help_text=_("Top of tube (Measured Depth)"))
    tvd_bottom = models.FloatField(blank=True, null=True, help_text=_("Bottom of the tube (True Vertical Depth)"))
    md_bottom = models.FloatField(blank=True, null=True, help_text=_("Bottom of the tube (Measured Depth)"))
    
    class Meta:
        verbose_name = "well_tubes"
        verbose_name_plural = "Well Tube"
    
    def __str__(self):
        return f"{self.well.name} - {self.name} - OD: {self.tube_catalogue.outer_diameter}"
