# Generated by Django 3.2.5 on 2021-07-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0012_van_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='van',
            name='cargo_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='cargo_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='cargo_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='drive',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='engine',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='external_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='external_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='external_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='fuel_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='max_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='mpg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='passengers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='price_new',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='price_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='transmission',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='wheelbase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
