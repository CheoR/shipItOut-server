"""Carrier ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import AppUser
from api.models import Carrier
from api.serializers import CarrierSerializer


class CarrierViewSet(ViewSet):
    """
        View module for handling requests about Carriers.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Carrier ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Carrier types.
        """

        user = request.auth.user
        print(user)

        try:
            carriers = Carrier.objects.all()
            serialzied_carriers = CarrierSerializer(
                carriers,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_carriers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
