"""Product Serializer"""

from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for Products"""

    class Meta:
        model = Product
        fields = ('id', 'commodity', 'weight', 'is_fragile', 'is_haz',
                  'is_damaged', 'is_reefer', 'container')
