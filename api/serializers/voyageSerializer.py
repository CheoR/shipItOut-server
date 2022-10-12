"""Voyage Serializer"""

from rest_framework import serializers

from api.models import Voyage
from api.serializers import ParitalVesselSerializer


class VoyageSerializer(serializers.ModelSerializer):
    """JSON serializer for Voyages"""

    class Meta:
        model = Voyage
        fields = '__all__'
        # fields = (
        #     'id', 'voyage', 'service', 'vessel',
        # )

        depth = 5


class PartialVoyageSerializer(VoyageSerializer):
    """JSON serializer for Voyages with some fields excluded"""
    
    service = serializers.SerializerMethodField()
    vessel = ParitalVesselSerializer()

    class Meta:
        model = Voyage
        # exclude = ('id', )
        fields = '__all__'
        depth = 1

    def get_service(self, obj):
        """Turn Enum choice Service selection from number into human-readble string."""
        return obj.get_service_display()

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)
        cs_representation = representation.pop('vessel')
        for key in cs_representation:
            if key == 'id':
                continue
            representation['vessel_' + key] = cs_representation[key]

        return representation
