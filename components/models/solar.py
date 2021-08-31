from django.db import models

from .categories import Category

# Solar
class SolarPanel(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    wattage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    power_per_cell = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    num_cells = models.IntegerField(null=True, blank=True)
    efficiency = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    walkable = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

class ChargeController(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    volts = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    amps = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
