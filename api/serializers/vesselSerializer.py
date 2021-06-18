"""Vessel Serializer"""

from rest_framework import serializers

from api.models import Vessel


class VesselSerializer(serializers.ModelSerializer):
    """JSON serializer for Vessels"""

    class Meta:
        model = Vessel
        fields = ('id', 'name', 'longitude', 'latitude', 'service')
