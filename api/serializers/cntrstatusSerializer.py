"""CntrStatusSerializer"""

from rest_framework import serializers

from api.models import CntrStatus


class CntrStatusSerializer(serializers.ModelSerializer):
    """JSON serializer for CntrStatus"""

    class Meta:
        model = CntrStatus
        fields = ('id', 'status')
