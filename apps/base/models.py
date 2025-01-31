from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)  # ISO 3166-1 alpha-3 country code

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="provinces")

    class Meta:
        unique_together = ('name', 'country')  # Ensures province names are unique within a country
        db_table = 'Province'

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        unique_together = ('name', 'province')  # Ensures city names are unique within a province
        db_table = 'City'

    def __str__(self):
        return f"{self.name}, {self.province.name}, {self.province.country.name}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subsidiaries')

    def __str__(self):
        return self.name
