from django.db import models

# Create your models here.

class Van(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    wheelbase = models.DecimalField(max_digits=15,decimal_places=2)
    price_low = models.DecimalField(max_digits=15,decimal_places=2)
    price_high = models.DecimalField(max_digits=15,decimal_places=2)
    max_weight = models.DecimalField(max_digits=15,decimal_places=2)
    engine = models.CharField(max_length=30)
    drive = models.CharField(max_length=30)
    width = models.DecimalField(max_digits=15,decimal_places=2)
    height = models.DecimalField(max_digits=15,decimal_places=2)
    passengers = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

# External Components
class Paint(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class RoofRack(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class HeadLights(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    style = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Suspension(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    style = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class ExternalFeature(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

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

# Insulation
class SoundInsulation(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class HeatInsulation(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    r_value = models.CharField(max_length=30, null=True, blank=True)

# Electrical
class Storage(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    battery_type = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    storage_capacity = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Wiring(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    power_transfer = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class WireInsulation(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    unit_measure = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Inverter(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    model = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=30, null=True, blank=True)
    wattage = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    surge = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    efficiency = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class BusBar(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Breaker(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Shore(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class SystemMonitor(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class TwelveVolt(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Lighting(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class ElectricalComponents(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    item = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

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
    cost_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    weight_per_unit = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class ShowerHead(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    brand = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=30, null=True, blank=True)
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

# Flooring / Walls
class SubFloor(models.Model):

class Flooring(models.Model):

# Bathroom
class Shower(models.Model):

class Toilet(models.Model):

class Wall(models.Model):

class Door(models.Model):

# Kitchen
class CounterTop(models.Model):

class Sink(models.Model):

class Refrigerator(models.Model):

class CookTop(models.Model):

class Microwave(models.Model):

class Oven(models.Model):

class KitchenComponents(models.Model):

# Decorative Finishing
class Backsplash(models.Model):

# Hardware
class DrawerSlides(models.Model):

class RivNuts(models.Model):

class SwivelSeats(models.Model):

class OtherHardware(models.Model):
