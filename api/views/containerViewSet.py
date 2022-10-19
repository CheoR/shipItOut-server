"""Container ViewSet"""
import random
import string

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseServerError

from api.models import Container, Booking
from api.serializers import DefaultContainerSerializer, ContainerSerializer, PartialContainerSerializer, ContainerListViewSerializer, ContainerRetrieveViewSerializer


class ContainerViewSet(ViewSet):
    """
        View module for handling requests about Containers.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Container ViewSet
    """
    
    def create(self, request):
        """
            Handle POST requests to post container resource.
            Returns:
                Response : JSON serialized single Container types.
        """
        try:
            booking = Booking.objects.get(pk=request.data['booking'])
        except:
            booking = None

        # TODO: MAKE SURE SERAIZLIERS WORK FOR CONTAINERS AND NESTED DATA
        container = Container.objects.create(
            container=''.join(random.sample(string.ascii_uppercase, k=4)) + ''.join(random.sample(string.digits, k=4)),
            container_type=request.data.get('container_type', 0),
            container_location=request.data.get('container_location', 0),
            is_container_damaged=request.data.get('is_container_damaged', False),
            is_needs_inspection=request.data.get('is_needs_inspection', False),
            is_overweight=request.data.get('is_overweight', False),
            is_in_use=False,
            container_notes=request.data.get('container_notes', ''),
            booking=booking,
        )

        serializer = DefaultContainerSerializer(container)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Container

        Returns:
            Response -- JSON serialized Container instance
        """

        try:
            container = Container.objects.get(pk=pk)
            # TODO: ADD EXPAND HERE
            # container = Container.objects.get(pk__in=Booking.objects.filter(agent__user=request.auth.user))
            # serializer = ContainerRetrieveViewSerializer(
            if (request.data.get('expand', False)):
                serializer = ContainerSerializer(
                    container,
                    context={'request': request},
                )
            else:
                serializer = DefaultContainerSerializer(
                container,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all container resources.
            Returns:
                Response : JSON serialized list of Container types.
            "id": 3,
            "container_type": "20ST",
            "container_location": 1,
            "product_count": 0,
            "container": "VWIK8214",
            "is_needs_inspection": true,
            "is_overweight": true,
            "is_container_damaged": true,
            "is_in_use": true,
            "container_notes": "<django.db.models.fields.TextField>",
            "booking": "S2JAUKL4ZQ"
        """

        try:
            # TODO: find better way to do this
            containers = Container.objects.filter(
                booking__in=Booking.objects.filter(
                    agent__user=request.auth.user
                )
            )

            if(request.data.get('expand', False)):
                serialzied_containers = PartialContainerSerializer(
                    containers,
                    many=True,
                    context={'request': request},
                )
            else:
                serialzied_containers = DefaultContainerSerializer(
                    containers,
                    many=True,
                    context={'request': request},
                )

            return Response(serialzied_containers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an Container

        Returns:
            Response -- Empty body with 204 status code
        """

        try:
            booking = Booking.objects.get(pk=request.data['booking'])
        except:
            booking = None
        container = Container.objects.get(pk=pk)

        container.container_location = request.data.get('container_location', container.container_location)
        container.is_in_use = request.data.get('is_in_use', container.is_in_use)
        container.is_container_damaged = request.data.get('is_container_damaged', container.is_container_damaged)
        container.is_needs_inspection = request.data.get('is_needs_inspection', container.is_needs_inspection)
        container.is_overweight = request.data.get('is_overweight', container.is_overweight)
        container.container_notes = request.data.get('container_notes', container.container_notes)

        container.booking = booking

        container.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Container

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            container = Container.objects.get(pk=pk)
            container.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Container.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def available_containers(self, request):
        """
            Handle GET requests to get available containers.
            Returns:
                Response : JSON serialized list of Container types.
        """

        try:
            # TODO: find better way to do this
            containers = Container.objects.filter(
                booking__in=Booking.objects.filter(
                    agent__user=request.auth.user
                )
            )

            serializer = ContainerDefaultSerializer(
                containers,
                many=True,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
