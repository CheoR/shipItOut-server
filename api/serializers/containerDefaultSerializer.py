"""Default Container Serializer"""

from rest_framework import serializers

from api.models import Container


class ContainerDefaultSerializer(serializers.ModelSerializer):
    """JSON serializer for Container"""

    class Meta:
        model = Container
        fields = '__all__'
        # fields = (
        #     'id', 'container', 'equipment_type', 'is_overweight',
        #     'equipment_location', 'is_damaged', 'is_needs_inspection',
        #     'is_in_use'
        # )
