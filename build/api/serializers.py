from build.models import User
from django.conf import settings
from rest_framework import serializers

from components.models import Van
from ..models import Build

from datetime import datetime
import os

SELECT_ACTIONS = settings.SELECT_ACTIONS

class BuildCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = [
            'user',
            'title', 
            'vehicle', 
            'budget',
        ]

class BuildListSerializer(serializers.ModelSerializer):
    build_title = serializers.SerializerMethodField(read_only=True)
    vehicle_info = serializers.SerializerMethodField(read_only=True)
    last_updated = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Build
        fields = [
            'id',
            'build_title', 
            'vehicle_info', 
            'budget',
            'last_updated',
            'image'
        ]
    
    def get_build_title(self, obj):
        return obj.title.upper()

    def get_vehicle_info(self, obj):
        make = obj.vehicle.make
        model = obj.vehicle.model
        year = obj.vehicle.year
        van_type = obj.vehicle.van_type
        wheelbase = obj.vehicle.wheelbase
        return year + ' ' + make + ' ' + model + ' ' + van_type + ' ' + str(wheelbase) + '"'

    def get_last_updated(self, obj):
        last_updated = datetime.strftime(obj.updated,"%m/%d/%Y")
        return last_updated

    def get_image(self, obj):
        request = self.context.get('request')
        host = request._current_scheme_host
        image_url = os.path.join(settings.MEDIA_URL, obj.vehicle.image.url)
        return host + image_url

class BuildSelectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in SELECT_ACTIONS:
            raise serializers.ValidationError("Not a valid action for post.")
        return value

class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Van
        fields = [
            'make',
            'model',
            'van_type',
            'year',
            'wheelbase',
            'price_new',
            'price_used',
            'max_weight',
        ]

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Van
        fields = [
            'make',
            'model', 
            'year',
            'van_type',
            'wheelbase',
            'price_new',
            'price_used',
            'max_weight',
            'engine',
            'transmission',
            'drive',
            'fuel_capacity',
            'mpg',
            'cargo_width',
            'cargo_height',
            'cargo_length',
            'external_width', 
            'external_height', 
            'external_length', 
            'passengers', 
        ]

class VehicleSelectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in SELECT_ACTIONS:
            raise serializers.ValidationError("Not a valid action for post.")
        return value