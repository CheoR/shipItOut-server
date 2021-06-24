"""Container Serializer"""

from api.serializers.cntrstatusSerializer import CntrStatusSerializer
from rest_framework import serializers

from api.models import Container


class ContainerSerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""

    container_status = CntrStatusSerializer()

    class Meta:
        model = Container
        fields = ('id', 'container', 'equipment_size',
                  'container_status', 'is_damaged', 'is_need_inspection',
                  'is_in_use', 'notes')
        # depth = 5

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)
        cs_representation = representation.pop('container_status')
        for key in cs_representation:
            if key == 'id':
                continue
            representation[key] = cs_representation[key]

        return representation
