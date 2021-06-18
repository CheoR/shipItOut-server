"""Product ViewSet"""

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

        user = request.auth.user
        print(user)

        try:
            products = Product.objects.all()
            serialzied_products = ProductSerializer(
                products,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_products.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
