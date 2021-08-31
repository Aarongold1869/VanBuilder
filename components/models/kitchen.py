from django.db import models

from .categories import Category

# Kitchen
class CounterTop(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Sink(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    water_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Refrigerator(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class CookTop(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Microwave(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Oven(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class KitchenComponents(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None) 
    brand = models.CharField(max_length=30, null=True, blank=True)
    Item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_usage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
