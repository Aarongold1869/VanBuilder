# Generated by Django 3.2.5 on 2021-07-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_auto_20210703_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundInsulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('material', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_measure', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='HeatInsulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('material', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_measure', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('r_value', models.CharField(blank=True, max_length=30, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
    ]
