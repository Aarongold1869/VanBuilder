from django.conf import settings
from rest_framework import serializers

from components.models import Van

SELECT_ACTIONS = settings.SELECT_ACTIONS

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