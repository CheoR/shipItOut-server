"""Product Serializer"""

from api.serializers.containerSerializer import ContainerSerializer
from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for Products"""

    container = ContainerSerializer()

    class Meta:
        model = Product
        fields = ('id', 'commodity', 'weight', 'is_fragile', 'is_haz',
                  'is_damaged', 'is_reefer', 'container')

        # depth = 3

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)
        cs_representation = representation.pop('container')
        for key in cs_representation:
            if key == 'id':
                continue
            representation[key] = cs_representation[key]

        return representation
