"""AppUser ViewSet"""

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from django.contrib.auth.models import User
from django.http import HttpResponseServerError

from api.models import AppUser
from api.serializers import DefaultAppUserSerializer, AppUserSerializer, AppUserCarrierSerializer


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

            if (request.data.get('expand', False)):
                serializer = AppUserSerializer(
                    user,
                    context={'request': request},
                )
            else:
                serializer = DefaultAppUserSerializer(
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
            if (request.data.get('expand', False)):
                serialzier = AppUserSerializer(
                    users,
                    many=True,
                    context={'request': request},
                )
            else:
                serialzier = DefaultAppUserSerializer(
                    users,
                    many=True,
                    context={'request': request},
                )
            return Response(serialzier.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an AppUser

        Returns:
            Response -- Empty body with 204 status code
        """

        appuser = AppUser.objects.get(pk=pk)
        user = User.objects.get(pk=appuser.id)
        
        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.first_name = request.data.get("first_name", user.first_name)
        user.last_name = request.data.get("last_name", user.last_name)

        appuser.company = request.data.get("company", appuser.company)
        appuser.role = request.data.get("role", appuser.role)
        appuser.phone = request.data.get("phone", appuser.phone)
        appuser.account_type = request.data.get("account_type", appuser.account_type)

        user.save()
        appuser.save()

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
            # TODO: confirm 4 is CARRIER
            carriers = AppUser.objects.filter(account_type=4).distinct('company')

            serializer = AppUserCarrierSerializer(
                carriers,
                many=True,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
