"""AppUser ViewSet"""

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from django.contrib.auth.models import User
from django.http import HttpResponseServerError

from api.models import AppUser
from api.serializers import AppUserSerializer, AppUserCarrierSerializer


class AppUserViewSet(ViewSet):
    """
        View module for handling requests about AppUsers.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.
        AppUser ViewSet
    """

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user instance
        """

        try:
            user = AppUser.objects.get(pk=pk)
            serializer = AppUserSerializer(
                user,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all users resources.
            Returns:
                Response : JSON serialized list of AppUser types.
        """

        try:
            users = AppUser.objects.all()
            serialzied_appUsers = AppUserSerializer(
                users,
                many=True,
                context={'request': request},
            )

            return Response(serialzied_appUsers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an AppUser

        Returns:
            Response -- Empty body with 204 status code
        """

        user = AppUser.objects.get(pk=pk)
        
        user.username = request.data["username"]
        user.email = request.data["email"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.company = request.data["company"]
        user.role = request.data["role"]
        user.phone = request.data["phone"]
        user.account_type = request.data["account_type"]

        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single AppUser

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            user = AppUser.objects.get(pk=pk)
            user.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except AppUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def just_carriers(self, request):
        """
            Handle GET requests to get available carriers.
            Returns:
                Response : JSON serialized list of User types.
        """

        try:
            carriers = AppUser.objects.filter(account_type=4).distinct('company')

            serializer = AppUserCarrierSerializer(
                carriers,
                many=True,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
