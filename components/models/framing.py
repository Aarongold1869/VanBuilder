from django.db import models

from .categories import Category

# Framing
class Framing(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)