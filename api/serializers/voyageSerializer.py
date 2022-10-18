"""Voyage Serializer"""

from rest_framework import serializers

from api.models import Voyage
from api.serializers import ParitalVesselSerializer


class DefaultVoyageSerializer(serializers.ModelSerializer):
    """Default JSON serializer for Voyages
        "id": 10,
        "voyage": "WCWC2283",
        "service": 1,
        "vessel": 9
    """

    class Meta:
        model = Voyage
        fields = '__all__'


class VoyageSerializer(serializers.ModelSerializer):
    """Expanded JSON serializer for Voyages and nested vessel.
        "id": 10,
        "voyage": "WCWC2283",
        "service": 1,
        "vessel": {
            "id": 9,
            "name": "Struthio camelus"
        }
    """

    class Meta:
        model = Voyage
        fields = '__all__'
        depth = 5


class PartialVoyageSerializer(VoyageSerializer):
    """Expand and stringify JSON serializer for Voyages
        "id": 10,
        "service": "WC",
        "voyage": "WCWC2283"
    """
    
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
