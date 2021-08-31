from django.db import models

from .categories import Category

# Water / Plumbing
class FreshWaterTank(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    volume = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class GrayWaterTank(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    volume = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class WaterHeater(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    volume = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Pump(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    pressure = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Tubing(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Accumulator(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Filter(models.Model): 
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Faucet(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    water_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class ShowerHead(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    water_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class WaterLevelMonitor(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
