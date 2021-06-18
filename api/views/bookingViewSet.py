"""Booking ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Booking
from api.serializers import BookingSerializer


class BookingViewSet(ViewSet):
    """
        View module for handling requests about bookings.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Booking ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Booking types.
        """

        user = request.auth.user
        print(user)

        try:
            bookings = Booking.objects.all()
            serialzied_bookings = BookingSerializer(
                bookings,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_bookings.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
