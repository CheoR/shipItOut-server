"""Booking ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Booking, AppUser
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

        user = AppUser.objects.get(user=request.auth.user)
        bookings = Booking.objects.filter(user=user)

        try:
            serialzied_bookings = BookingSerializer(
                bookings,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_bookings.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Booking types.
        """
        print("In retrieve")
        try:
            user = AppUser.objects.get(user=request.auth.user)
            booking = Booking.objects.get(user=user, pk=pk)
            print(booking)
            serialzied_booking = BookingSerializer(
                booking,
                many=False,
                context=({'request': request})
            )

            print("seraiized booking ")
            print(serialzied_booking)
            return Response(serialzied_booking.data)
        except Booking.DoesNotExist as ex:
            return Resposnse({'message': 'The requested order does not exist, or you do not have permission to access it.'},
                             status=status.HTTP_404_NOT_FOUND
                             )
        except Exception as ex:
            return HttpResponseServerError(ex)
