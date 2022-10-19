"""BookingCreate ViewSet"""

import random
import string

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.http import HttpResponseServerError

from api.models import (
	AppUser,
	Booking,
	Port,
	Voyage,
)

from api.serializers import DefaultBookingSerializer, BookingSerializer


class BookingViewSet(ViewSet):
	"""
		View module for handling requests about Booking.
		ViewSet handles GET, POST, PUT, DELETE requests sent from client
		over HTTP protocol.

		BookingCreate ViewSet
	"""

	# permission_classes = (IsAuthenticatedOrReadOnly,)

	def create(self, request):
		"""
			Handle GET requests to get all categories resources.
			Returns:
				Response : JSON serialized list of Booking types.
		"""

		agent = AppUser.objects.get(user=request.auth.user)
		voyage = Voyage.objects.get(pk=request.data['voyage'])
		carrier = AppUser.objects.get(pk=request.data['carrier'])
		loading_port = Port.objects.get(pk=request.data['loading_port'])
		unloading_port = Port.objects.get(pk=request.data['unloading_port'])

		booking = Booking.objects.create(
			# TODO: User Generator
			booking=''.join(random.sample(
				string.ascii_uppercase + string.digits, k=10)),
			unloading_destination_address=request.data['unloading_destination_address'],
			loading_origin_address=request.data['loading_origin_address'],
			pickup_address=request.data['pickup_address'],
			pickup_appt=request.data['pickup_appt'],
			rail_cutoff=request.data['rail_cutoff'],
			port_cutoff=request.data['port_cutoff'],
			delivery_address=request.data['delivery_address'],
			delivery_appt=request.data['delivery_appt'],
			booking_status=1, # Booking.PENDING
			are_documents_ready=request.data['are_documents_ready'],
			are_dues_paid=request.data['are_dues_paid'],
			has_issue=request.data['has_issue'],
			booking_notes=request.data['booking_notes'],
			agent=agent,
			carrier=carrier,
			voyage=voyage,
			loading_port=loading_port,
			unloading_port=unloading_port,
		)

		try:
			serializer = DefaultBookingSerializer(
				booking,
				context={'request': request},
			)

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		except ValidationError as ex:
			return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""Handle GET requests for single Booking

		Returns:
			Response -- JSON serialized Booking instance
		"""

		try:
			booking = Booking.objects.get(pk=pk)
			if (request.data.get('expand')):
				serializer = BookingSerializer(
					booking,
					context={'request': request},
				)
			else:
				serializer = DefaultBookingSerializer(
					booking,
					context={'request': request},
				)

			return Response(serializer.data)
		except Exception as ex:
			return HttpResponseServerError(ex)

	def list(self, request):
		"""
			Handle GET requests to get all categories resources.
			Returns:
				Response : JSON serialized list of Booking types.
		"""

		try:
			agent = AppUser.objects.get(user=request.auth.user)
			bookings = Booking.objects.filter(agent=agent) # agent__user=request.auth.user)

			serialzier = BookingSerializer(
				bookings,
				many=True,
				context={'request': request},
			)

			return Response(serialzier.data)
		except Exception as ex:
			return HttpResponseServerError(ex)

	def update(self, request, pk=None):
		"""Handle PUT requests for an Booking

		Returns:
			Response -- Empty body with 204 status code
		"""

		booking = Booking.objects.get(pk=pk)

		_carrier = request.data.get('carrier', booking.carrier.id)
		_voyage = request.data.get('voyage', booking.voyage.id)
		_loading_port = request.data.get('loading_port', booking.loading_port.id)
		_unloading_port = request.data.get('unloading_port', booking.unloading_port.id)

		agent = AppUser.objects.get(user=request.auth.user) # pk=request.data['agent'])
		carrier = AppUser.objects.get(pk=_carrier)
		voyage = Voyage.objects.get(pk=_voyage)
		loading_port = Port.objects.get(pk=_loading_port)
		unloading_port = Port.objects.get(pk=_unloading_port)

		booking.unloading_destination_address = request.data.get('unloading_destination_address', booking.unloading_destination_address)
		booking.loading_origin_address = request.data.get('loading_origin_address', booking.loading_origin_address)
		booking.pickup_address = request.data.get('pickup_address', booking.pickup_address)
		booking.pickup_appt = request.data.get('pickup_appt', booking.pickup_appt)
		booking.rail_cutoff = request.data.get('rail_cutoff', booking.rail_cutoff)
		booking.port_cutoff = request.data.get('port_cutoff', booking.port_cutoff)
		booking.has_issue = request.data.get('has_issue', booking.has_issue)
		booking.delivery_address = request.data.get('delivery_address', booking.delivery_address)
		booking.delivery_appt = request.data.get('delivery_appt', booking.delivery_appt)
		booking.booking_status = request.data.get('booking_status', booking.booking_status)
		booking.are_documents_ready = request.data.get('are_documents_ready', booking.are_documents_ready)
		booking.are_dues_paid = request.data.get('are_dues_paid', booking.are_dues_paid)
		booking.booking_notes = request.data.get('booking_notes', booking.booking_notes)

		booking.agent = agent
		booking.carrier = carrier
		booking.voyage = voyage
		booking.loading_port = loading_port
		booking.unloading_port = unloading_port

		booking.save()

		return Response({}, status=status.HTTP_204_NO_CONTENT)

	def destroy(self, request, pk=None):
		"""Handle DELETE requests for a single Voyage

		Returns:
			Response -- 200, 404, or 500 status code
		"""

		try:
			booking = Booking.objects.get(pk=pk)
			booking.delete()

			return Response({}, status=status.HTTP_204_NO_CONTENT)

		except Booking.DoesNotExist as ex:
			return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

		except Exception as ex:
			return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	@action(methods=['GET'], detail=False)
	def available_bookings(self, request):
		"""
			Handle GET requests to get available bookings.
			Returns:
				Response : JSON serialized list of Booking types.
		"""

		try:
			bookings = Booking.objects.filter(agent__user=request.auth.user)

			serializer = DefaultBookingSerializer(
				bookings,
				many=True,
				context={'request': request},
			)

			return Response(serializer.data)
		except Exception as ex:
			return HttpResponseServerError(ex)
