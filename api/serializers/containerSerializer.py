"""Container Serializer"""

from rest_framework import serializers

from api.models import Booking, Container
from api.serializers import PartialProductSerializer


class DefaultContainerSerializer(serializers.ModelSerializer):
    """JSON serializer for Container
        "id": 22,
        "container": "IAMU4250",
        "container_type": 0,
        "container_location": 0,
        "is_needs_inspection": false,
        "is_overweight": false,
        "is_container_damaged": false,
        "is_in_use": false,
        "container_notes": "",
        "booking": null
    """

    class Meta:
        model = Container
        fields = '__all__'
        # fields = (
        #     'id', 'container', 'container_type', 'is_overweight',
        #     'container_location', 'is_damaged', 'is_needs_inspection',
        #     'is_in_use'
        # )


class ContainerSerializer(serializers.ModelSerializer):
    """JSON serializer for Container
 "id": 22,
    "product_count": 0,
    "container": "IAMU4250",
    "container_type": 0,
    "container_location": 0,
    "is_needs_inspection": false,
    "is_overweight": false,
    "is_container_damaged": false,
    "is_in_use": false,
    "container_notes": "",
    "booking": {
        "id": 2,
        "booking": "PBU3YJCQTZ",
        "unloading_destination_address": "456 unloading destination park",
        "loading_origin_address": "321 loading origin way",
        "pickup_address": "321 fake pickup street",
        "pickup_appt": "2022-10-13T09:07:16Z",
        "rail_cutoff": "2022-10-13T09:14:02Z",
        "port_cutoff": "2022-10-13T09:16:33Z",
        "delivery_address": "123 fake delivery street",
        "delivery_appt": "2022-10-13T09:17:23Z",
        "booking_status": 1,
        "are_documents_ready": true,
        "are_dues_paid": true,
        "has_issue": true,
        "booking_notes": "no booking notes",
        "agent": {
            ...
        },
        ...
    }
    """
    
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'
        depth = 5

    def get_product_count(self, obj):
        return obj.product_count


class ProductBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('booking', )


class ContainerProductSerializer(serializers.ModelSerializer):
    pass


class ContainerRetrieveViewSerializer(serializers.ModelSerializer):
    booking = ProductBookingSerializer()

    container_type_label = serializers.SerializerMethodField()
    container_location_label = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'

    def get_product_count(self, obj):
        return obj.product_count

    def get_container_type_label(self, obj):
        """Turn Enum choice container_type selection from number into human-readble string."""
        return obj.get_container_type_display()

    def get_container_location_label(self, obj):
        """Turn Enum choice container_location selection from number into human-readble string."""
        return obj.get_container_location_display()

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('booking')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation


class ContainerListViewSerializer(serializers.ModelSerializer):
    booking = ProductBookingSerializer()

    container_type = serializers.SerializerMethodField()
    container_location = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = '__all__'

    def get_product_count(self, obj):
        return obj.product_count

    def get_container_type(self, obj):
        """Turn Enum choice container_type selection from number into human-readble string."""
        return obj.get_container_type_display()

    def get_container_location(self, obj):
        """Turn Enum choice container_location selection from number into human-readble string."""
        return obj.get_container_location_display()

    def to_representation(self, obj):
        """Flatten key,values from one-level deep"""
        representation = super().to_representation(obj)

        cs_representation = representation.pop('booking')
        for key in cs_representation:
            representation[key] = cs_representation[key]
        return representation


class PartialContainerSerializer(ContainerSerializer):
    """JSON serializer for Container with some fields excluded
            "id": 3,
        "product_count": 0,
        "products": [],
        "container_type": "20ST",
        "container_location": 1,
        "container": "VWIK8214",
        "is_needs_inspection": true,
        "is_overweight": true,
        "is_container_damaged": true,
        "is_in_use": true,
        "container_notes": "<django.db.models.fields.TextField>",
        "booking": {
            "id": 1,
            "booking": "S2JAUKL4ZQ",
            "unloading_destination_address": "456 unloading destination park",
            "loading_origin_address": "321 loading origin way",
            "pickup_address": "321 fake pickup street",
            "pickup_appt": "2022-10-13T09:07:16Z",
            "rail_cutoff": "2022-10-13T09:14:02Z",
            "port_cutoff": "2022-10-13T09:16:33Z",
            "delivery_address": "123 fake delivery street",
            "delivery_appt": "2022-10-13T09:17:23Z",
            "booking_status": 1,
            "are_documents_ready": true,
            "are_dues_paid": true,
            "has_issue": true,
            "booking_notes": "no booking notes",
            "agent": 1,
            "carrier": 1,
            "voyage": 3,
            "loading_port": 3,
            "unloading_port": 2
        }
    """

    products = PartialProductSerializer(read_only=True, many=True)
    container_type = serializers.SerializerMethodField()
    container_location = serializers.SerializerMethodField()


    class Meta:
        model = Container
        fields = '__all__'
        # exclude = ('booking', )

        depth = 1

    def get_container_type(self, obj):
        """Turn Enum choice container_type selection from number into human-readble string."""
        return obj.get_container_type_display()

    def get_container_location(self, obj):
        """Turn Enum choice container_location selection from number into human-readble string."""
        return obj.get_container_location_display()


class ContainerTypesSerializer(serializers.ModelSerializer):
    """Container Types
    So frontend does not need a separate copy of possible container types.
    """

    container_type = serializers.SerializerMethodField()

    def get_container_type(self, obj):
        return [{"id": key, "container_type": value} for key, value in Container.EQUIPMENT_CHOICES]

    class Meta:
        model = Booking
        fields = ('container_type', )


class ContainerLocationsSerializer(serializers.ModelSerializer):
    """Container Locations
    So frontend does not need a separate copy of possible container locations.
    """

    container_location = serializers.SerializerMethodField()

    def get_container_location(self, obj):
        return [{"id": key, "container_location": value} for key, value in Container.LOCATION_CHOICES]


    class Meta:
        model = Booking
        fields = ('container_location',)
