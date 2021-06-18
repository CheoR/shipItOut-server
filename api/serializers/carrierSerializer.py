"""Carrier Serializer"""
from rest_framework import serializers

from api.models import Carrier


class CarrierSerializer(serializers.ModelSerializer):
    """JSON serializer for Carriers"""

    class Meta:
        model = Carrier
        fields = ('id', 'name')
