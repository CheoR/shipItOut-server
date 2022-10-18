"""Vessel Serializer"""

from rest_framework import serializers

from api.models import Vessel


class DefaultVesselSerializer(serializers.ModelSerializer):
    """JSON serializer for Vessels"""

    class Meta:
        model = Vessel
        fields = '__all__'
        # fields = (
        #     'id', 'name',
        # )


class VesselSerializer(serializers.ModelSerializer):
    """JSON serializer for Vessels"""

    class Meta:
        model = Vessel
        fields = '__all__'
        depth = 5


class ParitalVesselSerializer(VesselSerializer):
    """JSON serializer for Vessels with some fields excluded
    {
        "id": 10,
        "service": "WC",
        "voyage": "WCWC2283",
        "vessel_name": "Struthio camelus"
    }
    {
    "id": 10,
    "service": "WC",
    "voyage": "WCWC2283"
    }
    """

    class Meta:
        model = Vessel
        # fields = '__all__'
        exclude = ('id', 'name', )
