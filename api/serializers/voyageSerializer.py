"""Voyage Serializer"""

from rest_framework import serializers

from api.models import Voyage


class VoyageSerializer(serializers.ModelSerializer):
    """JSON serializer for Voyages"""

    class Meta:
        model = Voyage
        fields = ('id', 'voyage', 'vessel')
