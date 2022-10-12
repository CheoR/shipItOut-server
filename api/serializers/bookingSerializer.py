"""Booking Serializer"""

from rest_framework import serializers

from api.models import Booking
from api.serializers import (
    # PartialAppUserSerializer,
    PartialPortSerializer,
    PartialVoyageSerializer,
    PartialContainerSerializer,
)


class BookingSerializer(serializers.ModelSerializer):
	"""JSON serializer for Bookings"""

	# carrier = PartialAppUserSerializer()
	# agent = PartialAppUserSerializer()
	loading_port = PartialPortSerializer()
	unloading_port = PartialPortSerializer()
	voyage = PartialVoyageSerializer()

	status = serializers.SerializerMethodField()
	container_count = serializers.SerializerMethodField()
	product_count = serializers.SerializerMethodField()

	# Mon Feb 14 2022 14:29:07 GMT-0600 (Central Standard Time)	
#  "yyyy-MM-ddThh:mm" followed by optional ":ss" or ":ss.SSS".
	# pickup_appt = serializers.DateTimeField(format="yyyy-MM-ddThh:mm:ss.SSS")

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

		depth = 5

	def get_product_count(self, obj):
		return obj.product_count

	def get_container_count(self, obj):
		return obj.container_count

	def get_containers(self, obj):
		serializer = PartialContainerSerializer(obj.containers, many=True)
		return serializer.data
		
	def get_status(self, obj):
		"""Turn Enum choice status selection from number into human-readble string."""
		return obj.get_status_display()

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
