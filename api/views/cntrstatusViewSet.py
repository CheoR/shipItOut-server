"""CntrStatus ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import CntrStatus
from api.serializers import CntrStatusSerializer


class CntrStatusViewSet(ViewSet):
    """
        View module for handling requests about CntrStatuss.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        CntrStatus ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of CntrStatus types.
        """

        user = request.auth.user
        print(user)

        try:
            cntrStatuses = CntrStatus.objects.all()
            serialzied_cntrStatuses = CntrStatusSerializer(
                cntrStatuses,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_cntrStatuses.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
