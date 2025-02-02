# Generated by Django 5.1.5 on 2025-02-02 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('well', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TubularCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer_diameter', models.FloatField()),
                ('inner_diameter', models.FloatField()),
                ('weight', models.FloatField()),
                ('grade', models.CharField(max_length=50)),
                ('tube_yield', models.FloatField(db_column='yield')),
                ('internal_drift', models.FloatField()),
                ('burst_pressure', models.FloatField()),
                ('collapse_pressure', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tubular Catalogue',
                'verbose_name_plural': 'Tubular Catalogue',
                'db_table': 'tubulartemp',
            },
        ),
        migrations.CreateModel(
            name='WellTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('CASING', 'CASING'), ('TUBING', 'TUBING'), ('LINER', 'LINER')], max_length=255, null=True)),
                ('hole_inner_diameter', models.FloatField(blank=True, help_text='Inner diameter of the drilled hole', null=True)),
                ('tvd_top', models.FloatField(blank=True, help_text='Top of the tube (True Vertical Depth)', null=True)),
                ('md_top', models.FloatField(blank=True, help_text='Top of tube (Measured Depth)', null=True)),
                ('tvd_bottom', models.FloatField(blank=True, help_text='Bottom of the tube (True Vertical Depth)', null=True)),
                ('md_bottom', models.FloatField(blank=True, help_text='Bottom of the tube (Measured Depth)', null=True)),
                ('tube_catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tubular.tubularcatalogue')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='well.well')),
            ],
            options={
                'verbose_name': 'well_tubes',
                'verbose_name_plural': 'Well Tube',
                'db_table': 'Well Tubes',
            },
        ),
    ]
