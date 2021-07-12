from django.conf import settings 
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html")