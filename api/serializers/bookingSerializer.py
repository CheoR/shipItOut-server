"""Booking Serializer"""

from rest_framework import serializers

from api.models import Booking
from api.serializers import (
    PartialAppUserSerializer,
    PartialPortSerializer,
    PartialVoyageSerializer,
    PartialContainerSerializer,
)


class DefaultBookingSerializer(serializers.ModelSerializer):
	"""JSON serializer for Bookings
		"id": 16,
		"booking": "2XGK9ATB07",
		"unloading_destination_address": "456 unloading destination park",
		"loading_origin_address": "321 loading origin way",
		"pickup_address": "321 fake pickup street",
		"pickup_appt": "2022-10-13T09:07:16Z",
		"rail_cutoff": "2022-10-13T09:14:02Z",
		"port_cutoff": "2022-10-13T09:16:33Z",
		"delivery_address": "123 fake delivery street",
		"delivery_appt": "2022-10-13T09:17:23Z",
		"booking_status": 3,
		"are_documents_ready": false,
		"are_dues_paid": false,
		"has_issue": false,
		"booking_notes": "oink oink moo cow will delete",
		"agent": 1,
		"carrier": 2,
		"voyage": 2,
		"loading_port": 4,
		"unloading_port": 5
	"""

	class Meta:
		model = Booking
		fields = '__all__'
		# fields = (
		# 	'id', 'agent', 'carrier', 'voyage', 'container',
		# 	'loading_port', 'unloading_port', 'notes', 'has_issue',
		# 	'are_documents_ready', 'are_dues_paid', 'status', 'unloading_destination_address',
		# 	'loading_origin_address', 'pickup_address', 'pickup_appt', 'delivery_address',
		# 	'delivery_appt', 'port_cutoff', 'rail_cutoff',
		# )


class BookingSerializer(serializers.ModelSerializer):
	"""JSON serializer for Bookings
		"id": 16,
		"booking_status": "CLOSED",
		"container_count": 0,
		"product_count": 0,
		"booking": "2XGK9ATB07",
		"unloading_destination_address": "456 unloading destination park",
		"loading_origin_address": "321 loading origin way",
		"pickup_address": "321 fake pickup street",
		"pickup_appt": "2022-10-13T09:07:16Z",
		"rail_cutoff": "2022-10-13T09:14:02Z",
		"port_cutoff": "2022-10-13T09:16:33Z",
		"delivery_address": "123 fake delivery street",
		"delivery_appt": "2022-10-13T09:17:23Z",
		"are_documents_ready": false,
		"are_dues_paid": false,
		"has_issue": false,
		"booking_notes": "oink oink moo cow will delete",
		"loading_port_name": "brownsville",
		"loading_port_code": "USBRV",
		"unloading_port_name": "stockton",
		"unloading_port_code": "USSTK",
		"service": "EC",
		"voyage": "WCWC8028",
		"carrier_first_name": "carrier2",
		"carrier_last_name": "carrier2",
		"carrier_username": "carrier2",
		"carrier_email": "carrier2@carrier.com",
		"carrier_account_type": "CARRIER",
		"carrier_company": "carrier2 carrier",
		"carrier_role": "driver",
		"carrier_phone": "123-456-7890",
		"agent_first_name": "peggy",
		"agent_last_name": "pug",
		"agent_username": "peggypug",
		"agent_email": "peggy@pug.com",
		"agent_account_type": "WAREHOUSE",
		"agent_company": "pug transport",
		"agent_role": "ops",
		"agent_phone": "615-123-4567"
	"""

	carrier = PartialAppUserSerializer()
	agent = PartialAppUserSerializer()
	loading_port = PartialPortSerializer()
	unloading_port = PartialPortSerializer()
	voyage = PartialVoyageSerializer()

	booking_status = serializers.SerializerMethodField()
	container_count = serializers.SerializerMethodField()
	product_count = serializers.SerializerMethodField()

	# Mon Feb 14 2022 14:29:07 GMT-0600 (Central Standard Time)	
	#  "yyyy-MM-ddThh:mm" followed by optional ":ss" or ":ss.SSS".
	# pickup_appt = serializers.DateTimeField(format="yyyy-MM-ddThh:mm:ss.SSS")

	class Meta:
		model = Booking
		fields = '__all__'
		depth = 5

	def get_product_count(self, obj):
		return obj.product_count

	def get_container_count(self, obj):
		return obj.container_count

	def get_containers(self, obj):
		serializer = PartialContainerSerializer(obj.containers, many=True)
		return serializer.data
		
	def get_booking_status(self, obj):
		"""Turn Enum choice status selection from number into human-readble string."""
		return obj.get_booking_status_display()

	def to_representation(self, obj):
		"""Flatten key,values from one-level deep"""
		representation = super().to_representation(obj)
		cs_representation = representation.pop('loading_port')
		for key in cs_representation:
			if key == 'id':
				continue
			representation['loading_port_' + key] = cs_representation[key]
		cs_representation = representation.pop('unloading_port')
		for key in cs_representation:
			if key == 'id':
				continue
			representation['unloading_port_' + key] = cs_representation[key]
		cs_representation = representation.pop('voyage')
		for key in cs_representation:
			if key == 'id':
				continue
			representation[key] = cs_representation[key]
		cs_representation = representation.pop('carrier')
		for key in cs_representation:
			if key == 'id':
				continue
			representation['carrier_' + key] = cs_representation[key]
		cs_representation = representation.pop('agent')
		for key in cs_representation:
			if key == 'id':
				continue
			representation['agent_' + key] = cs_representation[key]
		return representation


class BookingStatusesSerializer(serializers.ModelSerializer):
	"""Booking Statuses
	So frontend does not need a separate copy of possible statuses.
	"""

	booking_status = serializers.SerializerMethodField()

	def get_booking_status(self, obj):
		return [{"id": key, "booking_status": value} for key, value in Booking.BOOKING_STATUS_CHOICES]

	class Meta:
		model = Booking
		fields = ('booking_status',)



