from django.db import models

class Van(models.Model):
    image = models.ImageField()
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    van_type = models.CharField(max_length=30, null=True, blank=True)
    wheelbase = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    price_new = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    price_used = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    max_weight = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    engine = models.CharField(max_length=30, null=True, blank=True)
    transmission = models.CharField(max_length=30, null=True, blank=True)
    drive = models.CharField(max_length=30, null=True, blank=True)
    fuel_capacity = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    mpg = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cargo_width = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cargo_height = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    cargo_length = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    external_width = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    external_height = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    external_length = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} {} {} - {} {}"'.format(self.year, self.make, self.model, self.van_type, self.wheelbase)