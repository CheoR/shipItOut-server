"""Container ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Container
from api.serializers import ContainerSerializer


class ContainerViewSet(ViewSet):
    """
        View module for handling requests about Containers.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Container ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Container types.
        """

        user = request.auth.user
        print(user)

        try:
            containers = Container.objects.all()
            serialzied_containers = ContainerSerializer(
                containers,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_containers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
