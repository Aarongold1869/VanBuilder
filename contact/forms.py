from django import forms
from django.contrib.auth.models import User

from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactSubmission
        fields = ('name', 'email', 'subject', 'content')
