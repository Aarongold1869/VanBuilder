from django.conf import settings
from django.urls import path
from .views import *

'''
CLIENT
Base ENDPOINT /api/build/
'''
urlpatterns = [
    path('list/', build_list_view),
    path('create/', build_create_view),
    path('select/', build_select_view),
    path('vehicles/', vehicle_list_view),
    path('vehicles/<int:van_id>/', vehicle_detail_view),
    path('vehicles/select', vehicle_select_view),
] 
