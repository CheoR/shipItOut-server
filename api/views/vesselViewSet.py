"""Vessel ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Vessel
from api.serializers import VesselSerializer


class VesselViewSet(ViewSet):
    """
        View module for handling requests about Vessels.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Vessel ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Vessel types.
        """

        user = request.auth.user
        print(user)

        try:
            vessels = Vessel.objects.all()
            serialzied_vessels = VesselSerializer(
                vessels,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_vessels.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
