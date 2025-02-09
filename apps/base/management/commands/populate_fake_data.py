from django.core.management.base import BaseCommand
from faker import Faker
from base.models import (
    Country, Province, City, Company
)
from well.models import (
    Field, Well
)
from tubular.models import (
    TubularCatalogue, WellTube
)
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to populate fake data...'))

        # Create fake countries
        countries = []
        for _ in range(5):
            country = Country.objects.create(
                name=fake.country(),
                code=fake.unique.country_code(representation="alpha-3")
            )
            countries.append(country)
        self.stdout.write(self.style.SUCCESS('Created fake countries.'))

        # Create fake provinces
        provinces = []
        for country in countries:
            for _ in range(3):
                province = Province.objects.create(
                    name=fake.state(),
                    country=country
                )
                provinces.append(province)
        self.stdout.write(self.style.SUCCESS('Created fake provinces.'))

        # Create fake cities
        cities = []
        for province in provinces:
            for _ in range(2):
                city = City.objects.create(
                    name=fake.city(),
                    province=province
                )
                cities.append(city)
        self.stdout.write(self.style.SUCCESS('Created fake cities.'))

        # Create fake companies
        companies = []
        for _ in range(5):
            company = Company.objects.create(
                name=fake.company(),
                parent=None
            )
            companies.append(company)
        self.stdout.write(self.style.SUCCESS('Created fake companies.'))

        # Create fake fields
        fields = []
        for _ in range(10):
            field = Field.objects.create(
                name=fake.word(),
                area=random.uniform(100, 1000),
                country=random.choice(countries),
                company=random.choice(companies),
                field_type=random.choice(['gas', 'oil'])
            )
            fields.append(field)
        self.stdout.write(self.style.SUCCESS('Created fake fields.'))

        # Create fake wells
        wells = []
        for _ in range(20):
            well = Well.objects.create(
                field=random.choice(fields),
                city=random.choice(cities),
                name=fake.unique.word(),
                alias=fake.word(),
                current_status=random.choice(['active', 'inactive', 'suspended', 'decommissioned']),
                current_status_date=fake.date_between(start_date='-10y', end_date='today'),
                well_type=random.choice(['appraisal', 'development', 'exploration', 'injection']),
                lat=random.uniform(-90, 90),
                lon=random.uniform(-180, 180),
                remarks=fake.text()
            )
            wells.append(well)
        self.stdout.write(self.style.SUCCESS('Created fake wells.'))

        # Create fake tubular catalogues
        tubular_catalogues = []
        for _ in range(50):
            tubular = TubularCatalogue.objects.create(
                outer_diameter=random.uniform(1, 20),
                inner_diameter=random.uniform(0.5, 19),
                weight=random.uniform(10, 100),
                grade=fake.word(),
                tube_yield=random.uniform(100, 1000),
                internal_drift=random.uniform(0.5, 19),
                burst_pressure=random.uniform(100, 1000),
                collapse_pressure=random.uniform(100, 1000)
            )
            tubular_catalogues.append(tubular)
        self.stdout.write(self.style.SUCCESS('Created fake tubular catalogues.'))

        # Create fake well tubes
        for _ in range(100):
            WellTube.objects.create(
                well=random.choice(wells),
                tube_catalogue=random.choice(tubular_catalogues),
                name=random.choice(['CASING', 'TUBING', 'LINER']),
                hole_inner_diameter=random.uniform(0.5, 19),
                tvd_top=random.uniform(0, 5000),
                md_top=random.uniform(0, 5000),
                tvd_bottom=random.uniform(0, 5000),
                md_bottom=random.uniform(0, 5000)
            )
        self.stdout.write(self.style.SUCCESS('Created fake well tubes.'))

        self.stdout.write(self.style.SUCCESS('Successfully populated fake data!'))