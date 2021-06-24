"""Product ViewSet"""

from api.models.appuser import AppUser
from api.models.container import Container
from api.models.booking import Booking
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(ViewSet):
    """
        View module for handling requests about Products.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Product ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Product types.
        """

        user = AppUser.objects.get(user=request.auth.user)
        print(user)

        try:
            # bookings = Booking.objects.filter(user=user)
            # container = Container.objects.filter(id=bookings.container.id)
            # products = Product.objects.get(container__id=container.id)
            # products = extract_product_info(products)
            print("prodcs viwset")
            products = Product.objects.all()
            serialzied_products = ProductSerializer(
                products,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_products.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
