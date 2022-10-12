"""Container ViewSet"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError

from django.http import HttpResponseServerError

from api.models import Container, Booking
from api.serializers import ContainerSerializer, ContainerListViewSerializer, ContainerDefaultSerializer, ContainerRetrieveViewSerializer


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
        
        booking = Booking.objects.get(pk=request.data['booking'])
        print('*' * 10, "passed data", '*' * 10)
        print(request.data)
        print('*' * 10, "passed data", '*' * 10)
        container = Container.objects.create(
            container=request.data['container'],
            equipment_size=request.data['equipment_size'],
            equipment_location=request.data['equipment_location'],
            is_need_inspection=request.data['is_need_inspection'],
            # is_overweight=request.data['is_overweight'],
            is_damaged=request.data['is_damaged'],
            booking=booking, # request.data['booking'],
        )

        serializer = ContainerSerializer(container)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Container

        Returns:
            Response -- JSON serialized Container instance
        """

        try:
            container = Container.objects.get(pk=pk)
            # container = Container.objects.get(pk__in=Booking.objects.filter(agent__user=request.auth.user))
            serializer = ContainerRetrieveViewSerializer(
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
        """

        try:
            # TODO: find better way to do this
            containers = Container.objects.filter(
                booking__in=Booking.objects.filter(
                    agent__user=request.auth.user
                )
            )

            # serialzied_containers = PartialContainerSerializer(
            # serialzied_containers = ContainerSerializer(
            serialzied_containers = ContainerListViewSerializer(
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

        booking = Booking.objects.get(pk=request.data['booking'])
        container = Container.objects.get(pk=pk)

        container.container = request.data['container']
        container.is_need_inspection = request.data['is_need_inspection']
        # container.is_overweight = request.data['is_overweight']
        container.is_damaged = request.data['is_damaged']

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
