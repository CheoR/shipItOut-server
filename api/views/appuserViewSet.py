"""AppUser ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import AppUser
from api.serializers import AppUserSerializer


class AppUserViewSet(ViewSet):
    """
        View module for handling requests about AppUsers.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        AppUser ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of AppUser types.
        """

        user = request.auth.user
        print(user)

        try:
            users = AppUser.objects.all()
            serialzied_appUsers = AppUserSerializer(
                users,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_appUsers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
