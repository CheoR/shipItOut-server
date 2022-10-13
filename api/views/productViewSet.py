"""Product ViewSet"""

from rest_framework import status
# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.http import HttpResponseServerError

from api.models import Product, Container, Booking
from api.serializers import ProductSerializer, ProductListViewSerializer


class ProductViewSet(ViewSet):
    """
        View module for handling requests about Products.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Product ViewSet
    """

    def create(self, request):
        """Handle POST requests for single Product

        Returns:
            Response -- JSON serialized Product instance
        """

        container = Container.objects.get(pk=request.data['container'])
        product = Product.objects.create(
            product=request.data['product'],
            weight=request.data['weight'],
            is_product_damaged=request.data['is_product_damaged'],
            is_fragile=request.data['is_fragile'],
            is_reefer=request.data['is_reefer'],
            is_hazardous=request.data['is_hazardous'],
            product_notes=request.data['product_notes'],
            container=container,
        )

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        """Handle GET requests for single Product

        Returns:
            Response -- JSON serialized Product instance
        """

        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductListViewSerializer(
            # serializer = ProductSerializer(
                product,
                context={'request': request},
            )

            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Product types.
        """

        try:
            # TODO: find better way to do this
            products = Product.objects.filter(
                container__in=Container.objects.filter(
                    booking__in=Booking.objects.filter(
                        agent__user=request.auth.user
                    )
                )
            )
            serialzier = ProductListViewSerializer(
            # serialzier = ProductSerializer(
                products,
                many=True,
                context={'request': request},
            )

            return Response(serialzier.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an Product

        Returns:
            Response -- Empty body with 204 status code
        """

        product = Product.objects.get(pk=pk)
        container = Container.objects.get(pk=request.data['container'])
        
        product.product = request.data['product']
        product.weight = request.data['weight']
        product.is_product_damaged = request.data['is_product_damaged']
        product.is_fragile = request.data['is_fragile']
        product.is_reefer = request.data['is_reefer']
        product.is_hazardous = request.data['is_hazardous']
        product.product_notes = request.data['product_notes']
        product.container = container

        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Product

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
