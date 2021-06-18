"""Voyage ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Voyage
from api.serializers import VoyageSerializer


class VoyageViewSet(ViewSet):
    """
        View module for handling requests about Voyages.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Voyage ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Voyage types.
        """

        user = request.auth.user
        print(user)

        try:
            voyages = Voyage.objects.all()
            serialzied_voyages = VoyageSerializer(
                voyages,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_voyages.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
