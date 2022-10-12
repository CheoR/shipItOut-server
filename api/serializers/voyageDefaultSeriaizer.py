"""Default Voyage Serializer"""

from rest_framework import serializers

from api.models import Voyage


class VoyageSerializer(serializers.ModelSerializer):
    """JSON serializer for Voyages"""

    class Meta:
        model = Voyage
        fields = '__all__'
        # fields = (
        #     'id', 'voyage', 'service', 'vessel',
        # )
