from django.db import models

from .categories import Category

# Climate Control
class Fan(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Heater(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class AC(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
