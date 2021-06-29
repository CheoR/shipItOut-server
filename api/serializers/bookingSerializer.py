"""Booking Serializer"""

# from api.models.port import Port
# from api.models.document import Document
# from api.models.due import Due
# from api.models.carrier import Carrier
# from api.models.bkgstatus import BkgStatus
from rest_framework import serializers

from api.models import Booking  # , BkgStatus


# class BkgStatusSerializer(serializers.ModelSerializer):

#     # rename field
#     booking_status = serializers.CharField(source="status")

#     class Meta:
#         model = BkgStatus
#         fields = ('booking_status',)


# class CarrierSerializer(serializers.ModelSerializer):

#     carrier = serializers.CharField(source="name")

#     class Meta:
#         model = Carrier
#         fields = ('carrier',)


# class PortSerializer(serializers.ModelSerializer):

#     port_name = serializers.CharField(source="name")
#     port_location = serializers.CharField(source="location")
#     port_code = serializers.CharField(source="code")

#     class Meta:
#         model = Port
#         fields = ('port_name', 'port_location', 'port_code', )


# class DuesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Due
#         fields = ('are_dues_paid',)


# class DocumentsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Document
#         fields = ('are_docs_ready',)


class BookingSerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""

    # booking_status = BkgStatusSerializer()
    # carrier = CarrierSerializer()
    # due = DuesSerializer()
    # document = DocumentsSerializer()
    # port = PortSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'user', 'booking', 'voyage_reference', 'container',
                  'loading_origin', 'unloading_destination', 'pickup_appt',
                  'port', 'port_cutoff', 'rail_cutoff', 'document', 'due',
                  'has_issue', 'booking_status', 'notes')

        depth = 5
