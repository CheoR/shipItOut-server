"""Port Serializer"""

from rest_framework import serializers

from api.models import Port


class PortSerializer(serializers.ModelSerializer):
    """JSON serializer for Ports"""

    class Meta:
        model = Port
        fields = '__all__'
        # fields = (
        #     'id', 'name', 'code',
        # )

        depth = 5


class PartialPortSerializer(PortSerializer):
    """JSON serializer for Ports with some fields excluded"""

    class Meta:
        model = Port
        exclude = ('id', )
