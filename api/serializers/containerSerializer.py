"""Container Serializer"""

from rest_framework import serializers

from api.models import Booking, Container
from api.serializers import PartialProductSerializer


class ProductBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('booking', )


class ContainerProductSerializer(serializers.ModelSerializer):
    pass


class ContainerRetrieveViewSerializer(serializers.ModelSerializer):
    booking = ProductBookingSerializer()

    equipment_type_label = serializers.SerializerMethodField()
    equipment_location_label = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'

    def get_product_count(self, obj):
        return obj.product_count

    def get_equipment_type_label(self, obj):
        """Turn Enum choice equipment_type selection from number into human-readble string."""
        return obj.get_equipment_type_display()

    def get_equipment_location_label(self, obj):
        """Turn Enum choice equipment_location selection from number into human-readble string."""
        return obj.get_equipment_location_display()

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('booking')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation


class ContainerListViewSerializer(serializers.ModelSerializer):
    booking = ProductBookingSerializer()

    equipment_type = serializers.SerializerMethodField()
    equipment_location = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'

    def get_product_count(self, obj):
        return obj.product_count

    def get_equipment_type(self, obj):
        """Turn Enum choice equipment_type selection from number into human-readble string."""
        return obj.get_equipment_type_display()

    def get_equipment_location(self, obj):
        """Turn Enum choice equipment_location selection from number into human-readble string."""
        return obj.get_equipment_location_display()

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('booking')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation



class ContainerSerializer(serializers.ModelSerializer):
    """JSON serializer for Container"""
    
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'
        # fields = (
        #     'id', 'container', 'equipment_type', 'is_overweight',
        #     'equipment_location', 'is_container_damaged', 'is_needs_inspection',
        #     'is_in_use'
        # )

        depth = 5

    def get_product_count(self, obj):
        return obj.product_count


class PartialContainerSerializer(ContainerSerializer):
    """JSON serializer for Container with some fields excluded"""

    products = PartialProductSerializer(read_only=True, many=True)
    equipment_type = serializers.SerializerMethodField()
    equipment_location = serializers.SerializerMethodField()


    class Meta:
        model = Container
        fields = '__all__'
        # exclude = ('booking', )

        depth = 1

    def get_equipment_type(self, obj):
        """Turn Enum choice equipment_type selection from number into human-readble string."""
        return obj.get_equipment_type_display()

    def get_equipment_location(self, obj):
        """Turn Enum choice equipment_location selection from number into human-readble string."""
        return obj.get_equipment_location_display()
