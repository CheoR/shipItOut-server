"""BkgStatus ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import BkgStatus
from api.serializers import BkgStatusSerializer


class BkgStatusViewSet(ViewSet):
    """
        View module for handling requests about BkgStatuss.
        ViewSet handles POSTrequests sent from client
        over HTTP protocol.

        BkgStatus ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of BkgStatus types.
        """

        user = request.auth.user
        print(user)

        try:
            BkgStatuss = BkgStatus.objects.all()
            serialzied_bkgStatuss = BkgStatusSerializer(
                BkgStatuss,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_bkgStatuss.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
