# Generated by Django 3.2.5 on 2021-07-03 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20210703_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='wiring',
            name='power_transfer',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.CreateModel(
            name='WaterLevelMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='WaterHeater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('power_usage', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tubing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=30, null=True)),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('unit_measure', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='ShowerHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('pressure', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('power_usage', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Lighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='GrayWaterTank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='FreshWaterTank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Faucet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='ElectricalComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
        migrations.CreateModel(
            name='Accumulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('weight_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='components.category')),
            ],
        ),
    ]
