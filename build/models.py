from django.db import models
from django.conf import settings

from components.models import * 

User = settings.AUTH_USER_MODEL

# Create your models here.
class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True, blank=True)
    vehicle = models.ForeignKey(Van, on_delete=models.PROTECT)
    budget = models.DecimalField(max_digits=15,decimal_places=2, null=True, blank=True)
    
