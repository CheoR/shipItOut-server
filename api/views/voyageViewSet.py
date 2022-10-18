"""Voyage ViewSet"""

import string
import random

from rest_framework import status
# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from django.http import HttpResponseServerError

from api.models import Voyage, Vessel
from api.serializers import DefaultVoyageSerializer, VoyageSerializer, PartialVoyageSerializer


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

        try:
            vessel = Vessel.objects.get(pk=request.data['vessel'])
        except:
            vessel = None

        # so service and starting endpoint match up
        # e.g. all voyages starting at WC will be 1
        ENDPOINT = ['WC','EC','NE','SE','GU']
        start, end = random.sample([0, 1, 2, 3, 4], k=2)

        if (request.data.get('manual', False)):
            _voyage = request.data['voyage']
            _service = request.data['service']
        else:
            _voyage = ''.join([ENDPOINT[start], ENDPOINT[end]]) + ''.join(random.sample(string.digits, k=4))
            _service = request.data.get('service', start + 1)

        voyage = Voyage.objects.create(
            voyage=_voyage,
            service=_service,
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
            if(request.data.get('expand', False)):
                serializer = VoyageSerializer(
                    voyage,
                    context={'request': request},
                )
            else:
                serializer = DefaultVoyageSerializer(
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

            if(request.data.get('expand', False)):
                serializer = VoyageSerializer(
                    voyages,
                    many=True,
                    context={'request': request},
                )
            else:
                serializer = DefaultVoyageSerializer(
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

        try:
            vessel = Vessel.objects.get(pk=request.data['vessel'])
        except:
            vessel = None
        voyage.service = request.data.get('service', voyage.service)
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
