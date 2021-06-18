"""Due ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Due
from api.serializers import DueSerializer


class DueViewSet(ViewSet):
    """
        View module for handling requests about Dues.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Due ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Due types.
        """

        user = request.auth.user
        print(user)

        try:
            dues = Due.objects.all()
            serialzied_dues = DueSerializer(
                dues,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_dues.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
