"""Port ViewSet"""

from rest_framework import status
# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.http import HttpResponseServerError

from api.models import Port
from api.serializers import PortSerializer


class PortViewSet(ViewSet):
    """
        View module for handling requests about Ports.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Port ViewSet
    """

    def create(self, request):
        """Handle POST requests for single port

        Returns:
            Response -- JSON serialized port instance
        """

        port = Port.objects.create(
            name=request.data['name'],
            code=request.data['code'],
        )

        serializer = PortSerializer(port)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single port

        Returns:
            Response -- JSON serialized port instance
        """

        try:
            port = Port.objects.get(pk=pk)
            serializer = PortSerializer(
                port,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Port types.
        """

        try:
            ports = Port.objects.all()
            serialzied_ports = PortSerializer(
                ports,
                many=True,
                context={'request': request},
            )

            return Response(serialzied_ports.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an Port

        Returns:
            Response -- Empty body with 204 status code
        """

        port = Port.objects.get(pk=pk)
        
        port.name = request.data.get('name', port.name)
        port.code = request.data.get('code', port.code)

        port.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Port

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            port = Port.objects.get(pk=pk)
            port.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Port.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
