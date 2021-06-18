"""Port ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
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

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Port types.
        """

        user = request.auth.user
        print(user)

        try:
            ports = Port.objects.all()
            serialzied_ports = PortSerializer(
                ports,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_ports.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
