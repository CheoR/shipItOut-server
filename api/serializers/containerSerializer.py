"""Container Serializer"""

from rest_framework import serializers

from api.models import Container


class ContainerSerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""

    class Meta:
        model = Container
        fields = ('id', 'container', 'equipment_size',
                  'container_status', 'is_damaged', 'is_need_inspection',
                  'is_in_use', 'notes')
