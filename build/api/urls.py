from django.conf import settings
from django.urls import path
from .views import *

'''
CLIENT
Base ENDPOINT /api/build/
'''
urlpatterns = [
    path('vehicles/', vehicle_list_view),
    path('vehicles/<int:van_id>/', vehicle_detail_view)
] 
