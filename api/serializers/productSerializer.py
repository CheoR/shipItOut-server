"""Product Serializer"""

from rest_framework import serializers

from api.models import Booking, Container, Product


class ProductBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('booking', )


class ProductContainerSerializer(serializers.ModelSerializer):
    booking = ProductBookingSerializer()

    class Meta:
        model = Container
        fields = ('container', 'booking', )

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('booking')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation


class ProductListViewSerializer(serializers.ModelSerializer):
    """JSON serializer for Products"""
    
    container = ProductContainerSerializer()

    class Meta:
        model = Product
        fields = '__all__'


    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('container')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation


class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for Products"""

    class Meta:
        model = Product
        fields = '__all__'
        # fields = (
        #     'id', 'commodity', 'weight', 'is_fragile', 'is_haz',
        #     'is_damaged', 'is_reefer', 'container',
        # )

        # depth = 3


class PartialProductSerializer(ProductSerializer):
    """JSON serializer for Products with some fields excluded"""

    class Meta:
        model = Product
        exclude = ('id', 'container', )
        depth = 1
