"""Product Serializer"""

from rest_framework import serializers

from api.models import Booking, Container, Product


class DefaultProductSerializer(serializers.ModelSerializer):
    """JSON serializer for Products
        {
        "id": 1,
        "product": "deletable toys",
        "weight": 100.55,
        "is_product_damaged": false,
        "is_fragile": false,
        "is_reefer": false,
        "is_hazardous": false,
        "product_notes": "delete this pretty shitty product",
        "container": null
    }
    """

    class Meta:
        model = Product
        fields = '__all__'
        # fields = (
        #     'id', 'product', 'weight', 'is_fragile', 'is_hazardous',
        #     'is_product_damaged', 'is_reefer', 'container',
        # )


class PartialProductSerializer(DefaultProductSerializer):
    """JSON serializer for Products with some fields excluded
        "id": 1,
    "product": "deletable toys",
    "weight": 100.55,
    "is_product_damaged": false,
    "is_fragile": false,
    "is_reefer": false,
    "is_hazardous": false,
    "product_notes": "delete this pretty shitty product",
    "container": {
        "id": 2,
        "container": "LCXB4731",
        "container_type": 2,
        "container_location": 1,
        "is_needs_inspection": true,
        "is_overweight": true,
        "is_container_damaged": true,
        "is_in_use": true,
        "container_notes": "<django.db.models.fields.TextField>",
        "booking": 1
    }
    """

    class Meta:
        model = Product
        fields = '__all__'
        depth = 5


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
    """JSON serializer for Products
        "id": 1,
        "product": "deletable toys",
        "weight": 100.55,
        "is_product_damaged": false,
        "is_fragile": false,
        "is_reefer": false,
        "is_hazardous": false,
        "product_notes": "delete this pretty shitty product",
        "container": "LCXB4731",
        "booking": "S2JAUKL4ZQ"
    """
    
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
