# Generated by Django 5.1.5 on 2025-01-31 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.FloatField(blank=True, null=True)),
                ('field_type', models.CharField(choices=[('gas', 'Gas Field'), ('oil', 'Oil Field')], max_length=4)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.country')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('current_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended'), ('decommissioned', 'Decommissioned')], max_length=20)),
                ('current_status_date', models.DateField()),
                ('well_type', models.CharField(choices=[('appraisal', 'Appraisal'), ('development', 'Development'), ('exploration', 'Exploration'), ('injection', 'Injection')], max_length=20)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='base.city')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='well.field')),
            ],
        ),
    ]
