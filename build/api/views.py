from django.conf import settings 

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from components.models import Van
from build.models import Build

@api_view(['POST'])
def build_create_view(request, *args, **kwargs):
    serializer = BuildCreateSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = request.user)
        data = serializer.validated_data
        build_id = data.get('id')
        request.session['build_id'] = build_id
        return Response(serializer.data, status=201)
    return Response({}, status=400)
    
@api_view(['GET'])
def build_list_view(request, *args, **kwargs):
    qs = Build.objects.filter(user=request.user)
    if not qs.exists():
        return Response({}, status=204)
    serializer = BuildListSerializer(qs, context={"request":request}, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET','POST'])
def build_select_view(request, *args, **kwargs):
    serializer = VehicleSelectSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        build_id = data.get('id')
        qs = Build.objects.filter(id=build_id) 
        if not qs.exists():
            return Response({}, status=404) 
    request.session['build_id'] = build_id
    return Response({}, status=201)

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
    build_id = request.session.get('build_id')
    build = Build.objects.get(id=build_id)
    serializer = VehicleSelectSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        van_id = data.get('id')
        action = data.get('action')
        qs = Van.objects.filter(id=van_id)
        if not qs.exists():
            return Response({}, status=404) 
        van = qs.first()
        if action == 'select':
            build.vehicle = van
            build.save()
        else:
            build.vehicle = None
            build.save()
    return Response({}, status=201)
