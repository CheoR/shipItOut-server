"""Document ViewSet"""

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Document
from api.serializers import DocumentSerializer


class DocumentViewSet(ViewSet):
    """
        View module for handling requests about Documents.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Document ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Document types.
        """

        user = request.auth.user
        print(user)

        try:
            documents = Document.objects.all()
            serialzied_documents = DocumentSerializer(
                documents,
                many=True,
                context=({'request': request})
            )
            return Response(serialzied_documents.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
