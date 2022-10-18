"""Vessel Serializer"""

from rest_framework import serializers

from api.models import Vessel


class DefaultVesselSerializer(serializers.ModelSerializer):
    """JSON serializer for Vessels"""

    class Meta:
        model = Vessel


class VesselSerializer(serializers.ModelSerializer):
    """JSON serializer for Vessels"""

    class Meta:
        model = Vessel
        fields = '__all__'
        # fields = (
        #     'id', 'name',
        # )

        depth = 5


class ParitalVesselSerializer(VesselSerializer):
    """JSON serializer for Vessels with some fields excluded"""

    class Meta:
        model = Vessel
        exclude = ('id', 'name', )
