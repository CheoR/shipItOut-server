"""Port Serializer"""

from rest_framework import serializers

from api.models import Port


class PortSerializer(serializers.ModelSerializer):
    """JSON serializer for Ports"""

    class Meta:
        model = Port
        fields = ('id', 'name', 'location', 'code')
