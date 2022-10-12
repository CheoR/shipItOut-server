"""Voyage ViewSet"""

from rest_framework import status
# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from django.http import HttpResponseServerError

from api.models import Voyage, Vessel
from api.serializers import VoyageSerializer, PartialVoyageSerializer


class VoyageViewSet(ViewSet):
    """
        View module for handling requests about Voyages.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Voyage ViewSet
    """

    def create(self, request):
        """Handle POST requests for single Voyage

        Returns:
            Response -- JSON serialized Voyage instance
        """

        vessel = Vessel.objects.get(pk=request.data['vessel'])

        voyage = Voyage.objects.create(
            voyage=request.data['voyage'],
            service=request.data['service'],
            vessel=vessel,
        )
    
        serializer = VoyageSerializer(voyage)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Voyage

        Returns:
            Response -- JSON serialized Voyage instance
        """

        try:
            voyage = Voyage.objects.get(pk=pk)
            serializer = VoyageSerializer(
                voyage,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all Voyage resources.
            Returns:
                Response : JSON serialized list of Voyage types.
        """

        try:
            voyages = Voyage.objects.all()
            serializer = VoyageSerializer(
                voyages,
                many=True,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an Voyage

        Returns:
            Response -- Empty body with 204 status code
        """

        voyage = Voyage.objects.get(pk=pk)
        vessel = Vessel.objects.get(pk=request.data['vessel'])
        
        voyage.voyage = request.data['voyage']
        voyage.service = request.data['service']
        voyage.vessel = vessel

        voyage.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Voyage

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            voyage = Voyage.objects.get(pk=pk)
            voyage.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Voyage.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def just_voyages(self, request):
        """
            Handle GET requests to get available voyages.
            Returns:
                Response : JSON serialized list of User types.
        """

        try:
            voyages = Voyage.objects.all()

            serializer = PartialVoyageSerializer(
                voyages,
                many=True,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
