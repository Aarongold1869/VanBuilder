from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class ContactSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()