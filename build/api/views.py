from django.conf import settings 

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VehicleListSerializer, VehicleSerializer, VehicleSelectSerializer
from components.models import Van
from build.models import Build

def get_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_qs = paginator.paginate_queryset(qs, request) 
    serializer = VehicleListSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data) 

@api_view(['GET'])
def vehicle_list_view(request, *args, **kwargs):
    qs = Van.objects.all()
    return get_paginated_queryset_response(qs, request)

@api_view(['GET'])
def vehicle_detail_view(request, van_id, *args, **kwargs):
    qs = Van.objects.filter(id=van_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = VehicleSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['GET','POST'])
def vehicle_select_view(request, *args, **kwargs):
    user = request.user
    serializer = VehicleSelectSerializer(data=request.data) # get user inut to determine action
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        van_id = data.get('id')
        action = data.get('action')
        qs = Van.objects.filter(id=van_id) # does stock exist
        if not qs.exists():
            return Response({}, status=404) 
        van = qs.first()
        if action == 'select':
            Build.objects.get_or_create
        else:
