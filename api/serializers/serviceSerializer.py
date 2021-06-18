"""Service Serializer"""

from rest_framework import serializers

from api.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """JSON serializer for Services"""

    class Meta:
        model = Service
        fields = ('id', 'name')
