from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)  # ISO 3166-1 alpha-3 country code

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="provinces")

    class Meta:
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")
        unique_together = ('name', 'country')  # Ensures province names are unique within a country

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        unique_together = ('name', 'province')  # Ensures city names are unique within a province
        
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return f"{self.name}, {self.province.name}, {self.province.country.name}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subsidiaries')

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        
    def __str__(self):
        return self.name
