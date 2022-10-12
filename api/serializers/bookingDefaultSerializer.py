"""Default Booking Serializer"""

from rest_framework import serializers

from api.models import Booking


class BookingDefaultSerializer(serializers.ModelSerializer):
	"""JSON serializer for Bookings"""

	class Meta:
		model = Booking
		fields = '__all__'
		# fields = (
		# 	'id', 'agent', 'carrier', 'voyage', 'container',
		# 	'loading_port', 'unloading_port', 'notes', 'has_issue',
		# 	'are_docs_ready', 'are_dues_paid', 'status', 'unloading_destination',
		# 	'loading_origin', 'pickup_address', 'pickup_appt', 'delivery_address',
		# 	'delivery_appt', 'port_cutoff', 'rail_cutoff',
		# )
