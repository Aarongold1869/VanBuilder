
from django.urls import path

from .views import build_list_view

urlpatterns = [
    path('', build_list_view),
]