"""Booking Serializer"""

from rest_framework import serializers

from api.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """JSON serializer for Categories"""

    class Meta:
        model = Booking
        fields = ('id', 'user', 'booking', 'voyage_reference', 'container',
                  'loading_origin', 'unloading_destination', 'pickup_appt',
                  'port', 'port_cutoff', 'rail_cutoff', 'document', 'due',
                  'has_issue', 'booking_status', 'notes')
