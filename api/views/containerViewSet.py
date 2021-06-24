"""Container ViewSet"""

from api.models.carrier import Carrier
from api.models.booking import Booking
from api.models.appuser import AppUser
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
            Handle GET requests to get all container resources.
            Returns:
                Response : JSON serialized list of Container types.
        """

        user = request.auth.user

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

    def retrieve(self, request, pk=None):
        """
            Handle GET requests to get container resource.
            Returns:
                Response : JSON serialized single Container types.
        """

        def extract_product_info(products):
            obj_list = []
            for _ in products:
                obj = {}
                obj['commodity'] = _.commodity
                obj['weight'] = _.weight
                obj['product_fragile'] = _.is_fragile
                obj['product_haz'] = _.is_haz
                obj['product_damaged'] = _.is_damaged
                obj['reefer'] = _.is_reefer
                obj_list.append(obj)

            return obj_list

        user = request.auth.user

        try:
            user = AppUser.objects.get(user=request.auth.user)
            bookings = Booking.objects.filter(user=user)
            print("bookings")
            print(bookings)
            container = bookings.filter(container_id=pk)[0]
            # container = Container.objects.get(id=booking.container.id)
            # container = Container.objects.get(pk=pk)
            # container = Container.objects.get(id=booking.container.id)
            # cntr_status = CntrStatus.objects.get(
            #     id=container.container_status.id)
            # products = Product.objects.filter(container__id=container.id)
            # products = extract_product_info(products)
            serialzied_containers = ContainerSerializer(
                container,
                context=({'request': request})
            )
            return Response(serialzied_containers.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


# SELECT u.id, u.username, u.first_name, u.last_name, b.id, b.user_id, b.container_id, b.booking, b.id

# FROM auth_user u
# INNER JOIN api_appuser a
# ON u.id = a.user_id
# INNER JOIN api_booking b
# ON  a.user_id = b.user_id
# INNER JOIN api_container c
# ON c.id = b.container_id
# WHERE u.id = 1

# id |   username    | first_name | last_name | id | user_id | container_id |  booking   | id
# ----+---------------+------------+-----------+----+---------+--------------+------------+----
# 1 | superuser_bob |      Bobby |     Hill    | 19   | 1 |    4 |     USG4383274 |    19
# 1 | superuser_bob |      Bobby |     Hill    | 11   | 1 |    1 |     USM1300547 |    11
# 1 | superuser_bob |      Bobby |     Hill    | 10   | 1 |    5 |     USM8528880 |    10
# 1 | superuser_bob |      Bobby |     Hill    | 4    | 1 |    4 |     USG2257588 |     4
