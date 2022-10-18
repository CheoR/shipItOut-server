"""Vessel ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.http import HttpResponseServerError

from api.models import Vessel
from api.serializers import DefaultVesselSerializer, VesselSerializer


class VesselViewSet(ViewSet):
    """
        View module for handling requests about Vessels.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Vessel ViewSet
    """

    def create(self, request):
        """Handle POST requests for single Vessel

        Returns:
            Response -- JSON serialized Vessel instance
        """

        vessel = Vessel.objects.create(
            # TODO: AUTO-GENERATE VESSEL NAMES WITH MOCKAROO API I MADE
            name=request.data['name'],
        )

        serializer = DefaultVesselSerializer(vessel)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Vessel

        Returns:
            Response -- JSON serialized Vessel instance
        """
        try:
            vessel = Vessel.objects.get(pk=pk)
            serializer = DefaultVesselSerializer(
                vessel,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Vessel types.
        """

        try:
            vessels = Vessel.objects.all()
            serialzied_vessels = DefaultVesselSerializer(
                vessels,
                many=True,
                context={'request': request},
            )

            return Response(serialzied_vessels.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an Vessel

        Returns:
            Response -- Empty body with 204 status code
        """

        vessel = Vessel.objects.get(pk=pk)
        
        vessel.name = request.data['name']
        vessel.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Vessel

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            vessel = Vessel.objects.get(pk=pk)
            vessel.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Vessel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
