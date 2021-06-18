"""Document Serializer"""

from rest_framework import serializers

from api.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """JSON serializer for Documents"""

    class Meta:
        model = Document
        fields = ('id', 'are_docs_ready')
