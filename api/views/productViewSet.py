"""Product ViewSet"""

from rest_framework import status
# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.http import HttpResponseServerError

from api.models import Product, Container, Booking
from api.serializers import DefaultProductSerializer, PartialProductSerializer, ProductListViewSerializer


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

        try:
            container = Container.objects.get(pk=request.data['container'])
        except:
            container = None

        product = Product.objects.create(
            product=request.data['product'],
            weight=request.data.get('weight', 0),
            is_product_damaged=request.data.get('is_product_damaged', False),
            is_fragile=request.data.get('is_fragile', False),
            is_reefer=request.data.get('is_reefer', False),
            is_hazardous=request.data.get('is_hazardous', False),
            product_notes=request.data.get('product_notes', ''),
            container=container,
        )

        serializer = DefaultProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        """Handle GET requests for single Product

        Returns:
            Response -- JSON serialized Product instance
        """

        try:
            product = Product.objects.get(pk=pk)
            if(request.data.get('expand', False)):
                serializer =  PartialProductSerializer(
                    product,
                    context={'request': request},
                )
            else:
                serializer =  DefaultProductSerializer(
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
            if(request.data.get('just_user', False)):
                products = Product.objects.all()
            else:
                products = Product.objects.filter(
                    container__in=Container.objects.filter(
                        booking__in=Booking.objects.filter(
                            agent__user=request.auth.user
                        )
                    )
                )
            serialzier = ProductListViewSerializer(
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

        try:
            container = Container.objects.get(pk=request.data['container'])
        except:
            container = None

        product.product = request.data.get('product', product.product)
        product.weight = request.data.get('weight', product.weight)
        product.is_product_damaged = request.data.get('is_product_damaged', product.is_product_damaged)
        product.is_fragile = request.data.get('is_fragile', product.is_fragile)
        product.is_reefer = request.data.get('is_reefer', product.is_reefer)
        product.is_hazardous = request.data.get('is_hazardous', product.is_hazardous)
        product.product_notes = request.data.get('product_notes', product.product_notes)
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
